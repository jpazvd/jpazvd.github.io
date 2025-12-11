# Publication Statistics Update Protocol

This document outlines the protocol for updating publication statistics on jpazvd.github.io from various academic platforms.

## Data Sources

### Primary Sources

| Platform | Profile URL | Metrics Available |
|----------|-------------|-------------------|
| **Google Scholar** | https://scholar.google.com/citations?user=lTKXA78AAAAJ | Citations, h-index, i10-index, per-paper citations |
| **RePEc/IDEAS** | https://ideas.repec.org/e/pwa88.html | Downloads, citations, rankings, abstract views |
| **World Bank OKR** | https://openknowledge.worldbank.org/entities/person/360f7a2e-0784-56e1-acf4-7f805fd50257 | Publication count (downloads require auth) |
| **World Bank Blogs** | https://blogs.worldbank.org/en/team/j/joao-pedro-azevedo | Blog posts by channel |
| **ORCID** | https://orcid.org/0000-0003-2111-0596 | Verified publication list, employment history |
| **ResearchGate** | (if applicable) | Reads, citations, Research Interest score |
| **Scopus** | (Author ID needed) | h-index, citations, documents |
| **Web of Science** | (ResearcherID needed) | h-index, citations |

### Current Statistics (as of December 2025)

| Source | Key Metric | Value |
|--------|------------|-------|
| Google Scholar | Total Citations | 5,555 |
| Google Scholar | h-index | 30 |
| Google Scholar | i10-index | 62 |
| RePEc | Total Downloads (all time) | 32,265 |
| RePEc | Software Rankings (US) | #6 total downloads |
| World Bank OKR | Publications | 34 |
| World Bank Blogs | Blog Posts | 29 (24 EN + 5 translations) |

### RePEc Ranking Pages

| Ranking | URL | Description |
|---------|-----|-------------|
| **Software (Global)** | https://logec.repec.org/scripts/authorstat.pf?topnum=100&sortby=ld&item=software&country=all | Top software authors worldwide |
| **Software (US)** | https://logec.repec.org/scripts/authorstat.pf?topnum=100&sortby=ld&item=software&country=us | Top software authors in US |
| **All Works (Global)** | https://logec.repec.org/scripts/authorstat.pf?topnum=100&sortby=ld&item=all&country=all | Top authors overall |

### Metric Definitions

- **h-index**: Author has h papers with at least h citations each
- **i10-index**: Number of papers with at least 10 citations (Google Scholar only)
- **Citations**: Total number of times papers have been cited
- **Downloads**: Number of times papers have been downloaded (RePEc)

---

## Update Workflow

### Step 1: Gather Current Statistics

#### Google Scholar
1. Visit: https://scholar.google.com/citations?user=lTKXA78AAAAJ
2. Record:
   - Total citations
   - h-index
   - i10-index
   - Citations in last 5 years
   - Recent citations trend

#### RePEc/IDEAS
1. Visit: https://ideas.repec.org/e/pwa88.html
2. Record:
   - Total downloads (last 12 months)
   - Total abstract views
   - Author ranking (percentile)
   - Number of registered works

#### ORCID (if used)
1. Visit: https://orcid.org/0000-0003-2111-0596
2. Verify publication list is current
3. Check for any missing works

---

### Step 2: Update Website Files

#### Option A: Manual Update (Recommended for accuracy)

