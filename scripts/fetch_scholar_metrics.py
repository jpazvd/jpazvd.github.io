#!/usr/bin/env python3
"""
Fetch Google Scholar citation metrics for João Pedro Azevedo.

This script uses the scholarly library to fetch citation data
and updates the _data/citations.yml file.

Usage:
    python scripts/fetch_scholar_metrics.py

Requirements:
    pip install scholarly pyyaml

Note: Google Scholar may block automated access. Use with caution
and consider using proxies if running frequently.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from scholarly import scholarly
    import yaml
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install scholarly pyyaml")
    sys.exit(1)

# Configuration
SCHOLAR_ID = "lTKXA78AAAAJ"
CITATIONS_FILE = Path(__file__).parent.parent / "_data" / "citations.yml"


def fetch_scholar_metrics(author_id: str) -> dict:
    """Fetch metrics from Google Scholar."""
    print(f"Fetching Google Scholar data for author ID: {author_id}")
    
    try:
        # Search for author by ID
        author = scholarly.search_author_id(author_id)
        author = scholarly.fill(author, sections=['basics', 'indices', 'counts'])
        
        metrics = {
            'total_citations': author.get('citedby', None),
            'h_index': author.get('hindex', None),
            'i10_index': author.get('i10index', None),
            'citations_5yr': author.get('citedby5y', None),
        }
        
        print(f"  Total citations: {metrics['total_citations']}")
        print(f"  h-index: {metrics['h_index']}")
        print(f"  i10-index: {metrics['i10_index']}")
        
        return metrics
        
    except Exception as e:
        print(f"Error fetching Scholar data: {e}")
        return None


def update_citations_file(scholar_metrics: dict) -> bool:
    """Update the citations.yml file with new metrics."""
    
    if not CITATIONS_FILE.exists():
        print(f"Citations file not found: {CITATIONS_FILE}")
        return False
    
    try:
        # Load existing data
        with open(CITATIONS_FILE, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
        
        # Update Google Scholar section
        if 'google_scholar' not in data:
            data['google_scholar'] = {}
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        if scholar_metrics:
            data['google_scholar'].update({
                'total_citations': scholar_metrics['total_citations'],
                'h_index': scholar_metrics['h_index'],
                'i10_index': scholar_metrics['i10_index'],
                'citations_5yr': scholar_metrics['citations_5yr'],
                'last_updated': today
            })
        
        # Write back
        with open(CITATIONS_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        print(f"\nUpdated {CITATIONS_FILE}")
        return True
        
    except Exception as e:
        print(f"Error updating citations file: {e}")
        return False


def main():
    print("=" * 50)
    print("Citation Metrics Updater")
    print("=" * 50)
    print()
    
    # Fetch Google Scholar metrics
    scholar_metrics = fetch_scholar_metrics(SCHOLAR_ID)
    
    if scholar_metrics:
        update_citations_file(scholar_metrics)
        print("\nDone! Review changes and commit if correct.")
    else:
        print("\nFailed to fetch metrics. Try manual update.")
        sys.exit(1)


if __name__ == "__main__":
    main()
