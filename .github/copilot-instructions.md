# Copilot Instructions for jpazvd.github.io

## Project Overview
This is an academic personal website for João Pedro Azevedo, UNICEF Chief Statistician. Built with Jekyll 4 and jekyll-scholar, deployed via GitHub Actions to GitHub Pages.

## Tech Stack
- **Static Site Generator:** Jekyll 4.2.x
- **Theme:** Academic Pages (fork of Minimal Mistakes)
- **Bibliography:** jekyll-scholar with BibTeX (.bib files)
- **Deployment:** GitHub Actions → GitHub Pages
- **Branch Structure:** `source` (development) → `main` (deployed)

## Key Directories
```
_bibliography/     # BibTeX files (references.bib is the main one)
_includes/         # Liquid partials (head.html, seo.html, schemas)
_layouts/          # Page templates
_pages/            # Standalone pages (about.md, cv.md, publications.md)
_posts/            # Blog posts (date-prefixed markdown)
_data/             # YAML data files (navigation.yml, authors.yml)
_sass/             # SCSS stylesheets
assets/            # Static assets (CSS, JS, images)
images/            # Image files
files/             # Downloadable files (PDFs, etc.)
```

## Configuration Files
- `_config.yml` - Main Jekyll configuration
- `_config.scholar.yml` - Jekyll-scholar specific config (used in CI)
- `Gemfile` - Ruby dependencies
- `.github/workflows/pages.yml` - GitHub Actions deployment

## Code Conventions

### Front Matter (YAML)
All markdown files should have front matter:
```yaml
---
layout: single          # or archive, page, splash
title: "Page Title"
permalink: /url-path/
author_profile: true
description: "Meta description for SEO"
---
```

### Liquid Templating
- Use `{% include base_path %}` at the start of includes
- Site variables: `{{ site.author.name }}`, `{{ site.url }}`
- Page variables: `{{ page.title }}`, `{{ page.description }}`

### Jekyll-Scholar Citations
```liquid
{% bibliography %}                    # Full bibliography
{% bibliography --query @article %}   # Filter by type
{% cite key %}                        # Inline citation
{% reference key %}                   # Full reference
```

### BibTeX Entries
Located in `_bibliography/references.bib`. Standard BibTeX format:
```bibtex
@article{azevedo2021learning,
  title={Learning Poverty...},
  author={Azevedo, Jo{\~a}o Pedro and ...},
  journal={World Bank Research Observer},
  year={2021}
}
```

### Structured Data (Schema.org)
- `_includes/person-schema.html` - Person JSON-LD
- `_includes/website-schema.html` - WebSite JSON-LD
- Included in `_includes/head.html`

## Important Notes

## Practices & Lessons Learned (Operational)

### Archiving / Deprecation Strategy
- Prefer a **root-level** `_archive/` (or `_deprecated/`) for historical/backup content.
- **Avoid placing archive folders inside `_pages/`**: `_pages/` is explicitly included by config, so archived pages there may still be built/published.
- Keep archived material clearly segregated (e.g., `_archive/root/`, `_archive/_pages/`, `_archive/_bibliography/`, `_archive/talkmap/`).
- If you must keep backups in-place, use obvious suffixes like `.bak` and ensure they are excluded/ignored appropriately.

### Jekyll Front Matter & Encoding (Hard-Won Gotchas)
- YAML front matter must start at the **very first byte** of the file. A UTF-8 BOM can prevent Jekyll from detecting front matter.
  - Practice: save content pages as **UTF-8 without BOM**.
- Prefer `.md` for content pages unless you specifically need `.html`.
- Markdown inside raw HTML blocks may not render (e.g., headings like `###` appear literally).
  - Practice: either avoid wrapping Markdown in raw HTML, or add `markdown="1"` to the wrapper element (kramdown).

