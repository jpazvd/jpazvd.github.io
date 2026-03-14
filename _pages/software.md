---
layout: archive
title: "Data & Analytics Tools"
permalink: /softwares/
author_profile: true
description: "Stata modules and data analytics tools by João Pedro Azevedo including WBOPENDATA, poverty measurement, and survey analysis tools."
---

{% include base_path %}

<p>Open-source tools for data analysis, poverty measurement, and accessing international development data — available on SSC/RePEc, CRAN, and PyPI.</p>

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
  <a href="{{ base_path }}/research/">Focus</a>
</div>

<hr>

<!-- Featured Data Access Tools -->
<h2>Featured Data Access Tools</h2>

<table class="jp-table">
  <thead>
    <tr>
      <th class="jp-col-name">Tool</th>
      <th>Description</th>
      <th class="jp-col-dl"><i class="fas fa-download"></i></th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="{{ base_path }}/software/wbopendata/">wbopendata</a></strong></td>
      <td>Access 29,000+ indicators from 51 World Bank databases directly from Stata, covering 296 countries from 1960 to present</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s457234.html" target="_blank" title="ssc install wbopendata"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/wbopendata" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong>unicefData</strong></td>
      <td>Trilingual library for downloading UNICEF child welfare indicators via SDMX API with cross-language test parity</td>
      <td>
        <a href="{{ base_path }}/software/unicefdata-r/">R</a> ·
        <a href="{{ base_path }}/software/unicefdata-python/">Py</a> ·
        <a href="{{ base_path }}/software/unicefdata-stata/">Stata</a>
      </td>
      <td><a href="https://github.com/unicef-drp/unicefData" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/worldbank/datalibweb" target="_blank">datalibweb</a></strong></td>
      <td>Stata frontend for the World Bank microdata API, enabling access to global, regional, and country microdata catalogs</td>
      <td><a href="https://github.com/worldbank/datalibweb" target="_blank" title="Available on GitHub"><span class="jp-lang-icon jp-lang-icon--stata">S</span>GitHub</a></td>
      <td><a href="https://github.com/worldbank/datalibweb" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Stata Modules on SSC</h2>

<!-- Poverty, Inequality & Welfare -->
<h3>Poverty, Inequality & Welfare</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th class="jp-col-name">Module</th>
      <th>Description</th>
      <th class="jp-col-dl"><i class="fas fa-download"></i></th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
      <th class="jp-col-icon"><i class="fas fa-bug"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="{{ base_path }}/software/ainequal/">ainequal</a></strong></td>
      <td>Compute inequality and concentration indices with analytical standard errors</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s456748.html" target="_blank" title="ssc install ainequal"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/ainequal" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/ainequal/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/apoverty/">apoverty</a></strong></td>
      <td>FGT and other poverty measures with standard errors and hypothesis tests</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s456750.html" target="_blank" title="ssc install apoverty"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/apoverty" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/apoverty/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/mpovline/">mpovline</a></strong></td>
      <td>Poverty measures at multiple poverty lines simultaneously</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s457565.html" target="_blank" title="ssc install mpovline"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/mpovline" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/mpovline/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/isopoverty/">isopoverty</a></strong></td>
      <td>Graph iso-poverty curves showing growth-redistribution tradeoffs</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s456752.html" target="_blank" title="ssc install isopoverty"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/isopoverty" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/isopoverty/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/alorenz/">alorenz</a></strong></td>
      <td>Graph Lorenz and concentration curves with confidence intervals</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s456749.html" target="_blank" title="ssc install alorenz"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/alorenz" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/alorenz/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/hoi/">hoi</a></strong></td>
      <td>Human Opportunity Index for measuring inequality of opportunity (Barros et al.)</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s457191.html" target="_blank" title="ssc install hoi"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/hoi" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/hoi/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/mol/">mol</a></strong></td>
      <td>Measure of effective literacy using the Basu-Foster framework</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s456987.html" target="_blank" title="ssc install mol"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/mol" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/mol/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/jpazvd/groupdata" target="_blank">groupdata</a></strong></td>
      <td>Poverty and inequality estimation from grouped or tabulated data</td>
      <td><a href="https://github.com/jpazvd/groupdata" target="_blank" title="Available on GitHub"><span class="jp-lang-icon jp-lang-icon--stata">S</span>GitHub</a></td>
      <td><a href="https://github.com/jpazvd/groupdata" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/groupdata/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
  </tbody>
