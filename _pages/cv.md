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

{% include citation-metrics.html %}

**Recent Key Publications:**

* Azevedo JP, Banerjee A, Wilmoth J, Fu H, You D. "Hard truths about under-5 mortality: call for urgent global action." *The Lancet*. 2024.

* Strong K, You D, Banerjee A, Azevedo JP. "Global health estimates should be more responsive to country needs." *The Lancet*. 2024.

* Azevedo JP, Hasan A, Goldemberg D, Geven K, Iqbal SA. "Simulating the potential impacts of COVID-19 school closures on schooling and learning outcomes: A set of global estimates." *The World Bank Research Observer*. 2021; 36(1): 1-40.

* Azevedo JP, Crawford M, Nayar R, Rogers FH, et al. "Ending Learning Poverty: What Will It Take?" World Bank Report. 2019.

**Policy Impact & Recognition:**
* UNESCO Global Education Monitoring Report contributor
* World Bank flagship education reports lead author
* UNICEF State of the World's Children advisory role
* COVID-19 education response strategy development

*For complete publication list (70+ publications), see [Publications page]({{ base_path }}/publications/) or [Google Scholar](https://scholar.google.com/citations?user=lTKXA78AAAAJ).*
  
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
