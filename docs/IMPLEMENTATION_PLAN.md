# 🎯 Website Improvement Implementation Plan

## João Pedro Azevedo - jpazvd.github.io

**Created:** December 10, 2025  
**Status:** Ready for Implementation  
**Estimated Time:** 2-3 hours  

---

## 📋 Executive Summary

This plan outlines 12 specific improvements to enhance SEO, accessibility, structured data, and content quality for your GitHub Pages academic website. All changes are compatible with Jekyll 4 + jekyll-scholar and GitHub Actions deployment.

---

## 🏗️ Implementation Phases

### Phase 1: Configuration & SEO Foundation (Priority: HIGH)
### Phase 2: Structured Data (Priority: HIGH)  
### Phase 3: Content Cleanup (Priority: MEDIUM)
### Phase 4: Accessibility & Performance (Priority: MEDIUM)
### Phase 5: Documentation (Priority: LOW)

---

# PHASE 1: Configuration & SEO Foundation

## Task 1.1: Add Social Links for Schema.org JSON-LD

**File:** `_config.yml`  
**Location:** After line 36 (after `researchgate`)  
**Purpose:** Enable automatic Person schema generation in seo.html

### Current State:
```yaml
author:
  name                   : "João Pedro Azevedo"
  # ... other fields
  researchgate           : "https://ideas.repec.org/e/pwa88.html"
```

### Add This Configuration:
```yaml
# Social/Schema.org configuration (enables Person JSON-LD)
social:
  type: Person
  name: "João Pedro Azevedo"
  links:
    - "https://twitter.com/jpazvd"
    - "https://github.com/jpazvd"
    - "https://www.linkedin.com/in/jpazvd"
    - "https://scholar.google.com/citations?user=lTKXA78AAAAJ"
    - "https://orcid.org/0000-0002-3844-215X"
    - "https://ideas.repec.org/e/pwa88.html"

# Open Graph default image (for social sharing)
og_image: "profile.png"
```

### Why This Works:
- The existing `seo.html` (lines 117-127) already checks for `site.social` and generates JSON-LD
- Adding `og_image` enables Twitter/Facebook card images

---

## Task 1.2: Add Google Search Console Verification (Optional)

**File:** `_config.yml`  
**Location:** After the social section  
**Purpose:** Verify site ownership with Google

### Add (if you have verification code):
```yaml
# Search engine verification
google_site_verification: "YOUR_VERIFICATION_CODE_HERE"
```

### How to Get Code:
1. Go to https://search.google.com/search-console
2. Add property: `https://jpazvd.github.io`
3. Choose "HTML tag" verification method
4. Copy only the `content="..."` value

---

## Task 1.3: Fix Bibliography Source

**File:** `_config.yml`  
**Location:** Line 97  
**Purpose:** Point to your full publication list

### Current (WRONG):
```yaml
scholar:
  source: "_bibliography"
  bibliography: "minimal.bib"  # Only has 1 sample entry!
```

### Change To:
```yaml
scholar:
  source: "_bibliography"
  bibliography: "references.bib"  # Your actual 1,431-line bibliography
```

---

# PHASE 2: Enhanced Structured Data

## Task 2.1: Create Enhanced Person Schema Include

**File:** `_includes/person-schema.html` (NEW FILE)  
**Purpose:** Rich structured data for academic profile

