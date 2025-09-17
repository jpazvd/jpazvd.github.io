---
layout: archive
title: "Publications Test"
permalink: /publications-test/
author_profile: true
---

# Simple Bibliography Test

{% bibliography --max 5 %}

---

# By Year Test (Recent)

{% bibliography --query @*[year>=2023] %}

---

# Journal Articles Only

{% bibliography --query @article --max 3 %}