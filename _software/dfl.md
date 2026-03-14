---
title: "DFL"
excerpt: "Estimate DiNardo-Fortin-Lemieux counterfactual kernel density decomposition in Stata."
layout: software-page
permalink: /software/dfl/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Decomposition
  - Distribution
ssc_url: "https://ideas.repec.org/c/boc/bocode/s449001.html"
github_url: "https://github.com/jpazvd/dfl"
install_cmd: "ssc install dfl"
---

## Description

dfl implements the DiNardo, Fortin and Lemieux (1996) methodology for calculating counterfactual kernel densities. The module enables researchers to compare wage or welfare distributions between groups and estimate what distribution would occur under alternative scenarios.

The module provides three primary comparison graphs:

- **cfactual:** Shows how one group's distribution would change if compensated at another group's rates.
- **ufactual:** Compares an alternative distribution against actual outcomes.
- **diff:** Illustrates the gap between counterfactual and actual distributions.

Optionally integrates with Philippe van Kerm's `akdensity` routine for enhanced density estimation.

## Examples

```stata
webuse nlsw88, clear
gen ttl_exp2 = ttl_exp^2
gen lwage = log(wage)

* Basic counterfactual decomposition
dfl union ttl_exp ttl_exp2 married grade, outcome(lwage)

* With bandwidth control
dfl union ttl_exp ttl_exp2 married grade, outcome(lwage) w(.05)

* Adaptive kernel density
dfl union ttl_exp ttl_exp2 married grade, outcome(lwage) adaptive

* Step-wise decomposition
dfl union ttl_exp ttl_exp2 married grade, outcome(lwage) step(tenure collgrad)
```

## References

- DiNardo, J., Fortin, N.M. and Lemieux, T. (1996). "Labor market institutions and the distribution of wages, 1973-1992: a semiparametric approach." *Econometrica*, 64(5), 1001–1044.

## Citation

Azevedo, J.P. (2005). "DFL: Stata module to estimate DiNardo, Fortin and Lemieux Counterfactual Kernel Density." *Statistical Software Components* S449001, Boston College Department of Economics.