### Publishing Safety / Hygiene
- Never edit `_site/` (generated output).
- If the repo grows, consider excluding non-site tooling folders from Jekyll builds (e.g., `scripts/`, `docs/`, `resources/`, `markdown_generator/`) via `_config.yml` `exclude:`—but verify CI output before changing.
- After fixes that affect rendering, validate both:
  - Local build (when possible)
  - Live output on GitHub Pages (sometimes caches/propagation delay can confuse early checks)

### Local Development on Windows
- Jekyll on Windows can be brittle; prefer **WSL** when local `bundle exec jekyll serve` is flaky.
- Keep local dependencies aligned with CI where practical (CI uses `Gemfile.ci` + `_config.yml,_config.scholar.yml`).
- Don’t commit `Gemfile.lock` on the `source` branch (platform-specific), unless you intentionally change that policy.

### GitHub Pages & Jekyll
- **GitHub Actions is recommended** over the `github-pages` gem for deployment
- Jekyll is not officially supported for Windows (but works via WSL or Ruby DevKit)
- jekyll-scholar is NOT in the GitHub Pages plugin whitelist, so we use GitHub Actions
- No server-side code (PHP, Python, etc.)

### Jekyll Configuration Restrictions
These settings are enforced by GitHub Pages and cannot be changed:
```yaml
lsi: false
safe: true
incremental: false
highlighter: rouge
kramdown:
  math_engine: mathjax
  syntax_highlighter: rouge
```

### Default GitHub Pages Plugins (auto-enabled)
- jekyll-coffeescript, jekyll-default-layout, jekyll-gist
- jekyll-github-metadata, jekyll-optional-front-matter
- jekyll-paginate, jekyll-readme-index
- jekyll-titles-from-headings, jekyll-relative-links

### GitHub Metadata
Use `site.github` to access repository metadata in templates:
```liquid
{{ site.github.repository_name }}
{{ site.github.owner_name }}
{{ site.github.project_title }}
```

### Building Locally
```bash
bundle install
bundle exec jekyll serve
```

Note: On Windows, use WSL or ensure Ruby DevKit is properly installed.

### SEO Best Practices
- Every page needs a `description` in front matter
- Use semantic HTML headings (h1 → h2 → h3)
- Images need `alt` attributes
- Internal links use `{{ site.baseurl }}/path/`

### Content Guidelines
- Author name: "João Pedro Azevedo" (with proper Portuguese characters)
- Current role: "UNICEF Chief Statistician"
- Use APA citation style for bibliography
- Publications should link to DOIs when available

## File Naming Conventions
- Pages: `lowercase-with-dashes.md`
- Posts: `YYYY-MM-DD-title-slug.md`
- Includes: `lowercase-with-dashes.html`
- Images: `descriptive-name.png` (prefer PNG or WebP)

## Citation Metrics Updates

When asked to update publication statistics:

1. **Check the protocol**: See `docs/CITATION_METRICS_PROTOCOL.md`
2. **Data sources**:
   - Google Scholar: https://scholar.google.com/citations?user=lTKXA78AAAAJ
   - RePEc/IDEAS: https://ideas.repec.org/e/pwa88.html
  - ORCID: https://orcid.org/0000-0002-3844-215X
3. **Update file**: `_data/citations.yml`
4. **Automated script**: `scripts/fetch_scholar_metrics.py`

### Prompt Template for Updates
```
Update my citation metrics with these values:
- Google Scholar citations: [VALUE]
- h-index: [VALUE]
- i10-index: [VALUE]
- RePEc downloads: [VALUE]
```

## When Editing This Site

### Do
- Test changes locally before committing
- Use descriptive commit messages
- Keep bibliography entries in references.bib
- Add meta descriptions to new pages
- Maintain Schema.org structured data

### Don't
- Edit files in `_site/` (auto-generated)
- Use plugins not supported by GitHub Actions workflow
- Remove the safety tag `v1.0.0-pre-improvements`
- Commit Gemfile.lock to source branch (platform-specific)
