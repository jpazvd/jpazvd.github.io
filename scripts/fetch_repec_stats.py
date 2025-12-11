#!/usr/bin/env python3
"""
Fetch RePEc/IDEAS statistics for João Pedro Azevedo.

This script scrapes the LogEc statistics page and updates _data/citations.yml.

Usage:
    python scripts/fetch_repec_stats.py

Requirements:
    pip install requests beautifulsoup4 pyyaml

Data Sources:
    - Author stats: http://logec.repec.org/RAS/pwa88.htm
    - Global software ranking: https://logec.repec.org/scripts/authorstat.pf?topnum=100&sortby=ld&item=software&country=all
    - US software ranking: https://logec.repec.org/scripts/authorstat.pf?topnum=100&sortby=ld&item=software&country=us
"""

import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
    import yaml
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install requests beautifulsoup4 pyyaml")
    sys.exit(1)

# Configuration
REPEC_AUTHOR_ID = "pwa88"
AUTHOR_NAME = "Azevedo, João Pedro"
LOGEC_STATS_URL = f"http://logec.repec.org/RAS/{REPEC_AUTHOR_ID}.htm"
CITATIONS_FILE = Path(__file__).parent.parent / "_data" / "citations.yml"

# Ranking URLs - both monthly (ld) and total (td) downloads
RANKING_URLS = {
    # Monthly downloads rankings
    'software_global_monthly': 'https://logec.repec.org/scripts/authorstat.pf?topnum=100&sortby=ld&item=software&country=all',
    'software_us_monthly': 'https://logec.repec.org/scripts/authorstat.pf?topnum=100&sortby=ld&item=software&country=us',
    # Total downloads rankings (all-time)
    'software_global_total': 'https://logec.repec.org/scripts/authorstat.pf?topnum=100&sortby=td&item=software&country=all',
    'software_us_total': 'https://logec.repec.org/scripts/authorstat.pf?topnum=100&sortby=td&item=software&country=us',
}


def parse_stat_value(text: str) -> int:
    """Parse a statistics value, handling commas and empty strings."""
    if not text or text.strip() == "":
        return 0
    # Remove commas and convert to int
    clean = text.strip().replace(",", "")
    try:
        return int(clean)
    except ValueError:
        return 0


