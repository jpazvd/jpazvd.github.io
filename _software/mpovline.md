---
title: "MPOVLINE"
excerpt: "Calculate FGT0, FGT1 and FGT2 by intervals of multiple poverty thresholds in Stata."
layout: software-page
permalink: /software/mpovline/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Poverty
  - Measurement
ssc_url: "https://ideas.repec.org/c/boc/bocode/s457565.html"
github_url: "https://github.com/jpazvd/mpovline"
install_cmd: "ssc install mpovline"
---

## Description

mpovline calculates FGT0, FGT1 and FGT2 by intervals of multiple lines. This module can be used to calculate headcount for the poor, vulnerable and middle class as proposed by Azevedo and Sanfelice (2012) and applied in Azevedo et al. (2015).

## Examples

```stata
* Basic poverty measures with a poverty line variable
mpovline percapitainc, varpl(pline)

* With explicit poverty lines and FGT indicators
mpovline percapitainc [w=weight], line(100 500) in(fgt0 fgt1 fgt2)

* Multiple poverty lines as multiples of the base line
mpovline percapitainc [w=weight], varpl(pline) mpl(1 3.5 6)
```

## References

- Azevedo, J.P. and Sanfelice, V. (2012). "The rise of the middle class in Latin America." World Bank (mimeo).
- Azevedo, J.P., López-Calva, L.F., Lustig, N. and Ortiz-Juárez, E. (2015). "Inequality, Mobility and Middle Classes in Latin America." In Dayton-Johnson (ed.), *Latin America's Emerging Middle Classes*, Palgrave Macmillan.
- Foster, J., Greer, J. and Thorbecke, E. (1984). "A class of decomposable poverty measures." *Econometrica*, 52(3), 761–766.

## Citation

Azevedo, J.P. and Sanfelice, V. (2012). "MPOVLINE: Stata module to calculate FGT0, FGT1 and FGT2 by intervals of multiple thresholds." *Statistical Software Components* S457565, Boston College Department of Economics.
