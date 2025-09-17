---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

## Recent Publications (Last 5 Years)

{% bibliography --query @*[year>=2020] %}

---

## Journal Articles

{% bibliography --query @article[year<2020] %}

---

## Books and Book Chapters

{% bibliography --query @book[year<2020] %}

{% bibliography --query @incollection[year<2020] %}

{% bibliography --query @inbook[year<2020] %}

---

## Conference Papers

{% bibliography --query @inproceedings[year<2020] %}

{% bibliography --query @conference[year<2020] %}

---

## Working Papers and Reports

{% bibliography --query @techreport[year<2020] %}

{% bibliography --query @misc[year<2020] %}

{% bibliography --query @unpublished[year<2020] %}
