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

<p class="cv-download">
  <a href="/files/cv-joao-pedro-azevedo.pdf" class="btn btn--primary">
    Download PDF
  </a>
</p>

<!-- Citation Metrics Banner - pulls from _data/citations.yml -->
<div class="citation-metrics jp-gradient-banner">
  <h3 class="jp-gradient-banner__title">Citation Metrics</h3>
  <div class="jp-stats-row">
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.google_scholar.total_citations | default: '5,500+' }}</div>
      <div class="jp-stat__label">Citations</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.google_scholar.h_index | default: '30' }}</div>
      <div class="jp-stat__label">h-index</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.google_scholar.i10_index | default: '62' }}</div>
      <div class="jp-stat__label">i10-index</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.repec.total_downloads_all_time | default: '32,000+' }}</div>
      <div class="jp-stat__label">RePEc Downloads</div>
    </div>
  </div>
  <div class="jp-banner__footer">
    <a href="{{ site.data.citations.google_scholar.profile_url }}" target="_blank">Google Scholar</a> |
    <a href="{{ site.data.citations.repec.profile_url }}" target="_blank">RePEc/IDEAS</a> |
    <a href="{{ site.data.citations.orcid.profile_url }}" target="_blank">ORCID</a>
    <br>Last updated: {{ site.data.citations.google_scholar.last_updated }}
  </div>
</div>

## Profile

{{ site.data.profile.summary }}

### Selected contributions

<ul>
{% for contribution in site.data.profile.selected_contributions %}
<li>{{ contribution }}</li>
{% endfor %}
</ul>

## Education

<ul>
{% for edu in site.data.education %}
<li>
  <strong>{{ edu.degree }}</strong>, {{ edu.institution }} ({{ edu.location }}), {{ edu.year }}{% if edu.thesis_year %} (thesis submitted {{ edu.thesis_year }}){% endif %}.{% if edu.supervisors %} Supervisors: {{ edu.supervisors }}.{% endif %}
</li>
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

<p><a href="/teaching/">View detailed teaching & mentoring experience →</a></p>

## Skills

{% for category in site.data.skills.technical %}
### {{ category.category }}

<ul>
{% for item in category.items %}
<li>{{ item }}</li>
{% endfor %}
</ul>
{% endfor %}

### Domain Expertise

<ul>
{% for item in site.data.skills.domain %}
<li>{{ item }}</li>
{% endfor %}
</ul>

### Leadership & Management

<ul>
{% for item in site.data.skills.leadership %}
<li>{{ item }}</li>
{% endfor %}
</ul>

### Languages

<ul>
{% for lang in site.data.skills.languages %}
<li>{{ lang.language }} ({{ lang.level }})</li>
{% endfor %}
</ul>

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

<p><a href="/events/">View all speaking engagements →</a></p>

## Blogs, Opinion & Commentaries

{% assign wb_blogs = site.data.worldbank_blogs_full.posts | sort: "date" | reverse %}
{% assign other_blogs = site.data.other_blogs_full.posts | sort: "date" | reverse %}
{% assign linkedin_blogs = site.data.linkedin_blogs.posts | sort: "date" | reverse %}

### World Bank Blogs ({{ site.data.worldbank_blogs_full.metadata.total_posts }} posts)

<ul>
{% for post in wb_blogs limit:5 %}
<li>
  <a href="{{ post.url }}" target="_blank"><strong>{{ post.title }}</strong></a> ({{ post.year }})<br>
  <span class="cv-meta">{{ post.channel }}</span>
</li>
{% endfor %}
</ul>

### UNICEF & Other Organizations

<ul>
{% for post in other_blogs limit:5 %}
<li>
  <a href="{{ post.url }}" target="_blank"><strong>{{ post.title }}</strong></a> ({{ post.year }})<br>
  <span class="cv-meta">{{ post.organization }}</span>
</li>
{% endfor %}
</ul>

### LinkedIn Articles

<ul>
{% for post in linkedin_blogs limit:5 %}
<li>
  <a href="{{ post.url }}"><strong>{{ post.title }}</strong></a> ({{ post.year }})
</li>
{% endfor %}
</ul>

<p><a href="/blogs/">View all blogs and articles →</a></p>

<!-- 
===========================================
CV AUTO-GENERATION NOTES
===========================================
This CV page is auto-generated from YAML data files:
- _data/citations.yml    → Citation metrics banner
- _data/profile.yml      → Summary, contributions, service
- _data/education.yml    → Education entries
- _data/work_experience.yml → Work history
- _data/skills.yml       → Technical, domain, leadership skills

To update CV content, edit the YAML files directly.
The page will rebuild automatically on next Jekyll build.

Last refactored: 2025-12-15
-->
