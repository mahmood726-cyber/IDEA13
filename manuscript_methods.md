# Methods

## Overview

We conducted a two-part validation analysis. Part 1 (Empirical) used published summary data from two companion IPD meta-analyses to perform formal statistical tests. Part 2 (Simulation) generated synthetic datasets matching the original trial structure to quantify false-positive rates when no true threshold existed.

---

## Part 1: Empirical Analysis of Published Data

### Data Sources

We extracted summary statistics from two published IPD meta-analyses:[8,9]

1. **EF 40-49%**: 1,885 patients (991 beta-blockers, 894 control), 235 events (death, MI, or heart failure)[8]
2. **EF ≥50%**: 17,801 patients (8,831 beta-blockers, 8,970 control), 1,465 events[9]

Both drew from the same contemporary trials (REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT).

### Statistical Analyses

**Test for Interaction:** We calculated the formal interaction test to evaluate whether treatment effects differed significantly between EF subgroups using standard errors derived from published 95% CIs: SE = [log(CI_upper) - log(CI_lower)] / (2×1.96). The test statistic Z = [log(HR₁) - log(HR₂)] / √(SE₁² + SE₂²) provides the appropriate assessment of differential effects.[35,36]

**Fragility Index:** We calculated the minimum number of outcome events requiring reclassification to change the EF 40-49% result from significant (p<0.05) to non-significant (p≥0.05).[30,31] Starting with the observed 2×2 contingency table (events by treatment group), we iteratively transferred events from control to beta-blocker groups, recalculating chi-square p-values after each transfer using the Pearson chi-square test for 2×2 tables. Fragility index ≤5 indicates extreme statistical instability.[30,31]

**Power Analysis:** Using Schoenfeld's method for Cox regression,[32] we calculated power to detect clinically meaningful hazard ratios: Power = Φ[√(E/4) × |log(HR_true)| - 1.96], where E is the number of events (235). We determined events required for 80% power to detect HR=0.80.

**Interaction Test Power:** We calculated power of the interaction test itself using: Power = Φ[(|Δ|/SE_Δ) - 1.96], where Δ is the observed difference in log hazard ratios and SE_Δ = √(SE₁² + SE₂²). This addresses whether non-significant interaction reflects true equivalence or Type II error.

**Overall Pooled Effect:** We combined both EF ranges (40-49% and ≥50%) using inverse-variance weighted fixed-effect meta-analysis to estimate overall treatment effect across the entire EF spectrum from 40% onward. We used a fixed-effect model because these are two subgroups from the same IPD meta-analysis of the same four trials (not independent studies), making a common treatment effect assumption appropriate.

---

## Part 2: Simulation Study

### Design

We generated 10,000 synthetic IPD meta-analyses matching the original structure:
- 4 trials with sample size distribution proportional to actual trials (52%, 22%, 23%, 3%)
- 1,885 total patients per simulation
- Target ~235 events (12.5% event rate)
- LVEF sampled from truncated normal (mean 45%, SD 2.5%, range 40-49.9%)

**Crucially**, we programmed a **smooth, continuous decline** in beta-blocker effect as LVEF increased, with **no threshold**:

log(HR(EF)) = -0.287 + 0.0182 × (EF - 40)

This produces HR=0.75 at EF=40% declining linearly to HR=0.90 at EF=50%, with no discontinuities.

### Sensitivity Analysis: Six Alternative Models

To test robustness, we repeated simulations under six different true effect models:

- **Model 1 (Primary):** Linear decline (HR 0.75→0.90 across EF 40-50%)
- **Model 2:** Quadratic (accelerating decline)
- **Model 3:** Gentle threshold at EF=47% (HR 0.70 below, 0.90 above)
- **Model 4:** Complete null (HR=1.0 at all EF)
- **Model 5:** Random heterogeneous effects across trials
- **Model 6:** True threshold at EF=50% (HR 0.75 below, 0.97 above) - **matching observed data**

For Models 1-5, LVEF was sampled from truncated normal (mean 45%, SD 2.5%, range 40-49.9%) matching the EF 40-49% population. For **Model 6 only**, the LVEF range was extended to 40-60% (mean 50%, SD 5%) to allow testing of the threshold at the claimed EF=50% boundary. Model 6 tests **sensitivity**: can cross-validation detect TRUE thresholds when they exist? Models 1-5 test **specificity**: can it reject false thresholds? (Full model equations in supplementary materials)

### Analytical Methods Applied to Simulated Data

We applied four strategies to each of 10,000 simulated datasets:

**Method 1: Multiple Threshold Testing (Standard Practice)**
Tested 13 thresholds (42-48%, every 0.5%). Recorded whether **any** threshold showed significant benefit (p<0.05) in the "low EF" group using Cox models. False-positive rate = proportion where ≥1 threshold yielded p<0.05 despite no true threshold.

**Method 2: Single Interaction Test**
Tested interaction at pre-specified EF=45% (midpoint). False-positive rate = proportion with interaction p<0.05.

**Method 3: Continuous Modeling**
Modeled EF continuously (treatment × EF interaction). False-positive rate = proportion with continuous interaction p<0.05.

**Method 4: Cross-Validation (Gold Standard)**
Leave-one-trial-out validation:
1. Combine three trials (training)
2. Find threshold (42-48%) with smallest p-value in training set
3. Test discovered threshold in held-out fourth trial
4. Repeat for all four trials
False-positive rate = proportion where discovered threshold validated (p<0.05) in ≥1 held-out trial.

### Software

Empirical analyses used Python 3.11 with standard statistical libraries. Simulations used NumPy 1.24, SciPy 1.10, and lifelines 0.27. Code available at https://github.com/beta-blocker-validation/ef-threshold-analysis.

---

## Ethical Approval

This study used only published summary data and simulated data. No individual patient data were accessed. Ethical approval was not required.

## Data Availability

All data analyzed in this study were extracted from publicly available published meta-analyses.[8,9] Extracted summary statistics, event distributions, and 2×2 contingency tables are provided in Tables 1-2 and Supplementary Table S1. Simulation code, analysis scripts, and complete results are available at https://github.com/beta-blocker-validation/ef-threshold-analysis (DOI: 10.5281/zenodo.PENDING). Individual patient data were not accessed.

---

**Word Count:** ~850 words

**Note:** Detailed equation derivations, simulation parameter justifications, and step-by-step calculation examples provided in supplementary materials.
