---
layout: archive
title: "Data & Analytics Tools"
permalink: /softwares/
author_profile: true
description: "Stata modules and data analytics tools by João Pedro Azevedo including WBOPENDATA, poverty measurement, and survey analysis tools."
---

{% include base_path %}

<p>Open-source tools and Stata modules I have developed for data analysis, poverty measurement, and accessing World Bank data.</p>

<!-- Software Metrics Banner - matching Publications page style -->
<div class="citation-metrics jp-gradient-banner">
  <h3 class="jp-gradient-banner__title">RePEc Software Metrics</h3>
  <div class="jp-stats-row">
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.repec.software.count | default: '22' }}</div>
      <div class="jp-stat__label">Stata Modules</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value">{{ site.data.citations.repec.software.downloads_total | default: '26886' }}</div>
      <div class="jp-stat__label">Total Downloads</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value"><a href="https://logec.repec.org/scripts/authorstat.pf?topnum=50&sortby=td&item=software&country=all" target="_blank" rel="noopener" >#{{ site.data.citations.repec.rankings.software_global.rank_total_downloads | default: '19' }}</a></div>
      <div class="jp-stat__label">Global Rank</div>
    </div>
    <div class="jp-stat">
      <div class="jp-stat__value"><a href="https://logec.repec.org/scripts/authorstat.pf?topnum=50&sortby=td&item=software&country=us" target="_blank" rel="noopener" >#{{ site.data.citations.repec.rankings.software_us.rank_total_downloads | default: '6' }}</a></div>
      <div class="jp-stat__label">US Rank</div>
    </div>
  </div>
  <div class="jp-banner__footer">
    <a href="https://ideas.repec.org/e/pwa88.html#soft" target="_blank" rel="noopener">All Software on IDEAS</a> |
    <a href="{{ site.data.citations.repec.stats_url | default: 'https://logec.repec.org/RAS/pwa88.htm' }}" target="_blank" rel="noopener">Author Statistics</a>
    <br>{{ site.data.citations.repec.ranking_note | default: 'Top 5% of authors by downloads' }} · Last updated: {{ site.data.citations.repec.last_updated | default: '—' }}
  </div>
</div>

<div class="jp-quick-links">
  <a href="{{ base_path }}/publications/">Publications</a>
  <a href="{{ base_path }}/blogs/">Blogs</a>
  <a href="{{ base_path }}/research/">Research</a>
</div>

<hr>

<h2>Stata Modules on SSC</h2>

<h3><a href="https://ideas.repec.org/c/boc/bocode/s457234.html" target="_blank">WBOPENDATA</a></h3>
<p>
  Access over 29,000 indicators from 51 World Bank databases directly from Stata, covering 296 countries and regions from 1960 to present. Supports five download modes, multilingual metadata (EN/ES/FR), and wide or long output formats.
</p>
<ul>
  <li><strong>Install:</strong> <code>ssc install wbopendata</code></li>
  <li><a href="https://github.com/jpazvd/wbopendata" target="_blank">GitHub Repository</a> · <a href="https://github.com/jpazvd/wbopendata/issues/new" target="_blank">Report bugs / Request features</a></li>
  <li><a href="https://datahelpdesk.worldbank.org/knowledgebase/articles/889464-wbopendata-stata-module-to-access-world-bank-databases" target="_blank">Documentation</a></li>
</ul>

