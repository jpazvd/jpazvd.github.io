#!/usr/bin/env python3
"""
Fetch full content of World Bank Blog posts for João Pedro Azevedo.

This script reads the blog list from worldbank_blogs.yml and fetches
the full HTML content of each blog post, extracting the main text.

Usage:
    python scripts/fetch_blog_content.py

Requirements:
    pip install requests beautifulsoup4 pyyaml
"""

import sys
import time
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
    import yaml
except ImportError as e:
    missing = str(e).split("'")[1] if "'" in str(e) else "required packages"
    print(f"Missing dependency: {missing}")
    print("Install with:")
    print("  pip install requests beautifulsoup4 pyyaml")
    sys.exit(1)

# Configuration
BLOGS_FILE = Path(__file__).parent.parent / "_data" / "worldbank_blogs.yml"
OUTPUT_FILE = Path(__file__).parent.parent / "_data" / "worldbank_blogs_full.yml"


def fetch_blog_content(url: str) -> dict:
    """Fetch and extract content from a blog post URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"    ✗ Error fetching: {e}")
        return {}
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    content = {}
    
    # Try to find the main article content
    # World Bank blogs use various container classes
    article_selectors = [
        'article',
        '.blog-content',
        '.article-content',
        '.post-content',
        '.entry-content',
        '.blog_teaser__description',
        '.cmp-text',
        'main .container',
    ]
    
    article = None
    for selector in article_selectors:
        article = soup.select_one(selector)
        if article and len(article.get_text(strip=True)) > 200:
            break
    
    if article:
        # Remove script and style elements
        for element in article.find_all(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        # Get paragraphs
        paragraphs = []
        for p in article.find_all(['p', 'h2', 'h3', 'h4', 'blockquote', 'li']):
            text = p.get_text(strip=True)
            if text and len(text) > 20:  # Skip very short paragraphs
                tag = p.name
                if tag.startswith('h'):
                    paragraphs.append(f"\n## {text}\n")
                elif tag == 'blockquote':
                    paragraphs.append(f"> {text}")
                elif tag == 'li':
                    paragraphs.append(f"- {text}")
                else:
                    paragraphs.append(text)
        
        content['body'] = "\n\n".join(paragraphs)
    else:
        # Fallback: get all text from body
        body = soup.find('body')
        if body:
            # Remove navigation and footer
            for element in body.find_all(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                element.decompose()
            content['body'] = body.get_text(separator='\n', strip=True)[:5000]
    
    # Get meta description as summary
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        content['summary'] = meta_desc.get('content', '')
    
    # Get any images
    images = []
    for img in soup.find_all('img', src=True):
        src = img.get('src', '')
        alt = img.get('alt', '')
        if src and 'logo' not in src.lower() and 'icon' not in src.lower():
            if src.startswith('/'):
                src = f"https://blogs.worldbank.org{src}"
            images.append({'src': src, 'alt': alt})
    if images:
        content['images'] = images[:5]  # Limit to 5 images
    
    return content


def main():
    print(f"\n📖 Fetching full content for World Bank Blog posts")
    print("=" * 60)
    
    # Load existing blog list
    if not BLOGS_FILE.exists():
        print(f"  ✗ Blog list not found: {BLOGS_FILE}")
        print("  Run fetch_worldbank_blogs.py --list first")
        sys.exit(1)
    
    with open(BLOGS_FILE, 'r', encoding='utf-8') as f:
        blog_data = yaml.safe_load(f)
    
    posts = blog_data.get('posts', [])
    print(f"  Found {len(posts)} posts to fetch")
    
    # Fetch content for each post
    full_posts = []
    for i, post in enumerate(posts, 1):
        title = post.get('title', '')[:50]
        url = post.get('url', '')
        lang = post.get('language', 'en')
        
        print(f"\n  [{i}/{len(posts)}] {title}...")
        
        # Fetch content
        content = fetch_blog_content(url)
        
        # Merge with existing metadata
        full_post = {**post}
        if content.get('body'):
            full_post['content'] = content['body']
            print(f"    ✓ Fetched {len(content['body'])} chars")
        if content.get('summary'):
            full_post['summary'] = content['summary']
        if content.get('images'):
            full_post['images'] = content['images']
        
        full_posts.append(full_post)
        
        # Rate limiting
        time.sleep(0.5)
    
    # Save to output file
    output_data = {
        'metadata': blog_data.get('metadata', {}),
        'posts': full_posts
    }
    output_data['metadata']['includes_content'] = True
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(output_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=1000)
    
    print(f"\n✅ Saved full content to {OUTPUT_FILE}")
    
    # Summary
    posts_with_content = sum(1 for p in full_posts if p.get('content'))
    print(f"\n📊 Summary:")
    print(f"  Posts with content: {posts_with_content}/{len(full_posts)}")


if __name__ == "__main__":
    main()
