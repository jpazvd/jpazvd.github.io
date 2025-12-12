---
title: "Test Publications Page"
permalink: /test-publications/
author_profile: true
---

Testing Jekyll Scholar with your bibliography:

## All Publications

{% bibliography %}

## Recent Publications (2020-2025)

{% bibliography --query @*[year>=2020] %}

## Conference Papers

{% bibliography --query @inproceedings %}

## Journal Articles

{% bibliography --query @article %}
