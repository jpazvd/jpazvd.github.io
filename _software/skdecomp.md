---
title: "SKDECOMP"
excerpt: "Estimate Shapley value of growth, price, and distribution components on changes in poverty indicators."
layout: software-page
permalink: /software/skdecomp/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Decomposition
  - Poverty
ssc_url: "https://ideas.repec.org/c/boc/bocode/s457564.html"
github_url: "https://github.com/jpazvd/skdecomp"
install_cmd: "ssc install skdecomp"
---

## Description

skdecomp implements the Shapley value of the Kolenikov and Shorrocks (2003) decomposition of changes in a welfare indicator into growth, distribution, and price components. By applying Shapley values, the method resolves the path-dependence problem inherent in sequential decompositions.

## Examples

```stata
* Basic Shapley-Kolenikov-Shorrocks decomposition
skdecomp income, by(year) varpl(pline)

* With regional poverty lines
skdecomp income, by(year) varpl(pline) idpl(region)

* With multiple FGT indicators
skdecomp income, by(year) varpl(pline) in(fgt0 fgt1 fgt2)

* With multiple poverty lines
skdecomp income, by(year) varpl(pline) mpl(1 2.5 6)
```

## References

- Kolenikov, S. and Shorrocks, A. (2003). "A Decomposition Analysis of Regional Poverty in Russia." *Discussion Paper* No. 2003/74, United Nations University.
- Shorrocks, A.F. (2012). "Decomposition procedures for distributional analysis: a unified framework based on the Shapley value." *Journal of Economic Inequality*.

## Citation

Atuesta, B., Azevedo, J.P., Castaneda, A. and Sanfelice, V. (2012). "SKDECOMP: Stata module to estimate Shapley value of growth, price, and distribution components on changes in poverty indicators." *Statistical Software Components* S457564, Boston College Department of Economics.