def fetch_repec_stats() -> dict:
    """Fetch and parse RePEc statistics from LogEc."""
    print(f"Fetching RePEc stats from: {LOGEC_STATS_URL}")
    
    try:
        response = requests.get(LOGEC_STATS_URL, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching stats: {e}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all tables
    tables = soup.find_all('table')
    
    stats = {
        'working_papers': {'downloads_12mo': 0, 'downloads_total': 0, 'abstract_views_12mo': 0, 'abstract_views_total': 0},
        'journal_articles': {'downloads_12mo': 0, 'downloads_total': 0, 'abstract_views_12mo': 0, 'abstract_views_total': 0},
        'books': {'downloads_12mo': 0, 'downloads_total': 0, 'abstract_views_12mo': 0, 'abstract_views_total': 0},
        'chapters': {'downloads_12mo': 0, 'downloads_total': 0, 'abstract_views_12mo': 0, 'abstract_views_total': 0},
        'software': {'downloads_12mo': 0, 'downloads_total': 0, 'abstract_views_12mo': 0, 'abstract_views_total': 0},
    }
    
    # Category mapping from table headers
    category_map = {
        'working paper': 'working_papers',
        'journal article': 'journal_articles',
        'book': 'books',
        'chapter': 'chapters',
        'software item': 'software',
    }
    
    current_category = None
    
    for table in tables:
        # Check if this table has a header indicating category
        prev_element = table.find_previous(['h2', 'h3', 'p', 'b'])
        if prev_element:
            header_text = prev_element.get_text().lower()
            for key, value in category_map.items():
                if key in header_text:
                    current_category = value
                    break
        
        # Look for "Total" rows in each table
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if not cells:
                continue
            
            first_cell = cells[0].get_text().strip().lower()
            
            # Check if this is a total row
            if 'total' in first_cell:
                # Determine category from row text
                for key, value in category_map.items():
                    if key in first_cell:
                        current_category = value
                        break
                
                if current_category and len(cells) >= 9:
                    # Table structure: Name | Downloads (month, 3mo, 12mo, total) | Views (month, 3mo, 12mo, total)
                    try:
                        stats[current_category] = {
                            'downloads_12mo': parse_stat_value(cells[3].get_text()),
                            'downloads_total': parse_stat_value(cells[4].get_text()),
                            'abstract_views_12mo': parse_stat_value(cells[7].get_text()),
                            'abstract_views_total': parse_stat_value(cells[8].get_text()),
                        }
                        print(f"  Found {current_category}: {stats[current_category]}")
                    except (IndexError, ValueError) as e:
                        print(f"  Warning: Could not parse {current_category} stats: {e}")
    
    # Calculate totals
    total_downloads_12mo = sum(s['downloads_12mo'] for s in stats.values())
    total_downloads_all = sum(s['downloads_total'] for s in stats.values())
    total_views_12mo = sum(s['abstract_views_12mo'] for s in stats.values())
    total_views_all = sum(s['abstract_views_total'] for s in stats.values())
    
    print(f"\nTotals:")
    print(f"  Downloads (12mo): {total_downloads_12mo:,}")
    print(f"  Downloads (all time): {total_downloads_all:,}")
    print(f"  Abstract views (12mo): {total_views_12mo:,}")
    print(f"  Abstract views (all time): {total_views_all:,}")
    
    return {
        'categories': stats,
        'total_downloads_12mo': total_downloads_12mo,
        'total_downloads_all_time': total_downloads_all,
        'total_abstract_views_12mo': total_views_12mo,
        'total_abstract_views_all_time': total_views_all,
    }


def fetch_author_ranking(url: str, ranking_name: str) -> dict:
    """Fetch author ranking from a LogEc ranking page."""
    print(f"\nFetching {ranking_name} ranking from: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"  Error fetching ranking: {e}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the main table
    tables = soup.find_all('table')
    
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if len(cells) >= 2:
                # Check if this row contains our author
                row_text = row.get_text().lower()
                if 'azevedo' in row_text and 'joão' in row_text:
                    # Found the author - extract rank from first cell
                    rank_text = cells[0].get_text().strip()
                    try:
                        rank = int(rank_text)
                        print(f"  Found rank: #{rank}")
                        
                        # Also extract stats from the row
                        result = {'rank': rank}
                        if len(cells) >= 9:
                            result['downloads_month'] = parse_stat_value(cells[2].get_text())
                            result['downloads_3mo'] = parse_stat_value(cells[3].get_text())
                            result['downloads_12mo'] = parse_stat_value(cells[4].get_text())
                            result['downloads_total'] = parse_stat_value(cells[5].get_text())
                        return result
                    except ValueError:
                        continue
    
    print(f"  Author not found in top 100")
    return None


def fetch_all_rankings() -> dict:
    """Fetch all author rankings."""
    rankings = {}
    
    for key, url in RANKING_URLS.items():
        result = fetch_author_ranking(url, key)
        if result:
            rankings[key] = result
    
    return rankings


def update_citations_file(repec_stats: dict, rankings: dict = None) -> bool:
    """Update the citations.yml file with new RePEc statistics."""
    
    if not CITATIONS_FILE.exists():
        print(f"Citations file not found: {CITATIONS_FILE}")
        return False
    
    try:
        # Load existing data
        with open(CITATIONS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            data = yaml.safe_load(content) or {}
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Update RePEc section
        if 'repec' not in data:
            data['repec'] = {}
        
        data['repec'].update({
            'profile_url': f"https://ideas.repec.org/e/{REPEC_AUTHOR_ID}.html",
            'stats_url': LOGEC_STATS_URL,
            'working_papers': repec_stats['categories']['working_papers'],
            'journal_articles': repec_stats['categories']['journal_articles'],
            'books': repec_stats['categories']['books'],
            'chapters': repec_stats['categories']['chapters'],
            'software': repec_stats['categories']['software'],
            'total_downloads_12mo': repec_stats['total_downloads_12mo'],
            'total_downloads_all_time': repec_stats['total_downloads_all_time'],
            'total_abstract_views_12mo': repec_stats['total_abstract_views_12mo'],
            'total_abstract_views_all_time': repec_stats['total_abstract_views_all_time'],
            'ranking_note': "Top 5% of authors by downloads and abstract views (12 months)",
            'last_updated': today,
        })
        
        # Add rankings if available
        if rankings:
            data['repec']['rankings'] = {
                'software_global': {
                    'rank_monthly': rankings.get('software_global_monthly', {}).get('rank'),
                    'rank_total': rankings.get('software_global_total', {}).get('rank'),
                    'description': 'Global ranking for software downloads',
                },
                'software_us': {
                    'rank_monthly': rankings.get('software_us_monthly', {}).get('rank'),
                    'rank_total': rankings.get('software_us_total', {}).get('rank'),
                    'description': 'US ranking for software downloads',
                },
            }
        
        # Write back with nice formatting
        with open(CITATIONS_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
        
        print(f"\n✓ Updated {CITATIONS_FILE}")
        return True
        
    except Exception as e:
        print(f"Error updating citations file: {e}")
        return False


def main():
    print("=" * 60)
    print("RePEc/IDEAS Statistics Updater")
    print("=" * 60)
    print()
    
    # Fetch statistics
    repec_stats = fetch_repec_stats()
    
    if not repec_stats:
        print("\n✗ Failed to fetch RePEc statistics")
        sys.exit(1)
    
    # Fetch rankings
    rankings = fetch_all_rankings()
    
    # Update file
    if update_citations_file(repec_stats, rankings):
        print("\n✓ Done! Review changes and commit if correct.")
    else:
        print("\n✗ Failed to update citations file")
        sys.exit(1)


if __name__ == "__main__":
    main()
