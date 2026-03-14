---
title: "APOVERTY"
excerpt: "Compute a variety of poverty measures from individual-level or grouped data in Stata."
layout: software-page
permalink: /software/apoverty/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Poverty
  - Measurement
ssc_url: "https://ideas.repec.org/c/boc/bocode/s456750.html"
github_url: "https://github.com/jpazvd/apoverty"
install_cmd: "ssc install apoverty"
---

## Description

apoverty computes a series of poverty measures based on the welfare distribution described by varname. It is a revised and upgraded version of poverty published by Philippe Van Kerm.

**Poverty measures computed:**

- Headcount ratio and extreme poverty headcount
- Aggregate poverty gap and poverty gap ratio
- Income gap ratio
- Watts index
- Sen index, Takayama index, Thon index
- Foster-Greer-Thorbecke (FGT) indices with parameters 0.5, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
- Clark et al. indices with parameters 0.1, 0.25, 0.5, 0.75, 0.9

The poverty line is either directly specified by the user or computed relative to the median of varname (half or two-thirds).

## Example

```stata
* Poverty measures with a specified poverty line
sysuse nlsw88, clear
apoverty wage, line(5)
```

## References

- Foster, J., Greer, J. and Thorbecke, E. (1984) "A class of decomposable poverty measures." *Econometrica*, 52(3), 761–766.

## Citation

Azevedo, J.P. (2006). "APOVERTY: Stata module to compute poverty measures." *Statistical Software Components* S456750, Boston College Department of Economics.
