---
layout: archive
title: "CV Sections"
permalink: /cv/
author_profile: true
---

This section organizes my CV into different components.

{% for cv_item in site.cv %}
### [{{ cv_item.title }}]({{ cv_item.url }})
{{ cv_item.description }}

{% endfor %}