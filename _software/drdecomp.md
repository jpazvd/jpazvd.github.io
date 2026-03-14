---
title: "DRDECOMP"
excerpt: "Decompose changes in poverty indicators into growth and distribution components using Datt-Ravallion methodology with Shapley values."
layout: software-page
permalink: /software/drdecomp/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Decomposition
  - Poverty
ssc_url: "https://ideas.repec.org/c/boc/bocode/s457563.html"
github_url: "https://github.com/jpazvd/drdecomp"
install_cmd: "ssc install drdecomp"
---

## Description

drdecomp decomposes changes in poverty indicators into growth and distribution components using the Datt-Ravallion (1992) methodology combined with non-parametric Shapley value approaches from Shorrocks (1999/2012) and Kolenikov and Shorrocks (2003). This resolves the path-dependence problem inherent in the original Datt-Ravallion decomposition by averaging over all possible orderings.

## Examples

```stata
* Basic Datt-Ravallion decomposition
drdecomp percapitainc, by(year) varpl(pline)

* With multiple FGT indicators
drdecomp percapitainc, by(year) varpl(pline) in(fgt0 fgt1 fgt2)

* With multiple poverty lines
drdecomp percapitainc, by(year) varpl(pline) mpl(1 3.5 6)
```

## References

- Datt, G. and Ravallion, M. (1992). "Growth and redistribution components of changes in poverty measures." *Journal of Development Economics*, 38, 275–295.
- Shorrocks, A.F. (2012). "Decomposition procedures for distributional analysis: a unified framework based on the Shapley value." *Journal of Economic Inequality*.

## Citation

Azevedo, J.P., Sanfelice, V. and Castaneda, A. (2012). "DRDECOMP: Stata module to estimate the Datt-Ravallion decomposition of changes in poverty." *Statistical Software Components* S457563, Boston College Department of Economics.