### Create This File:
```html
<!-- Enhanced Person Schema for Academic Profile -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "{{ site.url }}/#person",
  "name": "{{ site.author.name }}",
  "givenName": "João Pedro",
  "familyName": "Azevedo",
  "jobTitle": "Chief Statistician",
  "description": "{{ site.description }}",
  "url": "{{ site.url }}",
  "image": "{{ site.url }}/images/{{ site.author.avatar }}",
  "sameAs": [
    "https://twitter.com/jpazvd",
    "https://github.com/jpazvd",
    "https://www.linkedin.com/in/jpazvd",
    "https://scholar.google.com/citations?user=lTKXA78AAAAJ",
    "https://orcid.org/0000-0002-3844-215X",
    "https://ideas.repec.org/e/pwa88.html",
    "https://openknowledge.worldbank.org/entities/person/360f7a2e-0784-56e1-acf4-7f805fd50257"
  ],
  "worksFor": {
    "@type": "Organization",
    "name": "UNICEF",
    "url": "https://www.unicef.org"
  },
  "alumniOf": [
    {
      "@type": "CollegeOrUniversity",
      "name": "Newcastle University",
      "url": "https://www.ncl.ac.uk"
    },
    {
      "@type": "CollegeOrUniversity", 
      "name": "Universidade Federal Fluminense"
    },
    {
      "@type": "CollegeOrUniversity",
      "name": "Universidade Federal do Rio de Janeiro"
    }
  ],
  "hasCredential": {
    "@type": "EducationalOccupationalCredential",
    "credentialCategory": "degree",
    "name": "PhD in Economics"
  },
  "knowsAbout": [
    "Learning Poverty",
    "Education Economics", 
    "Development Economics",
    "Poverty Measurement",
    "Child Statistics",
    "Sustainable Development Goals",
    "Stata Programming",
    "Welfare Measurement"
  ],
  "nationality": {
    "@type": "Country",
    "name": "Brazil"
  }
}
</script>
```

---

## Task 2.2: Include Person Schema in Head

**File:** `_includes/head.html`  
**Location:** After line 21 (after the closing stylesheet link)  
**Purpose:** Include schema on all pages

### Add This Line:
```html
{% include person-schema.html %}
```

### Final head.html Structure:
```html
<!-- For all browsers -->
<link rel="stylesheet" href="{{ base_path }}/assets/css/main.css">

{% include person-schema.html %}

<meta http-equiv="cleartype" content="on">
```

---

## Task 2.3: Create WebSite Schema Include

**File:** `_includes/website-schema.html` (NEW FILE)  
**Purpose:** Help search engines understand site structure

### Create This File:
```html
<!-- WebSite Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "{{ site.url }}/#website",
  "url": "{{ site.url }}",
  "name": "{{ site.title }}",
  "description": "{{ site.description }}",
  "publisher": {
    "@id": "{{ site.url }}/#person"
  },
  "inLanguage": "en-US"
}
</script>
```

### Add to head.html (after person-schema):
```html
{% include website-schema.html %}
```

---

# PHASE 3: Content Cleanup

## Task 3.1: Update CV Skills Section

**File:** `_pages/cv.md`  
**Location:** Lines 49-56  
**Purpose:** Replace placeholder with real skills

### Current (PLACEHOLDER):
```markdown
Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3
```

### Replace With:
```markdown
Skills
======

**Technical & Analytical**
* Stata (advanced, ado-file development, SSC contributor)
* R, Python, SQL
* Econometrics & Impact Evaluation
* Survey Design & Sampling
* Small Area Estimation & Poverty Mapping
* Data Visualization & Dashboard Development

**Domain Expertise**
* Poverty Measurement & Analysis
* Education Statistics & Learning Assessment
* Child Development Indicators
* SDG Monitoring & Reporting
* Human Capital Measurement

**Leadership & Management**
* Team Leadership (45+ staff at UNICEF)
* International Development Operations
* Multi-stakeholder Coordination
* Technical Assistance & Capacity Building

**Languages**
* Portuguese (native)
* English (fluent)
* Spanish (professional)
```

---

## Task 3.2: Update CV Service Section

**File:** `_pages/cv.md`  
**Location:** Lines 73-75 (end of file)  
**Purpose:** Replace placeholder

### Current (PLACEHOLDER):
```markdown
Service and leadership
======
* Currently signed in to 43 different slack teams
```

