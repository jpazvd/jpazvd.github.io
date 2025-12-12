#!/usr/bin/env python3
"""Fetch UNICEF Data for Action blog posts for João Pedro Azevedo.

This script mirrors the structure of:
- scripts/fetch_worldbank_blogs.py (harvest a list + stats)
- scripts/fetch_blog_content.py (optionally fetch full content)

IMPORTANT: UNICEF Data for Action may block automated HTTP clients (403).
This script does not attempt to bypass bot protections. If requests are blocked,
run it from a network/environment where access is permitted, or provide a local
HTML snapshot.

Default behaviour:
- Harvest posts from an author archive page discovered from a seed post.

Outputs:
- _data/unicef_blogs.yml (metadata only)
- _data/unicef_blogs_full.yml (if --with-content)

Usage:
  python scripts/fetch_unicef_blogs.py
  python scripts/fetch_unicef_blogs.py --list
  python scripts/fetch_unicef_blogs.py --list --with-content
  python scripts/fetch_unicef_blogs.py --seed-url <post-url>

Requirements:
  pip install requests beautifulsoup4 pyyaml
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

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


AUTHOR_NAME = "João Pedro Azevedo"
SOURCE_NAME = "UNICEF Data for Action"
BASE_URL = "https://data.unicef.org/data-for-action/"
DEFAULT_SEED_URL = (
    "https://data.unicef.org/data-for-action/"
    "unicef-report-puts-children-at-the-heart-of-sustainable-development/"
)

OUTPUT_LIST = Path(__file__).parent.parent / "_data" / "unicef_blogs.yml"
OUTPUT_FULL = Path(__file__).parent.parent / "_data" / "unicef_blogs_full.yml"


def _http_get(url: str, timeout: int = 30) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }

    resp = requests.get(url, headers=headers, timeout=timeout)
    if resp.status_code == 403:
        raise PermissionError(
            f"403 Forbidden when fetching {url}. "
            "UNICEF may be blocking automated clients from this network."
        )
    resp.raise_for_status()
    return resp.text


def _parse_date(soup: BeautifulSoup) -> Tuple[Optional[str], Optional[int]]:
    # Prefer machine-readable meta
    for selector in [
        'meta[property="article:published_time"]',
        'meta[name="date"]',
        'meta[name="publish_date"]',
    ]:
        m = soup.select_one(selector)
        content = m.get("content") if m else None
        if content:
            raw = str(content).strip()
            # ISO-ish
            if len(raw) >= 10:
                try:
                    dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
                    return dt.strftime("%Y-%m-%d"), dt.year
                except ValueError:
                    pass
                try:
                    year = int(raw[:4])
                    return raw[:10], year
                except ValueError:
                    pass

    # Common: <time datetime="2023-11-20"> ... </time>
    t = soup.find("time")
    dt_attr = t.get("datetime") if t else None
    if dt_attr:
        raw = str(dt_attr).strip()
        if len(raw) >= 10:
            try:
                dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
                return dt.strftime("%Y-%m-%d"), dt.year
            except ValueError:
                try:
                    year = int(raw[:4])
                    return raw[:10], year
                except ValueError:
                    return raw[:10], None

    return None, None


def _parse_title(soup: BeautifulSoup) -> str:
    for selector in ["h1", "h1.entry-title", "article h1"]:
        h = soup.select_one(selector)
        if h and h.get_text(strip=True):
            return h.get_text(strip=True)

    if soup.title and soup.title.string:
        return soup.title.string.strip()

    return ""


def _parse_author_archive_url(soup: BeautifulSoup) -> Optional[str]:
    # WordPress commonly uses rel=author
    a = soup.find("a", attrs={"rel": "author"})
    if a and a.get("href"):
        return str(a["href"]).strip()

    # Heuristic: first link containing /author/
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "/author/" in href:
            return str(href).strip()

    return None


def _parse_categories(soup: BeautifulSoup) -> List[str]:
    cats: List[str] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/category/" in href:
            name = a.get_text(strip=True)
            if name and name not in cats:
                cats.append(name)
    return cats


def _parse_description(soup: BeautifulSoup) -> Optional[str]:
    m = soup.find("meta", attrs={"name": "description"})
    content = m.get("content") if m else None
    if content:
        return str(content).strip()
    return None


def _normalize_url(url: str) -> str:
    return url.split("#", 1)[0].strip()


def extract_post_metadata(url: str, html: str) -> Dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")

    title = _parse_title(soup)
    date, year = _parse_date(soup)

    author_text = None
    a = soup.find("a", attrs={"rel": "author"})
    if a:
        author_text = a.get_text(strip=True) or None

    post = {
        "title": title,
        "url": _normalize_url(url),
        "date": date,
        "year": year,
        "organization": "UNICEF",
        "channel": SOURCE_NAME,
        "language": "en",
        "description": _parse_description(soup),
        "authors": [author_text] if author_text else [AUTHOR_NAME],
        "topics": _parse_categories(soup),
    }

    # Clean nulls
    return {k: v for k, v in post.items() if v not in (None, "", [], {})}


def _find_archive_posts(soup: BeautifulSoup) -> List[Tuple[str, str]]:
    """Return list of (title, url) from an author archive page."""
    posts: List[Tuple[str, str]] = []

    # Common: article h2 a, or h3 a
    for selector in ["article h2 a", "article h3 a", "h2 a", "h3 a"]:
        for a in soup.select(selector):
            href = a.get("href")
            title = a.get_text(strip=True)
            if not href or not title:
                continue
            href = _normalize_url(str(href))
            if href.startswith(BASE_URL) and href not in [u for _, u in posts]:
                posts.append((title, href))

    return posts


def _find_next_page_url(soup: BeautifulSoup) -> Optional[str]:
    # WordPress commonly uses rel=next
    a = soup.find("a", rel="next")
    if a and a.get("href"):
        return str(a["href"]).strip()

    # Or page-numbers
    for selector in ["a.next", "a.next.page-numbers", "a.nextpostslink", "a.pagination__next"]:
        a = soup.select_one(selector)
        if a and a.get("href"):
            return str(a["href"]).strip()

    # Or nav links containing 'Next'
    for a in soup.find_all("a", href=True):
        txt = a.get_text(strip=True).lower()
        if txt in {"next", "older posts", "older", "next page"}:
            return str(a["href"]).strip()

    return None


def harvest_post_urls(author_archive_url: str, max_pages: int = 20, sleep: float = 0.25) -> List[str]:
    print(f"  Author archive: {author_archive_url}")

    urls: List[str] = []
    current = author_archive_url

    for _page_num in range(1, max_pages + 1):
        html = _http_get(current)
        soup = BeautifulSoup(html, "html.parser")

        found = _find_archive_posts(soup)
        for _, u in found:
            if u not in urls:
                urls.append(u)

        nxt = _find_next_page_url(soup)
        if not nxt:
            break
        current = nxt
        time.sleep(sleep)

    return urls


def fetch_content_markdown(html: str) -> Dict[str, Any]:
    """Extract a lightweight markdown-ish body similar to fetch_blog_content.py."""
    soup = BeautifulSoup(html, "html.parser")

    article = None
    for selector in ["article", ".entry-content", ".post-content", "main"]:
        cand = soup.select_one(selector)
        if cand and len(cand.get_text(strip=True)) > 200:
            article = cand
            break

    if not article:
        return {}

    for element in article.find_all(["script", "style", "nav", "footer", "header", "aside"]):
        element.decompose()

    paragraphs: List[str] = []
    for p in article.find_all(["p", "h2", "h3", "h4", "blockquote", "li"]):
        text = p.get_text(strip=True)
        if not text or len(text) < 20:
            continue
        tag = p.name
        if tag.startswith("h"):
            paragraphs.append(f"\n## {text}\n")
        elif tag == "blockquote":
            paragraphs.append(f"> {text}")
        elif tag == "li":
            paragraphs.append(f"- {text}")
        else:
            paragraphs.append(text)

    body = "\n\n".join(paragraphs).strip()
    if not body:
        return {}

    return {"content": body}


def write_yaml(posts: List[Dict[str, Any]], out_path: Path, includes_content: bool = False):
    posts_sorted = sorted(posts, key=lambda p: (p.get("date") or "0000-00-00"), reverse=True)

    years: List[int] = []
    for p in posts_sorted:
        y = p.get("year")
        if isinstance(y, int):
            years.append(y)
        elif isinstance(y, str) and y.isdigit():
            years.append(int(y))
    first_year = min(years) if years else None
    last_year = max(years) if years else None

    payload = {
        "metadata": {
            "author": AUTHOR_NAME,
            "source": SOURCE_NAME,
            "source_url": BASE_URL,
            "last_updated": datetime.utcnow().strftime("%Y-%m-%d"),
            "total_posts": len(posts_sorted),
            "timeline": {"first_year": first_year, "last_year": last_year},
            "includes_content": includes_content,
        },
        "posts": posts_sorted,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Harvest UNICEF Data for Action posts for a given author.")
    parser.add_argument("--seed-url", default=DEFAULT_SEED_URL, help="A known post URL to discover the author archive")
    parser.add_argument("--author-archive-url", default=None, help="Author archive URL (skip discovery)")
    parser.add_argument("--list", action="store_true", help="Write _data/unicef_blogs.yml")
    parser.add_argument("--with-content", action="store_true", help="Also fetch full content into _data/unicef_blogs_full.yml")
    parser.add_argument("--max-pages", type=int, default=20, help="Max archive pages to follow")
    parser.add_argument("--sleep", type=float, default=0.25, help="Sleep between requests")
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()

    print(f"\n🧾 Harvesting {SOURCE_NAME} posts for {AUTHOR_NAME}")
    print("=" * 60)

    try:
        seed_html = _http_get(args.seed_url)
    except (PermissionError, requests.RequestException) as e:
        print(f"  ✗ Failed to fetch seed URL: {e}")
        print("  Tip: If UNICEF blocks automated clients (403), you may need to run this")
        print("  script from a different network/environment where access is permitted.")
        return 1

    seed_soup = BeautifulSoup(seed_html, "html.parser")

    author_archive_url = args.author_archive_url or _parse_author_archive_url(seed_soup)
    if not author_archive_url:
        print("  ✗ Could not discover author archive URL from seed page.")
        print("  Provide it explicitly with --author-archive-url.")
        return 1

    try:
        post_urls = harvest_post_urls(author_archive_url, max_pages=args.max_pages, sleep=args.sleep)
    except (PermissionError, requests.RequestException) as e:
        print(f"  ✗ Failed to harvest author archive: {e}")
        return 1

    if args.verbose:
        print(f"  ✓ Found {len(post_urls)} post URLs")

    posts: List[Dict[str, Any]] = []

    for i, url in enumerate(post_urls, 1):
        if args.verbose:
            print(f"  [{i}/{len(post_urls)}] {url}")

        try:
            html = _http_get(url)
        except (PermissionError, requests.RequestException) as e:
            print(f"    ✗ Error fetching {url}: {e}")
            continue

        meta = extract_post_metadata(url, html)
        if args.with_content:
            meta.update(fetch_content_markdown(html))

        posts.append(meta)
        time.sleep(args.sleep)

    # Always print stats
    print("\n📊 Summary")
    print("-" * 40)
    print(f"  Total posts harvested: {len(posts)}")

    if args.list:
        write_yaml(posts, OUTPUT_LIST, includes_content=False)
        print(f"  ✓ Wrote list: {OUTPUT_LIST}")

    if args.with_content:
        write_yaml(posts, OUTPUT_FULL, includes_content=True)
        print(f"  ✓ Wrote full content: {OUTPUT_FULL}")

    if not args.list and not args.with_content:
        print("  (No files written. Use --list and/or --with-content.)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
