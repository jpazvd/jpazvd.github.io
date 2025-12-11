---
layout: archive
title: "Data & Analytics Tools"
permalink: /tools/
author_profile: true
description: "Stata modules and data analytics tools by João Pedro Azevedo including WBOPENDATA, poverty measurement, and survey analysis tools."
---

{% include base_path %}

<p>Open-source tools and Stata modules I have developed for data analysis, poverty measurement, and accessing World Bank data.</p>

<div style="background: #e8f5e9; padding: 1rem; border-radius: 8px; margin-bottom: 2rem;">
  <strong>📈 Impact:</strong> {{ site.data.citations.repec.software.downloads_total | default: '26,000+' }} total downloads | 
  Ranked <strong>#{{ site.data.citations.repec.rankings.software_global.rank_total_downloads }}</strong> globally for software on RePEc
</div>

<h2>🔧 Stata Modules on SSC</h2>

<h3>WBOPENDATA</h3>
<p>
  Access World Bank databases directly from Stata. Query the World Development Indicators, 
  Doing Business, Health Nutrition and Population Statistics, and more.
</p>
<ul>
  <li><strong>Install:</strong> <code>ssc install wbopendata</code></li>
  <li><a href="https://github.com/worldbank/wbopendata" target="_blank">GitHub Repository</a></li>
  <li><a href="https://datahelpdesk.worldbank.org/knowledgebase/articles/889464-wbopendata-stata-module-to-access-world-bank-} databases" target="_blank">Documentation</a></li>
</ul>

<h3>POVCALNET / PIP</h3>
<p>
  Access the World Bank's global poverty estimates directly from Stata.
</p>
<ul>
  <li><strong>Install:</strong> <code>ssc install povcalnet</code></li>
  <li><a href="https://github.com/worldbank/povcalnet" target="_blank">GitHub Repository</a></li>
</ul>

<h3>Other Stata Modules</h3>

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
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong>ainequal</strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Inequality measures</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install ainequal</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong>apoverty</strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Poverty measures</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install apoverty</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong>adecomp</strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Shapley decomposition</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install adecomp</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong>drdecomp</strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Datt-Ravallion decomposition</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install drdecomp</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong>skdecomp</strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Shapley-Kelkar decomposition</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install skdecomp</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong>mpovline</strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Multiple poverty lines</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install mpovline</code></td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong>groupfunction</strong></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Collapse with multiple functions</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><code>ssc install groupfunction</code></td>
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
  <li><a href="https://github.com/worldbank/povcalnet" target="_blank">worldbank/povcalnet</a> - PovcalNet Stata module</li>
</ul>

<hr>

<p style="font-size: 0.85em; color: #666;">
  <em>All tools are open source and available for academic and research use.</em>
</p>
