---
title: "unicefdata (Stata)"
excerpt: "Stata module for downloading UNICEF child welfare indicators via SDMX API."
layout: software-page
permalink: /software/unicefdata-stata/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - UNICEF
  - SDMX
  - API
ssc_url: "https://ideas.repec.org/c/boc/bocode/s459598.html"
github_url: "https://github.com/unicef-drp/unicefData"
install_cmd: "ssc install unicefdata"
---

## Description

unicefdata is a Stata module that provides a consistent interface for downloading UNICEF child welfare indicators via the SDMX API. It is part of a trilingual family of packages (R, Python, and Stata) that maintain cross-language test parity, ensuring identical results across all three implementations.

**Key features:**

- Access UNICEF global indicator databases
- Multilingual metadata support
- Cross-language test parity with R and Python implementations

## Example

```stata
unicefdata, indicator(PT_CHLD_UNDER5) clear
list in 1/10
```

## Documentation

- Stata: `help unicefdata` (after install)