<h3>All Stata Modules</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th>Module</th>
      <th>Description</th>
      <th>Install</th>
      <th><i class="fab fa-github"></i></th>
      <th><i class="fas fa-bug"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s456748.html" target="_blank">ainequal</a></strong></td>
      <td>Inequality measures</td>
      <td><code>ssc install ainequal</code></td>
      <td><a href="https://github.com/jpazvd/ainequal" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/ainequal/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s456750.html" target="_blank">apoverty</a></strong></td>
      <td>Poverty measures</td>
      <td><code>ssc install apoverty</code></td>
      <td><a href="https://github.com/jpazvd/apoverty" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/apoverty/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s457562.html" target="_blank">adecomp</a></strong></td>
      <td>Shapley decomposition</td>
      <td><code>ssc install adecomp</code></td>
      <td><a href="https://github.com/jpazvd/adecomp" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/adecomp/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s457563.html" target="_blank">drdecomp</a></strong></td>
      <td>Datt-Ravallion decomposition</td>
      <td><code>ssc install drdecomp</code></td>
      <td><a href="https://github.com/jpazvd/drdecomp" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/drdecomp/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s457564.html" target="_blank">skdecomp</a></strong></td>
      <td>Shapley-Kelkar decomposition</td>
      <td><code>ssc install skdecomp</code></td>
      <td><a href="https://github.com/jpazvd/skdecomp" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/skdecomp/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s457565.html" target="_blank">mpovline</a></strong></td>
      <td>Multiple poverty lines</td>
      <td><code>ssc install mpovline</code></td>
      <td><a href="https://github.com/jpazvd/mpovline" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/mpovline/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s458475.html" target="_blank">groupfunction</a></strong></td>
      <td>Collapse with multiple functions</td>
      <td><code>ssc install groupfunction</code></td>
      <td><a href="https://github.com/jpazvd/groupfunction" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/groupfunction/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s458525.html" target="_blank">sae</a></strong></td>
      <td>Small area estimation</td>
      <td><code>ssc install sae</code></td>
      <td><a href="https://github.com/jpazvd/sae" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/sae/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s458495.html" target="_blank">fhsae</a></strong></td>
      <td>Fay-Herriot small area estimation</td>
      <td><code>ssc install fhsae</code></td>
      <td><a href="https://github.com/jpazvd/fhsae" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/fhsae/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s457191.html" target="_blank">hoi</a></strong></td>
      <td>Human Opportunity Index</td>
      <td><code>ssc install hoi</code></td>
      <td><a href="https://github.com/jpazvd/hoi" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/hoi/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s449001.html" target="_blank">dfl</a></strong></td>
      <td>DiNardo-Fortin-Lemieux decomposition</td>
      <td><code>ssc install dfl</code></td>
      <td><a href="https://github.com/jpazvd/dfl" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/dfl/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s437001.html" target="_blank">grqreg</a></strong></td>
      <td>Graphical quantile regression</td>
      <td><code>ssc install grqreg</code></td>
      <td><a href="https://github.com/jpazvd/grqreg" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/grqreg/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s419501.html" target="_blank">outtable</a></strong></td>
      <td>Export matrix to LaTeX table</td>
      <td><code>ssc install outtable</code></td>
      <td><a href="https://github.com/jpazvd/outtable" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/outtable/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s456749.html" target="_blank">alorenz</a></strong></td>
      <td>Lorenz and concentration curves</td>
      <td><code>ssc install alorenz</code></td>
      <td><a href="https://github.com/jpazvd/alorenz" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/alorenz/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s456752.html" target="_blank">isopoverty</a></strong></td>
      <td>Iso-poverty curves</td>
      <td><code>ssc install isopoverty</code></td>
      <td><a href="https://github.com/jpazvd/isopoverty" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/isopoverty/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s456751.html" target="_blank">changemean</a></strong></td>
      <td>Mean vs distribution effects</td>
      <td><code>ssc install changemean</code></td>
      <td><a href="https://github.com/jpazvd/changemean" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/changemean/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s456987.html" target="_blank">mol</a></strong></td>
      <td>Effective literacy index (Basu-Foster)</td>
      <td><code>ssc install mol</code></td>
      <td><a href="https://github.com/jpazvd/mol" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/mol/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s457125.html" target="_blank">turnbull</a></strong></td>
      <td>Willingness-to-pay estimation</td>
      <td><code>ssc install turnbull</code></td>
      <td><a href="https://github.com/jpazvd/turnbull" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/turnbull/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s457126.html" target="_blank">spike</a></strong></td>
      <td>Zero willingness-to-pay</td>
      <td><code>ssc install spike</code></td>
      <td><a href="https://github.com/jpazvd/spike" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/spike/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s436001.html" target="_blank">factortest</a></strong></td>
      <td>Tests for factor analysis</td>
      <td><code>ssc install factortest</code></td>
      <td><a href="https://github.com/jpazvd/factortest" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/factortest/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://ideas.repec.org/c/boc/bocode/s433202.html" target="_blank">crtest</a></strong></td>
      <td>Cramer-Ridder pooling test</td>
      <td><code>ssc install crtest</code></td>
      <td><a href="https://github.com/jpazvd/crtest" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/crtest/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
  </tbody>
