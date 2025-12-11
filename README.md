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
- 🔍 SEO optimized with Schema.org structured data

## Tech Stack
- Jekyll 4.2 with jekyll-scholar
- GitHub Pages (via GitHub Actions)
- Minimal Mistakes theme (Academic Pages fork)
- Schema.org JSON-LD for rich search results

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

## Structured Data
The site includes Schema.org markup for:
- Person (academic profile, credentials, expertise)
- WebSite (site metadata)
- Social profiles (Twitter, GitHub, LinkedIn, ORCID, Google Scholar)

## License
MIT License - See [LICENSE](LICENSE)

## Contact
- Twitter: [@jpazvd](https://twitter.com/jpazvd)
- GitHub: [jpazvd](https://github.com/jpazvd)
- ORCID: [0000-0002-3844-215X](https://orcid.org/0000-0002-3844-215X)
- Google Scholar: [Profile](https://scholar.google.com/citations?user=lTKXA78AAAAJ)
