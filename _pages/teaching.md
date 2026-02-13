---
layout: archive
title: "Teaching & Mentoring"
permalink: /teaching/
author_profile: true
description: "Teaching and mentoring experience by João Pedro Azevedo in econometrics, development economics, and policy evaluation."
---

{% include base_path %}

<p class="page__lead">Teaching and mentoring experience across university and professional settings, spanning econometrics, development economics, and policy evaluation.</p>

<!-- Tag Filter Buttons -->
<div class="tag-filters">
  <button class="tag-filter active" data-tag="all" onclick="filterTeaching('all', this)">All <span class="filter-count" id="all-count">{{ site.data.teaching.teaching | size }}</span></button>
  <button class="tag-filter" data-tag="statistics" onclick="filterTeaching('statistics', this)">Statistics</button>
  <button class="tag-filter" data-tag="methodology" onclick="filterTeaching('methodology', this)">Methodology</button>
  <button class="tag-filter" data-tag="econometrics" onclick="filterTeaching('econometrics', this)">Econometrics</button>
  <button class="tag-filter" data-tag="governance" onclick="filterTeaching('governance', this)">Governance</button>
  <button class="tag-filter" data-tag="policy" onclick="filterTeaching('policy', this)">Policy</button>
  <button class="tag-filter" data-tag="supervision" onclick="filterTeaching('supervision', this)">Supervision</button>
  <button class="tag-filter" data-tag="seminar" onclick="filterTeaching('seminar', this)">Seminar</button>
  <button class="tag-filter" data-tag="measurement" onclick="filterTeaching('measurement', this)">Measurement</button>
  <button class="tag-filter" data-tag="learning" onclick="filterTeaching('learning', this)">Learning</button>
  <button class="tag-filter" data-tag="poverty" onclick="filterTeaching('poverty', this)">Poverty</button>
</div>

<!-- Teaching List -->
<div id="teaching-container">
{% assign sorted_teaching = site.data.teaching.teaching | sort: "date_start" | reverse %}
{% assign current_year = "" %}
{% for teaching_entry in sorted_teaching %}
  {% if teaching_entry.year != current_year %}
    {% assign current_year = teaching_entry.year %}
<div class="year-divider" data-year="{{ current_year }}">{{ current_year }}</div>
  {% endif %}
  
<div class="teaching-card" data-tags="{{ teaching_entry.tags | join: ',' }}">
  <div class="teaching-header">
    <div class="teaching-header__body">
      <p class="teaching-title">{{ teaching_entry.course_title }}</p>
      <p class="teaching-institution">
        {{ teaching_entry.institution }} • {{ teaching_entry.country }}
      </p>
    </div>
    <span class="teaching-years">
      {% if teaching_entry.years.size > 1 %}{{ teaching_entry.years | join: ", " }}{% else %}{{ teaching_entry.year }}{% endif %}
    </span>
  </div>
  <span class="teaching-level">{{ teaching_entry.level }}</span>
  <span class="teaching-role">{{ teaching_entry.role }}</span>
  <span class="teaching-tags">
    {% for tag in teaching_entry.tags %}<span class="teaching-tag" data-tag="{{ tag }}">{{ tag }}</span>{% endfor %}
  </span>
  {% if teaching_entry.description %}<p class="teaching-description">{{ teaching_entry.description | strip_newlines | truncatewords: 50 }}</p>{% endif %}
  <div class="teaching-meta">
    {% if teaching_entry.duration_hours %}<p><strong>Duration:</strong> {{ teaching_entry.duration_hours }} hours/week</p>{% endif %}
    {% if teaching_entry.semesters %}<p><strong>Period:</strong> {{ teaching_entry.semesters }}</p>{% endif %}
    {% if teaching_entry.affiliation_role %}<p><strong>Position:</strong> {{ teaching_entry.affiliation_role }}</p>{% endif %}
    {% if teaching_entry.pedagogical_approach %}<p><strong>Approach:</strong> {{ teaching_entry.pedagogical_approach }}</p>{% endif %}
    {% if teaching_entry.student_demographics %}<p><strong>Students:</strong> {{ teaching_entry.student_demographics }}</p>{% endif %}
  </div>
</div>
{% endfor %}
</div>

<script src="{{ base_path }}/assets/js/teaching-filter.js"></script>
