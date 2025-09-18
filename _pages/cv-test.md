---
layout: archive
title: "Test CV"
permalink: /cv-test/
author_profile: true
---

# Test CV Page

This is a test page to verify Jekyll is working.

## Education
* PhD in Economics, University of Newcastle, 2005
* MSc in Economics, Universidade Federal Fluminense, 2001

## Current Position  
* Chief Statistician, UNICEF (March 2023 - Present)

## Test Data Access
{% if site.data.education %}
Education data is accessible!
{% else %}
Education data is NOT accessible.
{% endif %}

## Raw Data Test
{% for edu in site.data.education %}
* {{ edu.degree }} from {{ edu.institution }}
{% endfor %}