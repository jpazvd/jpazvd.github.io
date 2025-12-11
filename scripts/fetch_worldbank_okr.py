#!/usr/bin/env python3
"""
Fetch World Bank Open Knowledge Repository statistics for João Pedro Azevedo.

This script uses the DSpace 7 REST API to fetch publication data.

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


def parse_publication_count(profile_data: dict) -> int:
    """Extract publication count from profile metadata."""
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
    
    profile = fetch_author_profile(AUTHOR_UUID)
    
    if not profile:
        return None
    
    # Extract data
    publication_count = parse_publication_count(profile)
    handle = profile.get("handle", "")
    name = profile.get("name", AUTHOR_NAME)
    entity_type = profile.get("entityType", "")
    last_modified = profile.get("lastModified", "")
    
    # Extract specializations
    metadata = profile.get("metadata", {})
    specializations = [
        item.get("value", "") 
        for item in metadata.get("authorProfile.specialization", [])
    ]
    
    print(f"  ✓ Name: {name}")
    print(f"  ✓ Handle: {handle}")
    print(f"  ✓ Publication count: {publication_count}")
    print(f"  ✓ Specializations: {', '.join(specializations)}")
    
    return {
        'author_id': AUTHOR_UUID,
        'handle': handle,
        'name': name,
        'publication_count': publication_count,
        'specializations': specializations,
        'profile_last_modified': last_modified,
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
