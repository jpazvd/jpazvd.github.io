---
title: "OUTTABLE"
excerpt: "Export Stata matrix to a LaTeX table, with automatic row and column labeling."
layout: software-page
permalink: /software/outtable/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - LaTeX
  - Output
ssc_url: "https://ideas.repec.org/c/boc/bocode/s419501.html"
github_url: "https://github.com/jpazvd/outtable"
install_cmd: "ssc install outtable"
---

## Description

outtable automates the conversion of a Stata matrix to a LaTeX table, written to an external file. The table is presented with row and column names taken from the specified matrix, so one need only generate the appropriate matrix using standard Stata commands. By default, only the lower triangle of a symmetric matrix will be written, as inferred by Stata's `issym()` function.

## Examples

```stata
* Export regression results to LaTeX
use auto, clear
forval r=2/5 {
    qui reg price headroom-turn if rep78==`r'
    mat c`r'=e(b)'
}
mat c=c2,c3,c4,c5
mat colnames c=rep78_2 rep78_3 rep78_4 rep78_5
outtable using cars, mat(c) replace

* With formatting and caption
outtable using cars, mat(c) replace center f(%9.2f) ///
    cap("Regression coefficients by rep78")
```

## Citation

Baum, C.F. and Azevedo, J.P. (2001). "OUTTABLE: Stata module to write matrix to LaTeX table." *Statistical Software Components* S419501, Boston College Department of Economics.