</table>

<!-- Decomposition Methods -->
<h3>Decomposition Methods</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th class="jp-col-name">Module</th>
      <th>Description</th>
      <th class="jp-col-dl"><i class="fas fa-download"></i></th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
      <th class="jp-col-icon"><i class="fas fa-bug"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="{{ base_path }}/software/adecomp/">adecomp</a></strong></td>
      <td>Shapley decomposition of changes in poverty and inequality indicators</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s457562.html" target="_blank" title="ssc install adecomp"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/adecomp" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/adecomp/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/drdecomp/">drdecomp</a></strong></td>
      <td>Datt-Ravallion decomposition of poverty changes into growth and redistribution</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s457563.html" target="_blank" title="ssc install drdecomp"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/drdecomp" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/drdecomp/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/skdecomp/">skdecomp</a></strong></td>
      <td>Shapley value decomposition of changes in the income distribution</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s457564.html" target="_blank" title="ssc install skdecomp"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/skdecomp" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/skdecomp/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/dfl/">dfl</a></strong></td>
      <td>DiNardo-Fortin-Lemieux counterfactual density decomposition</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s449001.html" target="_blank" title="ssc install dfl"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/dfl" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/dfl/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/changemean/">changemean</a></strong></td>
      <td>Decompose poverty changes into growth and distributional effects</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s456751.html" target="_blank" title="ssc install changemean"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/changemean" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/changemean/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
  </tbody>
</table>

<!-- Small Area Estimation -->
<h3>Small Area Estimation</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th class="jp-col-name">Module</th>
      <th>Description</th>
      <th class="jp-col-dl"><i class="fas fa-download"></i></th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
      <th class="jp-col-icon"><i class="fas fa-bug"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="{{ base_path }}/software/sae/">sae</a></strong></td>
      <td>Unit-level small area estimation for poverty mapping using the ELL methodology</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s458525.html" target="_blank" title="ssc install sae"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/sae" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/sae/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/fhsae/">fhsae</a></strong></td>
      <td>Fay-Herriot area-level EBLUP small area estimation methods</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s458495.html" target="_blank" title="ssc install fhsae"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/fhsae" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/fhsae/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
  </tbody>
</table>

<!-- Econometrics & Estimation -->
<h3>Econometrics & Estimation</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th class="jp-col-name">Module</th>
      <th>Description</th>
      <th class="jp-col-dl"><i class="fas fa-download"></i></th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
      <th class="jp-col-icon"><i class="fas fa-bug"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="{{ base_path }}/software/grqreg/">grqreg</a></strong></td>
      <td>Graph quantile regression coefficients across the distribution</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s437001.html" target="_blank" title="ssc install grqreg"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/grqreg" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/grqreg/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/factortest/">factortest</a></strong></td>
      <td>Bartlett and Kaiser-Meyer-Olkin tests for factor analysis suitability</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s436001.html" target="_blank" title="ssc install factortest"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/factortest" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/factortest/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/crtest/">crtest</a></strong></td>
      <td>Cramer-Ridder test for pooling states in multinomial logit models</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s433202.html" target="_blank" title="ssc install crtest"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/crtest" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/crtest/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/turnbull/">turnbull</a></strong></td>
      <td>Turnbull nonparametric estimator for willingness-to-pay from contingent valuation</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s457125.html" target="_blank" title="ssc install turnbull"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/turnbull" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/turnbull/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/spike/">spike</a></strong></td>
      <td>Spike model for zero willingness-to-pay in contingent valuation surveys</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s457126.html" target="_blank" title="ssc install spike"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/spike" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/spike/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
  </tbody>
</table>

