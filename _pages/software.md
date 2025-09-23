---
layout: archive
title: "Data Science & Analytics Tools"
permalink: /softwares/
author_profile: true
---

This page lists the software packages, statistical commands, and datasets I have developed or co-developed. These tools are primarily designed for econometric and statistical analysis in development economics research. Most are available through the Boston College Statistical Software Components (SSC) archive or directly from GitHub.

---

{% if site.plugins contains 'jekyll-scholar' %}

### 💻 Software & Statistical Commands

{% bibliography --query @software %}

---

### 📊 Datasets

{% bibliography --query @dataset %}

---

### 🐙 GitHub Repositories

{% bibliography --query @github %}

{% else %}
<!-- Static fallback for GitHub Pages build -->

**For a complete list of my software and code, please visit:**
- [Boston College Statistical Software Components (SSC)](https://ideas.repec.org/e/pwa88.html)
- [GitHub Profile](https://github.com/jpazvd)

### Selected Software

- **povcalnet**: Stata command to access World Bank's PovcalNet data.
- **wdi**: Stata command to access World Bank's World Development Indicators.

*This list is dynamically generated when the site is built with the custom workflow. Please check the links above for the most current information.*

{% endif %}