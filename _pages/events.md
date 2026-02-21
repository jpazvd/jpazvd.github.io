---
layout: archive
title: "Events & Talks"
permalink: /events/
author_profile: true
description: "Speaking engagements, conference presentations, and panel discussions by João Pedro Azevedo on education measurement, official statistics, and child well-being."
---

{% include base_path %}

<p class="page__lead">Selected speaking engagements, conference presentations, and panel discussions.</p>

<!-- Tag Filter Buttons -->
<div class="tag-filters">
  <button class="tag-filter active" data-tag="all">All <span class="filter-count" id="all-count">{{ site.data.events.events | size }}</span></button>
  {% for tag in site.data.events.tags %}
    <button class="tag-filter" data-tag="{{ tag[0] }}">{{ tag[1].label }}</button>
  {% endfor %}
</div>



<!-- Events List -->
<div id="events-container">
{% assign current_year = "" %}
{% for event in site.data.events.events %}
  {% if event.year != current_year %}
    {% assign current_year = event.year %}
    <div class="year-divider" data-year="{{ current_year }}">{{ current_year }}</div>
  {% endif %}
  
  <div class="event-card" data-tags="{{ event.tags | join: ',' }}" data-year="{{ event.year }}">
    <div class="event-header">
      <div>
        <p class="event-title">
          {% if event.link %}<a href="{{ event.link }}" target="_blank">{{ event.event }}</a>{% else %}{{ event.event }}{% endif %}
        </p>
        <p class="event-location">{{ event.location }}</p>
      </div>
      <span class="event-date">{{ event.date | date: "%b %Y" }}</span>
    </div>
    <span class="event-role">{{ event.role }}</span>
    <span class="event-tags">
      {% for tag in event.tags %}
        <span class="event-tag" data-tag="{{ tag }}">{{ site.data.events.tags[tag].label }}</span>
      {% endfor %}
    </span>
    {% if event.session %}
      <p class="event-session"><strong>Session:</strong> {{ event.session }}</p>
    {% endif %}
    <div class="event-details">
      {% if event.co_panelists %}
        <p><strong>Co-panelists:</strong> {{ event.co_panelists }}</p>
      {% endif %}
      {% if event.co_speakers %}
        <p><strong>Co-speakers:</strong> {{ event.co_speakers }}</p>
      {% endif %}
      {% if event.co_presenters %}
        <p><strong>Co-presenters:</strong> {{ event.co_presenters }}</p>
      {% endif %}
      {% if event.partners %}
        <p><strong>Partners:</strong> {{ event.partners }}</p>
      {% endif %}
      {% if event.organizers %}
        <p><strong>Organizers:</strong> {{ event.organizers }}</p>
      {% endif %}
      {% if event.moderator %}
        <p><strong>Moderator:</strong> {{ event.moderator }}</p>
      {% endif %}
      {% if event.description %}
        <p>{{ event.description }}</p>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>

<script src="{{ base_path }}/assets/js/events-filter.js"></script>
