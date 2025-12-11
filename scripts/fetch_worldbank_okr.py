#!/usr/bin/env python3
"""
Fetch World Bank Open Knowledge Repository statistics for João Pedro Azevedo.

This script uses the DSpace 7 REST API to fetch publication data.
It searches for multiple name variations to get an accurate publication count.

Usage:
    python scripts/fetch_worldbank_okr.py

Requirements:
    pip install requests pyyaml

API Documentation:
    The World Bank OKR is built on DSpace 7.6
    Base API: https://openknowledge.worldbank.org/server/api

Note:
    Download/view statistics are not publicly available via API.
    Only publication count and metadata can be fetched without authentication.

Name Variations Found in OKR:
    - "Azevedo, Joao Pedro" (20 publications)
    - "Azevedo, João Pedro" (9 publications)
    - "Azevedo, Joao Pedro Wagner De" (3+ publications)
    - "Wagner De Azevedo, Joao Pedro"
"""

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
CITATIONS_FILE = Path(__file__).parent.parent / "_data" / "citations.yml"

# Name variations to search for (some publications use different formats)
NAME_VARIATIONS = [
    "Joao Pedro Azevedo",
    "Joao Pedro Wagner de Azevedo",
]


def fetch_author_profile(author_uuid: str) -> dict:
    """Fetch author profile from OKR API."""
    url = f"{OKR_API_BASE}/core/items/{author_uuid}"
    print(f"Fetching OKR profile from: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"  ✗ Error fetching profile: {e}")
        return None


def search_publications_by_name(name_query: str, size: int = 100) -> dict:
    """Search for publications by author name."""
    url = f"{OKR_API_BASE}/discover/search/objects"
    params = {
        "query": name_query,
        "dsoType": "item",
        "size": size
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"  ✗ Error searching for '{name_query}': {e}")
        return None


def count_unique_publications() -> tuple[int, set]:
    """
    Count unique publications across all name variations.
    Returns (count, set of UUIDs).
    """
    unique_uuids = set()
    
    for name in NAME_VARIATIONS:
        print(f"  Searching for: {name}")
        results = search_publications_by_name(name)
        
        if not results:
            continue
        
        search_result = results.get("_embedded", {}).get("searchResult", {})
        embedded = search_result.get("_embedded", {})
        objects = embedded.get("objects", [])
        
        for obj in objects:
            indexable = obj.get("_embedded", {}).get("indexableObject", {})
            entity_type = indexable.get("entityType", "")
            uuid = indexable.get("uuid", "")
            
            # Only count publications, not Person records
            if entity_type == "Publication" and uuid:
                unique_uuids.add(uuid)
        
        page_info = search_result.get("page", {})
        total = page_info.get("totalElements", 0)
        print(f"    Found {total} items ({len(objects)} publications)")
    
    return len(unique_uuids), unique_uuids


def parse_publication_count_from_profile(profile_data: dict) -> int:
    """Extract publication count from profile metadata (linked publications only)."""
    if not profile_data:
        return 0
    
    metadata = profile_data.get("metadata", {})
    publications = metadata.get("relation.isPublicationOfAuthor", [])
    
    return len(publications)


def fetch_okr_stats() -> dict:
    """Fetch all available OKR statistics."""
    print("=" * 60)
    print("World Bank Open Knowledge Repository Stats Fetcher")
    print("=" * 60)
    print()
    
    # First get the profile
    print("Step 1: Fetching author profile...")
    profile = fetch_author_profile(AUTHOR_UUID)
    
    if not profile:
        return None
    
    # Extract profile data
    linked_count = parse_publication_count_from_profile(profile)
    handle = profile.get("handle", "")
    name = profile.get("name", AUTHOR_NAME)
    
    # Extract specializations
    metadata = profile.get("metadata", {})
    specializations = [
        item.get("value", "") 
        for item in metadata.get("authorProfile.specialization", [])
    ]
    
    # Extract name variants from profile
    name_variants = [
        item.get("value", "") 
        for item in metadata.get("authorProfile.name.variant", [])
    ]
    
    print(f"  ✓ Name: {name}")
    print(f"  ✓ Handle: {handle}")
    print(f"  ✓ Linked publications: {linked_count}")
    print(f"  ✓ Name variants in profile: {name_variants}")
    print(f"  ✓ Specializations: {', '.join(specializations)}")
    
    # Search for all publications including those with name variations
    print()
    print("Step 2: Searching for publications across name variations...")
    total_count, unique_uuids = count_unique_publications()
    
    print()
    print(f"  ✓ Total unique publications found: {total_count}")
    
    # Use the higher count (search is more comprehensive than profile links)
    final_count = max(total_count, linked_count)
    
    if total_count > linked_count:
        print(f"  ℹ Note: {total_count - linked_count} additional publications found via name search")
        print("    (These may use alternative name formats like 'Joao Pedro Wagner de Azevedo')")
    
    return {
        'author_id': AUTHOR_UUID,
        'handle': handle,
        'name': name,
        'publication_count': final_count,
        'linked_count': linked_count,
        'search_count': total_count,
        'specializations': specializations,
        'name_variants': name_variants,
    }


def update_citations_file(okr_stats: dict) -> bool:
    """Update the citations.yml file with OKR statistics."""
    
    if not CITATIONS_FILE.exists():
        print(f"Citations file not found: {CITATIONS_FILE}")
        return False
    
    try:
        # Load existing data
        with open(CITATIONS_FILE, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Update World Bank OKR section
        if 'world_bank_okr' not in data:
            data['world_bank_okr'] = {}
        
        data['world_bank_okr'].update({
            'profile_url': OKR_PROFILE_URL,
            'api_url': f"{OKR_API_BASE}/core/items/{AUTHOR_UUID}",
            'author_id': okr_stats['author_id'],
            'handle': okr_stats['handle'],
            'publication_count': okr_stats['publication_count'],
            'last_updated': today,
        })
        
        # Write back
        with open(CITATIONS_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
        
        print(f"\n✓ Updated {CITATIONS_FILE}")
        return True
        
    except Exception as e:
        print(f"Error updating citations file: {e}")
        return False


def main():
    # Fetch statistics
    okr_stats = fetch_okr_stats()
    
    if not okr_stats:
        print("\n✗ Failed to fetch OKR statistics")
        sys.exit(1)
    
    # Update file
    if update_citations_file(okr_stats):
        print("\n✓ Done! Review changes and commit if correct.")
    else:
        print("\n✗ Failed to update citations file")
        sys.exit(1)


if __name__ == "__main__":
    main()
