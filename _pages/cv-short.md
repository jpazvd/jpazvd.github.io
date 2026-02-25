---
layout: archive
title: "Curriculum Vitae (Short)"
permalink: /cv-short/
author_profile: true
description: "Short Curriculum Vitae of João Pedro Azevedo - UNICEF Chief Statistician, former World Bank Lead Economist."
---

{% include base_path %}

<!-- Print-only header -->
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
  <a href="/files/cv-joao-pedro-azevedo-short.pdf" class="btn btn--primary">
    Download Short CV
  </a>
  <a href="/files/cv-joao-pedro-azevedo.pdf" class="btn">
    Full CV
  </a>
</p>

<!-- Mark body for tight spacing in print CSS -->
<div class="cv-short-body">

## Profile

{{ site.data.cv_short.summary_short }}

<ul>
{% for contribution in site.data.profile.selected_contributions limit:site.data.cv_short.selected_contributions_limit %}
<li>{{ contribution }}</li>
{% endfor %}
</ul>

## Work Experience

{% for job in site.data.work_experience limit:site.data.cv_short.work_experience_limit %}
<div class="cv-job">
<p class="cv-job__meta"><strong>{{ job.position }}</strong>, {{ job.organization }} — {{ job.start_date }}–{{ job.end_date }}</p>
</div>
{% endfor %}

## Education

<ul>
{% for edu in site.data.education %}{% unless edu.degree contains "High School" %}
<li>
  <strong>{{ edu.degree }}</strong>, {{ edu.institution }} ({{ edu.location }}), {{ edu.year }}.
</li>
{% endunless %}{% endfor %}
</ul>

## Selected Publications

<p class="cv-citation-summary">
  Google Scholar: {{ site.data.citations.google_scholar.total_citations | default: '5,500+' }} citations &bull;
  h-index: {{ site.data.citations.google_scholar.h_index | default: '30' }} &bull;
  i10-index: {{ site.data.citations.google_scholar.i10_index | default: '62' }} &bull;
  RePEc: {{ site.data.citations.repec.total_downloads_all_time | default: '32,000+' }} downloads.
  Full list: <a href="{{ site.data.citations.google_scholar.profile_url }}" target="_blank">Google Scholar</a> |
  <a href="{{ site.data.citations.repec.profile_url }}" target="_blank">RePEc/IDEAS</a>
</p>

### Journal Articles

<ul>
{% for pub in site.data.publications.journal_articles %}
<li class="cv-pub">
  {{ pub.authors | join: ", " }} ({{ pub.year }}). "{{ pub.title }}." <em>{{ pub.journal }}</em>{% if pub.volume %}, {{ pub.volume }}{% endif %}{% if pub.issue %}({{ pub.issue }}){% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}.{% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">doi</a>{% endif %}
</li>
{% endfor %}
</ul>

### Software

<ul>
{% for sw_id in site.data.cv_short.featured_software %}{% for pub in site.data.publications.softwares %}{% if pub.id == sw_id %}
<li class="cv-pub">
  {{ pub.authors | join: ", " }} ({{ pub.year }}). {{ pub.title }}: {{ pub.description }}.{% if pub.venue %} {{ pub.venue }}.{% endif %}{% if pub.citations %} ({{ pub.citations }} citations){% endif %}
</li>
{% endif %}{% endfor %}{% endfor %}
</ul>

## Service and Leadership

<ul>
{% for service in site.data.profile.service %}{% for role in site.data.cv_short.featured_service %}{% if service.role == role %}
<li><strong>{{ service.role }}</strong>{% if service.organization %}, {{ service.organization }}{% endif %}{% if service.parent %} ({{ service.parent }}){% endif %}</li>
{% break %}{% endif %}{% endfor %}{% endfor %}
</ul>

## Selected Talks

{% assign recent_events = site.data.events.events | sort: "date" | reverse %}
<ul>
{% for event in recent_events limit:site.data.cv_short.events_limit %}
<li>
  <strong>{{ event.event }}</strong> ({{ event.year }}) — {{ event.role }}{% if event.session %}: "{{ event.session }}"{% endif %}
</li>
{% endfor %}
</ul>

## Technical Skills

<p class="cv-prose">
{{ site.data.cv_short.skills_short }}
</p>

</div>
