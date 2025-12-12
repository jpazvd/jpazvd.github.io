---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
description: "Publications by João Pedro Azevedo: 144+ works on Learning Poverty, education economics, poverty measurement. Includes Lancet, World Development articles."
---

{% include base_path %}

<!-- Citation Metrics Banner -->
<div class="citation-metrics jp-gradient-banner">
  <h3 class="jp-gradient-banner__title">📊 Citation & Impact Metrics</h3>
  <div class="jp-stats-row">
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.google_scholar.total_citations | default: '5,500+' }}</div>
      <div class="jp-stat__label">Total Citations</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.google_scholar.h_index | default: '30' }}</div>
      <div class="jp-stat__label">h-index</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.google_scholar.i10_index | default: '62' }}</div>
      <div class="jp-stat__label">i10-index</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.repec.total_works | default: '84' }}</div>
      <div class="jp-stat__label">RePEc Works</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.repec.total_downloads_all_time | default: '32,000+' }}</div>
      <div class="jp-stat__label">Total Downloads</div>
    </div>
  </div>
  <div class="jp-banner__footer">
    <a href="{{ site.data.citations.google_scholar.profile_url }}" target="_blank" rel="noopener">Google Scholar</a> |
    <a href="{{ site.data.citations.repec.profile_url }}" target="_blank" rel="noopener">RePEc/IDEAS</a> |
    <a href="{{ site.data.citations.orcid.profile_url }}" target="_blank" rel="noopener">ORCID</a>
    <br>Last updated: {{ site.data.citations.google_scholar.last_updated }}
  </div>
</div>

<!-- Publication Outlets & Impact Factors -->
<div class="jp-soft-panel">
  <h3 class="jp-soft-panel__title">📰 Selected Publication Outlets</h3>
  <p class="jp-muted">Publications in high-impact peer-reviewed journals and policy outlets:</p>
  
  <table class="jp-table">
    <thead>
      <tr>
        <th>Journal / Outlet</th>
        <th class="jp-table__center">Impact Factor</th>
        <th class="jp-table__center">Category</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>The Lancet</strong></td>
        <td class="jp-table__center"><span class="jp-badge jp-badge--success">168.9</span></td>
        <td class="jp-table__center">Medical</td>
      </tr>
      <tr>
        <td><strong>World Development</strong></td>
        <td class="jp-table__center"><span class="jp-badge jp-badge--info">5.3</span></td>
        <td class="jp-table__center">Development Economics</td>
      </tr>
      <tr>
        <td><strong>World Bank Research Observer</strong></td>
        <td class="jp-table__center"><span class="jp-badge jp-badge--info">4.2</span></td>
        <td class="jp-table__center">Economics</td>
      </tr>
      <tr>
        <td><strong>CEPAL Review</strong></td>
        <td class="jp-table__center"><span class="jp-badge jp-badge--muted">0.8</span></td>
        <td class="jp-table__center">Development Policy</td>
      </tr>
      <tr>
        <td><strong>World Bank Economic Premise</strong></td>
        <td class="jp-table__center"><span class="jp-badge jp-badge--muted">Policy</span></td>
        <td class="jp-table__center">Policy Brief</td>
      </tr>
      <tr>
        <td><strong>World Bank Policy Research Working Papers</strong></td>
        <td class="jp-table__center"><span class="jp-badge jp-badge--muted">WP</span></td>
        <td class="jp-table__center">Working Papers</td>
      </tr>
    </tbody>
  </table>
  <p class="jp-muted"><em>Impact factors from 2024 Journal Citation Reports (Clarivate)</em></p>
</div>

<!-- Publication Breakdown by Type -->
<div class="jp-breakdown-grid">
  <div class="jp-breakdown-card">
    <div class="jp-breakdown-card__value">{{ site.data.citations.repec.journal_articles.count | default: '7' }}</div>
    <div class="jp-muted">Peer-Reviewed Articles</div>
  </div>
  <div class="jp-breakdown-card">
    <div class="jp-breakdown-card__value">{{ site.data.citations.repec.working_papers.count | default: '50' }}</div>
    <div class="jp-muted">Working Papers</div>
  </div>
  <div class="jp-breakdown-card">
    <div class="jp-breakdown-card__value">{{ site.data.citations.repec.books.count | default: '3' }}</div>
    <div class="jp-muted">Books</div>
  </div>
  <div class="jp-breakdown-card">
    <div class="jp-breakdown-card__value">{{ site.data.citations.repec.software.count | default: '22' }}</div>
    <div class="jp-muted">Software Modules</div>
  </div>
</div>

