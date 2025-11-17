# Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework

## Abstract

**Background:** Recent individual-patient data (IPD) meta-analyses published in *The Lancet* and *NEJM* suggest beta-blockers benefit post-myocardial infarction patients with left ventricular ejection fraction (LVEF) 40-49% (hazard ratio [HR] 0.75, 95% CI 0.58-0.97, p=0.031) but not those with LVEF ≥50% (HR 0.97, 95% CI 0.87-1.07, p=0.54), leading to calls for ejection fraction-stratified treatment guidelines. We evaluated the statistical robustness of this proposed threshold.

**Methods:** We conducted a two-part validation analysis. **Part 1 (Empirical):** Using published data from both meta-analyses (N=19,686 patients, 1,700 events), we calculated the formal test for statistical interaction between EF subgroups, assessed statistical power and fragility of the EF 40-49% finding, and determined the overall pooled treatment effect. **Part 2 (Simulation):** We generated 10,000 synthetic IPD meta-analyses matching the original trial structure, with a true continuous decline in beta-blocker effect as LVEF increases (no sharp threshold). We quantified false-positive rates when applying standard dichotomization methods versus cross-validation approaches.

**Results:**

*Part 1 - Empirical Analysis:* The test for interaction between EF subgroups was non-significant (p=0.069), providing no statistical evidence for different treatment effects. The EF 40-49% subgroup analysis was severely underpowered (235 events; 40% power to detect HR 0.80) and extremely fragile (fragility index=3 events, representing only 1.3% of total events). When both EF ranges were pooled, the overall HR was 0.94 (95% CI 0.85-1.03), indicating no significant benefit across the entire EF spectrum.

*Part 2 - Simulation Study:* When testing multiple EF thresholds in data with smooth, continuous effects (no true threshold), standard dichotomization methods produced questionable "significant" thresholds in 46.8% of simulations. In contrast, cross-validation correctly rejected false thresholds in 98.5% of cases, representing a 31-fold reduction in false-positive rates.

**Conclusions:** The proposed LVEF 50% threshold appears to represent statistical overfitting from underpowered subgroup analysis and dichotomization of a continuous variable rather than a true biological phenomenon. The non-significant interaction test (p=0.069), extreme statistical fragility (FI=3), and high false-positive rates from dichotomization (46.8%) indicate this threshold may be unreliable for guideline development. Adoption of EF-stratified beta-blocker recommendations would be premature based on current evidence.

**Implications:** This case demonstrates how even high-quality IPD meta-analyses can produce questionable subgroup findings through standard analytical approaches. We propose a validation framework requiring: (1) significant interaction testing (p<0.05), (2) adequate statistical power (>80%), (3) fragility index >5, and (4) cross-validation of threshold claims before informing clinical practice. We call for the original investigators to apply cross-validation methods to their IPD data and for methodological standards requiring rigorous validation of subgroup claims before guideline adoption.

---

**Word Count:** 399 words
**Keywords:** subgroup analysis, overfitting, ejection fraction, beta-blockers, myocardial infarction, cross-validation, statistical fragility, meta-analysis methodology

---

## Key Statistics Summary

| Finding | Value | Interpretation |
|---------|-------|----------------|
| **Interaction test** | p = 0.069 | Non-significant; no evidence for threshold |
| **Fragility Index** | 3 events (1.3%) | Extremely fragile; <5 recommended minimum |
| **Statistical power** | 40% at HR 0.80 | Severely underpowered; <80% recommended |
| **Pooled effect** | HR 0.94 (0.85-1.03) | No overall benefit when combined |
| **Dichotomization false-positive rate** | 46.8% | Standard approach highly unreliable |
| **Cross-validation false-positive rate** | 1.5% | 31× more accurate than standard approach |
| **Validation tests not met** | 3 / 3 | Interaction, fragility, power criteria not met |

---

## Clinical Bottom Line

**Question:** Should beta-blockers be given based on ejection fraction thresholds after MI?

**Answer:** No. The claimed EF 50% threshold appears to be a statistical artifact rather than biological reality.

**Evidence:**
- The treatment effects at EF 40-49% vs ≥50% do not significantly differ (p=0.069)
- The finding is extremely fragile (only 3 events needed to flip result)
- The analysis was severely underpowered (40% power)
- Overall, no benefit across the EF spectrum (HR 0.94, CI 0.85-1.03)
- Simulations show this type of finding occurs in 47% of analyses even when no true threshold exists

**Recommendation:** Do not change clinical practice or guidelines based on this evidence.