### Replace With:
```markdown
Service and Leadership
======
* Co-Lead, Global Solution Group on Welfare Measurement and Statistical Capacity (World Bank)
* Co-Lead, Data for Goals Initiative (World Bank)
* Education Statistics Coordinator (World Bank Education Global Practice)
* Member, Technical Cooperation Group on SDG 4 indicators (UNESCO Institute for Statistics)
* Reviewer for: World Development, Journal of Development Economics, World Bank Research Observer
* SSC Statistical Software Components contributor (Boston College)
```

---

## Task 3.3: Delete or Update Sample Blog Posts

**Files to Address:**
- `_posts/2012-08-14-blog-post-1.md`
- `_posts/2013-08-14-blog-post-2.md`
- `_posts/2014-08-14-blog-post-3.md`
- `_posts/2015-08-14-blog-post-4.md`
- `_posts/2199-01-01-future-post.md`

### Option A - DELETE (Recommended if not blogging):
```powershell
# Run in terminal
Remove-Item "_posts/2012-08-14-blog-post-1.md"
Remove-Item "_posts/2013-08-14-blog-post-2.md"
Remove-Item "_posts/2014-08-14-blog-post-3.md"
Remove-Item "_posts/2015-08-14-blog-post-4.md"
Remove-Item "_posts/2199-01-01-future-post.md"
```

### Option B - KEEP ONE as template:
Keep `_posts/_posts.md` as documentation, delete the rest.

---

## Task 3.4: Update README.md

**File:** `README.md`  
**Purpose:** Professional repository documentation

### Replace Entire Content With:
```markdown
# João Pedro Azevedo - Personal Website

[![Build Status](https://github.com/jpazvd/jpazvd.github.io/actions/workflows/pages.yml/badge.svg)](https://github.com/jpazvd/jpazvd.github.io/actions)

**Live Site:** [https://jpazvd.github.io](https://jpazvd.github.io)

## About

Personal academic website of João Pedro Azevedo, UNICEF Chief Statistician and Development Economist. 

### Features
- 📚 Full publication list with 144+ entries via jekyll-scholar
- 📊 Automated Google Scholar citation metrics (weekly updates)
- 📄 Comprehensive CV and research portfolio
- 🔧 Custom GitHub Actions deployment (Jekyll 4 + Scholar)

## Tech Stack
- Jekyll 4.2 with jekyll-scholar
- GitHub Pages (via GitHub Actions)
- Minimal Mistakes theme (Academic Pages fork)

## Local Development

### Prerequisites
- Ruby 3.x
- Bundler

### Quick Start
```bash
bundle install
bundle exec jekyll serve
```

### With Scholar Support
```powershell
./scripts/bootstrap-jekyll.ps1 -Mode scholar -Task serve
```

## Citation Metrics
Citation data is automatically updated weekly from Google Scholar via GitHub Actions.

## License
MIT License - See [LICENSE](LICENSE)

## Contact
- Twitter: [@jpazvd](https://twitter.com/jpazvd)
- GitHub: [jpazvd](https://github.com/jpazvd)
- ORCID: [0000-0002-3844-215X](https://orcid.org/0000-0002-3844-215X)
```

---

# PHASE 4: Accessibility & Performance

## Task 4.1: Add Meta Description to Key Pages

### File: `_pages/about.md`
**Add to front matter:**
```yaml
description: "João Pedro Azevedo is UNICEF's Chief Statistician, leading global child data initiatives. PhD economist with 70+ publications in Lancet, World Development."
```

### File: `_pages/cv.md`
**Add to front matter:**
```yaml
description: "Curriculum Vitae of João Pedro Azevedo - UNICEF Chief Statistician, former World Bank Lead Economist. PhD Economics, Newcastle University."
```

### File: `_pages/publications.md`
**Add to front matter:**
```yaml
description: "Publications by João Pedro Azevedo: 144+ works on Learning Poverty, education economics, poverty measurement. Includes Lancet, World Development articles."
```

---

## Task 4.2: Add Alt Text Audit

**File:** `_includes/author-profile.html`  
**Check:** Ensure profile image has proper alt text

### Verify This Pattern Exists:
```html
<img src="{{ author.avatar }}" alt="{{ author.name }}" ...>
```

