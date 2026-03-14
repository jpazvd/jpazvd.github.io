---
title: "ADECOMP"
excerpt: "Estimate Shapley decomposition by components of a welfare measure."
layout: software-page
permalink: /software/adecomp/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Decomposition
  - Poverty
  - Inequality
ssc_url: "https://ideas.repec.org/c/boc/bocode/s457562.html"
github_url: "https://github.com/jpazvd/adecomp"
install_cmd: "ssc install adecomp"
---

## Description

adecomp implements the Shapley decomposition of changes in a welfare indicator as proposed by Azevedo, Sanfelice and Nguyen (2012). Following Barros et al. (2006), the method takes advantage of the additivity property of a welfare aggregate to construct counterfactual unconditional distributions by changing each component at a time, calculating their contribution to observed changes in poverty and inequality.

The approach calculates the decomposition across all possible paths and takes the average — the Shapley-Shorrocks estimates — resolving the path-dependence problem common in micro-decomposition methods.

The `equation()` option captures the relationship between the welfare variable and its components, where component variables are denoted by `c#` and separated by arithmetic operators.

## Examples

```stata
* Basic decomposition with poverty and inequality indicators
adecomp percapitainc laborinc nonlaborinc, by(year) ///
    equation(c1+c2) indicator(fgt0 fgt1 fgt2 gini theil) varpl(pline)

* Decomposition with growth incidence curve
adecomp percapitainc laborinc nonlaborinc, by(year) ///
    equation(c1+c2) indicator(fgt0) varpl(pline) gic(100)

* Multi-component income decomposition
adecomp percapitainc padults laborinc capitalinc pensioninc transferinc othersinc, ///
    by(year) equation(c1*(c2+c3+c4+c5+c6)) indicator(fgt0) varpl(pline)
```

## References

- Azevedo, J.P., Nguyen, M.C. and Sanfelice, V. (2012). "Shapley decomposition by components of a welfare aggregate." Washington, DC: World Bank.
- Azevedo, J.P., Inchauste, G. and Sanfelice, V. (2013). "Decomposing the recent inequality decline in Latin America." *Policy Research Working Paper* 6715, World Bank.
- Barros, R.P. de, Carvalho, M., Franco, S. and Mendoça, R. (2006). "Uma Análise das Principais Causas da Queda Recente na Desigualdade de Renda Brasileira." *Revista Econômica*, 8(1), 117–147.
- Inchauste, G., Azevedo, J.P. et al. (2014). *Understanding Changes in Poverty*. World Bank.
- Shapley, L. (1953). "A value for n-person games." In Kuhn and Tucker (eds.), *Contributions to the Theory of Games*, Vol. 2, Princeton University Press.

## Citation

Azevedo, J.P., Nguyen, M.C. and Sanfelice, V. (2012). "ADECOMP: Stata module to estimate Shapley Decomposition by Components of a Welfare Measure." *Statistical Software Components* S457562, Boston College Department of Economics.
