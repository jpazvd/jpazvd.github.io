---
title: "SPIKE"
excerpt: "Model non-zero probability of zero willingness-to-pay in contingent valuation experiments in Stata."
layout: software-page
permalink: /software/spike/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Willingness to Pay
  - Contingent Valuation
ssc_url: "https://ideas.repec.org/c/boc/bocode/s457126.html"
github_url: "https://github.com/jpazvd/spike"
install_cmd: "ssc install spike"
---

## Description

spike allows for a non-zero probability of zero willingness-to-pay in referendum-style contingent valuation experiments. When large segments of a population decline to consume the offered good, traditional parametric approaches based on probit and logit models tend to predict unrealistic negative WTP values. The spike model methodology, based on Kriström (1997), provides a solution by explicitly modeling the mass point at zero.

## Example

```stata
* Spike model for zero willingness-to-pay
spike s t bid
```

## References

- Kriström, B. (1997). "Spike Models in Contingent Valuation." *American Journal of Agricultural Economics*, 79(3), 1013–1023.

## Citation

Azevedo, J.P. (2010). "SPIKE: Stata module for the estimation of zero willingness-to-pay." *Statistical Software Components* S457126, Boston College Department of Economics.
