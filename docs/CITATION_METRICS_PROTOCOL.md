# Publication Statistics Update Protocol

This document outlines the protocol for updating publication statistics on jpazvd.github.io from various academic platforms.

## Data Sources

### Primary Sources

| Platform | Profile URL | Metrics Available |
|----------|-------------|-------------------|
| **Google Scholar** | https://scholar.google.com/citations?user=lTKXA78AAAAJ | Citations, h-index, i10-index, per-paper citations |
| **RePEc/IDEAS** | https://ideas.repec.org/e/pwa88.html | Downloads, citations, rankings, abstract views |
| **ORCID** | https://orcid.org/0000-0003-2111-0596 | Verified publication list, employment history |
| **ResearchGate** | (if applicable) | Reads, citations, Research Interest score |
| **Scopus** | (Author ID needed) | h-index, citations, documents |
| **Web of Science** | (ResearcherID needed) | h-index, citations |

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

The automated pipeline fetches:
1. **Author statistics** from `http://logec.repec.org/RAS/pwa88.htm`
2. **Global software ranking** from LogEc ranking pages
3. **US software ranking** from LogEc ranking pages

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
        run: |
          pip install requests beautifulsoup4 pyyaml
      
      - name: Fetch RePEc statistics and rankings
        run: python scripts/fetch_repec_stats.py
      
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add _data/citations.yml
          git diff --staged --quiet || git commit -m "chore: Update citation metrics [skip ci]"
          git push
```

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
| CV display | `_pages/cv.md` |
| About page | `_pages/about.md` |
| Schema.org data | `_includes/person-schema.html` |
| Automation | `.github/workflows/update-citations.yml` |
| RePEc fetch script | `scripts/fetch_repec_stats.py` |
| Scholar fetch script | `scripts/fetch_scholar_metrics.py` |
| Python requirements | `scripts/requirements.txt` |

---

## Automated Pipeline

### What the Script Fetches

The `scripts/fetch_repec_stats.py` script automatically retrieves:

1. **Author Statistics** (from LogEc)
   - Working papers: downloads & views (12mo + total)
   - Journal articles: downloads & views (12mo + total)
   - Books: downloads & views (12mo + total)
   - Chapters: downloads & views (12mo + total)
   - Software: downloads & views (12mo + total)

2. **Author Rankings**
   - Global software downloads ranking
   - US software downloads ranking
   - Global all-works ranking

### Running Locally

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Run the script
python scripts/fetch_repec_stats.py
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
- [ORCID Profile](https://orcid.org/0000-0003-2111-0596)
- [scholarly Python package](https://github.com/scholarly-python-package/scholarly)
