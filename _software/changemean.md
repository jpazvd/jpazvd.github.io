---
title: "CHANGEMEAN"
excerpt: "Compute the contribution of changes in mean income and distribution on 25 poverty measures in Stata."
layout: software-page
permalink: /software/changemean/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Poverty
  - Decomposition
ssc_url: "https://ideas.repec.org/c/boc/bocode/s456751.html"
github_url: "https://github.com/jpazvd/changemean"
install_cmd: "ssc install changemean"
---

## Description

changemean analyzes how changes in mean income and distribution affect poverty indicators. The module supports 25 different welfare measures:

- Standard poverty metrics: headcount ratio, poverty gap ratio, income gap ratio
- Advanced indices: Watts, Sen, Takayama, Thon
- Foster-Greer-Thorbecke (FGT) indices with multiple parameters
- Clark-Ulph-Hemming indices with varying beta coefficients

## Examples

```stata
* Basic usage with weights
changemean rdpc [fw=peso]

* By education group with poverty line variable
changemean rdpc [fw=peso], by(educa) varpl(lp)

* By education group with explicit poverty line and base group
changemean rdpc [fw=peso], by(educa) base(1) line(240)
```

## Citation

Azevedo, J.P. and Franco, S. (2006). "CHANGEMEAN: Stata module to compute Income and Inequality Contribution on Poverty Variation." *Statistical Software Components* S456751, Boston College Department of Economics.