If missing `alt`, add: `alt="{{ site.author.name }}"`

---

## Task 4.3: Add Preconnect for External Resources

**File:** `_includes/head.html`  
**Location:** After line 4 (after charset)  
**Purpose:** Speed up Google Fonts/external resources

### Add:
```html
<!-- Preconnect to external domains -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

---

# PHASE 5: Documentation & Cleanup

## Task 5.1: Update .gitignore

**File:** `.gitignore`  
**Purpose:** Ignore local development artifacts

### Ensure These Lines Exist:
```gitignore
# Jekyll
_site/
.sass-cache/
.jekyll-cache/
.jekyll-metadata

# Local development
Gemfile.lock
*.log

# OS files
.DS_Store
Thumbs.db

# Editor
.vscode/
*.swp
```

---

## Task 5.2: Commit Uncommitted Changes

**Current Status:** Modified Gemfile, Gemfile.lock not staged

### Run:
```powershell
git add Gemfile Gemfile.lock
git commit -m "chore: update dependencies"
```

---

# 📝 Implementation Checklist

## Phase 1: Configuration
- [x] Task 1.1: Add social links to _config.yml
- [x] Task 1.2: Add og_image to _config.yml  
- [x] Task 1.3: Fix bibliography source (minimal.bib → references.bib)

## Phase 2: Structured Data
- [x] Task 2.1: Create _includes/person-schema.html
- [x] Task 2.2: Include person-schema in head.html
- [x] Task 2.3: Create _includes/website-schema.html

## Phase 3: Content
- [x] Task 3.1: Update CV Skills section
- [x] Task 3.2: Update CV Service section
- [x] Task 3.3: Delete sample blog posts
- [x] Task 3.4: Update README.md

## Phase 4: Accessibility
- [x] Task 4.1: Add meta descriptions to key pages
- [x] Task 4.2: Verify alt text on images
- [x] Task 4.3: Add preconnect hints

## Phase 5: Cleanup
- [x] Task 5.1: Update .gitignore (expand)
- [x] Task 5.2: Commit pending changes

## Additional Completed Work (December 2025)
- [x] World Bank OKR publications harvesting (34 publications)
- [x] World Bank Blogs harvesting (29 posts)
- [x] Full blog content extraction
- [x] Citation metrics automation (Google Scholar, RePEc)
- [x] CITATION_METRICS_PROTOCOL.md documentation

---

# 🧪 Verification Steps

After implementation, verify:

1. **Local Build Test:**
   ```powershell
   bundle exec jekyll build
   ```
   Should complete without errors.

2. **Schema Validation:**
   - Visit https://validator.schema.org/
   - Enter https://jpazvd.github.io after deploy
   - Should show Person and WebSite schemas

3. **SEO Check:**
   - Run Lighthouse in Chrome DevTools
   - Check SEO score (target: 90+)

4. **PageSpeed Insights:**
   - Visit https://pagespeed.web.dev/
   - Enter site URL
   - Review Core Web Vitals

5. **Google Search Console:**
   - After 1-2 weeks, check indexing status
   - Review any crawl errors

---

# ⚠️ Important Notes

1. **GitHub Pages Compatibility:**
   - All changes use standard Jekyll/Liquid
   - No server-side code (GitHub Pages limitation)
   - JSON-LD is client-side JavaScript

2. **Bibliography Fix:**
   - The `minimal.bib` → `references.bib` change is CRITICAL
   - Current setup only shows 1 sample publication

3. **Testing Before Push:**
   - Always run `bundle exec jekyll build` locally
   - Check for Liquid syntax errors

4. **Deployment:**
   - Push to `main` branch triggers GitHub Actions
   - Wait ~2-3 minutes for deploy
   - Clear browser cache if changes don't appear

---

# 🚀 Ready to Implement?

Say "implement all" and I will execute all tasks in order, or specify individual tasks like:
- "implement phase 1"
- "implement task 3.1"
- "implement structured data only"
