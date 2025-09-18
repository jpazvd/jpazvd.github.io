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
<p><strong>Recent Publications:</strong></p>

<ul>
<li>Azevedo JP, Banerjee A, Wilmoth J, Fu H, You D. "Hard truths about under-5 mortality: call for urgent global action." <em>Lancet</em>. 2024. DOI: <a href="https://doi.org/10.1016/S0140-6736(24)00501-4">10.1016/S0140-6736(24)00501-4</a></li>

<li>Strong K, You D, Banerjee A, Azevedo JP. "Global health estimates should be more responsive to country needs." <em>Lancet</em>. 2024. DOI: <a href="https://doi.org/10.1016/S0140-6736(24)00463-X">10.1016/S0140-6736(24)00463-X</a></li>

<li>Azevedo JP, Hasan A, Goldemberg D, Geven K, Iqbal SA. "Simulating the potential impacts of COVID-19 school closures on schooling and learning outcomes: A set of global estimates." <em>The World Bank Research Observer</em>. 2021; 36(1): 1-40.</li>

<li>Azevedo JP, Crawford M, Nayar R, Rogers FH, et al. "Ending Learning Poverty: What Will It Take?" World Bank Report. 2019.</li>

<li>Castañeda A, Doan D, Newhouse D, Nguyen MC, Uematsu H, Azevedo JP. "A New Profile of the Global Poor." <em>World Development</em>. 2018; 101(C): 250-267.</li>
</ul>

<p><em>For a complete list of 70+ publications, see <a href="{{ base_path }}/publications/">Publications page</a> or <a href="https://scholar.google.com/citations?user=lTKXA78AAAAJ">Google Scholar</a>.</em></p>
  
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
