---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

## All Publications

{% bibliography %}

---

## Recent Publications (Last 5 Years)

{% bibliography --query @*[year>=2020] --max 10 %}

---

## Journal Articles

{% bibliography --query @article %}

---

## Books and Book Chapters

{% bibliography --query @book,@incollection,@inbook %}

---

## Conference Papers

{% bibliography --query @inproceedings,@conference %}

---

## Working Papers and Reports

{% bibliography --query @techreport,@misc,@unpublished %}

