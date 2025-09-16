---
layout: archive
title: "Blog Posts"
permalink: /blogs/
author_profile: true
---

# Blog Posts

This section contains my blog posts and academic commentary.

{% for post in site.blogs %}
  <article>
    <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
    <p class="meta">{{ post.date | date: "%B %d, %Y" }}</p>
    <p>{{ post.excerpt }}</p>
  </article>
{% endfor %}