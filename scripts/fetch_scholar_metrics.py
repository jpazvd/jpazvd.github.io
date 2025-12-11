#!/usr/bin/env python3
"""
Fetch Google Scholar citation metrics for João Pedro Azevedo.

This script supports multiple methods to fetch citation data:
1. SerpAPI (recommended for automation) - requires SERPAPI_KEY environment variable
2. scholarly library (may be blocked by Google)
3. Manual input fallback

Usage:
    # With SerpAPI (recommended):
    export SERPAPI_KEY=your_api_key
    python scripts/fetch_scholar_metrics.py

    # Without API key (uses scholarly, may be blocked):
    python scripts/fetch_scholar_metrics.py

    # Force manual input:
    python scripts/fetch_scholar_metrics.py --manual

Requirements:
    pip install requests pyyaml scholarly

API Services Supported:
    - SerpAPI: https://serpapi.com (free tier: 100 searches/month)
    - ScraperAPI: https://www.scraperapi.com (alternative)
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
    import yaml
except ImportError:
    print("Missing core dependencies. Install with:")
    print("  pip install requests pyyaml")
    sys.exit(1)

# Configuration
SCHOLAR_ID = "lTKXA78AAAAJ"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}"
CITATIONS_FILE = Path(__file__).parent.parent / "_data" / "citations.yml"

# API Configuration
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"


def fetch_via_serpapi(author_id: str, api_key: str) -> dict:
    """Fetch metrics using SerpAPI (recommended for automation)."""
    print("Fetching via SerpAPI...")
    
    params = {
        "engine": "google_scholar_author",
        "author_id": author_id,
        "api_key": api_key,
    }
    
    try:
        response = requests.get(SERPAPI_ENDPOINT, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Extract citation stats
        cited_by = data.get("cited_by", {})
        table = cited_by.get("table", [])
        
        # Parse the citation table
        metrics = {
            'total_citations': None,
            'h_index': None,
            'i10_index': None,
            'citations_5yr': None,
            'h_index_5yr': None,
            'i10_index_5yr': None,
        }
        
        for row in table:
            citations = row.get("citations", {})
            if "all" in citations:
                metrics['total_citations'] = citations["all"]
            if "since_2020" in citations:  # Adjust year as needed
                metrics['citations_5yr'] = citations["since_2020"]
            
            h_index = row.get("h_index", {})
            if "all" in h_index:
                metrics['h_index'] = h_index["all"]
            if "since_2020" in h_index:
                metrics['h_index_5yr'] = h_index["since_2020"]
            
            i10_index = row.get("i10_index", {})
            if "all" in i10_index:
                metrics['i10_index'] = i10_index["all"]
            if "since_2020" in i10_index:
                metrics['i10_index_5yr'] = i10_index["since_2020"]
        
        # Also get graph data for yearly citations if available
        graph = cited_by.get("graph", [])
        if graph:
            metrics['citations_by_year'] = {item['year']: item['citations'] for item in graph}
        
        # Get publication count
        if "articles" in data:
            metrics['publication_count'] = len(data.get("articles", []))
        
        print(f"  ✓ Total citations: {metrics['total_citations']}")
        print(f"  ✓ h-index: {metrics['h_index']}")
        print(f"  ✓ i10-index: {metrics['i10_index']}")
        
        return metrics
        
    except requests.RequestException as e:
        print(f"  ✗ SerpAPI request failed: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"  ✗ Error parsing SerpAPI response: {e}")
        return None


def fetch_via_scholarly(author_id: str) -> dict:
    """Fetch metrics using scholarly library (may be blocked)."""
    print("Fetching via scholarly library...")
    print("  Note: This may be blocked by Google Scholar")
    
    try:
        from scholarly import scholarly
    except ImportError:
        print("  ✗ scholarly not installed. Install with: pip install scholarly")
        return None
    
    try:
        # Search for author by ID
        author = scholarly.search_author_id(author_id)
        author = scholarly.fill(author, sections=['basics', 'indices', 'counts'])
        
        metrics = {
            'total_citations': author.get('citedby', None),
            'h_index': author.get('hindex', None),
            'i10_index': author.get('i10index', None),
            'citations_5yr': author.get('citedby5y', None),
            'h_index_5yr': author.get('hindex5y', None),
            'i10_index_5yr': author.get('i10index5y', None),
        }
        
        # Get citations by year if available
        cites_per_year = author.get('cites_per_year', {})
        if cites_per_year:
            metrics['citations_by_year'] = cites_per_year
        
        print(f"  ✓ Total citations: {metrics['total_citations']}")
        print(f"  ✓ h-index: {metrics['h_index']}")
        print(f"  ✓ i10-index: {metrics['i10_index']}")
        
        return metrics
        
    except Exception as e:
        print(f"  ✗ Error fetching Scholar data: {e}")
        return None


def fetch_manual() -> dict:
    """Prompt user for manual input of metrics."""
    print("\n" + "=" * 50)
    print("Manual Input Mode")
    print("=" * 50)
    print(f"\nPlease visit: {SCHOLAR_URL}")
    print("and enter the values below:\n")
    
    def get_int(prompt: str) -> int:
        while True:
            value = input(f"  {prompt}: ").strip()
            if value == "":
                return None
            try:
                return int(value.replace(",", ""))
            except ValueError:
                print("    Please enter a valid number")
    
    metrics = {
        'total_citations': get_int("Total citations (all time)"),
        'h_index': get_int("h-index (all time)"),
        'i10_index': get_int("i10-index (all time)"),
        'citations_5yr': get_int("Citations (since 2020)"),
        'h_index_5yr': get_int("h-index (since 2020)"),
        'i10_index_5yr': get_int("i10-index (since 2020)"),
    }
    
    return metrics


def fetch_scholar_metrics(author_id: str, force_manual: bool = False) -> dict:
    """Fetch metrics using the best available method."""
    
    if force_manual:
        return fetch_manual()
    
    # Try SerpAPI first (if API key is available)
    serpapi_key = os.environ.get("SERPAPI_KEY") or os.environ.get("SERP_API_KEY")
    if serpapi_key:
        metrics = fetch_via_serpapi(author_id, serpapi_key)
        if metrics:
            return metrics
        print("  Falling back to scholarly...")
    else:
        print("No SERPAPI_KEY found in environment variables")
        print("  Tip: Get a free API key at https://serpapi.com")
        print()
    
    # Try scholarly library
    metrics = fetch_via_scholarly(author_id)
    if metrics:
        return metrics
    
    # Fall back to manual input
    print("\nAutomated fetching failed. Switching to manual input...")
    return fetch_manual()


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
            update_data = {
                'profile_url': SCHOLAR_URL,
                'total_citations': scholar_metrics.get('total_citations'),
                'h_index': scholar_metrics.get('h_index'),
                'i10_index': scholar_metrics.get('i10_index'),
                'citations_5yr': scholar_metrics.get('citations_5yr'),
                'h_index_5yr': scholar_metrics.get('h_index_5yr'),
                'i10_index_5yr': scholar_metrics.get('i10_index_5yr'),
                'last_updated': today
            }
            
            # Add citations by year if available
            if 'citations_by_year' in scholar_metrics:
                update_data['citations_by_year'] = scholar_metrics['citations_by_year']
            
            # Add publication count if available
            if 'publication_count' in scholar_metrics:
                update_data['publication_count'] = scholar_metrics['publication_count']
            
            # Remove None values to keep YAML clean
            update_data = {k: v for k, v in update_data.items() if v is not None}
            
            data['google_scholar'].update(update_data)
        
        # Write back
        with open(CITATIONS_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
        
        print(f"\n✓ Updated {CITATIONS_FILE}")
        return True
        
    except Exception as e:
        print(f"Error updating citations file: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Google Scholar citation metrics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # With SerpAPI (recommended):
  export SERPAPI_KEY=your_api_key
  python scripts/fetch_scholar_metrics.py

  # Manual input:
  python scripts/fetch_scholar_metrics.py --manual

Environment Variables:
  SERPAPI_KEY    API key for SerpAPI (https://serpapi.com)
        """
    )
    parser.add_argument(
        "--manual", "-m",
        action="store_true",
        help="Force manual input mode"
    )
    parser.add_argument(
        "--author-id",
        default=SCHOLAR_ID,
        help=f"Google Scholar author ID (default: {SCHOLAR_ID})"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Google Scholar Metrics Updater")
    print("=" * 60)
    print()
    
    # Fetch Google Scholar metrics
    scholar_metrics = fetch_scholar_metrics(args.author_id, force_manual=args.manual)
    
    if scholar_metrics:
        update_citations_file(scholar_metrics)
        print("\n✓ Done! Review changes and commit if correct.")
    else:
        print("\n✗ Failed to fetch metrics.")
        sys.exit(1)


if __name__ == "__main__":
    main()
