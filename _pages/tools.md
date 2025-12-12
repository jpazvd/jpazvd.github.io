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

<h3><a href="https://ideas.repec.org/c/boc/bocode/s457234.html" target="_blank">WBOPENDATA</a></h3>
<p>
  Access World Bank databases directly from Stata. Query the World Development Indicators, 
  Doing Business, Health Nutrition and Population Statistics, and more.
</p>
<ul>
  <li><strong>Install:</strong> <code>ssc install wbopendata</code></li>
  <li><a href="https://github.com/worldbank/wbopendata" target="_blank">GitHub Repository</a></li>
  <li><a href="https://datahelpdesk.worldbank.org/knowledgebase/articles/889464-wbopendata-stata-module-to-access-world-bank-} databases" target="_blank">Documentation</a></li>
</ul>

<h3><a href="https://ideas.repec.org/c/boc/bocode/s458007.html" target="_blank">POVCALNET / PIP</a></h3>
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
  <li><a href="https://github.com/worldbank/povcalnet" target="_blank">worldbank/povcalnet</a> - PovcalNet Stata module</li>
</ul>

<hr>

<p style="font-size: 0.85em; color: #666;">
  <em>All tools are open source and available for academic and research use.</em>
</p>
