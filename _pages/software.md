---
layout: archive
title: "Data & Analytics Tools"
permalink: /softwares/
author_profile: true
description: "Stata modules and data analytics tools by João Pedro Azevedo including WBOPENDATA, poverty measurement, and survey analysis tools."
---

{% include base_path %}

<p>Open-source tools and Stata modules I have developed for data analysis, poverty measurement, and accessing World Bank data.</p>

<!-- Citation Metrics Banner -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
  
  <!-- Google Scholar Card -->
  <div style="background: linear-gradient(135deg, #4285f4 0%, #34a853 100%); color: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(66, 133, 244, 0.3);">
    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
      <svg style="width: 24px; height: 24px;" viewBox="0 0 24 24" fill="white"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5l4.838 3.94A8 8 0 0 1 12 9a8 8 0 0 1 7.162 4.44L24 9.5z"/></svg>
      <strong style="font-size: 1.1rem;">Google Scholar</strong>
    </div>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; text-align: center;">
      <div>
        <div style="font-size: 1.8rem; font-weight: bold;">{{ site.data.citations.google_scholar.total_citations | default: '5,555' }}</div>
        <div style="font-size: 0.8rem; opacity: 0.9;">Citations</div>
      </div>
      <div>
        <div style="font-size: 1.8rem; font-weight: bold;">{{ site.data.citations.google_scholar.h_index | default: '30' }}</div>
        <div style="font-size: 0.8rem; opacity: 0.9;">h-index</div>
      </div>
      <div>
        <div style="font-size: 1.8rem; font-weight: bold;">{{ site.data.citations.google_scholar.i10_index | default: '62' }}</div>
        <div style="font-size: 0.8rem; opacity: 0.9;">i10-index</div>
      </div>
    </div>
    <div style="font-size: 0.75rem; opacity: 0.8; margin-top: 1rem; text-align: right;">
      Updated: {{ site.data.citations.google_scholar.last_updated | default: '2025-12-10' }}
    </div>
  </div>

  <!-- RePEc Software Card -->
  <div style="background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%); color: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(44, 62, 80, 0.3);">
    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
      <svg style="width: 24px; height: 24px;" viewBox="0 0 24 24" fill="white"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
      <strong style="font-size: 1.1rem;">RePEc Software</strong>
    </div>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; text-align: center;">
      <div>
        <div style="font-size: 1.8rem; font-weight: bold;">{{ site.data.citations.repec.software.downloads_total | default: '26,886' }}</div>
        <div style="font-size: 0.8rem; opacity: 0.9;">Downloads</div>
      </div>
      <div>
        <div style="font-size: 1.8rem; font-weight: bold;">#{{ site.data.citations.repec.rankings.software_global.rank_total_downloads | default: '19' }}</div>
        <div style="font-size: 0.8rem; opacity: 0.9;">Global Rank</div>
      </div>
      <div>
        <div style="font-size: 1.8rem; font-weight: bold;">{{ site.data.citations.repec.software.count | default: '22' }}</div>
        <div style="font-size: 0.8rem; opacity: 0.9;">Modules</div>
      </div>
    </div>
    <div style="font-size: 0.75rem; opacity: 0.8; margin-top: 1rem; text-align: right;">
      Updated: {{ site.data.citations.repec.last_updated | default: '2024-12-10' }}
    </div>
  </div>

</div>

<!-- Citations by Year Chart -->
<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem;">
  <h3 style="margin-top: 0; margin-bottom: 1rem;">📈 Citations by Year</h3>
  <div style="display: flex; align-items: flex-end; gap: 4px; height: 120px; padding: 0.5rem 0;">
    {% assign max_citations = 800 %}
    {% for year in (2015..2025) %}
      {% assign citations = site.data.citations.google_scholar.citations_by_year[year] | default: 0 %}
      {% assign height_percent = citations | times: 100 | divided_by: max_citations %}
      {% if height_percent > 100 %}{% assign height_percent = 100 %}{% endif %}
      {% if height_percent < 5 %}{% assign height_percent = 5 %}{% endif %}
      <div style="flex: 1; display: flex; flex-direction: column; align-items: center;">
        <div style="font-size: 0.65rem; color: #666; margin-bottom: 4px;">{{ citations }}</div>
        <div style="width: 100%; max-width: 30px; height: {{ height_percent }}%; background: linear-gradient(to top, #4285f4, #34a853); border-radius: 4px 4px 0 0;"></div>
        <div style="font-size: 0.6rem; color: #888; margin-top: 4px;">{{ year | slice: 2, 2 }}</div>
      </div>
    {% endfor %}
  </div>
  <p style="font-size: 0.75rem; color: #666; margin-bottom: 0; text-align: center;">
    Source: <a href="{{ site.data.citations.google_scholar.profile_url }}" target="_blank">Google Scholar</a>
  </p>