</table>

<p>
  <a href="https://ideas.repec.org/e/pwa88.html#soft" target="_blank">View all {{ site.data.citations.repec.software.count }} modules on RePEc →</a>
</p>

<hr>

<h2>Data Platforms & Research Infrastructure</h2>

<p>Institutional projects I have led or co-developed for data access, education measurement, and analytics.</p>

<h3>Data Access Platforms</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th>Project</th>
      <th>Description</th>
      <th><i class="fab fa-github"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="https://github.com/unicef-drp/unicefData" target="_blank">unicefData</a></strong></td>
      <td>Trilingual R, Python, and Stata library for downloading UNICEF child welfare indicators via SDMX API. Provides consistent interfaces across all three languages with cross-language test parity.<br>
        <strong>Install:</strong>
        <a href="https://cran.r-project.org/package=unicefData" target="_blank">CRAN</a> ·
        <a href="https://pypi.org/project/unicefdata/" target="_blank">PyPI</a> ·
        <a href="https://ideas.repec.org/c/boc/bocode/s459598.html" target="_blank">SSC</a>
      </td>
      <td><a href="https://github.com/unicef-drp/unicefData" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/jpazvd/wbopendata" target="_blank">wbopendata</a></strong></td>
      <td>Stata module to access 29,000+ indicators from 51 World Bank databases (also available via <code>ssc install wbopendata</code>)</td>
      <td><a href="https://github.com/jpazvd/wbopendata" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/worldbank/datalibweb" target="_blank">datalibweb</a></strong></td>
      <td>Stata frontend for the World Bank microdata API, enabling access to global, regional, and country microdata catalogs</td>
      <td><a href="https://github.com/worldbank/datalibweb" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/jpazvd/wb-api-repo" target="_blank">wb-api-repo</a></strong></td>
      <td>World Bank API data extraction tools</td>
      <td><a href="https://github.com/jpazvd/wb-api-repo" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
  </tbody>
</table>

<h3>Education & Learning Analytics</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th>Project</th>
      <th>Description</th>
      <th><i class="fab fa-github"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="https://github.com/worldbank/LearningPoverty" target="_blank">LearningPoverty</a></strong></td>
      <td>Learning Poverty indicator — combining schooling and learning data to measure the share of children unable to read by age 10</td>
      <td><a href="https://github.com/worldbank/LearningPoverty" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/worldbank/GLAD" target="_blank">GLAD</a></strong></td>
      <td>Global Learning Assessment Database — harmonized learning assessment datasets at student and country level</td>
      <td><a href="https://github.com/worldbank/GLAD" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/worldbank/EduAnalyticsToolkit" target="_blank">EduAnalyticsToolkit</a></strong></td>
      <td>EduAnalytics team toolkit for data management, documentation, and analytics</td>
      <td><a href="https://github.com/worldbank/EduAnalyticsToolkit" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
  </tbody>
</table>

<h3>Utilities</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th>Project</th>
      <th>Description</th>
      <th><i class="fab fa-github"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="https://github.com/jpazvd/groupdata" target="_blank">groupdata</a></strong></td>
      <td>Poverty and inequality estimation using grouped data</td>
      <td><a href="https://github.com/jpazvd/groupdata" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/jpazvd/package" target="_blank">package</a></strong></td>
      <td>Stata module to create GitHub dissemination packages</td>
      <td><a href="https://github.com/jpazvd/package" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/jpazvd/useful_tweaks" target="_blank">useful_tweaks</a></strong></td>
      <td>Useful tweaks to user-written ado files</td>
      <td><a href="https://github.com/jpazvd/useful_tweaks" target="_blank"><i class="fab fa-github"></i></a></td>
    </tr>
  </tbody>
</table>

<p>
  <a href="https://github.com/jpazvd" target="_blank">View all repositories on GitHub →</a>
</p>

<hr>

<p class="jp-muted">
  <em>All tools are open source and available for academic and research use.</em>
</p>