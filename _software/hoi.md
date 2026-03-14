---
title: "HOI"
excerpt: "Compute the Human Opportunity Index for measuring inequality of opportunity in Stata."
layout: software-page
permalink: /software/hoi/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Inequality
  - Opportunity
ssc_url: "https://ideas.repec.org/c/boc/bocode/s457191.html"
github_url: "https://github.com/jpazvd/hoi"
install_cmd: "ssc install hoi"
---

## Description

hoi calculates the Human Opportunity Index (HOI) and related equity metrics proposed by Barros et al. (2008). The command computes three primary measures:

- **Coverage of Basic Opportunities (C):** The percentage of the population with access to specific opportunities.
- **Dissimilarity Index (D):** A measure of inequality in opportunity distribution.
- **Human Opportunity Index (HOI):** A composite metric combining coverage and equality.

The module provides analytical standard errors and confidence intervals for all three measures, and supports counterfactual decomposition analysis when comparing different time periods or geographic locations using the `by()` option.

## Examples

```stata
* Basic HOI with circumstance variables
hoi agua id13 id14 id15 id16 sexo educac educac2 lrdpc casal scr area [fw=peso], ///
    adjust1(id13=1 id14=0 id15=0 id16=0) format(%9.3f)

* HOI by subregion with counterfactual decomposition
hoi agua id13 id14 id15 id16 sexo educac educac2 lrdpc casal scr area [fw=peso], ///
    format(%9.3f) adjust1(id13=1 id14=0 id15=0 id16=0) by(subregion)
```

## References

- Barros, R.P. de, Ferreira, F.H.G., Vega, J.R.M. and Chanduvi, J.S. (2008). *Measuring Inequality of Opportunities in Latin America and the Caribbean*. World Bank.

## Citation

Azevedo, J.P., Franco, S., Rubiano, E. and Hoyos, A. (2010). "HOI: Stata module to compute Human Opportunity Index." *Statistical Software Components* S457191, Boston College Department of Economics.
