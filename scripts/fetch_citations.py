#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.parse import urlencode

ORCID = os.getenv("ORCID", "0000-0002-3844-215X")
DATA_PATH = os.getenv("DATA_PATH", "_data/citations.json")
OPENALEX_BASE = "https://api.openalex.org"

# Simple OpenAlex client without external deps

def http_get(url: str):
    req = Request(url, headers={"User-Agent": "jpazvd.github.io/metrics (contact: github.com/jpazvd)"})
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_author_id(orcid: str):
    url = f"{OPENALEX_BASE}/authors/ORCID:{orcid}"
    data = http_get(url)
    return data


def get_h_index(works_count: int, citations_by_year: list):
    # OpenAlex returns citations_by_year as list of {"year": int, "cited_by_count": int}
    # h-index requires citation counts per work; OpenAlex provides h_index at author level in summary_stats
    # We'll prefer summary_stats if present; otherwise we return None.
    return None


def main():
    try:
        author = get_author_id(ORCID)
    except Exception as e:
        print(f"Failed to fetch author: {e}", file=sys.stderr)
        return 1

    # Build summary using OpenAlex fields
    display_name = author.get("display_name")
    summary_stats = author.get("summary_stats", {})
    counts_by_year = author.get("counts_by_year", [])
    cited_by_count = author.get("cited_by_count")

    out = {
        "author": display_name,
        "orcid": ORCID,
        "summary": {
            "total_citations": cited_by_count,
            "h_index": summary_stats.get("h_index"),
            # i10-index is Google Scholar specific; not provided by OpenAlex
            "i10_index": None,
        },
        "counts_by_year": counts_by_year,
        "source": "openalex",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }

    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Wrote metrics to {DATA_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
