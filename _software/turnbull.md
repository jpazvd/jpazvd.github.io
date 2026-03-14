---
title: "TURNBULL"
excerpt: "Non-parametric Turnbull estimation of willingness-to-pay from contingent valuation data in Stata."
layout: software-page
permalink: /software/turnbull/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Willingness to Pay
  - Contingent Valuation
ssc_url: "https://ideas.repec.org/c/boc/bocode/s457125.html"
github_url: "https://github.com/jpazvd/turnbull"
install_cmd: "ssc install turnbull"
---

## Description

turnbull estimates the Turnbull empirical distribution estimator of willingness to pay proposed by Carson et al. (1994). Haab and McConnell (1997) argue that this estimator solves the problem of estimating negative willingness to pay without resorting to ad hoc distribution assumptions, and show that central tendency measures of WTP from parametric models are sensitive to the assumed distribution, while the lower bound Turnbull estimate is robust across distributions.

## Examples

```stata
* Turnbull WTP estimation
turnbull bid t

* Short output format
turnbull bid t, short
```

## References

- Carson, R.T. et al. (1994). "Prospective Interim Lost Use Value Due to DDT and PCB Contamination in the Southern California Bight." NOAA Contract.
- Haab, T. and McConnell, K. (1997). "Referendum Models and Negative Willingness to Pay." *Journal of Environmental Economics and Management*, 32(2), 251–270.

## Citation

Azevedo, J.P. (2010). "TURNBULL: Stata module to estimate the Turnbull empirical distribution estimator of willingness to pay." *Statistical Software Components* S457125, Boston College Department of Economics.
