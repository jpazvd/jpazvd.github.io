---
title: "FACTORTEST"
excerpt: "Perform Bartlett's sphericity test and Kaiser-Meyer-Olkin measure to assess factor analysis suitability in Stata."
layout: software-page
permalink: /software/factortest/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Factor Analysis
  - Statistics
ssc_url: "https://ideas.repec.org/c/boc/bocode/s436001.html"
github_url: "https://github.com/jpazvd/factortest"
install_cmd: "ssc install factortest"
---

## Description

factortest evaluates whether factor analysis is suitable for a given dataset by performing two key tests:

1. **Bartlett's Test for Sphericity:** Examines the correlation matrix's determinant by converting it to a chi-square statistic. The null hypothesis is that variables are non-collinear.

2. **Kaiser-Meyer-Olkin (KMO) Measure:** Compares observed correlation coefficients against partial correlation coefficients with the following interpretation scale:
   - 0.90+: Excellent
   - 0.80–0.89: Meritorious
   - 0.70–0.79: Middling
   - 0.60–0.69: Mediocre
   - 0.50–0.59: Miserable
   - Below 0.50: Unacceptable

## Example

```stata
* Bartlett's sphericity and KMO tests
factortest price mpg rep78 rep77 headroom rseat trunk
```

## Citation

Azevedo, J.P. (2003). "FACTORTEST: Stata module to perform tests for factor analysis suitability." *Statistical Software Components* S436001, Boston College Department of Economics.
