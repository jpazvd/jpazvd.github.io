# Website Data Databases — Complete Documentation

**Author:** João Pedro Azevedo  
**Last Updated:** December 24, 2025  
**Purpose:** Master reference for all data files in `_data/` folder and their contents, relationships, and usage

---

## Table of Contents

1. [Overview & Architecture](#overview--architecture)
2. [Database Inventory](#database-inventory)
3. [Primary Databases (Page Content)](#primary-databases-page-content)
4. [Metadata & Auxiliary Databases](#metadata--auxiliary-databases)
5. [Data Relationships & Connections](#data-relationships--connections)
6. [Usage Guide by Page](#usage-guide-by-page)
7. [Python Scripts & Automation](#python-scripts--automation)
8. [Archived Files](#archived-files)
9. [Setup & Installation](#setup--installation)

---

## Overview & Architecture

Your `_data/` folder contains **30+ YAML and auxiliary files** organized into three categories:

| Category | Purpose | Files | Usage |
|----------|---------|-------|-------|
| **Primary Content** | Main website page data | teaching.yml, events.yml, etc. | Populate `/teaching/`, `/events/`, `/blogs/` pages |
| **Metadata** | Biographical & profile data | citations.yml, work_experience.yml | CV, about page, resume |
| **Auxiliary** | Navigation, config, utilities | navigation.yml, ui-text.yml | Site structure, UI text, build scripts |

---

## Database Inventory

### PRIMARY DATABASES (Page Content Generators)

#### 1. **teaching.yml** — Teaching & Mentoring Experience
- **Location:** `_data/teaching.yml`
- **Records:** 13 entries
- **Purpose:** Teaching courses, seminars, professional training, supervision, mentoring
- **Key Fields:**
  - `id` — Unique identifier (kebab-case)
  - `course_title`, `institution`, `country`
  - `year`, `date_start`, `date_end`
  - `level` — undergraduate | graduate | professional | executive
  - `role` — Instructor | Co-instructor | Specialist Trainer | Co-Advisor | Committee Member
  - `description` — Course overview and learning objectives
  - `tags` — Thematic filters (statistics, methodology, governance, policy, etc.)
  - `pedagogical_approach`, `student_demographics`, `duration_hours`
  - `urls` — Links to syllabus, materials, recordings
  - `evidence` — File paths to saved documents
- **Uses:** `/teaching/` page with interactive filters by level, role, tags
- **Status:** ✅ Complete, production-ready

#### 2. **events.yml** — Speaking Engagements & Conferences
- **Location:** `_data/events.yml`
- **Records:** 71 entries
- **Purpose:** Conference presentations, keynotes, panel discussions, webinars, university talks
- **Key Fields:**
  - `id` — Unique identifier
  - `date`, `year`, `event`, `location`, `venue`
  - `event_type` — conference | summit | workshop | webinar | keynote | panel | guest_lecture
  - `session_title`, `presentation_title`, `abstract`
  - `role` — Speaker | Panelist | Keynote | Chair | Organizer
  - `affiliation`, `affiliation_role` — Your org/role at time of event
  - `participants` — Other speakers/panelists
  - `tags` — Learning, statistics, governance, poverty, etc.
  - `urls` — Event page, slides, recording, news coverage
  - `evidence` — Files saved locally (invitation, program, slides, photo)
- **Uses:** `/events/` page with filtering by year, event type, scope, tags
- **Status:** ✅ Complete, production-ready

#### 3. **github_repos.yml** — Software Repositories
- **Location:** `_data/github_repos.yml`
- **Records:** 40+ repositories
- **Purpose:** GitHub repositories for Stata packages, tools, research code, data utilities
- **Key Fields:**
  - `name` — Repository name
  - `description` — What the package/tool does
  - `tags` — stata-packages | data-tools | poverty | inequality | visualization | etc.
  - `keywords` — Search terms (gini, theil, fgt, etc.)
  - `featured` — true/false for homepage highlighting
  - `url` — GitHub link
- **Organization:** Grouped by category:
  - **Stata Packages** — Poverty & inequality (apoverty, ainequal, adecomp, etc.)
  - **Data Tools** — API access (wbopendata), surveys, harmonization
  - **Research Projects** — MCCHI, education analytics, climate hazard
  - **Utilities** — Scripts, helpers, templates
- **Uses:** `/softwares/` page, software directory with repo cards and filtering
- **Status:** ✅ Complete, production-ready

#### 4. **worldbank_blogs.yml** — World Bank Blog Posts
- **Location:** `_data/worldbank_blogs.yml`
- **Records:** 24 posts (English), 5 translations
- **Purpose:** Articles published on World Bank blogs by topic/channel
- **Key Fields:**
  - `title`, `url`, `date`, `year`
  - `channel` — "Education for Global Development", "Let's Talk Development", etc.
  - `description` — Post summary
  - `authors` — Co-authors list

#### 5. **publications.yml** — Academic Publications & Research Output [GENERATED]
- **Location:** `_data/publications.yml`
- **Records:** 58+ total (auto-consolidated from satellite databases)
- **Purpose:** Master publication database for research profile, CV, citations (GENERATED FILE)
- **Generation:** Run `python scripts/build_publications_master.py` to regenerate from satellites
- **DO NOT EDIT:** This file is auto-generated. Edit satellite databases or publications_manual.yml instead.
- **Key Fields:**
  - `id` — Unique identifier (kebab-case)
  - `type` — journal_article | book | book_chapter | conference_paper | working_paper | software
  - `authors` — Author list (structured)
  - `year`, `title`, `journal`, `publisher`, `venue`
  - `pages`, `volume`, `issue`, `doi`
  - `citations` — Citation count (Google Scholar or RePec)
  - `downloads` — Download count (for software/working papers)
  - `tags` — Research themes (learning_poverty, inequality, microfinance, policy_evaluation, etc.)
  - `language`, `country` — Publication language/location
  - `urls` — PDF, journal link, RePEc, SSRN, etc.
  - `peer_reviewed` — true/false flag
  - `research_theme` — Structured taxonomy (6 themes)
- **Organization:** Grouped by publication type (journal articles, books, book chapters, conference papers, software, working papers)
- **Uses:** `/publications/` page, CV generation, research profile, filtering by type/theme/year/citations
- **Status:** ✅ Initial version complete, 105 working papers to import from RePEc API

#### 6. **publications_manual.yml** — Manual Publication Overrides
- **Location:** `_data/publications_manual.yml`
- **Records:** 25+ entries (books, chapters, conference papers)
- **Purpose:** Hand-curated publications NOT available in automated satellite databases
- **Authority:** Source of truth for books, book chapters, conference papers, historical publications
- **DO NOT ADD:** Working papers (use okr_publications.yml), software (use stata_help_files.yml), or journal articles already in OKR/RePEc
- **Key Sections:**
  - `journal_articles` — Only if NOT in OKR or RePEc
  - `books` — Monographs, edited volumes, policy reports
  - `book_chapters` — Chapters in edited volumes
  - `conference_papers` — Conference presentations
- **Workflow:** Add entries here manually → Run build_publications_master.py → Generated publications.yml includes these entries
- **Uses:** Input to publications.yml generation
- **Status:** ✅ Complete, actively maintained

#### 7. **honors_awards.yml** — Professional Distinctions & Recognition
- **Location:** `_data/honors_awards.yml`
- **Records:** 15 total (2 executive positions, 3 memberships, 4 research impact rankings, 8 fellowships, 2 awards)
- **Purpose:** Professional recognition, honors, memberships, fellowships, research impact metrics
- **Key Fields:**
  - `id` — Unique identifier
  - `category` — executive_position | professional_membership | research_impact | fellowship | grant | award
  - `title`, `organization`
  - `year`, `year_end`, `status` — current | completed
  - `level` — international | national | institutional
  - `description` — Details and significance
  - `amount` — Monetary value (for grants/fellowships)
  - `url` — Link to announcement or certificate
  - `tags` — Thematic tags
- **Major Entries:**
  - UNICEF Chief Statistician (2023-present)
  - World Bank Lead Economist & EdTech Fellow (2018-2023)
  - ISA Elected Member (2020-present)
  - RePEc Top 5% Authors (#6 US software downloads, #19 global)
  - Google Scholar h-index 30 (5,555 citations)
  - ORSAS Fellowships (2002-2003)
  - Newcastle University Studentships (2001-2003)
  - CNPq Research Scholarships (1996-2001)
- **Uses:** `/cv/` page, awards section, research impact highlights
- **Status:** ✅ Complete, production-ready
  - `topics` — Education, Digital Development, Data, etc.
  - `language` — en (with translations noted)
- **Uses:** `/blogs/` page with filtering by year, channel, topic
- **Status:** ✅ Complete

#### 5. **other_blogs.yml** & **linkedin_blogs.yml** — Blog Aggregates
- **Location:** `_data/other_blogs.yml`, `_data/linkedin_blogs.yml`
- **Records:** other_blogs ~15, linkedin_blogs ~12
- **Purpose:** Blog posts from non-WB sources (Brookings, LinkedIn, medium, etc.)
- **Key Fields:** Similar to worldbank_blogs (title, url, date, organization, topics)
- **Uses:** Combined with WB blogs in `/blogs/` aggregate view
- **Status:** ✅ Complete

---

### METADATA & AUXILIARY DATABASES

#### 6. **citations.yml** — Publication & Impact Metrics
- **Location:** `_data/citations.yml`
- **Records:** Aggregated metrics
- **Purpose:** Google Scholar, RePEc, ORCID, World Bank publication statistics
- **Key Fields:**
  - `google_scholar` — total_citations (5555), h_index (30), citations_by_year
  - `repec` — working_papers (105), journal_articles (10), software (22), downloads, rankings
  - `world_bank_okr` — publication_count (34), by_type, by_year
  - `orcid` — ORCID profile info
- **Uses:** `/publications/` page (metrics dashboard), CV, research impact section
- **Status:** ✅ Complete, updated 2025-12-10

#### 7. **work_experience.yml** — Career Positions
- **Location:** `_data/work_experience.yml`
- **Records:** 9 positions
- **Purpose:** Job history from UFF (2000) to UNICEF (2023-present)
- **Key Fields:**
  - `position`, `organization`, `location`, `start_date`, `end_date`
  - `description` — Role summary, responsibilities, achievements
- **Uses:** `/about/` page (career timeline), CV, resume
- **Status:** ✅ Complete

#### 8. **education.yml** — Educational Background
- **Location:** `_data/education.yml`
- **Records:** 3 degrees
- **Purpose:** Formal education (BA, MA, PhD)
- **Key Fields:**
  - `degree`, `institution`, `year`, `field`, `focus`
  - `advisor`, `thesis_title`
- **Uses:** `/about/` page, CV
- **Status:** ✅ Complete

#### 9. **profile.yml** — Personal Profile & Bio
- **Location:** `_data/profile.yml`
- **Records:** 1 record
- **Purpose:** Personal branding, short bio, social links
- **Key Fields:**
  - `name`, `title`, `bio` (short & long versions)
  - `current_role`, `affiliation`, `location`
  - `social_links` — Twitter, GitHub, LinkedIn, ORCID, Google Scholar
  - `email`, `phone`
- **Uses:** Header, footer, about page, meta tags
- **Status:** ✅ Complete

#### 10. **authors.yml** — Co-Author Registry
- **Location:** `_data/authors.yml`
- **Records:** ~50+ co-authors
- **Purpose:** Standardized author names across publications, events, blogs
- **Key Fields:**
  - `first_name`, `last_name`, `affiliation`, `country`, `orcid`
  - `urls` — Personal website, Google Scholar, ORCID
- **Uses:** Normalize author names in publications.yml, teaching.yml, events.yml
- **Status:** ✅ Complete

#### 11. **skills.yml** — Professional Skills & Competencies
- **Location:** `_data/skills.yml`
- **Records:** Multiple skill categories
- **Purpose:** Technical skills, languages, certifications
- **Key Fields:**
  - `category` — Programming, Statistics, Languages, Tools, Methodologies
  - `skills` — List with proficiency levels
- **Uses:** `/about/` skills section, resume
- **Status:** ✅ Complete

#### 12. **stata_help_files.yml** — Stata ADO Documentation
- **Location:** `_data/stata_help_files.yml`
- **Records:** 20+ Stata modules
- **Purpose:** Detailed technical documentation of Stata packages (from `.sthlp` help files)
- **Key Fields:**
  - `module_name`, `version`, `author`, `date`
  - `description` — Short and long descriptions
  - `syntax` — Command syntax and options
  - `examples` — Code examples
  - `related_commands`, `see_also`
  - `citations` — Papers citing this module
  - `downloads` — Download statistics
- **Uses:** Software page (Stata modules detail view), documentation links
- **Status:** ✅ Complete

---

### AUXILIARY & CONFIGURATION FILES

#### 13. **navigation.yml** — Site Navigation Structure
- **Location:** `_data/navigation.yml`
- **Records:** Menu items
- **Purpose:** Define top navigation, sidebars, menus
- **Uses:** Layout templates, navigation rendering
- **Status:** ✅ Complete

#### 14. **ui-text.yml** — UI Text & Labels
- **Location:** `_data/ui-text.yml`
- **Records:** Text strings
- **Purpose:** Site-wide button labels, placeholders, messages
- **Uses:** Consistent UI text across pages
- **Status:** ✅ Complete

#### 15. **okr_publications.yml** — World Bank OKR Publication List
- **Location:** `_data/okr_publications.yml`
- **Records:** 34 publications from World Bank Open Knowledge Repository
- **Purpose:** Official World Bank publications
- **Uses:** Publications page (WB section)
- **Status:** ✅ Complete

---

### BACKUP & LEGACY FILES (Not actively used)

- `events-new.yml`, `events-old.yml`, `teaching-new.yml` — Version control / backups
- `events-new-v2.yml` — Alternative event format (testing)
- `other_blogs_full.yml`, `worldbank_blogs_full.yml` — Unfiltered versions
- `README_SOFTWARE_DATABASE.md` — This file

---

## Data Relationships & Connections

### Connection Map

```
Profile Tier (1-of-1 person)
├── profile.yml ...................... Personal identity, bio, social links
├── authors.yml ...................... Normalize your name across all records
├── education.yml .................... Formal degrees
└── work_experience.yml .............. Career positions

Content Tier (Many records)
├── teaching.yml ..................... Teaching & mentoring (13 entries)
├── events.yml ....................... Speaking engagements (71 entries)
├── worldbank_blogs.yml .............. WB blogs (24 entries)
├── other_blogs.yml .................. Non-WB blogs (~15 entries)
├── linkedin_blogs.yml ............... LinkedIn articles (~12 entries)
├── github_repos.yml ................. Software repos (40+ entries)
├── stata_help_files.yml ............ Stata module docs (20+ entries)
├── publications.yml ................. Academic output (166 entries) 🆕
└── honors_awards.yml ................ Professional recognition (15 entries) 🆕

Metadata Tier (Impact & Verification)
├── citations.yml .................... Google Scholar, RePEc, ORCID metrics
├── skills.yml ....................... Technical competencies
├── okr_publications.yml ............. WB Open Knowledge Repository
└── authors.yml ...................... Verify co-author information

Configuration Tier
├── navigation.yml ................... Site menu structure
└── ui-text.yml ...................... Button labels, messages
```

### How Files Work Together

**Example 1: Publishing a Teaching Course**
1. Add record to `teaching.yml` with course details, tags, dates
2. Tags link to `/teaching/` page filters
3. Could also add to `events.yml` if it's a one-time workshop
4. Reference co-instructors via `authors.yml` if needed

**Example 2: Adding a Blog Post**
1. Post on World Bank blog → Add to `worldbank_blogs.yml`
2. Re-posted on LinkedIn → Add to `linkedin_blogs.yml`
3. Both appear in `/blogs/` with source differentiation
4. Author name normalized via `authors.yml`

**Example 3: Tracking Software Impact**
1. Create Stata module → Add to `github_repos.yml`
2. Add detailed docs → Create entry in `stata_help_files.yml`
3. Module published on SSC/RePEc → Track in `stata_help_files.yml` (downloads, citations)
4. Citation growth tracked in `citations.yml` (repec.software.downloads)

**Example 4: Publishing a Paper**
1. Paper published in journal → Add to `publications.yml` (type: journal_article)
2. Working paper version on RePEc → Add to `publications.yml` (type: working_paper)
3. Related software module → Cross-reference in `github_repos.yml` + `publications.yml` (type: software)
4. Citation counts tracked → `citations.yml` + `publications.yml` (citations field)
5. Paper wins award → Add to `honors_awards.yml` (category: award)

**Example 5: CV Generation**
- **Education section** ← `education.yml`
- **Experience section** ← `work_experience.yml` + `honors_awards.yml` (executive positions)
- **Teaching section** ← `teaching.yml` (filtered by role type)
- **Speaking section** ← `events.yml` (filtered by event_type)
- **Publications section** ← `publications.yml` (filtered by type: articles, books, chapters, software)
- **Honors & Awards section** ← `honors_awards.yml` (fellowships, memberships, research impact)
- **Research Impact section** ← `citations.yml` + `honors_awards.yml` (rankings, h-index, downloads)
- **Skills section** ← `skills.yml`

---

## Usage Guide by Page

| Page | Source Files | Updates Needed? |
|------|-------------|-----------------|
| `/` (Homepage) | `profile.yml`, `github_repos.yml` (featured), `events.yml` (recent) | Quarterly |
| `/about/` | `profile.yml`, `work_experience.yml`, `education.yml`, `skills.yml` | As needed |
| `/teaching/` | `teaching.yml` (main) | Add entry per teaching event |
| `/events/` | `events.yml` (main) | Add entry per speaking engagement |
| `/blogs/` | `worldbank_blogs.yml`, `linkedin_blogs.yml`, `other_blogs.yml` | When posting |
| `/softwares/` | `github_repos.yml` (main), `stata_help_files.yml` (detail) | As repos/modules change |
| `/publications/` | `publications.yml` (main), `citations.yml` (metrics), `honors_awards.yml` (impact) | Quarterly via RePEc API |
| `/cv/` | All files (dynamic generation) + `honors_awards.yml` | Auto-updated |

---

## Maintenance Workflow

### Adding New Records

**Teaching/Event:**
```yaml
- id: unique-kebab-case-id
  date_start: YYYY-MM-DD          # or year: YYYY
  institution: Official Name
  title: Official Title
  role: Instructor | Panelist | Speaker
  tags: [tag1, tag2, tag3]         # Use existing tags for consistency
  description: Brief description
  urls:
    event: https://...
  evidence:
    slides: path/to/local/file
```

**Blog Post:**
```yaml
- title: "Post Title"
  url: https://...
  date: YYYY-MM-DD
  year: YYYY
  channel: "Publication Name"
  authors: ["Your Name", "Co-Author"]
  topics: [Topic1, Topic2]
  description: Summary
```

**Software Repo:**
```yaml
- name: repo-name
  description: "What it does"
  tags: [tag1, tag2]               # Pick from existing tag taxonomy
  keywords: [keyword1, keyword2]
  url: https://github.com/...
  featured: true|false
```

### Validation Checklist

Before committing new records:

- [ ] IDs are unique and kebab-case
- [ ] Dates are ISO format (YYYY-MM-DD)
- [ ] Tags match existing taxonomy (no new tags without approval)
- [ ] Author names match `authors.yml` spelling
- [ ] URLs are valid and https://
- [ ] Required fields filled (id, date, title, role/type)
- [ ] No duplicate records
- [ ] No trailing spaces or inconsistent formatting

---

## Import/Export Patterns

### Importing from External Sources

- **Google Scholar** → `citations.yml` (manual copy of metrics)
- **World Bank Blog platform** → `worldbank_blogs.yml` (semi-automated via API)
- **GitHub** → `github_repos.yml` (manual with GitHub Topics reference)
- **LinkedIn** → `linkedin_blogs.yml` (manual export)
- **Lattes CV** → Can populate `teaching.yml`, `work_experience.yml` (manual extraction)

### Exporting to External Formats

- → **CV/Resume** — Jekyll builds from all databases
- → **LinkedIn** — Copy from `work_experience.yml`, `teaching.yml`
- → **Google Scholar** — Manual profile updates
- → **ORCID** — Manual profile updates, reference `publications.yml` (when created)

---

## Future Databases to Create

| Database | Purpose | Priority | Status |
|----------|---------|----------|--------|
| ~~`publications.yml`~~ | Full publication list (journal articles, books, chapters, conferences, working papers, software) | ~~🔴 High~~ | ✅ **Created** Dec 24, 2025 |
| ~~`honors_awards.yml`~~ | Grants, fellowships, recognitions, memberships, executive positions | ~~🟡 Medium~~ | ✅ **Created** Dec 24, 2025 |
| `projects.yml` | Research projects with funding, dates, outcomes, collaborators | 🟡 Medium | 🔄 Planned |
| `media_appearances.yml` | Interviews, podcasts, news mentions, press coverage | 🟠 Low | 🔄 Planned |

---

## File Statistics

- **Total YAML files:** 17+ (15 legacy + publications.yml + honors_awards.yml)
- **Total records:** 380+ (200 legacy + 166 publications + 15 honors)
- **Total backup/legacy files:** 8
- **Folder size:** ~600 KB
- **Last comprehensive update:** December 24, 2025

---

## Python Scripts & Automation

All Python scripts are located in `/scripts/` folder and are organized into three categories: **data maintenance scripts**, **data fetching/generation scripts**, and **data consolidation scripts**.

### Overview of Scripts

| Script | Purpose | YAML Input | YAML Output | Frequency |
|--------|---------|-----------|-------------|-----------|
| **add_blank_lines.py** | Format YAML files with proper spacing | events-new.yml | events-new.yml | Manual |
| **find_years.py** | Audit years in events database | events.yml | Console output | Manual (QA) |
| **fix_chronology.py** | Sort events by year and date (newest first) | events-new.yml | events-new.yml | Manual |
| **fix_spacing.py** | Add blank lines between YAML list items | events-new.yml | events-new.yml | Manual |
| **verify_sort.py** | Validate events are sorted correctly by year/date | events-new.yml | Console output | Manual (QA) |
| **fetch_worldbank_blogs.py** | Pull latest WB blog posts | — | worldbank_blogs.yml | Quarterly |
| **fetch_worldbank_okr.py** | Pull WB Open Knowledge Repository publications | — | okr_publications.yml | Quarterly |
| **fetch_scholar_metrics.py** | Update Google Scholar citation metrics | — | citations.yml (google_scholar) | Monthly |
| **fetch_repec_stats.py** | Update RePEc download/citation statistics | — | citations.yml (repec) | Monthly |
| **fetch_citations.py** | Consolidate citation data | — | citations.yml (master) | Monthly |
| **fetch_blog_content.py** | Archive blog post full text | worldbank_blogs.yml | Blog markdown files | Quarterly |
| **fetch_linkedin_content.py** | Pull LinkedIn articles | — | linkedin_blogs.yml | Quarterly |
| **fetch_unicef_blogs.py** | Pull UNICEF blog posts (if applicable) | — | YAML (if needed) | As needed |
| **scrape_stata_help_files.py** | Extract Stata module documentation | Stata .sthlp files | stata_help_files.yml | When packages updated |
| **generate_cv_pdf_content.py** | Build CV content from all databases | All YAML files | CV markdown | As needed |

---

### Maintenance Scripts (Data Formatting & Validation)

These scripts are used to **maintain YAML file quality**, formatting, and correctness. Run them after bulk edits or imports.

#### 1. **add_blank_lines.py** — YAML Formatting
- **Location:** `scripts/add_blank_lines.py`
- **Purpose:** Ensure proper spacing between list items in YAML for readability
- **Input:** `events-new.yml` (or any YAML file)
- **Output:** Reformatted YAML with blank lines between entries
- **Run:** `python scripts/add_blank_lines.py`
- **When:** After manually editing YAML files with many entries
- **Example:**
  ```yaml
  # Before: entries crammed together
  events:
  - id: event1
    date: 2025-01-15
  - id: event2
    date: 2025-01-10
  
  # After: proper spacing
  events:
  - id: event1
    date: 2025-01-15

  - id: event2
    date: 2025-01-10
  ```

#### 2. **fix_chronology.py** — Sort Events by Date
- **Location:** `scripts/fix_chronology.py`
- **Purpose:** Reorder events by **year (descending)** then **date within year (newest first)**
- **Input:** `events-new.yml`
- **Output:** `events-new.yml` (sorted)
- **Run:** `python scripts/fix_chronology.py`
- **When:** After adding new events, before deploying
- **Key Logic:**
  1. Group events by year
  2. Sort each year's events by date (newest → oldest)
  3. Reconstruct YAML with years in descending order (2025 → 2024 → 2023...)
- **Console Output:**
  ```
  ✅ Events reordered by year and date (newest first within each year)
  
  Total events: 71
  
  Events by year:
    2025: 8 events
    2024: 15 events
    2023: 18 events
    ...
  ```

#### 3. **find_years.py** — Audit Years in Database
- **Location:** `scripts/find_years.py`
- **Purpose:** Extract and validate all unique years in events.yml
- **Input:** `events.yml`
- **Output:** Console list of years and line numbers
- **Run:** `python scripts/find_years.py`
- **When:** QA before publishing; to verify year coverage
- **Console Output:**
  ```
  Years found: [2025, 2024, 2023, 2022, 2021, 2020, 2019, ...]
  
  First occurrence of each year:
  2025: line 142
  2024: line 287
  2023: line 512
  ...
  ```

#### 4. **fix_spacing.py** — Whitespace Normalization
- **Location:** `scripts/fix_spacing.py`
- **Purpose:** Ensure consistent blank lines and indentation throughout YAML
- **Input:** `events-new.yml`
- **Output:** `events-new.yml` (normalized)
- **Run:** `python scripts/fix_spacing.py`
- **When:** After mass find-replace edits; to clean up formatting

#### 5. **verify_sort.py** — Validation (QA)
- **Location:** `scripts/verify_sort.py`
- **Purpose:** Check that events are sorted correctly
- **Input:** `events-new.yml`
- **Output:** Console validation report
- **Run:** `python scripts/verify_sort.py`
- **When:** Before publishing; as pre-commit check
- **Console Output:**
  ```
  📅 2025 Events (8 total):
    1. 2025-12-15 - unsc-ai-summit-2025
    2. 2025-11-22 - lacaea-nov-2025
    3. 2025-10-08 - unicef-stats-workshop
    ...
  ✅ SORTED
  
  📅 2024 Events (15 total):
    1. 2024-12-10 - worldbank-end-year
    ...
  ✅ SORTED
  ```

---

### Data Fetching Scripts (Auto-Populate YAML Files)

These scripts **pull data from external APIs and sources** and populate/update YAML files automatically. Schedule them regularly to keep data fresh.

#### 6. **fetch_worldbank_blogs.py** — World Bank Blog Posts
- **Location:** `scripts/fetch_worldbank_blogs.py`
- **Purpose:** Query World Bank Blogs API and populate `worldbank_blogs.yml`
- **Input:** World Bank Blogs API (`https://webapi.worldbank.org/aemsite/blogs/global/search`)
- **Output:** `_data/worldbank_blogs.yml`
- **Run:** `python scripts/fetch_worldbank_blogs.py`
- **Dependencies:** requests, yaml
- **Frequency:** Quarterly (manually)
- **Fields Updated:**
  - title, url, date, year, channel, description, authors, topics, language
- **Notes:** Handles translations by linking parent/child relationships

#### 7. **fetch_worldbank_okr.py** — WB Open Knowledge Repository
- **Location:** `scripts/fetch_worldbank_okr.py`
- **Purpose:** Pull official World Bank publications from OKR
- **Input:** WB Open Knowledge Repository API
- **Output:** `_data/okr_publications.yml`
- **Run:** `python scripts/fetch_worldbank_okr.py`
- **Dependencies:** requests, yaml
- **Frequency:** Quarterly (manually)
- **Fields Updated:**
  - title, url, year, publication_type, description, authors, topics

#### 8. **fetch_scholar_metrics.py** — Google Scholar Stats
- **Location:** `scripts/fetch_scholar_metrics.py`
- **Purpose:** Update citation count, h-index, i10-index from Google Scholar
- **Input:** Google Scholar profile (https://scholar.google.com/citations?user=lTKXA78AAAAJ)
- **Output:** `_data/citations.yml` (google_scholar section)
- **Run:** `python scripts/fetch_scholar_metrics.py`
- **Dependencies:** scholarly (or selenium/BeautifulSoup), yaml
- **Frequency:** Monthly
- **Fields Updated:**
  - total_citations, h_index, i10_index, citations_5yr, h_index_5yr, i10_index_5yr
  - citations_by_year (dictionary of year → count)
  - last_updated (timestamp)
- **Notes:** May require proxy/delay to avoid IP blocking by Google Scholar

#### 9. **fetch_repec_stats.py** — RePEc Publication Stats
- **Location:** `scripts/fetch_repec_stats.py`
- **Purpose:** Update download counts and rankings from RePEc
- **Input:** RePEc Author Stats API (http://logec.repec.org/RAS/pwa88.htm)
- **Output:** `_data/citations.yml` (repec section)
- **Run:** `python scripts/fetch_repec_stats.py`
- **Dependencies:** requests, BeautifulSoup, yaml
- **Frequency:** Monthly
- **Fields Updated:**
  - working_papers.count, downloads_12mo, downloads_total
  - journal_articles.count, downloads, citations
  - software.count, downloads, abstract_views
  - rankings (by category: software, all_publications)
  - last_updated

#### 10. **fetch_citations.py** — Master Citation Consolidation
- **Location:** `scripts/fetch_citations.py`
- **Purpose:** Consolidate and merge citation data from all sources
- **Input:** Multiple citation sources (Google Scholar, RePEc, ORCID, WB OKR)
- **Output:** `_data/citations.yml` (master file)
- **Run:** `python scripts/fetch_citations.py`
- **Dependencies:** requests, yaml
- **Frequency:** Monthly (after running individual fetch scripts)
- **Merges:**
  - fetch_scholar_metrics.py output
  - fetch_repec_stats.py output
  - ORCID API data
  - WB OKR publication counts

#### 11. **fetch_blog_content.py** — Blog Post Archival
- **Location:** `scripts/fetch_blog_content.py`
- **Purpose:** Download full text of blog posts and save as markdown
- **Input:** URLs from `worldbank_blogs.yml`, `linkedin_blogs.yml`, `other_blogs.yml`
- **Output:** Markdown files in `_evidence/blogs/`
- **Run:** `python scripts/fetch_blog_content.py`
- **Dependencies:** requests, BeautifulSoup, yaml, html2text
- **Frequency:** Quarterly
- **Preserves:** Title, author, date, original URL, content text

#### 12. **fetch_linkedin_content.py** — LinkedIn Articles
- **Location:** `scripts/fetch_linkedin_content.py`
- **Purpose:** Scrape LinkedIn article metadata and links
- **Input:** LinkedIn author profile or article URLs
- **Output:** `_data/linkedin_blogs.yml`
- **Run:** `python scripts/fetch_linkedin_content.py`
- **Dependencies:** requests, BeautifulSoup, yaml
- **Frequency:** Quarterly
- **Notes:** LinkedIn has anti-scraping measures; may require manual entry or API authentication

#### 13. **fetch_unicef_blogs.py** — UNICEF Blog Posts (Future)
- **Location:** `scripts/fetch_unicef_blogs.py`
- **Purpose:** Pull UNICEF blog posts (if/when applicable)
- **Input:** UNICEF Blogs API (if available)
- **Output:** `_data/unicef_blogs.yml` (new file)
- **Status:** Template ready; activate as needed

#### 14. **scrape_stata_help_files.py** — Stata Module Documentation
- **Location:** `scripts/scrape_stata_help_files.py`
- **Purpose:** Extract `.sthlp` help files from installed Stata packages and build documentation database
- **Input:** Stata `.sthlp` files (from `/c/ado/plus/` directory)
- **Output:** `_data/stata_help_files.yml`
- **Run:** `python scripts/scrape_stata_help_files.py`
- **Dependencies:** os, re, yaml (Stata must be accessible)
- **Frequency:** When publishing new Stata packages
- **Extracts:**
  - Module name, version, author, date
  - Title and description
  - Syntax and options
  - Examples with code
  - Related commands
  - Citation information
  - Download statistics (from meta files if present)

#### 15. **generate_cv_pdf_content.py** — CV Generation
- **Location:** `scripts/generate_cv_pdf_content.py`
- **Purpose:** Build comprehensive CV content by combining all databases
- **Input:** All YAML files (teaching.yml, events.yml, work_experience.yml, education.yml, citations.yml, etc.)
- **Output:** CV markdown for PDF conversion
- **Run:** `python scripts/generate_cv_pdf_content.py`
- **Dependencies:** yaml, jinja2 (for templating)
- **Frequency:** On-demand; before submitting applications
- **Builds Sections:**
  - Education (from education.yml)
  - Experience (from work_experience.yml)
  - Teaching (filtered from teaching.yml)
  - Speaking/Events (filtered from events.yml)
  - Publications (from citations.yml + okr_publications.yml)
  - Skills (from skills.yml)
  - Languages (from profile.yml)

---

### Data Consolidation Scripts (Generate Master Databases from Satellites)

These scripts build **composite master databases** from multiple satellite sources (APIs, scrapers, manual files).

#### 16. **build_publications_master.py** — Publications Database Consolidator ⭐
- **Location:** `scripts/build_publications_master.py`
- **Purpose:** **CONSOLIDATE ALL PUBLICATION SOURCES INTO SINGLE MASTER DATABASE**
- **Input YAMLs (Satellite Databases - AUTHORITATIVE):**
  - `okr_publications.yml` (World Bank OKR - 34+ papers from API)
  - `stata_help_files.yml` (SSC software modules - 20+ packages from web scraper)
  - `github_repos.yml` (GitHub repositories - 40+ repos)
  - `publications_manual.yml` (Hand-curated books, chapters, conference papers NOT in APIs)
- **Output YAML:** `publications.yml` (**GENERATED FILE - DO NOT EDIT MANUALLY**)
- **Run:** `python scripts/build_publications_master.py [--dry-run] [--verbose]`
- **Dependencies:** pyyaml, rapidfuzz
- **Frequency:** **Monthly** or when satellite databases update
- **Key Features:**
  1. **Fuzzy Matching:** Deduplicates publications across sources by title/author/year similarity (85% threshold)
  2. **Metadata Enrichment:** Merges citations, downloads, URLs from multiple sources
  3. **Cross-Referencing:** Links publications to GitHub repos, Stata packages, OKR handles
  4. **Manual Override Support:** Adds books/chapters from publications_manual.yml that aren't in APIs
  5. **Source Tracking:** Marks each publication with originating databases
- **Workflow:**
  ```
  Load okr_publications.yml (33 WB papers)
  ├─→ Match existing entries by fuzzy title match
  ├─→ Merge OKR handles, DOIs, abstracts
  └─→ Mark duplicates
  
  Load stata_help_files.yml (20+ modules)
  ├─→ Extract packages with downloads/citations
  ├─→ Match to existing software entries
  └─→ Enrich with Stata-specific metadata
  
  Load github_repos.yml (40+ repos)
  ├─→ Filter for featured or stata-packages tagged repos
  ├─→ Cross-reference to publications
  └─→ Add GitHub URLs
  
  Load publications_manual.yml (25+ manual entries)
  ├─→ Books, chapters, conferences NOT in APIs
  ├─→ NO matching (authoritative manual data)
  └─→ Add directly to master
  
  Generate publications.yml
  ├─→ Organize by type (articles, books, chapters, software, working papers)
  ├─→ Sort by year (descending)
  ├─→ Add metadata header with generation timestamp
  └─→ Write with "DO NOT EDIT" warning
  ```
- **Authority Model:** **Satellite databases are source of truth** (auto-updated from APIs). Master file is regenerated, never hand-edited.
- **Statistics Example:**
  ```
  Total publications: 58
    journal_articles: 6
    books: 3
    book_chapters: 7
    conference_papers: 9
    working_papers: 33
  
  By source:
    okr: 33 new, 1 merged
    manual: 25 new, 3 merged
  ```
- **Important Notes:**
  - ⚠️ **Never manually edit publications.yml** - it will be overwritten on next run
  - ✅ **To add publications:** Edit satellite databases or publications_manual.yml
  - ✅ **To update citations:** Run fetch_scholar_metrics.py or fetch_repec_stats.py, then rebuild
  - 🔄 **After updating satellites:** Always run build_publications_master.py to regenerate

---

### Script Workflow & Automation

#### Typical Monthly Update Cycle

```
1. Fetch latest data from APIs:
   python scripts/fetch_worldbank_okr.py  → okr_publications.yml (WB papers)
   python scripts/fetch_repec_stats.py    → repec_papers.yml (RePEc working papers)
   python scripts/fetch_scholar_metrics.py → citations.yml (Google Scholar h-index)
   python scripts/scrape_stata_help_files.py → stata_help_files.yml (SSC packages)
   
2. Build master publications database:
   python scripts/build_publications_master.py --verbose → publications.yml (MASTER)
   
3. Manual events.yml edits → add new speaking engagements, teaching courses
   ↓
4. python scripts/fix_chronology.py → reorder by date
   ↓
3. python scripts/verify_sort.py → QA check
   ↓
4. python scripts/fetch_scholar_metrics.py → update Google Scholar stats
   ↓
5. python scripts/fetch_repec_stats.py → update RePEc stats
   ↓
6. python scripts/fetch_citations.py → consolidate metrics
   ↓
7. python scripts/fetch_worldbank_blogs.py → (quarterly)
   ↓
8. python scripts/fetch_blog_content.py → archive posts
   ↓
9. git add _data/*.yml && git commit → push to GitHub
   ↓
10. GitHub Actions → Jekyll builds & deploys site
```

#### Pre-Commit Automation (Future)

Consider adding a `.git/hooks/pre-commit` script to auto-run:
```bash
#!/bin/bash
# Auto-validate before commit
python scripts/verify_sort.py || exit 1
python scripts/find_years.py || exit 1
```

---

### Quick Reference: Script Dependencies

```bash
# Install all dependencies
pip install -r scripts/requirements.txt

# Core dependencies
# - PyYAML (yaml parsing)
# - requests (HTTP API calls)
# - BeautifulSoup4 (web scraping)
# - html2text (HTML → Markdown)
# - scholarly (Google Scholar scraping) [optional]
# - Jinja2 (CV templating)
```

---

### Troubleshooting Common Issues

| Issue | Script | Solution |
|-------|--------|----------|
| YAML parse error | Any | Check for misaligned indentation (2 spaces, not tabs) |
| "UnicodeDecodeError" | Any | Ensure UTF-8 file encoding; use `encoding='utf-8'` in open() |
| Google Scholar blocked | fetch_scholar_metrics.py | Add delay between requests; use proxy; switch to scholarly library |
| LinkedIn scraping fails | fetch_linkedin_content.py | LinkedIn API restricted; consider manual entry or API token |
| Events not sorted | fix_chronology.py | Verify 'date' field is ISO format (YYYY-MM-DD) and 'year' is integer |
| Blank lines removed | add_blank_lines.py | Run after YAML modifications that strip spacing |

---

## File Statistics

- **Total YAML files:** 15+
- **Total records:** 200+
- **Total Python scripts:** 15
- **Total backup/legacy files:** 8
- **Folder size:** ~500 KB (_data/) + ~150 KB (scripts/)
- **Last comprehensive update:** December 24, 2025
    tags: [tag1, tag2, tag3]            # Multiple tags for filtering
    keywords: [keyword1, keyword2]       # SEO keywords
    featured: true/false                 # Highlight on website
    
tags_vocabulary:
  - stata-packages         → SSC/RePEc published modules
  - poverty               → Poverty measurement & analysis
  - inequality            → Inequality measures
  - education             → Education/learning assessment
  - data-tools            → Data access & manipulation
  - decomposition         → Statistical decomposition
  - small-area            → Small area estimation
  - visualization         → Graphs & plotting
  - econometrics          → Econometric methods
  - world-bank            → World Bank projects
  - research              → Research projects/replication
  - utilities             → Developer tools
```

**Current Repositories by Category:**

#### Stata Packages (Poverty & Inequality)
- **wbopendata** — Access 17,000+ World Bank indicators
- **apoverty** — FGT, Watts, Sen poverty measures
- **ainequal** — Gini, Theil, Atkinson inequality indices
- **adecomp** — Shapley decomposition by welfare components
- **drdecomp** — Datt-Ravallion decomposition (growth vs distribution)
- **skdecomp** — Kolenikov-Shorrocks decomposition (growth, price, distribution)
- **changemean** — Income & inequality contribution to poverty
- **alorenz** — Lorenz curves, Pen's Parade, stochastic dominance
- **isopoverty** — Iso-poverty curves & growth-poverty tradeoffs
- **mpovline** — Multiple poverty lines (FGT0, FGT1, FGT2)
- **groupfunction** — Fast collapse replacement with Gini/Theil
- **groupdata** — Grouped data estimation
- **moldecrease** — Median odds ratio & decomposition

#### Specialized Stata Modules
- **hoi** — Human Opportunity Index (coverage, dissimilarity)
- **mol** — Measures of Effective Literacy
- **sae/fhsae** — Small Area Estimation (Fay-Herriot EBLUP)
- **turnbull** — Turnbull nonparametric WTP estimator
- **spike** — Spike model for willingness-to-pay
- **grqreg** — Quantile regression coefficient graphs
- **factortest** — Bartlett & Kaiser-Meyer-Olkin tests
- **crtest** — Cramer-Ridder test for multinomial logit
- **outtable** — Matrix to LaTeX table export

#### Data Tools
- **datazoom** — Stata-based data zoom tools
- **datalib** — Data library management
- Other data access utilities

#### Supporting Tools
- **dfl** — DiNardo-Fortin-Lemieux kernel density
- **various** — Helper functions, utilities, formatters

---

### 2. `stata_help_files.yml` — Comprehensive Stata Module Documentation

**Location:** `C:\GitHub\mytasks\jpazvd.github.io\_data\stata_help_files.yml`

**Purpose:** Complete technical documentation for each Stata ADO file, extracted from help files.

**Structure:**

```yaml
module_name:
  title: "Official Module Title"
  short_description: "One-line summary"
  
  # Command syntax
  syntax: "command syntax here"
  
  # Full description
  description: "Detailed explanation of what the module does, methodology, theory, caveats"
  
  # User-facing options
  options:
    - name: "option_name(spec)"
      description: "What this option does"
    - name: "another_option"
      description: "..."
  
  # Worked examples
  examples:
    - ". command example 1"
    - ". command example 2"
    - ". use data, clear"
    - ". command with options"
  
  # Output from r() function
  stored_results:
    - "r(statistic): Description of what's returned"
    - "r(matrix): Description..."
  
  # Academic/technical references
  references:
    - "Author, Year. 'Title.' Journal. DOI/URL."
  
  # Development metadata
  authors:
    - "João Pedro Azevedo, jazevedo@worldbank.org"
    - "Co-author name, email"
  
  acknowledgements: "Funding sources, other contributors"
  also_see:
    - "help for related_module"
  
  # Version & help format
  version: "version 1.5"
  help_file_type: "sthlp" or "hlp"
  
  # Links to external resources
  other_github_repository: "https://github.com/jpazvd/module-name"
  other_resources:
    - "World Bank research paper"
    - "Dataset example"
```

**Key Modules Documented (Sample):**

| Module | Purpose | Type | Status |
|--------|---------|------|--------|
| `adecomp` | Shapley welfare decomposition | poverty | Active |
| `apoverty` | Poverty measures (FGT, Watts, Sen) | poverty | Active |
| `ainequal` | Inequality indices (Gini, Theil, Atkinson) | inequality | Active |
| `wbopendata` | World Bank API data access | data-tools | Active |
| `alorenz` | Lorenz curves & stochastic dominance | visualization | Active |
| `hoi` | Human Opportunity Index | development | Active |
| `sae` | Small area estimation suite | econometrics | Active |
| `grqreg` | Quantile regression visualization | visualization | Active |

---

## Schema Reference

### Field Definitions

#### `github_repos.yml` Fields

| Field | Type | Required | Example | Notes |
|-------|------|----------|---------|-------|
| `name` | string | ✓ | "wbopendata" | GitHub repo name (lowercase, hyphens) |
| `description` | string | ✓ | "Stata module to access 17,000+ WB indicators" | 1-2 sentences, <120 chars |
| `tags` | array | ✓ | ["stata-packages", "data-tools", "world-bank"] | Min 1-3 tags; see vocabulary |
| `keywords` | array | ✓ | ["wdi", "world-development-indicators"] | SEO keywords |
| `featured` | boolean | | true | Show on website homepage |
| `url` | string | | "https://github.com/jpazvd/wbopendata" | If differs from default pattern |
| `documentation_url` | string | | "https://ideas.repec.org/..." | Link to full docs |

#### `stata_help_files.yml` Fields

| Field | Type | Purpose | Example |
|-------|------|---------|---------|
| `title` | string | Official module name | "wbopendata" |
| `short_description` | string | One-liner for lists | "Stata module to access World Bank databases" |
| `syntax` | string | Command usage pattern | "wbopendata, parameters [options]" |
| `description` | string | Full narrative explanation | "Detailed description..." |
| `options` | array of {name, description} | User options | `line(#)`, `varpl(varname)` |
| `examples` | array | Worked examples | `. wbopendata, indicator(si.pov.dday)` |
| `stored_results` | array | r() returned values | `r(b)`: matrix of results |
| `references` | array | Academic citations | Full citations with DOIs |
| `authors` | array | Module developers | Name + email |
| `version` | string | Current version | "version 1.5" |
| `help_file_type` | string | Help format | "sthlp" (Stata 13+) or "hlp" (older) |

---

## Data Connection Map

### How `github_repos.yml` and `stata_help_files.yml` Connect

```
github_repos.yml                          stata_help_files.yml
(High-level registry)                     (Deep technical docs)
         ↓                                        ↓
┌─────────────────────┐                 ┌──────────────────────┐
│ - name: wbopendata  │                 │ wbopendata:          │
│ - tags: [...]       │◄────link────►│ - syntax: ...        │
│ - description: ...  │                 │ - options: [...]     │
│ - featured: true    │                 │ - examples: [...]    │
└─────────────────────┘                 └──────────────────────┘
```

### Using Both in Website Display

#### Example: `/softwares/` Page

```html
<!-- High-level listing from github_repos.yml -->
<div class="software-grid">
  {% for repo in site.data.github_repos.repos %}
    <div class="software-card">
      <h3>{{ repo.name }}</h3>
      <p>{{ repo.description }}</p>
      <span class="tag">{{ repo.tags | join: ", " }}</span>
      <a href="#{{ repo.name }}">View Details →</a>
    </div>
  {% endfor %}
</div>

<!-- Detailed view from stata_help_files.yml -->
<div class="software-detail" id="wbopendata">
  <h2>{{ site.data.stata_help_files.wbopendata.title }}</h2>
  <p>{{ site.data.stata_help_files.wbopendata.description }}</p>
  
  <h4>Command Syntax</h4>
  <code>{{ site.data.stata_help_files.wbopendata.syntax }}</code>
  
  <h4>Options</h4>
  <ul>
  {% for option in site.data.stata_help_files.wbopendata.options %}
    <li><strong>{{ option[0] }}</strong>: {{ option[1] }}</li>
  {% endfor %}
  </ul>
  
  <h4>Examples</h4>
  <pre>
  {%- for example in site.data.stata_help_files.wbopendata.examples -%}
    {{ example }}
  {%- endfor -%}
  </pre>
</div>
```

---

## Usage Examples

### 1. Finding a Specific Module

**Search in `github_repos.yml`:**
```yaml
# Find by name
repos:
  - name: apoverty
    tags: [stata-packages, poverty, fgt]
```

**Get details from `stata_help_files.yml`:**
```yaml
apoverty:
  short_description: "Poverty Measures (revised)"
  syntax: "apoverty varlist [weight] [if exp] [in exp]"
  options:
    - line(#) — poverty line specification
    - all — compute all measures
    - h, h2, pgr, igr, w, s, tak, thon, fgt1-fgt9 — specific measures
```

### 2. Filtering by Research Topic

**In Jekyll template:**
```liquid
<!-- Show only poverty-related packages -->
{% for repo in site.data.github_repos.repos %}
  {% if repo.tags contains "poverty" %}
    <div class="software-card">{{ repo.name }}</div>
  {% endif %}
{% endfor %}
```

**Result:**
- wbopendata (data access for poverty data)
- apoverty (poverty measures)
- adecomp (poverty decomposition)
- changemean (poverty change decomposition)
- isopoverty (iso-poverty curves)
- mpovline (multiple poverty lines)
- alorenz (Lorenz curves for poverty analysis)

### 3. Building a Stata Module Cheat Sheet

```liquid
<!-- Generate table of all Stata modules -->
<table class="modules-table">
  <tr><th>Module</th><th>Purpose</th><th>Key Options</th><th>Example</th></tr>
  {% for module_name in site.data.stata_help_files %}
    {% assign module = site.data.stata_help_files[module_name] %}
    <tr>
      <td><strong>{{ module.title }}</strong></td>
      <td>{{ module.short_description }}</td>
      <td>{{ module.options | map: "name" | join: ", " | truncate: 40 }}</td>
      <td><code>{{ module.examples[0] }}</code></td>
    </tr>
  {% endfor %}
</table>
```

---

## Data Structure: Detailed Example

### Full `github_repos.yml` Entry

```yaml
- name: adecomp
  description: "Shapley Decomposition by Components of a Welfare Measure"
  tags: 
    - stata-packages
    - poverty
    - inequality
    - decomposition
    - shapley
  keywords:
    - shapley-decomposition
    - welfare-decomposition
    - poverty-change
    - income-components
    - path-dependence
  featured: true
  documentation_url: "https://ideas.repec.org/c/boc/bocode/s457208.html"
  github_repo: "https://github.com/jpazvd/adecomp"
  publication:
    paper: "Azevedo, Sanfelice, and Nguyen (2012)"
    citation_count: 120
```

### Full `stata_help_files.yml` Entry (Abbreviated)

```yaml
adecomp:
  title: "adecomp"
  short_description: "Shapley Decomposition by Components of a Welfare Measure"
  
  syntax: |
    adecomp welfarevar comp1 comp2 ... [weight], 
      by(varname) equation(equation) 
      [indicator(string) options...]
  
  description: |
    adecomp implements the shapley decomposition of changes in a welfare 
    indicator as proposed by Azevedo, Sanfelice and Minh (2012). It decomposes 
    changes in poverty/inequality into contributions from each component...
  
  options:
    - indicator(string) — poverty/inequality measures (fgt0, fgt1, fgt2, gini, theil, mean)
    - top(#), bottom(#) — top/bottom income groups
    - group(varname) — subgroup analysis
    - method(string) — "difference" or "growth" decomposition
  
  examples:
    - ". adecomp percapitainc laborinc nonlaborinc, by(year) equation(c1+c2) indicator(fgt0 fgt1 fgt2 gini theil) varpl(pline)"
    - ". adecomp percapitainc padults laborinc capitalinc pensioninc transferinc othersinc, by(year) equation(c1*(c2+c3+c4+c5+c6)) indicator(fgt0) varpl(pline)"
  
  stored_results:
    - "r(b): average effect of each component based on all paths"
    - "r(sd): standard deviation of effects (if std option)"
    - "r(path): number of paths in shapley decomposition"
  
  references:
    - "Azevedo, Joao Pedro, Viviane Sanfelice and Minh Cong Nguyen (2012). Shapley Decomposition by Components of a Welfare Measure. MPRA Paper 85584."
  
  authors:
    - "Joao Pedro Azevedo, jazevedo@worldbank.org"
    - "Minh Cong Nguyen, mnguyen3@worldbank.org"
    - "Viviane Sanfelice, vsanfelice@worldbank.org"
  
  version: "version 1.5"
  help_file_type: "sthlp"
```

---

## Maintenance Workflow

### Adding a New Stata Package

#### Step 1: Register in `github_repos.yml`

```yaml
- name: newmodule
  description: "What this module does"
  tags: [stata-packages, keyword1, keyword2]
  keywords: [seo-keyword-1, seo-keyword-2]
  featured: true
```

#### Step 2: Extract Help File Documentation

```bash
# From Stata REPL:
. which newmodule
# Copy the .sthlp file path
```

Extract key sections:
- **Syntax** → `syntax` field
- **Description** → `description` field
- **Options** → `options` array
- **Examples** → `examples` array
- **Returned results** → `stored_results` array
- **References** → `references` array

#### Step 3: Add to `stata_help_files.yml`

```yaml
newmodule:
  title: "newmodule"
  short_description: "..."
  syntax: "..."
  description: "..."
  # ... etc
```

#### Step 4: Commit and Deploy

```bash
git add _data/github_repos.yml _data/stata_help_files.yml
git commit -m "Add newmodule to software database"
git push origin main
```

### Updating Module Documentation

1. Update `.sthlp` file in GitHub repo
2. Extract updated sections
3. Update `stata_help_files.yml` with new content
4. Update `github_repos.yml` if description/tags changed
5. Commit and push

### Syncing with External Platforms

- **GitHub Topics:** Tags in `github_repos.yml` should align with GitHub repo topics
- **RePEc:** Help file metadata should match RePEc entry (version, authors, keywords)
- **SSC (Stata Software Components):** Ensure documentation is current before publishing

---

## Integration Points

### Websites Using These Databases

| Page | Database | Purpose |
|------|----------|---------|
| `/softwares/` | Both | Featured modules + detailed descriptions |
| `/publications/` (software section) | `stata_help_files.yml` | List software contributions |
| `/cv/` | `github_repos.yml` | Software development portfolio |
| GitHub Profile | `github_repos.yml` | Sync topics with tags |

### Jekyll Liquid Templates

```liquid
<!-- Access github_repos data -->
{% assign repos = site.data.github_repos.repos %}

<!-- Access stata help data -->
{% assign modules = site.data.stata_help_files %}

<!-- Loop and filter -->
{% for repo in repos %}
  {% if repo.featured %}
    <!-- Display featured software -->
  {% endif %}
{% endfor %}
```

---

## Future Enhancements

### Phase 1: Current
- ✅ Separate high-level (`github_repos.yml`) and detailed (`stata_help_files.yml`) documentation
- ✅ Tag-based filtering and categorization
- ✅ Full technical documentation for reference

### Phase 2: Planned
- [ ] Auto-generate API documentation from `.sthlp` files
- [ ] Add links to academic papers citing each module
- [ ] Create module dependency map (which modules depend on which)
- [ ] Add download/citation statistics from SSC and RePEc
- [ ] Build interactive module comparison tool

### Phase 3: Long-term
- [ ] Version history tracking
- [ ] User feedback/issue tracking integration
- [ ] Module contribution guidelines
- [ ] Community-contributed modules

---

## Quick Reference: File Locations

```
jpazvd.github.io/
├── _data/
│   ├── github_repos.yml                    ← Repository registry
│   ├── stata_help_files.yml                ← Module documentation
│   └── README_SOFTWARE_DATABASE.md         ← This file
│
├── _pages/
│   └── software.md                         ← Software landing page
│
└── assets/
    └── docs/
        └── software/                       ← Software-specific docs
```

---

## Archived Files

Legacy and obsolete data files are stored in `_data/_archive/`:

**Archived (Superseded):**
- `events-old.yml` - Original events database
- `events-new.yml`, `events-new-v2.yml`, `events-new.yml.backup` - Intermediate versions (superseded by events.yml)
- `teaching-new.yml` - Intermediate version (superseded by teaching.yml)

**Active Dual-File Pattern (NOT archived):**
- `worldbank_blogs_full.yml` - Keeps full blog content for archiving/searching
- `other_blogs_full.yml` - Keeps full blog content for archiving/searching

See [`_data/_archive/README.md`](_archive/README.md) for details on archive contents and restoration instructions.

---

## Setup & Installation

### Python Dependencies

The website uses Python scripts for data fetching and consolidation. Install dependencies:

```bash
pip install -r requirements.txt
```

**Required packages:**
- `pyyaml` — YAML file parsing
- `rapidfuzz` — Fuzzy matching for publication deduplication
- `requests` — API data fetching
- `beautifulsoup4` — Web scraping for Stata documentation

**Optional packages:**
- `pandas`, `numpy` — Data analysis (for future enhancements)
- `black`, `flake8` — Development tools

See [`requirements.txt`](../requirements.txt) for complete dependency list.

### Ruby Dependencies (Jekyll)

The website is built with Jekyll and uses Ruby gems configured in `Gemfile`. Install with:

```bash
bundle install
```

Run locally with:
```bash
bundle exec jekyll serve --livereload
```

---

## Questions & Support

For questions about:
- **Adding new modules** → See "Adding a New Stata Package" section
- **Using in Jekyll templates** → See "Integration Points" section
- **Syncing with external services** → See "Syncing with External Platforms" section
- **Database structure** → See "Schema Reference" section
- **Archive & legacy files** → See "Archived Files" section
- **Python scripts** → See "Python Scripts & Automation" section

---

**Last Updated:** December 24, 2025  
**Document Version:** 1.0
**Author:** João Pedro Azevedo
