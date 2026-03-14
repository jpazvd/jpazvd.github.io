---
title: "ISOPOVERTY"
excerpt: "Generate iso-poverty, inequality-poverty, and growth-poverty curves for analyzing pro-poor growth dynamics in Stata."
layout: software-page
permalink: /software/isopoverty/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Poverty
  - Visualization
ssc_url: "https://ideas.repec.org/c/boc/bocode/s456752.html"
github_url: "https://github.com/jpazvd/isopoverty"
install_cmd: "ssc install isopoverty"
---

## Description

isopoverty generates data for plotting three types of analytical curves used in poverty and inequality analysis:

- **Inequality-Poverty curves:** How changes in inequality affect poverty measures.
- **Growth-Poverty curves:** How growth affects poverty measures.
- **Iso-Poverty curves:** Combinations of growth and inequality reduction that yield the same poverty level.

The tool builds on methodologies from Kakwani, Pernia, Bourguignon, and others studying pro-poor growth dynamics. Results are stored as matrices (`r(ineqreduc)`, `r(growth)`, `r(frontier)`) that can be exported using `svmat` for customized visualization.

**Note:** The iso-poverty computation is computationally intensive. It is recommended to first estimate the inequality-poverty and growth-poverty curves to identify optimal parameters.

## Examples

```stata
* Inequality-poverty curve
isopoverty rdpc [fw=peso], stepinq(50) varpl(lp)

* Iso-poverty frontier with growth and inequality dimensions
isopoverty rdpc [fw=peso], stepinq(50) stepgrw(10) ///
    mininq(0) maxinq(.50) mingrw(0) maxgrw(1.50) ///
    target(25) int(2) frontier varpl(lp)
```

## Citation

Azevedo, J.P. and Franco, S. (2006). "ISOPOVERTY: Stata module to generate data for Inequality-Poverty and Iso-Poverty curves." *Statistical Software Components* S456752, Boston College Department of Economics.
