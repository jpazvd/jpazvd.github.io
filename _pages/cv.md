---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
{% for edu in site.data.education %}
* {{ edu.degree }}. {{ edu.institution }}, {{ edu.location }}. {{ edu.year }}. {% if edu.supervisors %}Supervisors: {{ edu.supervisors }}.{% elsif edu.supervisor %}Supervisor: {{ edu.supervisor }}.{% endif %}
{% endfor %}

Work experience
======
{% for job in site.data.work_experience %}
* {{ job.position }}, {{ job.organization }}  {{ job.start_date }} - {{ job.end_date }}
{{ job.description }}

{% endfor %}

Skills
======
* Statistical Analysis & Econometrics
* Data Analytics & Visualization  
* Program Evaluation & Impact Assessment
* Educational Measurement & Learning Analytics
* Policy Analysis & Development
* Team Leadership & Management

Publications
======
{% bibliography --max 20 %}

*For a complete list of publications, see [Publications page]({{ base_path }}/publications/) or [Google Scholar](https://scholar.google.com/citations?user=lTKXA78AAAAJ).*
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Chief Statistician role overseeing global child data initiatives
* Editorial board member for development economics journals
* Reviewer for major academic journals in economics and education
* Technical advisor for international development organizations
