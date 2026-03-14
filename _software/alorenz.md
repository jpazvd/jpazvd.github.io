---
title: "ALORENZ"
excerpt: "Generate Pen's Parade, Lorenz, and Generalized Lorenz curves with stochastic dominance tests in Stata."
layout: software-page
permalink: /software/alorenz/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Inequality
  - Lorenz Curve
ssc_url: "https://ideas.repec.org/c/boc/bocode/s456749.html"
github_url: "https://github.com/jpazvd/alorenz"
install_cmd: "ssc install alorenz"
---

## Description

alorenz generates and visualizes three key distributional curves: Pen's Parade, Lorenz, and Generalized Lorenz curves. The module enables comparative analysis of income inequality across different social states with the following analytical capabilities:

- **Stochastic dominance tests:** First-order and second-order stochastic dominance analyses.
- **Lorenz dominance analysis:** Evaluates distributional differences per Atkinson's framework.
- **Pigou-Dalton ranking:** Compares multiple social states using established inequality principles.
- **Distribution testing:** Two-sample Kolmogorov-Smirnov tests for equality assessment.

**Dependencies:** Requires `groupfunction` and `which_version`.

## Examples

```stata
sysuse auto, clear

* Basic Lorenz curve
alorenz price, view

* Weighted with full view (Pen's Parade + Lorenz + Generalized Lorenz)
alorenz price [pw=weight], fullview

* All curves with 45-degree line, by group
alorenz price [pw=weight], points(20) view gl ge gp ///
    angle45 format(%12.0f) by(foreign)
```

## Citation

Azevedo, J.P. and Franco, S. (2006). "ALORENZ: Stata module to produce Pen's Parade, Lorenz and Generalised Lorenz curve." *Statistical Software Components* S456749, Boston College Department of Economics.
