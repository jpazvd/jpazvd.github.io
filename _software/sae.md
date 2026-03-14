---
title: "SAE"
excerpt: "Unit-level small area estimation for poverty mapping using the ELL methodology in Stata."
layout: software-page
permalink: /software/sae/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Small Area Estimation
  - Poverty Mapping
ssc_url: "https://ideas.repec.org/c/boc/bocode/s458525.html"
github_url: "https://github.com/jpazvd/sae"
install_cmd: "ssc install sae"
---

## Description

sae is a Stata family of functions for small area estimation, using the methodology from Elbers, Lanjouw, and Lanjouw (2003). The package introduces new mata functions and a plugin used to circumvent memory limitations that inevitably arise when working with larger datasets.

The ELL methodology combines census and survey data to produce poverty estimates at fine geographic levels (e.g., district or municipality), enabling the creation of poverty maps for policy targeting and resource allocation.

## Examples

```stata
* Modeling stage
sae model ell Y x1 x2 x3 x4 x5 x6, area(area)

* Simulation stage
sae sim ell Y x1 x2 x3 x4 x5 x6, area(area) ///
    eta(normal) epsilon(normal) matin("censo") lny ///
    seed(31916) rep(500) pwcensus(hhsize) ///
    indicators(FGT0 FGT1 FGT2) aggids(0) ///
    uniq(hhid_n) plines(16.2) allmata
```

## References

- Elbers, C., Lanjouw, J.O. and Lanjouw, P. (2003). "Micro-level estimation of poverty and inequality." *Econometrica*, 71(1), 355–364.
- Nguyen, M.C., Corral, P., Azevedo, J.P. and Zhao, Q. (2018). "sae: A Stata Package for Unit Level Small Area Estimation." *Policy Research Working Paper* 8630, World Bank.
- Molina, I. and Rao, J. (2010). "Small area estimation of poverty indicators." *Canadian Journal of Statistics*, 38(3), 369–385.
- Rao, J.N. and Molina, I. (2015). *Small Area Estimation*. John Wiley & Sons.

## Citation

Nguyen, M.C., Corral, P., Azevedo, J.P. and Zhao, Q. (2018). "SAE: Stata module to provide commands and mata functions devoted to unit level small area estimation." *Statistical Software Components* S458525, Boston College Department of Economics.