<!-- Rankings -->
<div class="jp-rankings">
  <h3 class="jp-rankings__title">🏆 RePEc Rankings</h3>
  <div class="jp-rankings-row">
    <div class="jp-rankings-card">
      <div class="jp-rankings-card__value">#{{ site.data.citations.repec.rankings.software_global.rank_total_downloads | default: '19' }}</div>
      <div class="jp-muted">Software Downloads<br>(Global)</div>
    </div>
    <div class="jp-rankings-card">
      <div class="jp-rankings-card__value">#{{ site.data.citations.repec.rankings.software_us.rank_total_downloads | default: '6' }}</div>
      <div class="jp-muted">Software Downloads<br>(US)</div>
    </div>
    <div class="jp-rankings-card">
      <div class="jp-rankings-card__value">Top 5%</div>
      <div class="jp-muted">Authors by<br>Downloads</div>
    </div>
  </div>
</div>

<hr class="jp-hr">

<h2>📚 Full Publication Profiles</h2>

<ul>
  <li><a href="https://scholar.google.com/citations?user=lTKXA78AAAAJ" target="_blank"><strong>Google Scholar</strong></a> — Complete citation record ({{ site.data.citations.google_scholar.total_citations }} citations)</li>
  <li><a href="https://ideas.repec.org/e/pwa88.html" target="_blank"><strong>RePEc/IDEAS</strong></a> — Working papers, articles, and software ({{ site.data.citations.repec.total_works }} works)</li>
  <li><a href="https://openknowledge.worldbank.org/entities/person/360f7a2e-0784-56e1-acf4-7f805fd50257" target="_blank"><strong>World Bank Open Knowledge Repository</strong></a> — Official World Bank publications ({{ site.data.citations.world_bank_okr.publication_count }} publications)</li>
  <li><a href="https://orcid.org/0000-0002-3844-215X" target="_blank"><strong>ORCID</strong></a> — Persistent author identifier</li>
</ul>

<hr style="margin: 2rem 0;">

<h2>🔬 Selected High-Impact Publications</h2>

<h3>Peer-Reviewed Journal Articles</h3>

<ol>
  <li><strong>Azevedo, JP</strong>, Hasan, A, Goldemberg, D, Geven, K, Iqbal, SA (2021). <a href="https://doi.org/10.1093/wbro/lkab003" target="_blank">"Simulating the Potential Impacts of COVID-19 School Closures on Schooling and Learning Outcomes: A Set of Global Estimates."</a> <em>The World Bank Research Observer</em>, 36(1), 1-40. <span style="background: #17a2b8; color: white; padding: 1px 6px; border-radius: 3px; font-size: 0.8rem;">IF: 4.2</span></li>
  
  <li>Castañeda, A, Doan, D, Newhouse, D, Nguyen, MC, Uematsu, H, <strong>Azevedo, JP</strong> (2018). <a href="https://doi.org/10.1016/j.worlddev.2017.08.002" target="_blank">"A New Profile of the Global Poor."</a> <em>World Development</em>, 101, 250-267. <span style="background: #17a2b8; color: white; padding: 1px 6px; border-radius: 3px; font-size: 0.8rem;">IF: 5.3</span></li>
  
  <li>Andalón, M, <strong>Azevedo, JP</strong>, Rodríguez-Castelán, C, Sanfelice, V, Valderrama-González, D (2016). <a href="https://doi.org/10.1016/j.worlddev.2015.12.020" target="_blank">"Weather Shocks and Health at Birth in Colombia."</a> <em>World Development</em>, 82, 69-82. <span style="background: #17a2b8; color: white; padding: 1px 6px; border-radius: 3px; font-size: 0.8rem;">IF: 5.3</span></li>
</ol>

<h3>World Bank Flagship Publications</h3>

<ol>
  <li><strong>Azevedo, JP</strong>, et al. (2021). <a href="https://www.worldbank.org/en/topic/education/publication/state-of-global-learning-poverty" target="_blank">"Learning Poverty: Measures and Simulations."</a> <em>World Bank Policy Research Working Paper</em> No. 9446.</li>
  
  <li><strong>Azevedo, JP</strong>, et al. (2020). <a href="https://openknowledge.worldbank.org/handle/10986/34654" target="_blank">"Simulating the Potential Impacts of COVID-19 School Closures on Schooling and Learning Outcomes."</a> <em>World Bank Policy Research Working Paper</em> No. 9284.</li>
</ol>

<p style="margin-top: 2rem; font-size: 0.9rem; color: #666;"><em>For a complete list of publications, please visit my <a href="https://scholar.google.com/citations?user=lTKXA78AAAAJ" target="_blank">Google Scholar</a> or <a href="https://ideas.repec.org/e/pwa88.html" target="_blank">RePEc</a> profiles.</em></p>
