---
title: "WBOPENDATA"
excerpt: "Access over 29,000 indicators from 51 World Bank databases directly from Stata, covering 296 countries and regions from 1960 to present."
layout: software-page
permalink: /software/wbopendata/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - World Bank
  - Open Data
  - API
ssc_url: "https://ideas.repec.org/c/boc/bocode/s457234.html"
github_url: "https://github.com/jpazvd/wbopendata"
install_cmd: "ssc install wbopendata"
---

## Description

WBOPENDATA provides direct access to the World Bank's Open Data platform from within Stata. Query over 29,000 indicators across 51 databases, covering 296 countries and regions from 1960 to present.

**Key features:**
- Five download modes: indicator, country, topic, region, and source
- Multilingual metadata in English, Spanish, and French
- Output in wide or long format
- Built-in caching for faster repeated queries

## Examples

### Basic usage: GDP per capita

```stata
wbopendata, indicator(NY.GDP.PCAP.CD) long clear
line ny_gdp_pcap_cd year if countrycode == "BRA", ///
    title("GDP per capita — Brazil") ///
    ytitle("Current US$")
```

### Multiple countries comparison

```stata
wbopendata, indicator(SE.PRM.NENR) long clear
keep if inlist(countrycode, "BRA", "IND", "NGA", "IDN")
twoway (line se_prm_nenr year if countrycode == "BRA") ///
       (line se_prm_nenr year if countrycode == "IND") ///
       (line se_prm_nenr year if countrycode == "NGA") ///
       (line se_prm_nenr year if countrycode == "IDN"), ///
       legend(order(1 "Brazil" 2 "India" 3 "Nigeria" 4 "Indonesia")) ///
       title("Net primary enrollment rate")
```

<!-- Add example figures here:
<figure class="software-example">
  <img src="/images/software/wbopendata-example1.png" alt="GDP per capita plot">
  <figcaption>GDP per capita for Brazil, 1960–2023</figcaption>
</figure>
-->

## Documentation

- [World Bank Data Help Desk guide](https://datahelpdesk.worldbank.org/knowledgebase/articles/889464-wbopendata-stata-module-to-access-world-bank-databases)
- [Stata help file](https://ideas.repec.org/c/boc/bocode/s457234.html) (after install: `help wbopendata`)
