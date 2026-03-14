---
title: "unicefdata (Python)"
excerpt: "Python package for downloading UNICEF child welfare indicators via SDMX API."
layout: software-page
permalink: /software/unicefdata-python/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Pstats
  - UNICEF
  - SDMX
  - API
pypi_url: "https://pypi.org/project/unicefdata/"
github_url: "https://github.com/unicef-drp/unicefData"
install_python: "pip install unicefdata"
---

## Description

unicefdata is a Python package that provides a consistent interface for downloading UNICEF child welfare indicators via the SDMX API. It is part of a trilingual family of packages (R, Python, and Stata) that maintain cross-language test parity, ensuring identical results across all three implementations.

**Key features:**

- Access UNICEF global indicator databases
- Multilingual metadata support
- Cross-language test parity with R and Stata implementations

## Example

```python
import unicefdata
df = unicefdata.get_indicator("PT_CHLD_UNDER5")
df.head()
```

## Documentation

- [PyPI documentation](https://pypi.org/project/unicefdata/)
