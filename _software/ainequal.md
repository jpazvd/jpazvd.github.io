---
title: "AINEQUAL"
excerpt: "Compute a variety of inequality measures from individual-level or grouped data in Stata."
layout: software-page
permalink: /software/ainequal/
author_profile: true
share: true
header:
  teaser: /images/software/stata-module.png
tags:
  - Stata
  - Inequality
  - Poverty
ssc_url: "https://ideas.repec.org/c/boc/bocode/s456748.html"
github_url: "https://github.com/jpazvd/ainequal"
install_cmd: "ssc install ainequal"
---

## Description

ainequal computes a series of inequality measures of the variables in varlist. It is a revised and upgraded version of inequal7 and inequal published by Edward Whitehouse in STB-23.

The inequality measures computed are: the relative mean deviation, the coefficient of variation, the standard deviation of logs, the Gini index, the Mehran index, the Piesch index, the Kakwani index, Theil entropy index, the mean log deviation, the generalised entropy measure for all sensitivity parameters, the Atkinson Inequality Index using the inequality aversion parameter epsilon, and the Donaldson-Weymark relative S-Gini using the distributional sensitivity parameter delta.

In addition, ainequal also computes the relative poverty line proposed by Hoffmann (2001) and Lambert and Lanza (2006), for the Gini, Theil-T and Theil-L.

## Example

```stata
* Basic inequality measures
sysuse nlsw88, clear
ainequal wage
```

## References

- Amiel, Y. and Cowell, F.A. (1999) *Thinking about Inequality*. Cambridge University Press.
- Cowell, F.A. (1995) *Measuring Inequality* (second edition). Prentice-Hall/Harvester-Wheatsheaf.
- Hoffmann, R. (2001) "Effect of the rise of a person's income on inequality." *Brazilian Review of Econometrics*, 21(2), 237–262.
- Lambert, P.J. and Lanza, G. (2006) "The effect on inequalities of changing one or two incomes." *Journal of Economic Inequality*, 4, 253–277.

## Citation

Azevedo, J.P. (2006). "AINEQUAL: Stata module to compute measures of inequality." *Statistical Software Components* S456748, Boston College Department of Economics.
