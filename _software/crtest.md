---
title: "CRTEST"
excerpt: "Perform the Cramer-Ridder test for pooling states in a multinomial logit model in Stata."
layout: software-page
permalink: /software/crtest/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Testing
  - Multinomial Logit
ssc_url: "https://ideas.repec.org/c/boc/bocode/s433202.html"
github_url: "https://github.com/jpazvd/crtest"
install_cmd: "ssc install crtest"
---

## Description

crtest performs the Cramer-Ridder test for pooling states in a multinomial logit model. Given a multinomial logit model with (S+1) states and two candidate states for pooling (s1 and s2), the null hypothesis is that s1 and s2 have the same regression coefficients apart from the intercept.

## Example

```stata
* Cramer-Ridder pooling test after multinomial logit
mlogit occup1 female under35 married2
crtest
```

## References

- Cramer, J.S. and Ridder, G. (1991). "Pooling states in multinomial logit model." *Journal of Econometrics*, 47, 267–272.

## Citation

Azevedo, J.P. (2003). "CRTEST: Stata module to perform Cramer-Ridder Test for pooling states in a Multinomial logit." *Statistical Software Components* S433202, Boston College Department of Economics.
