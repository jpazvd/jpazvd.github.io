---
layout: single
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
last_modified_at: 2026-03-27
description: "João Pedro Azevedo is UNICEF's Chief Statistician, leading global child data initiatives. PhD economist with publications in Lancet, World Development, and World Bank Research Observer."
redirect_from:
  - /about/
  - /about.html
---

**Development economist using data, measurement, and analytics to improve outcomes for children and vulnerable populations.**

I am [UNICEF's first Chief Statistician](https://data.unicef.org), appointed in February 2023 to lead the organization's global data and statistical work.

Before joining UNICEF, I spent 16 years at the [World Bank](https://www.worldbank.org/en/about/people/j/joao-pedro-azevedo), most recently as Lead Economist in the Education Global Practice and the Poverty and Equity Practice. I served as EdTech Fellow, Education Statistics Coordinator, and co-led the Global Solution Group on Welfare Measurement and Statistical Capacity for Results, and the Data for Goals initiative.

Earlier in my career I was Superintendent of Monitoring and Evaluation at the [Secretariat of Finance of the State of Rio de Janeiro](https://www.fazenda.rj.gov.br/) and a research fellow at the [Institute of Applied Economic Research (IPEA)](https://ipea.gov.br) in Rio de Janeiro.

I hold a PhD in Economics from Newcastle University and am an elected member of the [International Statistical Institute (ISI)](https://www.isi-web.org/). My research includes peer-reviewed articles in *The Lancet*, *World Development*, *World Bank Research Observer*, and *Frontiers in Public Health*, along with {{ site.data.citations.repec.software.count }} open-source statistical software packages.

<!-- At a Glance — values come ONLY from _data/citations.yml; numeric fallbacks
     are banned (they silently mask a broken data path — see docs/AUTOMATION.md) -->
<div class="jp-stats-row jp-at-a-glance">
  <div class="jp-stat">
    <div class="jp-stat__value">{% include format-number.html number=site.data.citations.google_scholar.total_citations %}</div>
    <div class="jp-stat__label">Citations</div>
  </div>
  <div class="jp-stat">
    <div class="jp-stat__value">{{ site.data.citations.repec.total_works | default: '—' }}</div>
    <div class="jp-stat__label">Works</div>
  </div>
  <div class="jp-stat">
    <div class="jp-stat__value">{{ site.data.citations.repec.software.count | default: '—' }}</div>
    <div class="jp-stat__label">Software Packages</div>
  </div>
  <div class="jp-stat">
    <div class="jp-stat__value">{{ site.data.citations.google_scholar.h_index | default: '—' }}</div>
    <div class="jp-stat__label">h-index</div>
  </div>
</div>

<!-- Featured Work -->
{% if site.data.featured.items %}
<h2>Featured Work</h2>
<div class="jp-featured-list">
  {% for item in site.data.featured.items %}
  <div class="jp-featured-item jp-featured-item--stacked">
    <div class="jp-featured-item__header">
      <span class="jp-featured-item__type">{{ item.type }}</span>
      <a href="{{ item.url }}" target="_blank" rel="noopener" class="jp-featured-item__title">{{ item.title }}</a>
    </div>
    <span class="jp-featured-item__desc">{{ item.description }}</span>
  </div>
  {% endfor %}
</div>
{% endif %}

<!-- Recent Posts -->
{% if site.posts.size > 0 %}
<h2>Recent Writing</h2>
<div class="jp-featured-list">
  {% for post in site.posts limit:3 %}
  <div class="jp-featured-item jp-featured-item--stacked">
    <div class="jp-featured-item__header">
      <span class="jp-featured-item__type">{{ post.date | date: "%b %Y" }}</span>
      <a href="{{ post.url }}" class="jp-featured-item__title">{{ post.title }}</a>
    </div>
    <span class="jp-featured-item__desc">{{ post.excerpt | strip_html | truncate: 120 }}</span>
  </div>
  {% endfor %}
</div>
<p style="margin-top: 0.5em;"><a href="{{ site.baseurl }}/blogs/">View all articles →</a></p>
{% endif %}

{% include subscribe-form.html %}

<div class="jp-cta-row">
  <a href="{{ site.baseurl }}/research/" class="btn btn--primary btn--large">Explore my Research</a>
  <a href="{{ site.baseurl }}/publications/" class="btn btn--inverse btn--large">Publications</a>
  <a href="{{ site.baseurl }}/cv/" class="btn btn--inverse btn--large">CV</a>
</div>
