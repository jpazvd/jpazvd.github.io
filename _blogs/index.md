---
layout: archive
title: "Blog Posts"
permalink: /blogs/
author_profile: true
---

This section contains my blog posts and academic commentary on development economics, education policy, and global poverty issues.

{% assign all_posts = site.blogs | sort: 'date' | reverse %}

{% for post in all_posts limit: 10 %}
  <article class="archive__item">
    <h3 class="archive__item-title">
      <a href="{{ post.url }}">{{ post.title }}</a>
    </h3>
    <p class="archive__item-excerpt">
      {{ post.excerpt | strip_html | truncate: 160 }}
    </p>
    <p class="archive__item-meta">
      <time datetime="{{ post.date | date: '%Y-%m-%d' }}">
        {{ post.date | date: "%B %d, %Y" }}
      </time>
      {% if post.tags %}
        •
        {% for tag in post.tags %}
          <a href="/blogs/tag/{{ tag | slugify }}/" class="tag">{{ tag }}</a>
        {% endfor %}
      {% endif %}
      {% if post.categories %}
        •
        {% for category in post.categories %}
          <a href="/blogs/category/{{ category | slugify }}/" class="category">{{ category }}</a>
        {% endfor %}
      {% endif %}
    </p>
  </article>
{% endfor %}

## Browse by Topic

{% assign all_tags = "" | split: "" %}
{% for post in all_posts %}
  {% for tag in post.tags %}
    {% assign all_tags = all_tags | push: tag %}
  {% endfor %}
{% endfor %}
{% assign unique_tags = all_tags | uniq | sort %}

{% if unique_tags.size > 0 %}
<div class="tag-cloud">
  <h3>Tags</h3>
  {% for tag in unique_tags %}
    <a href="/blogs/tag/{{ tag | slugify }}/" class="tag-link">{{ tag }}</a>
  {% endfor %}
</div>
{% endif %}

## Archive by Year

{% assign posts_by_year = all_posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year_group in posts_by_year %}
  <h3>{{ year_group.name }}</h3>
  <ul class="archive-list">
    {% for post in year_group.items %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <time datetime="{{ post.date | date: '%Y-%m-%d' }}">
          {{ post.date | date: "%B %d" }}
        </time>
      </li>
    {% endfor %}
  </ul>
{% endfor %}

---

*Subscribe to my [RSS feed]({{ '/feed.xml' | relative_url }}) to stay updated with new posts.*