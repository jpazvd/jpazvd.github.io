#!/usr/bin/env python3
"""
Fetch World Bank Blog posts for João Pedro Azevedo.

This script uses the World Bank Blogs API to fetch blog posts.
The API is discovered from the author page at blogs.worldbank.org.

Usage:
    python scripts/fetch_worldbank_blogs.py              # Show stats only
    python scripts/fetch_worldbank_blogs.py --list       # Export blog list to YAML
    python scripts/fetch_worldbank_blogs.py --verbose    # Show detailed output
    python scripts/fetch_worldbank_blogs.py --update-citations  # Update citations.yml

Requirements:
    pip install requests pyyaml

API Details:
    - Endpoint: https://webapi.worldbank.org/aemsite/blogs/global/search
    - Uses OData-style filter for blogger ID
    - Author page: blogs.worldbank.org/en/team/j/joao-pedro-azevedo
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
    import yaml
except ImportError as e:
    missing = str(e).split("'")[1] if "'" in str(e) else "required packages"
    print(f"Missing dependency: {missing}")
    print("Install with:")
    print("  pip install requests pyyaml")
    sys.exit(1)

# Configuration
AUTHOR_NAME = "João Pedro Azevedo"
AUTHOR_SLUG = "joao-pedro-azevedo"
AUTHOR_GUID = "51402549393fa514d4308c0d3cb9c35d"  # From author page data-guid attribute

# API Configuration
BLOGS_API_URL = "https://webapi.worldbank.org/aemsite/blogs/global/search"
BLOGS_API_KEY = "a02440fa123c4740a83ed288591eafe4"

BLOGS_BASE_URL = "https://blogs.worldbank.org"
AUTHOR_PAGE_URL = f"{BLOGS_BASE_URL}/en/team/j/{AUTHOR_SLUG}"
OUTPUT_FILE = Path(__file__).parent.parent / "_data" / "worldbank_blogs.yml"
CITATIONS_FILE = Path(__file__).parent.parent / "_data" / "citations.yml"

# Known World Bank blog series/channels
BLOG_CHANNELS = {
    "education": "Education for Global Development",
    "developmenttalk": "Let's Talk Development",
    "opendata": "Data Blog",
    "impactevaluations": "Development Impact",
    "voices": "Voices",
    "africacan": "Africa Can End Poverty",
    "eastasiapacific": "East Asia & Pacific on the Rise",
    "latinamerica": "Latin America & Caribbean",
    "europeandcentralasia": "Europe & Central Asia",
    "endpovertyinsouthasia": "End Poverty in South Asia",
    "arabvoices": "Arab Voices",
    "ppps": "Getting Infrastructure Finance Right",
    "allaboutfinance": "All About Finance",
}


def fetch_blogs_from_api(author_guid: str, verbose: bool = False) -> list:
    """
    Fetch all blog posts for an author using the World Bank Blogs API.
    
    Args:
        author_guid: The GUID of the author from the author page
        verbose: Whether to print detailed progress
    
    Returns:
        List of blog post dictionaries
    """
    headers = {
        'Ocp-Apim-Subscription-Key': BLOGS_API_KEY,
        'Content-Type': 'application/json'
    }
    
    all_posts = []
    skip = 0
    page_size = 50
    
    while True:
        payload = {
            'top': page_size,
            'skip': skip,
            'filter': f"bloggers/any(b: b/id eq '{author_guid}')",
            'orderby': 'blogDate desc'
        }
        
        if verbose:
            print(f"  Fetching posts {skip+1} to {skip+page_size}...")
        
        try:
            response = requests.post(BLOGS_API_URL, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            print(f"  ✗ API error: {e}")
            break
        
        posts = data.get('value', [])
        if not posts:
            break
        
        all_posts.extend(posts)
        
        # Check if there are more pages
        if len(posts) < page_size:
            break
        
        skip += page_size
        
        # Safety limit
        if skip > 500:
            print("  ⚠ Reached maximum page limit")
            break
    
    return all_posts


def parse_blog_channel(url: str, channels: list = None) -> str:
    """Extract blog channel/series name from URL or channel list."""
    if channels:
        return channels[0] if channels else "World Bank Blogs"
    
    # URLs like /en/education/... or /en/developmenttalk/...
    match = re.search(r'/en/([^/]+)/', url)
    if match:
        channel_key = match.group(1)
        return BLOG_CHANNELS.get(channel_key, channel_key.replace('-', ' ').title())
    return "World Bank Blogs"


def parse_api_date(date_str: str) -> tuple:
    """Parse ISO date string from API to date and year."""
    if not date_str:
        return None, None
    try:
        # Format: "2023-04-20T12:00:00Z"
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d"), dt.year
    except ValueError:
        return date_str[:10] if len(date_str) >= 10 else None, None


def transform_api_posts(api_posts: list) -> list:
    """Transform API response posts to our standard format."""
    posts = []
    
    for p in api_posts:
        date_iso, year = parse_api_date(p.get('blogDate'))
        
        # Get co-authors
        bloggers = p.get('bloggers', [])
        authors = [b.get('fullName', '').strip() for b in bloggers if b.get('fullName')]
        
        # Determine language from title or language field
        lang = p.get('languageCode', 'en')
        
        post = {
            'title': p.get('title', p.get('blogTitle', '')),
            'url': p.get('pagePublishPath', p.get('shortLink', '')),
            'date': date_iso,
            'year': year,
            'channel': parse_blog_channel(p.get('pagePublishPath', ''), p.get('channels', [])),
            'description': p.get('description', '')[:500] if p.get('description') else None,
            'topics': p.get('topics', []),
            'authors': authors,
            'language': lang,
            'guid': p.get('guid'),
        }
        
        posts.append(post)
    
    return posts


def fetch_all_blog_posts(verbose: bool = False) -> list:
    """Fetch all blog posts for the author."""
    print(f"\n📚 Fetching World Bank Blog posts for {AUTHOR_NAME}")
    print("=" * 60)
    print(f"  Author page: {AUTHOR_PAGE_URL}")
    print(f"  Using API: {BLOGS_API_URL}")
    
    # Fetch from API
    api_posts = fetch_blogs_from_api(AUTHOR_GUID, verbose)
    
    if not api_posts:
        print("  ⚠ No posts found via API")
        return []
    
    print(f"  ✓ Found {len(api_posts)} posts from API")
    
    # Transform to standard format
    posts = transform_api_posts(api_posts)
    
    return posts


def print_statistics(posts: list):
    """Print blog post statistics."""
    print(f"\n📊 Blog Statistics")
    print("-" * 40)
    print(f"  Total blog posts: {len(posts)}")
    
    if posts:
        # Filter English-only for main stats
        english_posts = [p for p in posts if p.get('language', 'en') == 'en']
        if len(english_posts) != len(posts):
            print(f"  English posts: {len(english_posts)}")
            print(f"  Translations: {len(posts) - len(english_posts)}")
        
        # By channel/series
        channel_counts = {}
        for post in posts:
            channel = post.get('channel', 'Unknown')
            channel_counts[channel] = channel_counts.get(channel, 0) + 1
        
        print("\n  By Blog Channel:")
        for channel, count in sorted(channel_counts.items(), key=lambda x: -x[1]):
            print(f"    • {channel}: {count}")
        
        # By year
        years = [p.get('year') for p in posts if p.get('year')]
        if years:
            print("\n  By Year:")
            year_counts = {}
            for y in years:
                year_counts[y] = year_counts.get(y, 0) + 1
            for year in sorted(year_counts.keys(), reverse=True):
                print(f"    • {year}: {year_counts[year]}")
            
            print(f"\n  Timeline: {min(years)} - {max(years)}")


def export_to_yaml(posts: list, filepath: Path):
    """Export posts to YAML file."""
    # Sort by date descending
    sorted_posts = sorted(
        posts, 
        key=lambda x: x.get('date') or '0000-00-00', 
        reverse=True
    )
    
    # Count English vs translations
    english_posts = [p for p in posts if p.get('language', 'en') == 'en']
    
    # Prepare export data
    export_data = {
        'metadata': {
            'author': AUTHOR_NAME,
            'source': 'World Bank Blogs',
            'source_url': AUTHOR_PAGE_URL,
            'api_url': BLOGS_API_URL,
            'last_updated': datetime.now().strftime('%Y-%m-%d'),
            'total_posts': len(posts),
            'english_posts': len(english_posts),
            'translations': len(posts) - len(english_posts),
        },
        'posts': []
    }
    
    for post in sorted_posts:
        entry = {
            'title': post.get('title'),
            'url': post.get('url'),
            'date': post.get('date'),
            'year': post.get('year'),
            'channel': post.get('channel'),
            'language': post.get('language', 'en'),
        }
        # Add optional fields
        if post.get('description'):
            entry['description'] = post['description'][:300]
        if post.get('authors'):
            entry['authors'] = post['authors']
        if post.get('topics'):
            entry['topics'] = post['topics']
        
        export_data['posts'].append(entry)
    
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.dump(export_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    print(f"\n✅ Exported to {filepath}")


def update_citations_file(posts: list):
    """Update the main citations.yml with blog statistics."""
    if not CITATIONS_FILE.exists():
        print(f"  ⚠ Citations file not found: {CITATIONS_FILE}")
        return
    
    try:
        with open(CITATIONS_FILE, 'r', encoding='utf-8') as f:
            citations = yaml.safe_load(f) or {}
    except Exception as e:
        print(f"  ⚠ Error reading citations file: {e}")
        return
    
    # Prepare blog statistics
    english_posts = [p for p in posts if p.get('language', 'en') == 'en']
    years = [p.get('year') for p in posts if p.get('year')]
    
    channel_counts = {}
    for post in posts:
        channel = post.get('channel', 'Unknown')
        channel_counts[channel] = channel_counts.get(channel, 0) + 1
    
    blog_stats = {
        'post_count': len(posts),
        'english_posts': len(english_posts),
        'translations': len(posts) - len(english_posts),
        'source_url': AUTHOR_PAGE_URL,
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
    }
    
    if years:
        blog_stats['timeline'] = {
            'first_year': min(years),
            'latest_year': max(years),
        }
    
    if channel_counts:
        blog_stats['by_channel'] = channel_counts
    
    citations['world_bank_blogs'] = blog_stats
    
    try:
        with open(CITATIONS_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(citations, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        print(f"  ✅ Updated {CITATIONS_FILE}")
    except Exception as e:
        print(f"  ⚠ Error updating citations file: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch World Bank Blog posts for João Pedro Azevedo"
    )
    parser.add_argument(
        '--list', 
        action='store_true',
        help='Export full blog list to YAML file'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output'
    )
    parser.add_argument(
        '--update-citations',
        action='store_true',
        help='Update citations.yml with blog statistics'
    )
    args = parser.parse_args()
    
    # Fetch all posts
    posts = fetch_all_blog_posts(verbose=args.verbose)
    
    # Print statistics
    print_statistics(posts)
    
    # Print posts
    if posts:
        print("\n📝 Blog Posts:")
        print("-" * 40)
        for i, post in enumerate(posts, 1):
            date_str = post.get('date', 'Unknown date')
            lang = post.get('language', 'en')
            lang_marker = f" [{lang}]" if lang != 'en' else ""
            title = post['title'][:55] + "..." if len(post['title']) > 55 else post['title']
            print(f"  {i}. [{date_str}] {title}{lang_marker}")
            print(f"     Channel: {post.get('channel', 'Unknown')}")
            print(f"     URL: {post['url']}")
            print()
    
    # Export if requested
    if args.list:
        export_to_yaml(posts, OUTPUT_FILE)
    
    # Update citations file if requested
    if args.update_citations:
        update_citations_file(posts)


if __name__ == "__main__":
    main()
