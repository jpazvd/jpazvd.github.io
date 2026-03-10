---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
description: "Curriculum Vitae of João Pedro Azevedo - UNICEF Chief Statistician, former World Bank Lead Economist. PhD Economics, Newcastle University."
redirect_from:
  - /resume
---

{% include base_path %}

<!-- Print-only header: hidden on screen, visible when printing/generating PDF -->
<div class="cv-print-header">
  <p class="cv-print-header__name">João Pedro Azevedo</p>
  <p class="cv-print-header__title">Chief Statistician, UNICEF &bull; Development Economist</p>
  <p class="cv-print-header__contact">
    <a href="https://jpazvd.github.io">jpazvd.github.io</a> &bull;
    <a href="{{ site.data.citations.google_scholar.profile_url }}">Google Scholar</a> &bull;
    <a href="{{ site.data.citations.orcid.profile_url }}">ORCID</a>
  </p>
</div>

<p class="cv-download">
  <a href="/files/cv-joao-pedro-azevedo.pdf" class="btn btn--primary">
    Download PDF
  </a>
</p>

## Profile

{{ site.data.profile.summary }}

### Selected contributions

<ul>
{% for contribution in site.data.profile.selected_contributions %}
<li>{{ contribution }}</li>
{% endfor %}
</ul>

## Work Experience

{% for job in site.data.work_experience %}
<div class="cv-job">
<h3>{{ job.organization }}</h3>
<p class="cv-job__meta"><strong>{{ job.position }}</strong> — {{ job.start_date }}–{{ job.end_date }}</p>
<p class="cv-job__desc">{{ job.description }}</p>
</div>
{% endfor %}

## Education

<ul>
{% for edu in site.data.education %}
<li>
  <strong>{{ edu.degree }}</strong>, {{ edu.institution }} ({{ edu.location }}), {{ edu.year }}{% if edu.thesis_year %} (thesis submitted {{ edu.thesis_year }}){% endif %}.{% if edu.supervisors %} Supervisors: {{ edu.supervisors }}.{% endif %}
</li>
{% endfor %}
</ul>

## Selected Publications

<p class="cv-citation-summary">
  Google Scholar: {{ site.data.citations.google_scholar.total_citations | default: '5,500+' }} citations &bull;
  h-index: {{ site.data.citations.google_scholar.h_index | default: '30' }} &bull;
  i10-index: {{ site.data.citations.google_scholar.i10_index | default: '62' }} &bull;
  RePEc: {{ site.data.citations.repec.total_downloads_all_time | default: '32,000+' }} downloads.
  Full list: <a href="{{ site.data.citations.google_scholar.profile_url }}" target="_blank">Google Scholar</a> |
  <a href="{{ site.data.citations.repec.profile_url }}" target="_blank">RePEc/IDEAS</a> |
  <a href="{{ site.data.citations.orcid.profile_url }}" target="_blank">ORCID</a>
</p>

### Journal Articles

