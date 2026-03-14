---
title: "YAML"
excerpt: "Stata module for reading, writing, and manipulating YAML configuration files."
layout: software-page
permalink: /software/yaml/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Data Management
  - Utilities
ssc_url: "https://ideas.repec.org/c/boc/bocode/s459607.html"
github_url: "https://github.com/jpazvd/yaml"
install_cmd: "ssc install yaml"
---

## Description

yaml is a Stata command for reading, writing, and manipulating YAML configuration files. It provides a unified interface with nine subcommands that enable Stata users to integrate YAML-based workflows into their data pipelines.

The command implements the **JSON Schema** subset of YAML 1.2 (3rd Edition, 2021), the current authoritative YAML standard. It is implemented in pure Stata with no external dependencies.

**Key features:**

- Read YAML files into Stata's data structure or frames
- Write YAML files from Stata datasets or scalars
- Query values using hierarchical key paths
- Validate configurations with required keys and type checking
- Multiple frame support (Stata 16+) for managing multiple configurations
- Fast-scan mode and Mata bulk parser for large metadata catalogs
- Indicators preset for wbopendata/unicefdata metadata

## Examples

```stata
* Read a YAML configuration file
yaml read using config.yaml, replace

* View the structure
yaml describe

* Get a specific value
yaml get database:host
return list

* Validate required keys
yaml validate, required(name version database)

* Write modified configuration
yaml write using output.yaml, replace

* Parse wbopendata/unicefdata indicator metadata
yaml read using indicators.yaml, indicators replace
list key code name in 1/5
```

## Citation

Azevedo, João Pedro. 2025. "yaml: Stata module for YAML file processing." *Statistical Software Components* S459607, Boston College Department of Economics.

## Documentation

- Stata: `help yaml` (after install)
- [SSC page](https://ideas.repec.org/c/boc/bocode/s459607.html)
