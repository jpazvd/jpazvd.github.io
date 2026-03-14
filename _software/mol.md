---
title: "MOL"
excerpt: "Compute the Basu-Foster effective literacy measure accounting for intrahousehold externalities in Stata."
layout: software-page
permalink: /software/mol/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Literacy
  - Education
ssc_url: "https://ideas.repec.org/c/boc/bocode/s456987.html"
github_url: "https://github.com/jpazvd/mol"
install_cmd: "ssc install mol"
---

## Description

mol computes effective literacy measures that go beyond the standard literacy rate by accounting for household-level literacy externalities. The module calculates:

- **Crude Literacy Rate (R):** Traditional percentage of literate adults.
- **Effective Literacy (Re):** Accounts for intrahousehold benefits from having literate members.
- **Isolated Illiteracy Rate (I):** Measures illiteracy without household support.
- **Efficiency Loss (Q):** Ranges from 0 to 1, showing literacy gaps.
- **Externality-adjusted Literacy Rate (R\*):** Extended Subramanian measure.

The approach builds on Sen's work on social indicators, implementing frameworks from Basu and Foster (1998) and extensions by Subramanian (2004).

## Examples

```stata
* Basic effective literacy measure
mol alfab [fw=weight], house(domicilio)

* With multiple alpha sensitivity parameters
mol alfab [fw=weight], house(domicilio) alpha(.2 .5 .8)

* By region with generated variables
mol alfab [fw=weight], house(domicilio) by(region) gen

* By state with ranking
mol alfab [fw=weight], house(domicilio) by(state) rank
```

## References

- Basu, K. and Foster, J.E. (1998). "On measuring literacy." *Economic Journal*, 108(451), 1733–1749.
- Subramanian, S. (2004). "Measuring literacy: some extensions of the Basu-Foster framework." *Journal of Development Economics*, 73(1), 453–463.

## Citation

Azevedo, J.P. (2009). "MOL: Stata module to evaluate literacy." *Statistical Software Components* S456987, Boston College Department of Economics.
