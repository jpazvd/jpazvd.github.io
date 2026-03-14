---
layout: single
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
description: "João Pedro Azevedo is UNICEF's Chief Statistician, leading global child data initiatives. PhD economist with publications in Lancet, World Development, and World Bank Research Observer."
redirect_from: 
  - /about/
  - /about.html
---

**Development economist using data, measurement, and analytics to improve outcomes for children and vulnerable populations.**

I am [UNICEF's first Chief Statistician](https://data.unicef.org), appointed in February 2023 to lead the organization's global data and statistical work.

Before joining UNICEF, I spent 16 years at the [World Bank](https://www.worldbank.org/en/about/people/j/joao-pedro-azevedo), most recently as Lead Economist in the Education Global Practice and the Poverty and Equity Practice. I served as EdTech Fellow, Education Statistics Coordinator, and co-led the Global Solution Group on Welfare Measurement and Statistical Capacity for Results, and the Data for Goals initiative.

Earlier in my career I was Superintendent of Monitoring and Evaluation at the [Secretariat of Finance of the State of Rio de Janeiro](https://www.fazenda.rj.gov.br/) and a research fellow at the [Institute of Applied Economic Research (IPEA)](https://ipea.gov.br) in Rio de Janeiro.

I hold a PhD in Economics from Newcastle University and am an elected member of the [International Statistical Institute (ISI)](https://www.isi-web.org/). My research includes peer-reviewed articles in *The Lancet*, *World Development*, *World Bank Research Observer*, and *Frontiers in Public Health*, along with over 20 open-source statistical software packages.

<!-- At a Glance -->
<div class="jp-stats-row jp-at-a-glance">
  <div class="jp-stat">
    <div class="jp-stat__value">{{ site.data.citations.google_scholar.total_citations | default: '5500+' }}</div>
    <div class="jp-stat__label">Citations</div>
  </div>
  <div class="jp-stat">
    <div class="jp-stat__value">{{ site.data.citations.repec.total_works | default: '166' }}</div>
    <div class="jp-stat__label">Works</div>
  </div>
  <div class="jp-stat">
    <div class="jp-stat__value">{{ site.data.citations.repec.software.count | default: '22' }}</div>
    <div class="jp-stat__label">Software Packages</div>
  </div>
  <div class="jp-stat">
    <div class="jp-stat__value">{{ site.data.citations.google_scholar.h_index | default: '30' }}</div>
    <div class="jp-stat__label">h-index</div>
  </div>
</div>

<!-- Featured Work -->
{% if site.data.featured.items %}
<h2>Featured Work</h2>
<div class="jp-featured-list">
  {% for item in site.data.featured.items %}
  <div class="jp-featured-item">
    <span class="jp-featured-item__type">{{ item.type }}</span>
    <a href="{{ item.url }}" target="_blank" rel="noopener" class="jp-featured-item__title">{{ item.title }}</a>
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

<div class="jp-quick-links">
  <a href="{{ site.baseurl }}/research/">Focus</a>
  <a href="{{ site.baseurl }}/publications/">Publications</a>
  <a href="{{ site.baseurl }}/softwares/">Software</a>
  <a href="{{ site.baseurl }}/blogs/">Writing</a>
</div>