<ul>
{% for pub in site.data.publications.journal_articles %}
<li class="cv-pub">
  {{ pub.authors | join: ", " }} ({{ pub.year }}). "{{ pub.title }}." <em>{{ pub.journal }}</em>{% if pub.volume %}, {{ pub.volume }}{% endif %}{% if pub.issue %}({{ pub.issue }}){% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}.{% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">doi</a>{% endif %}
</li>
{% endfor %}
</ul>

### Books

<ul>
{% for pub in site.data.publications.books %}
<li class="cv-pub">
  {{ pub.authors | join: ", " }} ({{ pub.year }}). <em>{{ pub.title }}</em>. {{ pub.publisher }}.{% if pub.urls.pdf %} <a href="{{ pub.urls.pdf }}">PDF</a>{% endif %}
</li>
{% endfor %}
</ul>

### Book Chapters

<ul>
{% for pub in site.data.publications.book_chapters %}
<li class="cv-pub">
  {{ pub.authors | join: ", " }} ({{ pub.year }}). "{{ pub.title }}." In {% if pub.editor %}{{ pub.editor }} (Ed.), {% endif %}<em>{{ pub.book }}</em>. {{ pub.publisher }}{% if pub.pages %}, {{ pub.pages }}{% endif %}.
</li>
{% endfor %}
</ul>

### Selected Reports

<ul>
{% for pub in site.data.publications.reports %}
<li class="cv-pub">
  {{ pub.authors | join: ", " }} ({{ pub.year }}). <em>{{ pub.title }}</em>. {{ pub.institution }}.{% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">doi</a>{% elsif pub.urls.report %} <a href="{{ pub.urls.report }}">link</a>{% endif %}
</li>
{% endfor %}
</ul>

### Selected Working Papers

<ul>
{% for pub in site.data.publications.working_papers limit:10 %}
<li class="cv-pub">
  {{ pub.authors | join: ", " }} ({{ pub.year }}). "{{ pub.title }}." <em>{{ pub.venue }}</em>.{% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">doi</a>{% elsif pub.url %} <a href="{{ pub.url }}">link</a>{% endif %}
</li>
{% endfor %}
</ul>

<p class="cv-nav-link"><a href="/publications/">View full publication record →</a></p>

## Service and Leadership

<ul>
{% for service in site.data.profile.service %}
<li><strong>{{ service.role }}</strong>{% if service.organization %}, {{ service.organization }}{% endif %}{% if service.parent %} ({{ service.parent }}){% endif %}</li>
{% endfor %}
</ul>

## Selected Talks & Presentations

{% assign recent_events = site.data.events.events | sort: "date" | reverse %}
<ul>
{% for event in recent_events limit:15 %}
<li>
  <strong>{{ event.event }}</strong> ({{ event.year }})<br>
  <span class="cv-teaching__meta">{{ event.role }}{% if event.session %}: "{{ event.session }}"{% endif %}</span><br>
  <span class="cv-teaching__years">{{ event.location }}</span>
</li>
{% endfor %}
</ul>

<p class="cv-nav-link"><a href="/events/">View all speaking engagements →</a></p>

## Teaching & Mentoring

### Teaching

{% assign sorted_teaching = site.data.teaching.teaching | sort: "date_start" | reverse %}
<ul>
{% for entry in sorted_teaching %}
  {% if entry.role contains "Substitute Professor" or entry.role contains "Training Instructor" or entry.role contains "Specialist Trainer" %}
  <li>
    <strong>{{ entry.course_title }}</strong>, {{ entry.institution }} ({{ entry.country }})<br>
    <span class="cv-teaching__meta">{{ entry.role }} • {{ entry.level }}</span><br>
    <span class="cv-teaching__years">{{ entry.years | join: "–" }}</span>
  </li>
  {% endif %}
{% endfor %}
</ul>

### Supervision & Mentoring

<ul>
{% for entry in sorted_teaching %}
  {% if entry.role contains "Co-Advisor" or entry.role contains "Committee Member" %}
  <li>
    <strong>{{ entry.course_title }}</strong>, {{ entry.institution }} ({{ entry.country }})<br>
    <span class="cv-teaching__meta">{{ entry.role }} • {{ entry.level }}</span><br>
    <span class="cv-teaching__years">{{ entry.years | join: "–" }}</span>
  </li>
  {% endif %}
{% endfor %}
</ul>

## Technical Expertise

<p class="cv-prose">
Technical work draws on advanced statistical programming in Stata (including ado-file development and SSC contributions), R, Python, and SQL, combined with experience building analytical data services using SDMX, REST, and data warehouse APIs. Recent work integrates LLM-assisted analysis with human-in-the-loop review workflows, and emphasizes reproducible pipelines, data quality engineering, and PII compliance. Core quantitative methods include econometrics and impact evaluation, survey design and sampling, small area estimation and poverty mapping, and data visualization.
</p>

<p class="cv-prose">
Domain expertise spans poverty measurement and analysis, education statistics and learning assessment, child development indicators, SDG monitoring and reporting, and human capital measurement. Languages: {% for lang in site.data.skills.languages %}{{ lang.language }} ({{ lang.level }}){% unless forloop.last %}, {% endunless %}{% endfor %}.
</p>

## Writing & Commentary

{% assign wb_count = site.data.worldbank_blogs_full.metadata.total_posts | default: 0 %}
{% assign other_count = site.data.other_blogs_full.metadata.total_posts | default: 0 %}
{% assign li_count = site.data.linkedin_blogs.metadata.total_posts | default: 0 %}

<p class="cv-prose">
Regular contributor to policy discourse through {{ wb_count }} World Bank blog posts on education, poverty, and development data; {{ other_count }} UNICEF Data commentaries on child well-being and SDG monitoring; and {{ li_count }} LinkedIn articles on data systems and learning assessment. Selected recent posts:
</p>

{% assign wb_blogs = site.data.worldbank_blogs_full.posts | sort: "date" | reverse %}
{% assign other_blogs = site.data.other_blogs_full.posts | sort: "date" | reverse %}

<ul>
{% for post in wb_blogs limit:3 %}
<li class="cv-pub"><a href="{{ post.url }}" target="_blank">{{ post.title }}</a> ({{ post.year }}, {{ post.channel }})</li>
{% endfor %}
{% for post in other_blogs limit:2 %}
<li class="cv-pub"><a href="{{ post.url }}" target="_blank">{{ post.title }}</a> ({{ post.year }}, {{ post.organization }})</li>
{% endfor %}
</ul>

<p class="cv-nav-link"><a href="/blogs/">View all blogs and articles →</a></p>

<!--
===========================================
CV AUTO-GENERATION NOTES
===========================================
This CV page is auto-generated from YAML data files:
- _data/profile.yml      → Summary, contributions, service
- _data/work_experience.yml → Work history
- _data/education.yml    → Education entries
- _data/citations.yml    → Citation metrics (compact summary)
- _data/publications.yml → Selected publications by type
- _data/events.yml       → Talks & presentations
- _data/teaching.yml     → Teaching & mentoring
- _data/skills.yml       → Technical expertise (prose)
- _data/worldbank_blogs_full.yml → Blog counts and recent posts
- _data/other_blogs_full.yml    → UNICEF/other blog posts
- _data/linkedin_blogs.yml      → LinkedIn articles

To update CV content, edit the YAML files directly.
The page will rebuild automatically on next Jekyll build.

Section order (Option C - Hybrid):
1. Profile + contributions
2. Work Experience
3. Education
4. Selected Publications (with compact citation metrics)
5. Service & Leadership
6. Talks & Presentations
7. Teaching & Mentoring
8. Technical Expertise (prose from skills.yml)
9. Writing & Commentary (prose from blog data)

Last refactored: 2026-02-14
-->
