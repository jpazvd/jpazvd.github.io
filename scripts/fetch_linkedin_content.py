#!/usr/bin/env python3
"""Fetch LinkedIn content for this site (without scraping).

LinkedIn does NOT provide a broadly-open, stable "public profile REST API" for
personal posts/articles. Access to member content via LinkedIn's official APIs is
permissioned and typically requires a LinkedIn Developer app + approved products.

To keep this repo compliant and maintainable, this script supports:

1) Export mode (recommended): parse a LinkedIn "Download your data" export folder.
   This avoids scraping and works without special API access.

2) Export + analytics merge (optional): parse an additional CSV you export from
    LinkedIn analytics (e.g., a "content performance" export) and merge metrics
    like impressions/views/clicks into the normalized items.

3) API mode (optional): placeholder wiring for official LinkedIn API access.
   You must provide an access token and *confirm* the correct endpoints and
   permissions for your application.

Outputs:
- Writes normalized YAML to `_data/linkedin_content.yml` for Jekyll consumption.

Usage:
  python scripts/fetch_linkedin_content.py --export-dir /path/to/linkedin-export
  python scripts/fetch_linkedin_content.py --export-dir ... --out _data/linkedin_content.yml
    python scripts/fetch_linkedin_content.py --export-dir ... --analytics-csv /path/to/analytics.csv

Requirements:
  pip install pyyaml

Notes:
- This script intentionally does NOT scrape linkedin.com.
- If you want API mode, add a small config file with endpoints once you confirm
  your permitted LinkedIn API products/permissions.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml")
    print("Install with: pip install pyyaml")
    sys.exit(1)


DEFAULT_OUT = Path(__file__).parent.parent / "_data" / "linkedin_content.yml"


@dataclass(frozen=True)
class NormalizedItem:
    type: str  # e.g., "article", "post", "share"
    title: str
    url: Optional[str]
    date: Optional[str]  # YYYY-MM-DD
    year: Optional[int]
    text: Optional[str]
    impressions: Optional[int] = None
    views: Optional[int] = None
    clicks: Optional[int] = None
    reactions: Optional[int] = None
    comments: Optional[int] = None
    shares: Optional[int] = None


def _parse_date(value: str) -> Tuple[Optional[str], Optional[int]]:
    value = (value or "").strip()
    if not value:
        return None, None

    # Try common formats from exports (varies by locale/version).
    candidates = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%m-%d-%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
    ]

    for fmt in candidates:
        try:
            dt = datetime.strptime(value, fmt)
            return dt.strftime("%Y-%m-%d"), dt.year
        except ValueError:
            pass

    # Fallback: take first 10 chars if it looks like an ISO date.
    if len(value) >= 10 and value[4] in "-/" and value[7] in "-/":
        ymd = value[:10].replace("/", "-")
        try:
            year = int(ymd[:4])
        except ValueError:
            year = None
        return ymd, year

    return None, None


def _to_int(value: str) -> Optional[int]:
    value = (value or "").strip()
    if not value:
        return None

    # Common export formats: "1,234" or "1234".
    value = value.replace(",", "")
    try:
        return int(float(value))
    except ValueError:
        return None


def _best_field(row: Dict[str, str], field_names: Iterable[str]) -> str:
    for name in field_names:
        for key in row.keys():
            if key.strip().lower() == name.strip().lower():
                return row.get(key, "") or ""
    return ""


def _best_int(row: Dict[str, str], field_names: Iterable[str]) -> Optional[int]:
    return _to_int(_best_field(row, field_names))


def _read_csv_items(csv_path: Path, item_type: str) -> List[NormalizedItem]:
    items: List[NormalizedItem] = []

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return items

        for row in reader:
            date_raw = _best_field(row, [
                "Date",
                "Created Date",
                "Creation Date",
                "Time",
                "Timestamp",
            ])
            date, year = _parse_date(date_raw)

            url = _best_field(row, ["URL", "Url", "Link", "Permalink"])
            title = _best_field(row, ["Title", "Subject"]).strip()
            text = _best_field(row, ["Text", "Body", "Content", "Comment"]).strip()

            # If the export includes metrics columns, capture them.
            impressions = _best_int(row, ["Impressions", "Impression", "Impression Count"])
            views = _best_int(row, ["Views", "View", "View Count"])
            clicks = _best_int(row, ["Clicks", "Click", "Click Count"])
            reactions = _best_int(row, ["Reactions", "Reaction Count", "Likes", "Like Count"])
            comments = _best_int(row, ["Comments", "Comment Count"])
            shares = _best_int(row, ["Shares", "Share Count"])

            # If there's no explicit title, use the first line of text.
            if not title:
                title = (text.splitlines()[0] if text else "LinkedIn item").strip()

            if not title:
                continue

            items.append(
                NormalizedItem(
                    type=item_type,
                    title=title,
                    url=url or None,
                    date=date,
                    year=year,
                    text=text or None,
                    impressions=impressions,
                    views=views,
                    clicks=clicks,
                    reactions=reactions,
                    comments=comments,
                    shares=shares,
                )
            )

    return items


def load_from_export(export_dir: Path) -> List[NormalizedItem]:
    """Parse a LinkedIn export directory.

    LinkedIn's export file names/columns may change; this tries multiple common
    filenames and extracts a minimal, safe subset.
    """

    candidates = [
        ("Articles.csv", "article"),
        ("Posts.csv", "post"),
        ("Shares.csv", "share"),
    ]

    all_items: List[NormalizedItem] = []

    for filename, item_type in candidates:
        path = export_dir / filename
        if path.exists():
            all_items.extend(_read_csv_items(path, item_type=item_type))

    return all_items


def _read_analytics(csv_path: Path) -> List[Dict[str, Any]]:
    """Read an analytics export CSV.

    LinkedIn's analytics export formats vary by product (member vs page) and UI.
    This function extracts a minimal subset and returns rows with best-effort
    normalization.
    """

    rows_out: List[Dict[str, Any]] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return rows_out

        for row in reader:
            date_raw = _best_field(row, ["Date", "Created Date", "Creation Date", "Time", "Timestamp"])
            date, _year = _parse_date(date_raw)

            url = _best_field(row, ["URL", "Url", "Link", "Permalink", "Update URL", "Content URL"])
            title = _best_field(row, ["Title", "Subject", "Content", "Post", "Update"])

            rows_out.append(
                {
                    "date": date,
                    "title": (title or "").strip(),
                    "url": (url or "").strip() or None,
                    "impressions": _best_int(row, ["Impressions", "Impression", "Impression Count"]),
                    "views": _best_int(row, ["Views", "View", "View Count"]),
                    "clicks": _best_int(row, ["Clicks", "Click", "Click Count"]),
                    "reactions": _best_int(row, ["Reactions", "Reaction Count", "Likes", "Like Count"]),
                    "comments": _best_int(row, ["Comments", "Comment Count"]),
                    "shares": _best_int(row, ["Shares", "Share Count"]),
                }
            )

    return rows_out


def merge_analytics(items: List[NormalizedItem], analytics_rows: List[Dict[str, Any]]) -> List[NormalizedItem]:
    """Merge analytics metrics into normalized items.

    Strategy:
    - Prefer matching by URL when available.
    - Fallback to (date, normalized title) for exports lacking URLs.
    """

    by_url: Dict[str, Dict[str, Any]] = {}
    by_key: Dict[Tuple[str, str], Dict[str, Any]] = {}

    for r in analytics_rows:
        if r.get("url"):
            by_url[str(r["url"]).strip()] = r
        if r.get("date") and r.get("title"):
            key = (str(r["date"]).strip(), str(r["title"]).strip().lower())
            by_key[key] = r

    merged: List[NormalizedItem] = []
    for item in items:
        r: Optional[Dict[str, Any]] = None
        if item.url and item.url.strip() in by_url:
            r = by_url[item.url.strip()]
        elif item.date and item.title:
            key = (item.date.strip(), item.title.strip().lower())
            r = by_key.get(key)

        if not r:
            merged.append(item)
            continue

        merged.append(
            NormalizedItem(
                type=item.type,
                title=item.title,
                url=item.url,
                date=item.date,
                year=item.year,
                text=item.text,
                impressions=item.impressions if item.impressions is not None else r.get("impressions"),
                views=item.views if item.views is not None else r.get("views"),
                clicks=item.clicks if item.clicks is not None else r.get("clicks"),
                reactions=item.reactions if item.reactions is not None else r.get("reactions"),
                comments=item.comments if item.comments is not None else r.get("comments"),
                shares=item.shares if item.shares is not None else r.get("shares"),
            )
        )

    return merged


def write_yaml(items: List[NormalizedItem], out_path: Path):
    items_sorted = sorted(items, key=lambda i: (i.date or "0000-00-00"), reverse=True)

    if items_sorted:
        years = [i.year for i in items_sorted if i.year]
        first_year = min(years) if years else None
        last_year = max(years) if years else None
    else:
        first_year = None
        last_year = None

    total_impressions = sum((i.impressions or 0) for i in items_sorted)
    total_views = sum((i.views or 0) for i in items_sorted)
    total_clicks = sum((i.clicks or 0) for i in items_sorted)

    payload: Dict[str, Any] = {
        "metadata": {
            "source": "LinkedIn",
            "last_updated": datetime.utcnow().strftime("%Y-%m-%d"),
            "total_items": len(items_sorted),
            "timeline": {"first_year": first_year, "last_year": last_year},
            "notes": "Generated from LinkedIn export (no scraping).",
            "traffic_totals": {
                "impressions": total_impressions if total_impressions else None,
                "views": total_views if total_views else None,
                "clicks": total_clicks if total_clicks else None,
            },
        },
        "items": [
            {
                "type": i.type,
                "title": i.title,
                "url": i.url,
                "date": i.date,
                "year": i.year,
                "text": i.text,
                "impressions": i.impressions,
                "views": i.views,
                "clicks": i.clicks,
                "reactions": i.reactions,
                "comments": i.comments,
                "shares": i.shares,
            }
            for i in items_sorted
        ],
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate _data/linkedin_content.yml from LinkedIn export.")
    parser.add_argument("--export-dir", type=str, help="Path to LinkedIn data export folder")
    parser.add_argument(
        "--analytics-csv",
        type=str,
        help=(
            "Optional: path to a LinkedIn analytics CSV export to merge traffic metrics "
            "(impressions/views/clicks/etc.) into items."
        ),
    )
    parser.add_argument("--out", type=str, default=str(DEFAULT_OUT), help="Output YAML file path")

    args = parser.parse_args()

    if not args.export_dir:
        print("Error: --export-dir is required.")
        print("Tip: Request a LinkedIn 'Download your data' export, then point this script at the extracted folder.")
        return 2

    export_dir = Path(args.export_dir)
    if not export_dir.exists() or not export_dir.is_dir():
        print(f"Error: export dir not found: {export_dir}")
        return 2

    items = load_from_export(export_dir)

    if args.analytics_csv:
        analytics_path = Path(args.analytics_csv)
        if not analytics_path.exists() or not analytics_path.is_file():
            print(f"Error: analytics CSV not found: {analytics_path}")
            return 2

        analytics_rows = _read_analytics(analytics_path)
        items = merge_analytics(items, analytics_rows)

    out_path = Path(args.out)
    write_yaml(items, out_path)

    print(f"Wrote {len(items)} items to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
