# Methods - Part 1: Empirical Analysis (CONDENSED)

## Overview

We conducted a two-part validation analysis. Part 1 (Empirical) used published summary data from two companion IPD meta-analyses to perform formal statistical tests. Part 2 (Simulation) generated synthetic datasets to quantify false-positive rates under controlled conditions where no true threshold existed.

---

## Part 1: Empirical Analysis of Published Data

### Data Sources

We extracted summary statistics from two IPD meta-analyses:

1. **EF 40-49%**: Rossello et al., *Lancet*, August 2025.[8] Included 1,885 patients (991 beta-blockers, 894 control) with 235 primary endpoint events (death, MI, or heart failure).

2. **EF ≥50%**: *NEJM*, November 2025.[9] Included 17,801 patients (8,831 beta-blockers, 8,970 control) with 1,465 events.

Both drew from the same contemporary trials (REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT). We extracted hazard ratios, 95% CIs, patient numbers, and event counts.

### Statistical Analyses

**Test for Interaction**

We performed the formal test for interaction to evaluate whether treatment effects differed significantly between EF subgroups.[35,36] Standard errors were calculated from published 95% CIs:

$$SE = \frac{\log(CI_{upper}) - \log(CI_{lower})}{2 \times 1.96}$$

The test statistic was:

$$Z = \frac{\log(HR_1) - \log(HR_2)}{\sqrt{SE_1^2 + SE_2^2}}$$

P-value <0.05 indicates statistically significant heterogeneity between subgroups.

**Fragility Index**

The fragility index quantifies the minimum events needing reclassification to change p<0.05 to p≥0.05.[30,31] Starting with the observed 2×2 table, we iteratively transferred events from control to beta-blocker group and recalculated p-values. Fragility index ≤5 indicates extreme instability; >10 is recommended for practice-changing claims.

**Power Analysis**

We assessed statistical power using Schoenfeld's method:[32]

$$\text{Power} = \Phi\left(\sqrt{\frac{E}{4}} \times |\log(HR_{true})| - Z_{\alpha/2}\right)$$

where $E$ is the number of events. We calculated power for assumed true HRs of 0.70-0.90 and determined events required for 80% power.

**Power of Interaction Test**

We calculated power of the interaction test itself—often overlooked but critical, as non-significant results could reflect insufficient power rather than truly equivalent effects:

$$\text{Power}_{interaction} = \Phi\left(\frac{|\Delta|}{SE_{\Delta}} - Z_{\alpha/2}\right)$$

where $\Delta = \log(HR_1) - \log(HR_2)$.

**Overall Pooled Effect**

We combined both EF ranges in a fixed-effect meta-analysis using inverse-variance weighting to estimate overall treatment effect across LVEF 40-100%.

### Software

All empirical analyses were conducted using Python 3.11 with standard statistical libraries. Code available at [GitHub repository].

---

**Word Count:** ~420 words (estimated original ~600 words; saves ~180 words) ✓

**Content Preserved:**
- ✅ Overview of two-part design
- ✅ Data sources clearly described
- ✅ All five statistical methods with key equations
- ✅ Rationale for each analysis
- ✅ Software information

**Content Condensed:**
- Extended equation derivations → Key formulas only
- Detailed justifications → Brief mentions
- Example calculations → Removed (available in Supplement)

**Moved to Supplement:**
- Complete equation derivations → Supplementary Methods S1
- Example calculations → Table S1-S2