</div>

<hr>

<h2>🔧 Stata Modules on SSC</h2>

<h3><a href="https://ideas.repec.org/c/boc/bocode/s457234.html" target="_blank">WBOPENDATA</a></h3>
<p>
  Access World Bank databases directly from Stata. Query the World Development Indicators, 
  Doing Business, Health Nutrition and Population Statistics, and more.
</p>
<ul>
  <li><strong>Install:</strong> <code>ssc install wbopendata</code></li>
  <li><a href="https://github.com/worldbank/wbopendata" target="_blank">GitHub Repository</a></li>
  <li><a href="https://datahelpdesk.worldbank.org/knowledgebase/articles/889464-wbopendata-stata-module-to-access-world-bank-databases" target="_blank">Documentation</a></li>
</ul>

<h3>All Stata Modules</h3>

<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr style="background: #f5f5f5;">
      <th style="padding: 8px; text-align: left; border-bottom: 2px solid #ddd;">Module</th>
      <th style="padding: 8px; text-align: left; border-bottom: 2px solid #ddd;">Description</th>
      <th style="padding: 8px; text-align: left; border-bottom: 2px solid #ddd;">Install</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s456748.html" target="_blank">ainequal</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Inequality measures</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install ainequal</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s456750.html" target="_blank">apoverty</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Poverty measures</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install apoverty</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s457562.html" target="_blank">adecomp</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Shapley decomposition</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install adecomp</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s457563.html" target="_blank">drdecomp</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Datt-Ravallion decomposition</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install drdecomp</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s457564.html" target="_blank">skdecomp</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Shapley-Kelkar decomposition</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install skdecomp</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s457565.html" target="_blank">mpovline</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Multiple poverty lines</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install mpovline</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s458475.html" target="_blank">groupfunction</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Collapse with multiple functions</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install groupfunction</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s458525.html" target="_blank">sae</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Small area estimation</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install sae</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s458495.html" target="_blank">fhsae</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Fay-Herriot small area estimation</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install fhsae</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s457191.html" target="_blank">hoi</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Human Opportunity Index</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install hoi</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s449001.html" target="_blank">dfl</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">DiNardo-Fortin-Lemieux decomposition</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install dfl</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s437001.html" target="_blank">grqreg</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Graphical quantile regression</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install grqreg</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s419501.html" target="_blank">outtable</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Export matrix to LaTeX table</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install outtable</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s456749.html" target="_blank">alorenz</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Lorenz and concentration curves</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install alorenz</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s456752.html" target="_blank">isopoverty</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Iso-poverty curves</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install isopoverty</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s456751.html" target="_blank">changemean</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Mean vs distribution effects</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install changemean</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s456987.html" target="_blank">mol</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Effective literacy index (Basu-Foster)</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install mol</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s457125.html" target="_blank">turnbull</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Willingness-to-pay estimation</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install turnbull</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s457126.html" target="_blank">spike</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Zero willingness-to-pay</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install spike</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s436001.html" target="_blank">factortest</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Tests for factor analysis</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install factortest</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong><a href="https://ideas.repec.org/c/boc/bocode/s433202.html" target="_blank">crtest</a></strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Cramer-Ridder pooling test</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install crtest</code></td>
    </tr>
  </tbody>
</table>

<p style="margin-top: 1rem;">
  <a href="https://ideas.repec.org/e/pwa88.html#soft" target="_blank">View all {{ site.data.citations.repec.software.count }} modules on RePEc →</a>
</p>

<hr>

<h2>📁 GitHub Repositories</h2>

<ul>
  <li><a href="https://github.com/worldbank/wbopendata" target="_blank">worldbank/wbopendata</a> - World Bank Open Data Stata module</li>
  <li><a href="https://github.com/jpazvd" target="_blank">jpazvd</a> - Personal GitHub profile with additional code</li>
</ul>

<hr>

<p style="font-size: 0.85em; color: #666;">
  <em>All tools are open source and available for academic and research use.</em>
</p>