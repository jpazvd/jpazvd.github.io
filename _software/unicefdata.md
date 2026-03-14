---
title: "unicefData"
excerpt: "Trilingual R, Python, and Stata library for downloading UNICEF child welfare indicators via SDMX API."
layout: software-page
permalink: /software/unicefdata/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - R
  - Python
  - Stata
  - UNICEF
  - SDMX
  - API
ssc_url: "https://ideas.repec.org/c/boc/bocode/s459598.html"
cran_url: "https://cran.r-project.org/package=unicefData"
pypi_url: "https://pypi.org/project/unicefdata/"
github_url: "https://github.com/unicef-drp/unicefData"
install_cmd: "ssc install unicefdata"
install_r: "install.packages('unicefData')"
install_python: "pip install unicefdata"
---

## Description

unicefData provides a consistent interface for downloading UNICEF child welfare indicators across three languages (R, Python, and Stata) via the SDMX API. All three implementations maintain cross-language test parity.

**Key features:**

- Access UNICEF global indicator databases
- Consistent API across R, Python, and Stata
- Multilingual metadata support
- Cross-language test parity ensures identical results

## Examples

### R

```r
library(unicefData)
df <- unicefData::get_indicator("PT_CHLD_UNDER5")
head(df)
```

### Python

```python
import unicefdata
df = unicefdata.get_indicator("PT_CHLD_UNDER5")
df.head()
```

### Stata

```stata
unicefdata, indicator(PT_CHLD_UNDER5) clear
list in 1/10
```

## Documentation

- [CRAN documentation](https://cran.r-project.org/package=unicefData)
- [PyPI documentation](https://pypi.org/project/unicefdata/)
- Stata: `help unicefdata` (after install)