**1. Update `_data/citations.yml`** (create if doesn't exist):
```yaml
# Citation Metrics - Last Updated: YYYY-MM-DD
google_scholar:
  total_citations: XXXX
  h_index: XX
  i10_index: XX
  citations_5yr: XXXX
  last_updated: "YYYY-MM-DD"

repec:
  downloads_12mo: XXXX
  abstract_views: XXXX
  author_rank_percentile: XX
  registered_works: XX
  last_updated: "YYYY-MM-DD"

orcid:
  works_count: XXX
  last_updated: "YYYY-MM-DD"
```

**2. Display on CV page** (`_pages/cv.md`):
Add this section after Publications:
```liquid
## Citation Metrics

{% if site.data.citations %}
### Google Scholar
- **Total Citations:** {{ site.data.citations.google_scholar.total_citations }}
- **h-index:** {{ site.data.citations.google_scholar.h_index }}
- **i10-index:** {{ site.data.citations.google_scholar.i10_index }}

### RePEc/IDEAS
- **Downloads (12 months):** {{ site.data.citations.repec.downloads_12mo }}
- **Abstract Views:** {{ site.data.citations.repec.abstract_views }}

*Last updated: {{ site.data.citations.google_scholar.last_updated }}*
{% endif %}
```

#### Option B: Automated Update (GitHub Actions)

Both **RePEc/LogEc** and **Google Scholar** can be updated automatically:

| Source | Script | API Required |
|--------|--------|-------------|
| RePEc/LogEc | `scripts/fetch_repec_stats.py` | None (free) |
| Google Scholar | `scripts/fetch_scholar_metrics.py` | SerpAPI (free tier: 100/mo) |

The automated pipeline fetches:
1. **RePEc Author statistics** from `http://logec.repec.org/RAS/pwa88.htm`
2. **RePEc Rankings** (software downloads/abstract views, global/US)
3. **Google Scholar metrics** via SerpAPI (citations, h-index, i10-index, yearly data)

Create `.github/workflows/update-citations.yml`:
```yaml
name: Update Citation Metrics

on:
  schedule:
    - cron: '0 6 * * 1'  # Weekly on Monday at 6 AM UTC
  workflow_dispatch:  # Manual trigger

jobs:
  update-citations:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: source
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r scripts/requirements.txt
      
      - name: Fetch RePEc statistics and rankings
        run: python scripts/fetch_repec_stats.py
      
      - name: Fetch Google Scholar metrics
        if: env.SERPAPI_KEY != ''
        env:
          SERPAPI_KEY: ${{ secrets.SERPAPI_KEY }}
        run: python scripts/fetch_scholar_metrics.py
      
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add _data/citations.yml
          git diff --staged --quiet || git commit -m "chore: Update citation metrics [skip ci]"
          git push
```

**Setup for Google Scholar automation:**
1. Get a free SerpAPI key at https://serpapi.com
2. Add it as a repository secret: Settings → Secrets → `SERPAPI_KEY`

### Data Structure

The `_data/citations.yml` file stores:

```yaml
repec:
  # Individual category stats
  working_papers:
    downloads_12mo: 124
    downloads_total: 4833
    abstract_views_12mo: 569
    abstract_views_total: 15903
  software:
    downloads_12mo: 444
    downloads_total: 26886
    # ... etc
  
  # Totals
  total_downloads_12mo: 590
  total_downloads_all_time: 32265
  
  # Rankings
  rankings:
    software_global:
      rank: 27
      description: "Global ranking for software downloads (monthly)"
    software_us:
      rank: 10
      description: "US ranking for software downloads (monthly)"
```

---

### Step 3: Copilot-Assisted Update

When asking Copilot to help update metrics, use this prompt template:

```
Please help me update my publication statistics. Here are the current values:

**Google Scholar** (https://scholar.google.com/citations?user=lTKXA78AAAAJ):
- Total citations: [VALUE]
- h-index: [VALUE]
- i10-index: [VALUE]

**RePEc/IDEAS** (https://ideas.repec.org/e/pwa88.html):
- Downloads (12 months): [VALUE]
- Abstract views: [VALUE]
- Author ranking: [VALUE]

Please update the _data/citations.yml file with these values.
```

---

## File Locations

| Purpose | File Path |
|---------|-----------|
| Citation data | `_data/citations.yml` |
| OKR publications list | `_data/okr_publications.yml` |
| World Bank blog list | `_data/worldbank_blogs.yml` |
| World Bank blog content | `_data/worldbank_blogs_full.yml` |
| CV display | `_pages/cv.md` |
| About page | `_pages/about.md` |
| Schema.org data | `_includes/person-schema.html` |
| Automation | `.github/workflows/update-citations.yml` |
| RePEc fetch script | `scripts/fetch_repec_stats.py` |
| Scholar fetch script | `scripts/fetch_scholar_metrics.py` |
| World Bank OKR script | `scripts/fetch_worldbank_okr.py` |
| World Bank Blogs script | `scripts/fetch_worldbank_blogs.py` |
| Blog content script | `scripts/fetch_blog_content.py` |
| Python requirements | `scripts/requirements.txt` |

---

## Automated Pipeline

### Scripts Overview

| Script | Source | Data Retrieved |
|--------|--------|----------------|
| `fetch_repec_stats.py` | LogEc/RePEc | Downloads, views, rankings by category |
| `fetch_scholar_metrics.py` | Google Scholar | Citations, h-index, i10-index, yearly data |
| `fetch_worldbank_okr.py` | World Bank OKR | Publication count, metadata, abstracts via DSpace API |
| `fetch_worldbank_blogs.py` | World Bank Blogs | Blog posts via Blogs API (29 posts) |
| `fetch_blog_content.py` | World Bank Blogs | Full blog content scraping |

### What `fetch_repec_stats.py` Retrieves

1. **Author Statistics** (from LogEc)
   - Working papers: downloads & views (12mo + total)
   - Journal articles: downloads & views (12mo + total)
   - Books: downloads & views (12mo + total)
   - Chapters: downloads & views (12mo + total)
   - Software: downloads & views (12mo + total)

2. **Author Rankings**
   - Global software downloads ranking (monthly + total)
   - US software downloads ranking (monthly + total)
   - Global software abstract views ranking
   - US software abstract views ranking

### What `fetch_scholar_metrics.py` Retrieves

1. **All-Time Metrics**
   - Total citations
   - h-index
   - i10-index

2. **Last 5 Years Metrics**
   - Citations (5yr)
   - h-index (5yr)
   - i10-index (5yr)

3. **Historical Data**
   - Citations by year (full timeline)

**API Options:**
- **SerpAPI** (recommended): Set `SERPAPI_KEY` environment variable
- **scholarly library**: Falls back if no API key (may be blocked)
- **Manual input**: Use `--manual` flag for interactive mode

### What `fetch_worldbank_okr.py` Retrieves

1. **Publication Metadata** (via DSpace 7 REST API)
   - Publication count (34 publications)
   - Title, authors, year, type
   - DOI and handle links
   - Abstracts (truncated to 500 chars)

2. **Authorship Statistics**
   - Solo vs co-authored breakdown
   - First author count
   - Top co-authors with counts
   - Unique co-author count (76)

3. **Publication Types**
   - Working papers: 16
   - Journal articles: 2
   - Reports: 1
   - Briefs: 1
   - Other: 14

**Output Files:**
- `_data/citations.yml` (statistics only)
- `_data/okr_publications.yml` (full publication list with abstracts)

### What `fetch_worldbank_blogs.py` Retrieves

1. **Blog Post Metadata** (via World Bank Blogs API)
   - 29 total posts (24 English + 5 translations)
   - Title, URL, date, channel
   - Authors and co-authors
   - Topics and descriptions

2. **Channel Distribution**
   - Education for Global Development: 14
   - Let's Talk Development: 8
   - Data Blog: 3
   - Latin America and Caribbean: 2
   - All About Finance: 1
   - Voices: 1

3. **Timeline**
   - First post: 2012
   - Latest post: 2023

**API Details:**
- Endpoint: `https://webapi.worldbank.org/aemsite/blogs/global/search`
- Key: `a02440fa123c4740a83ed288591eafe4`
- Author GUID: `51402549393fa514d4308c0d3cb9c35d`

**Output Files:**
- `_data/worldbank_blogs.yml` (metadata only)
- `_data/worldbank_blogs_full.yml` (with full content)

### Running Locally

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Run RePEc script (no API key needed)
python scripts/fetch_repec_stats.py

# Run Google Scholar script
# Option 1: With SerpAPI (recommended)
export SERPAPI_KEY=your_key_here  # or use .env file
python scripts/fetch_scholar_metrics.py

# Option 2: Manual input mode
python scripts/fetch_scholar_metrics.py --manual

# Run World Bank OKR script
python scripts/fetch_worldbank_okr.py          # Stats only
python scripts/fetch_worldbank_okr.py --list   # Export full list with abstracts

# Run World Bank Blogs script
python scripts/fetch_worldbank_blogs.py                    # Stats only
python scripts/fetch_worldbank_blogs.py --list             # Export to YAML
python scripts/fetch_worldbank_blogs.py --update-citations # Update citations.yml

# Fetch full blog content
python scripts/fetch_blog_content.py           # Creates worldbank_blogs_full.yml
```

**Windows PowerShell:**
```powershell
# Load from .env file and run
Get-Content .env | ForEach-Object { if ($_ -match '^([^#][^=]+)=(.*)$') { [Environment]::SetEnvironmentVariable($matches[1], $matches[2]) } }
python scripts/fetch_scholar_metrics.py
```

### GitHub Actions Schedule

The workflow runs automatically:
- **Weekly**: Every Monday at 6:00 AM UTC
- **Manual**: Can be triggered via GitHub Actions "Run workflow" button

---

## Update Schedule

| Task | Frequency | Responsible |
|------|-----------|-------------|
| Google Scholar metrics | Monthly | Manual or automated |
| RePEc statistics | Monthly | Manual |
| ORCID verification | Quarterly | Manual |
| New publications to BibTeX | As published | Manual |

---

## Quality Checks

Before committing updates:

1. **Verify data accuracy**: Cross-check numbers with source platforms
2. **Check for anomalies**: Large jumps may indicate errors or viral papers
3. **Update timestamps**: Always update `last_updated` field
4. **Test locally**: Run `bundle exec jekyll serve` to verify display

---

## Troubleshooting

### Google Scholar Scraping Issues
- Google Scholar blocks automated access; use `scholarly` library with proxies
- Consider manual updates for reliability

### RePEc Data
- Data updates monthly; check their update schedule
- Some metrics have delayed reporting

### Missing Publications
- Add to `_bibliography/references.bib`
- Ensure BibTeX key is unique
- Run build to verify no parsing errors

---

## Example Update Session

```bash
# 1. Create/update the data file
# Edit _data/citations.yml with new values

# 2. Test locally
bundle exec jekyll serve

# 3. Verify display on http://localhost:4000/cv/

# 4. Commit changes
git add _data/citations.yml
git commit -m "chore: Update citation metrics - [DATE]"
git push origin source
```

---

## Related Links

- [Google Scholar Profile](https://scholar.google.com/citations?user=lTKXA78AAAAJ)
- [RePEc/IDEAS Profile](https://ideas.repec.org/e/pwa88.html)
- [World Bank OKR Profile](https://openknowledge.worldbank.org/entities/person/360f7a2e-0784-56e1-acf4-7f805fd50257)
- [World Bank Blogs Author Page](https://blogs.worldbank.org/en/team/j/joao-pedro-azevedo)
- [ORCID Profile](https://orcid.org/0000-0003-2111-0596)
- [scholarly Python package](https://github.com/scholarly-python-package/scholarly)

---

## Future Enhancements

**Completed:**
- [x] Google Scholar automated fetching (via SerpAPI)
- [x] Track abstract views rankings (global/US)
- [x] Track work counts by category
- [x] World Bank OKR publication count (via DSpace API)
- [x] World Bank OKR publication metadata and abstracts
- [x] World Bank Blogs harvesting (via Blogs API)
- [x] Full blog content extraction

**Potential additions:**
- [ ] Track working papers rankings (global/US)
- [ ] Track journal articles rankings (global/US)
- [ ] Track books rankings
- [ ] World Bank OKR download statistics (requires authentication)
- [ ] Add Scopus/Web of Science integration
- [ ] Display citation metrics on CV page with Liquid templates
- [ ] Add citation trend charts/visualizations
- [ ] UNICEF publications harvesting
