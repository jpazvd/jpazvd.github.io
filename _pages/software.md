---
layout: archive
title: "Data & Analytics Tools"
permalink: /softwares/
author_profile: true
---

## Overview

Over the past two decades, I have authored or co-authored **22 Stata modules** hosted on the SSC archive. These contributions span three areas:  
- **Methodological Innovation**: extending the frontier of poverty, inequality, and opportunity analysis.  
- **Method Dissemination & Operationalization**: translating established methods into reproducible, accessible Stata commands.  
- **Data Access, Reproducibility & Scalability**: embedding open data, efficient computation, and standardized reporting into analytical workflows.  

Together, these tools are used by researchers, national statistical offices, and international agencies to produce results that are rigorous, reproducible, and operational at scale.

---

### Methodological Innovation  
Modules where I developed or co-developed new analytical approaches.  

- ADECOMP, DRDECOMP, SKDECOMP, MPOVLINE — Shapley decompositions of poverty changes (growth, distribution, prices).  
- HOI — Human Opportunity Index.  
- ALORENZ, ISOPOVERTY, CHANGEMEAN — Lorenz dominance, iso-poverty curves, mean vs. distribution effects.  
- GRQREG — Graphical quantile regression coefficients.  

---

### Method Dissemination & Operationalization  
Modules where I translated established methods into reproducible, accessible Stata commands.  

- DFL — DiNardo–Fortin–Lemieux counterfactual density decomposition.  
- SAE / FHSAE — Small area estimation: unit- and area-level models.  
- APOVERTY, AINEQUAL — FGT poverty measures and inequality indices.  
- TURNBULL, SPIKE — Nonparametric willingness-to-pay estimators.  
- MOL — Effective literacy index (Basu–Foster).  
- FACTORTEST, CRTEST — Econometric tests for factor analysis and multinomial logit pooling.  

---

### Data Access, Reproducibility & Scalability  
Modules that make data workflows more reliable, auditable, and efficient.  

- WBOPENDATA — API access to World Bank databases.  
- GROUPFUNCTION — High-performance data aggregation for large datasets.  
- OUTTABLE — Standardized export of results to LaTeX.  

---

### Impact  

📊 **Software Impact (RePEc/LogEc, Aug 2025)**  

- **22 SSC modules** authored/co-authored (2001–2021)  
- **26,798 downloads** | **111,269 abstract views**  
- Ranked **#20 worldwide** and **#6 among U.S. authors** by software downloads  
- Widely adopted tools include **WBOPENDATA**, **HOI**, **DFL**, and **SAE/FHSAE**

---

{% if site.data.navigation %}
<!-- Jekyll Scholar is available in CI builds -->

## Portfolio Table  

{% bibliography --query @software %}

---

### 📊 Datasets

{% bibliography --query @dataset %}


{% else %}
<!-- Static fallback for GitHub Pages build -->


{% endif %}


### 🐙 Code Repositories
**For a complete list of my software and code, please visit:**

- [Boston College Statistical Software Components (SSC)](https://ideas.repec.org/e/pwa88.html)
- [GitHub Profile](https://github.com/jpazvd)