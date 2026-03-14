---
title: "GRQREG"
excerpt: "Graph the coefficients of a quantile regression with confidence intervals in Stata."
layout: software-page
permalink: /software/grqreg/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Quantile Regression
  - Visualization
ssc_url: "https://ideas.repec.org/c/boc/bocode/s437001.html"
github_url: "https://github.com/jpazvd/grqreg"
install_cmd: "ssc install grqreg"
---

## Description

grqreg graphs the coefficients of a quantile regression (Koenker and Bassett, 1978). It also has the option to graph the confidence interval, the OLS coefficient and the OLS confidence interval on the same graph.

grqreg rewards the use of variable labels — labels are used in the graphs, providing more intelligible variable descriptions than 8-letter names. Works after `qreg`, `bsqreg` and `sqreg`.

**Note:** For extreme quantiles, it is not recommended to push tau too far into the tails, especially with many parameters. A rough rule of thumb: min{n*tau, n*(1-tau)} should be at least 10*p where p is the number of parameters.

## Examples

```stata
* After simultaneous quantile regression
webuse auto, clear
sqreg price weight length foreign, quantile(.25 .5 .75) reps(100)
grqreg, ci ols olsci title(Fig.1a Fig.1b Fig.1c)

* After basic quantile regression with all coefficients
qreg price mpg headroom
grqreg, cons ci ols olsci title(Fig.1a Fig.1b Fig.1c)

* Compare specific coefficients
qreg price mpg trunk weight length
grqreg weight length, compare
```

## References

- Koenker, R. and Bassett, G. (1978). "Regression Quantiles." *Econometrica*, 46(1), 33–50.
- Koenker, R. and Hallock, K.F. (2001). "Quantile Regression." *Journal of Economic Perspectives*, 15(4), 143–156.

## Citation

Azevedo, J.P. (2004). "GRQREG: Stata module to graph the coefficients of a quantile regression." *Statistical Software Components* S437001, Boston College Department of Economics.
