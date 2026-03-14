---
title: "unicefData (R)"
excerpt: "R package for downloading UNICEF child welfare indicators via SDMX API."
layout: software-page
permalink: /software/unicefdata-r/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Rstats
  - UNICEF
  - SDMX
  - API
cran_url: "https://cran.r-project.org/package=unicefData"
github_url: "https://github.com/unicef-drp/unicefData"
install_r: "install.packages('unicefData')"
---

## Description

unicefData is an R package that provides a consistent interface for downloading UNICEF child welfare indicators via the SDMX API. It is part of a trilingual family of packages (R, Python, and Stata) that maintain cross-language test parity, ensuring identical results across all three implementations.

**Key features:**

- Access UNICEF global indicator databases
- Multilingual metadata support
- Cross-language test parity with Python and Stata implementations

## Example

```r
library(unicefData)
df <- unicefData::get_indicator("PT_CHLD_UNDER5")
head(df)
```

## Documentation

- [CRAN documentation](https://cran.r-project.org/package=unicefData)
