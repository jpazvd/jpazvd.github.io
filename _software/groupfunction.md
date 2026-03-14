---
title: "GROUPFUNCTION"
excerpt: "Fast replacement for Stata's collapse command supporting multiple aggregation functions simultaneously."
layout: software-page
permalink: /software/groupfunction/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Data Management
  - Utilities
ssc_url: "https://ideas.repec.org/c/boc/bocode/s458475.html"
github_url: "https://github.com/jpazvd/groupfunction"
install_cmd: "ssc install groupfunction"
---

## Description

groupfunction replaces several collapse functions (mean, sum, variance, first, max, min). The command is several orders of magnitude faster than Stata's built-in `collapse` command, making it particularly useful for large datasets.

## Examples

```stata
* Basic usage: mean and min by group
sysuse auto, clear
groupfunction [aw=weight], mean(price) min(weight) by(foreign)
```

## Citation

Corral, P., Nguyen, M.C. and Azevedo, J.P. "GROUPFUNCTION: Stata module to replace several basic collapse functions." *Statistical Software Components* S458475, Boston College Department of Economics.
