#!/usr/bin/env python3
"""
Fetch World Bank Open Knowledge Repository statistics for João Pedro Azevedo.

This script uses the DSpace 7 REST API to fetch publication data.
It searches for multiple name variations to get an accurate, deduplicated count.

Usage:
    python scripts/fetch_worldbank_okr.py
    python scripts/fetch_worldbank_okr.py --list    # Export publication list

Requirements:
    pip install requests pyyaml

API Documentation:
    The World Bank OKR is built on DSpace 7.6
    Base API: https://openknowledge.worldbank.org/server/api

Note:
    Download/view statistics are not publicly available via API.
    Only publication count and metadata can be fetched without authentication.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
    import yaml
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install requests pyyaml")
    sys.exit(1)

# Configuration
AUTHOR_UUID = "360f7a2e-0784-56e1-acf4-7f805fd50257"
AUTHOR_NAME = "Azevedo, João Pedro"
OKR_API_BASE = "https://openknowledge.worldbank.org/server/api"
OKR_PROFILE_URL = f"https://openknowledge.worldbank.org/entities/person/{AUTHOR_UUID}"
OKR_ITEM_URL = "https://openknowledge.worldbank.org/handle"
CITATIONS_FILE = Path(__file__).parent.parent / "_data" / "citations.yml"
PUBLICATIONS_FILE = Path(__file__).parent.parent / "_data" / "okr_publications.yml"

# All known name variations to search for
# Each variation may match different publications in the OKR database
NAME_VARIATIONS = [
    # Standard names (with and without Portuguese characters)
    "Joao Pedro Azevedo",
    "João Pedro Azevedo",
    # Full name with Wagner (with and without Portuguese characters)
    "Joao Pedro Wagner de Azevedo",
    "João Pedro Wagner de Azevedo",
    # Inverted formats that appear in OKR metadata
    "Azevedo, Joao Pedro",
    "Azevedo, João Pedro",
    "Azevedo, Joao Pedro Wagner De",
    "Wagner De Azevedo, Joao Pedro",
]


def fetch_author_profile(author_uuid: str) -> dict:
    """Fetch author profile from OKR API."""
    url = f"{OKR_API_BASE}/core/items/{author_uuid}"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"  ✗ Error fetching profile: {e}")
        return None


def search_publications_by_name(name_query: str, size: int = 200) -> list:
    """
    Search for publications by author name.
    Returns list of publication objects with metadata.
    """
    url = f"{OKR_API_BASE}/discover/search/objects"
    params = {
        "query": name_query,
        "dsoType": "item",
        "size": size
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        search_result = data.get("_embedded", {}).get("searchResult", {})
        embedded = search_result.get("_embedded", {})
        objects = embedded.get("objects", [])
        
        publications = []
        for obj in objects:
            indexable = obj.get("_embedded", {}).get("indexableObject", {})
            entity_type = indexable.get("entityType", "")
            
            # Only include publications, not Person records
            if entity_type == "Publication":
                publications.append(indexable)
        
        return publications
        
    except requests.RequestException as e:
        print(f"  ✗ Error searching for '{name_query}': {e}")
        return []


def extract_publication_metadata(pub: dict) -> dict:
    """Extract relevant metadata from a publication object."""
    metadata = pub.get("metadata", {})
    
    # Get first value from metadata fields
    def get_first(field_name: str, default: str = "") -> str:
        values = metadata.get(field_name, [])
        if values and len(values) > 0:
            return values[0].get("value", default)
        return default
    
    # Get all authors
    authors = [a.get("value", "") for a in metadata.get("dc.contributor.author", [])]
    
    # Get all subjects/keywords
    subjects = [s.get("value", "") for s in metadata.get("dc.subject", [])][:5]  # Limit to 5
    
    # Build URL
    handle = pub.get("handle", "")
    url = f"{OKR_ITEM_URL}/{handle}" if handle else ""
    
    return {
        "uuid": pub.get("uuid", ""),
        "title": pub.get("name", ""),
        "handle": handle,
        "url": url,
        "year": get_first("dc.date.issued", "")[:4] if get_first("dc.date.issued") else "",
        "type": get_first("dc.type"),
        "authors": authors,
        "abstract": get_first("dc.description.abstract", "")[:500],  # Truncate long abstracts
        "doi": get_first("dc.identifier.doi") or get_first("okr.identifier.doi"),
        "publisher": get_first("dc.publisher"),
        "topics": [t.get("value", "") for t in metadata.get("okr.topic", [])][:3],
        "subjects": subjects,
    }


def collect_all_publications() -> tuple:
    """
    Search all name variations and collect unique publications.
    Returns tuple: (dict of UUID->metadata, search statistics dict)
    """
    all_publications = {}  # UUID -> publication metadata
    search_stats = {}  # Track which search found what
    
    for name in NAME_VARIATIONS:
        print(f"  Searching: '{name}'", end="")
        pubs = search_publications_by_name(name)
        
        new_count = 0
        for pub in pubs:
            uuid = pub.get("uuid", "")
            if uuid and uuid not in all_publications:
                all_publications[uuid] = extract_publication_metadata(pub)
                new_count += 1
        
        print(f" → {len(pubs)} results, {new_count} new unique")
        search_stats[name] = {"total": len(pubs), "new": new_count}
    
    return all_publications, search_stats


def get_profile_linked_publications(profile: dict) -> set:
    """Get UUIDs of publications linked to the author profile."""
    if not profile:
        return set()
    
    metadata = profile.get("metadata", {})
    linked = metadata.get("relation.isPublicationOfAuthor", [])
    
    return {item.get("value", "") for item in linked if item.get("value")}


def fetch_okr_stats(export_list: bool = False) -> dict:
    """Fetch all available OKR statistics."""
    print("=" * 70)
    print("World Bank Open Knowledge Repository - Publication Collector")
    print("=" * 70)
    print()
    
    # Step 1: Get author profile
    print("Step 1: Fetching author profile...")
    print(f"  URL: {OKR_API_BASE}/core/items/{AUTHOR_UUID}")
    profile = fetch_author_profile(AUTHOR_UUID)
    
    if not profile:
        return None
    
    # Extract profile info
    handle = profile.get("handle", "")
    name = profile.get("name", AUTHOR_NAME)
    profile_linked_uuids = get_profile_linked_publications(profile)
    
    metadata = profile.get("metadata", {})
    specializations = [item.get("value", "") for item in metadata.get("authorProfile.specialization", [])]
    profile_name_variants = [item.get("value", "") for item in metadata.get("authorProfile.name.variant", [])]
    
    print(f"  ✓ Name: {name}")
    print(f"  ✓ Handle: {handle}")
    print(f"  ✓ Profile-linked publications: {len(profile_linked_uuids)}")
    print(f"  ✓ Name variants in profile: {profile_name_variants}")
    print()
    
    # Step 2: Search all name variations
    print("Step 2: Searching across all name variations...")
    all_publications, search_stats = collect_all_publications()
    
    # Step 3: Analyze results
    print()
    print("Step 3: Analyzing results...")
    
    search_uuids = set(all_publications.keys())
    
    # Publications found by search but not linked to profile
    unlinked = search_uuids - profile_linked_uuids
    # Publications linked to profile but not found by search (shouldn't happen but check)
    missing_from_search = profile_linked_uuids - search_uuids
    
    print(f"  ✓ Total unique publications from search: {len(search_uuids)}")
    print(f"  ✓ Publications linked to profile: {len(profile_linked_uuids)}")
    
    if unlinked:
        print(f"  ℹ {len(unlinked)} publications found by search but not linked to profile:")
        for uuid in list(unlinked)[:5]:  # Show first 5
            pub = all_publications.get(uuid, {})
            print(f"      - {pub.get('title', 'Unknown')[:60]}...")
    
    if missing_from_search:
        print(f"  ⚠ {len(missing_from_search)} profile-linked publications not found by search")
    
    # Final consolidated count
    all_uuids = search_uuids | profile_linked_uuids
    final_count = len(all_uuids)
    
    print()
    print(f"  ★ CONSOLIDATED TOTAL: {final_count} unique publications")
    
    # Sort publications by year (newest first)
    sorted_pubs = sorted(
        all_publications.values(),
        key=lambda x: x.get("year", "0000"),
        reverse=True
    )
    
    return {
        'author_id': AUTHOR_UUID,
        'handle': handle,
        'name': name,
        'publication_count': final_count,
        'profile_linked_count': len(profile_linked_uuids),
        'search_count': len(search_uuids),
        'specializations': specializations,
        'name_variants': profile_name_variants,
        'publications': sorted_pubs,
        'search_stats': search_stats,
    }


def update_citations_file(okr_stats: dict) -> bool:
    """Update the citations.yml file with OKR statistics."""
    
    if not CITATIONS_FILE.exists():
        print(f"Citations file not found: {CITATIONS_FILE}")
        return False
    
    try:
        with open(CITATIONS_FILE, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        if 'world_bank_okr' not in data:
            data['world_bank_okr'] = {}
        
        data['world_bank_okr'].update({
            'profile_url': OKR_PROFILE_URL,
            'api_url': f"{OKR_API_BASE}/core/items/{AUTHOR_UUID}",
            'author_id': okr_stats['author_id'],
            'handle': okr_stats['handle'],
            'publication_count': okr_stats['publication_count'],
            'profile_linked_count': okr_stats['profile_linked_count'],
            'search_count': okr_stats['search_count'],
            'last_updated': today,
        })
        
        with open(CITATIONS_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
        
        print(f"✓ Updated {CITATIONS_FILE}")
        return True
        
    except Exception as e:
        print(f"Error updating citations file: {e}")
        return False


def export_publications_list(okr_stats: dict) -> bool:
    """Export detailed publication list to YAML file."""
    
    try:
        publications = okr_stats.get('publications', [])
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Prepare export data
        export_data = {
            'metadata': {
                'author': okr_stats['name'],
                'author_id': okr_stats['author_id'],
                'profile_url': OKR_PROFILE_URL,
                'total_count': okr_stats['publication_count'],
                'generated': today,
                'note': 'Publications collected from World Bank Open Knowledge Repository',
            },
            'publications': []
        }
        
        for pub in publications:
            export_data['publications'].append({
                'title': pub['title'],
                'year': pub['year'],
                'type': pub['type'],
                'url': pub['url'],
                'handle': pub['handle'],
                'doi': pub['doi'] if pub['doi'] else None,
                'authors': pub['authors'],
            })
        
        with open(PUBLICATIONS_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(export_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
        
        print(f"✓ Exported publication list to {PUBLICATIONS_FILE}")
        return True
        
    except Exception as e:
        print(f"Error exporting publications: {e}")
        return False


def print_publication_list(okr_stats: dict):
    """Print formatted publication list to console."""
    publications = okr_stats.get('publications', [])
    
    print()
    print("=" * 70)
    print(f"PUBLICATION LIST ({len(publications)} items)")
    print("=" * 70)
    
    current_year = None
    for i, pub in enumerate(publications, 1):
        year = pub.get('year', 'Unknown')
        
        if year != current_year:
            current_year = year
            print(f"\n--- {year} ---")
        
        title = pub.get('title', 'Untitled')
        url = pub.get('url', '')
        doc_type = pub.get('type', '')
        
        print(f"\n{i}. {title}")
        print(f"   Type: {doc_type}")
        print(f"   URL: {url}")
        
        if pub.get('doi'):
            print(f"   DOI: {pub['doi']}")
        
        # Show first 3 authors
        authors = pub.get('authors', [])
        if len(authors) > 3:
            print(f"   Authors: {', '.join(authors[:3])}, et al.")
        elif authors:
            print(f"   Authors: {', '.join(authors)}")


def main():
    parser = argparse.ArgumentParser(description='Fetch World Bank OKR publication statistics')
    parser.add_argument('--list', action='store_true', help='Print and export full publication list')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()
    
    # Fetch statistics
    okr_stats = fetch_okr_stats(export_list=args.list)
    
    if not okr_stats:
        print("\n✗ Failed to fetch OKR statistics")
        sys.exit(1)
    
    print()
    
    # Update citations file
    update_citations_file(okr_stats)
    
    # Export/print list if requested
    if args.list:
        export_publications_list(okr_stats)
        print_publication_list(okr_stats)
    
    if args.json:
        # Output JSON for programmatic use
        output = {
            'count': okr_stats['publication_count'],
            'publications': okr_stats['publications']
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    
    print("\n✓ Done!")


if __name__ == "__main__":
    main()