<!-- Data Management & Utilities -->
<h3>Data Management & Utilities</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th class="jp-col-name">Module</th>
      <th>Description</th>
      <th class="jp-col-dl"><i class="fas fa-download"></i></th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
      <th class="jp-col-icon"><i class="fas fa-bug"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="{{ base_path }}/software/wbopendata/">wbopendata</a></strong></td>
      <td>Access 29,000+ World Bank indicators from 51 databases via Stata</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s457234.html" target="_blank" title="ssc install wbopendata"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/wbopendata" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/wbopendata/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/unicefdata-stata/">unicefdata</a></strong></td>
      <td>Download UNICEF child welfare indicators via SDMX API</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s459598.html" target="_blank" title="ssc install unicefdata"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/unicef-drp/unicefData" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/unicef-drp/unicefData/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/groupfunction/">groupfunction</a></strong></td>
      <td>Fast replacement for collapse supporting multiple aggregation functions</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s458475.html" target="_blank" title="ssc install groupfunction"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/groupfunction" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/groupfunction/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/outtable/">outtable</a></strong></td>
      <td>Export Stata matrix to LaTeX table with formatting options</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s419501.html" target="_blank" title="ssc install outtable"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/outtable" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/outtable/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="{{ base_path }}/software/yaml/">yaml</a></strong></td>
      <td>Read, write, and manipulate YAML configuration files for reproducible workflows</td>
      <td><a href="https://ideas.repec.org/c/boc/bocode/s459607.html" target="_blank" title="ssc install yaml"><span class="jp-lang-icon jp-lang-icon--stata">S</span>SSC</a></td>
      <td><a href="https://github.com/jpazvd/yaml" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
      <td><a href="https://github.com/jpazvd/yaml/issues/new" target="_blank" title="Report bug or request feature"><i class="fas fa-bug"></i></a></td>
    </tr>
  </tbody>
</table>

<p>
  <a href="https://ideas.repec.org/e/pwa88.html#soft" target="_blank">View all {{ site.data.citations.repec.software.count }} modules on RePEc →</a>
</p>

<hr>

<h2>R Packages on CRAN</h2>

<table class="jp-table">
  <thead>
    <tr>
      <th class="jp-col-name">Package</th>
      <th>Description</th>
      <th class="jp-col-dl"><i class="fas fa-download"></i></th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="{{ base_path }}/software/unicefdata-r/">unicefData</a></strong></td>
      <td>Download UNICEF child welfare indicators via SDMX API with consistent R interface</td>
      <td><a href="https://cran.r-project.org/package=unicefData" target="_blank" title="install.packages('unicefData')"><i class="fab fa-r-project jp-lang-icon"></i>CRAN</a></td>
      <td><a href="https://github.com/unicef-drp/unicefData" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Python Packages on PyPI</h2>

<table class="jp-table">
  <thead>
    <tr>
      <th class="jp-col-name">Package</th>
      <th>Description</th>
      <th class="jp-col-dl"><i class="fas fa-download"></i></th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="{{ base_path }}/software/unicefdata-python/">unicefdata</a></strong></td>
      <td>Download UNICEF child welfare indicators via SDMX API with consistent Python interface</td>
      <td><a href="https://pypi.org/project/unicefdata/" target="_blank" title="pip install unicefdata"><i class="fab fa-python jp-lang-icon"></i>PyPI</a></td>
      <td><a href="https://github.com/unicef-drp/unicefData" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
    </tr>
    <tr>
      <td><strong><a href="https://github.com/jpazvd/wb-api-repo" target="_blank">wb-api-repo</a></strong></td>
      <td>World Bank API data extraction scripts in Python</td>
      <td><a href="https://github.com/jpazvd/wb-api-repo" target="_blank" title="Available on GitHub"><i class="fab fa-python jp-lang-icon"></i>GitHub</a></td>
      <td><a href="https://github.com/jpazvd/wb-api-repo" target="_blank" title="GitHub repo"><i class="fab fa-github"></i></a></td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Other Projects: Reproducible & Scalable Analytics</h2>

<p>Institutional projects I have led or co-developed for reproducible data access, education measurement, and scalable analytics.</p>

<h3>Education & Learning Analytics</h3>

<table class="jp-table">
  <thead>
    <tr>
      <th class="jp-col-name">Project</th>
      <th>Description</th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
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
      <th class="jp-col-name">Project</th>
      <th>Description</th>
      <th class="jp-col-icon"><i class="fab fa-github"></i></th>
    </tr>
  </thead>
  <tbody>
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
