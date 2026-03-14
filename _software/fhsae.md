---
title: "FHSAE"
excerpt: "Fay-Herriot area-level small area estimation methods (EBLUP) in Stata."
layout: software-page
permalink: /software/fhsae/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Small Area Estimation
  - Fay-Herriot
ssc_url: "https://ideas.repec.org/c/boc/bocode/s458495.html"
github_url: "https://github.com/jpazvd/fhsae"
install_cmd: "ssc install fhsae"
---

## Description

fhsae implements Fay-Herriot's EBLUP (Empirical Best Linear Unbiased Prediction) small area estimation methods. This Stata implementation translates the functionality from R's SAE package developed by Molina and Marhuenda, providing area-level small area estimates when unit-level microdata is not available.

The Fay-Herriot model combines direct survey estimates with auxiliary administrative or census data to improve the precision of small area estimates, particularly useful when sample sizes within areas are too small for reliable direct estimation.

## Example

```stata
* Fay-Herriot area-level small area estimation
fhsae yield hh_f hh_size, revar(vd) method(FH) ///
    fhpredict(fh) fhse(fhse) outsample
```

## References

- Fay, R.E. and Herriot, R.A. (1979). "Estimates of income for small places: an application of James-Stein procedures to census data." *Journal of the American Statistical Association*, 74, 269–277.
- Molina, I. and Marhuenda, Y. (2015). "sae: An R Package for Small Area Estimation." *The R Journal*, 7(1), 81–98.

## Citation

Corral, P., Seitz, W., Azevedo, J.P. and Nguyen, M.C. (2018). "FHSAE: Stata module to fit Fay-Herriot EBLUP small area estimation." *Statistical Software Components* S458495, Boston College Department of Economics.
