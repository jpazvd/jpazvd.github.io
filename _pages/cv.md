---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

<!-- Include citation metrics at the top -->
{% include citation-metrics.html %}

### 📋 Quick Navigation

**👤 Profile:** [Education](#education) • [Experience](#work-experience) • [Skills](#skills)  
**📑 Research:** [Recent Publications](#recent-publications-last-5-years) • [All Publications](#publications-by-type) • [Books](#books-and-book-chapters) • [Reports](#reports)  
**🎓 Academic:** [Talks](#talks) • [Teaching](#teaching) • [Service](#service-and-leadership)

---

## Professional Summary

Development economist and data scientist with over two decades of experience at the intersection of education policy, poverty analysis, and global development. Currently serving in senior leadership roles at UNICEF and previously at the World Bank, with a focus on using rigorous quantitative methods to inform evidence-based policymaking. Leading author on global education and child development indicators, with expertise in measuring learning poverty, education inequality, and the socioeconomic impacts of global crises. Published 70+ peer-reviewed articles, books, and policy reports that have shaped international development strategies and COVID-19 education recovery frameworks.

---

## Education
======
{% for edu in site.data.education %}
* {{ edu.degree }}. {{ edu.institution }}, {{ edu.location }}. {{ edu.year }}. {% if edu.supervisors %}Supervisors: {{ edu.supervisors }}.{% elsif edu.supervisor %}Supervisor: {{ edu.supervisor }}.{% endif %}
{% endfor %}

---

## Work Experience
======
{% for job in site.data.work_experience %}
* **{{ job.position }}**, {{ job.organization }}  
  {{ job.start_date }} - {{ job.end_date }}  
  {{ job.description }}

{% endfor %}

---

## Skills
======
* **Statistical Analysis & Econometrics**: Advanced econometric modeling, causal inference, impact evaluation
* **Data Analytics & Visualization**: Large-scale data processing, statistical software (R, Stata, Python), dashboard development  
* **Program Evaluation & Impact Assessment**: Randomized controlled trials, quasi-experimental methods, cost-effectiveness analysis
* **Educational Measurement & Learning Analytics**: Learning assessments, psychometric analysis, educational data mining
* **Policy Analysis & Development**: Evidence-based policy design, stakeholder engagement, international development frameworks
* **Team Leadership & Management**: Cross-functional team leadership, international collaboration, capacity building

---

## Recent Publications (Last 5 Years)
======

{% bibliography --query @*[year>=2020] %}

---

## Publications by Type
======

### Journal Articles (Pre-2020)

{% bibliography --query @article[year<2020] %}

### Books and Book Chapters

{% bibliography --query @book %}

{% bibliography --query @incollection %}

{% bibliography --query @inbook %}

### Reports

{% bibliography --query @report %}

### Working Papers and Technical Reports

{% bibliography --query @workingpaper %}

{% bibliography --query @techreport %}

{% bibliography --query @series %}

### Conference Papers

{% bibliography --query @inproceedings %}

{% bibliography --query @conference %}

### Other Publications

{% bibliography --query @misc %}

{% bibliography --query @unpublished %}

{% bibliography --query @online %}

---

## Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
---

## Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

---
  
## Service and Leadership
======

### Editorial and Review Services
* Editorial board member for development economics journals
* Peer reviewer for major academic journals in economics, education, and development
* Technical reviewer for World Bank, UNESCO, and UNICEF flagship reports

### International Advisory Roles
* **UNICEF**: Chief Statistician role overseeing global child data initiatives
* **UNESCO**: Global Education Monitoring Report contributor and technical advisor
* **World Bank**: Flagship education reports lead author and strategic advisor
* **COVID-19 Response**: Education recovery strategy development and policy guidance

### Professional Memberships and Leadership
* American Economic Association (AEA)
* Latin American and Caribbean Economic Association (LACEA)
* Association for the Evaluation of Educational Achievement (IEA)
* Technical advisory committees for major international assessments

---

### 📚 **Publication Statistics**

**Total Publications:** 70+ spanning 2002-2024  
**Recent Impact:** Lead author on major COVID-19 education studies cited 500+ times  
**Policy Influence:** Research directly informing UNESCO SDG 4 monitoring and World Bank education strategy  
**Geographic Expertise:** Global development focus with deep Latin America specialization

[⬆️ Back to Top](#top) • [🏠 Home](/) • [📚 Publications](/publications/) • [💼 Research](/research/)
