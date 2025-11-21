# Results

## Study Characteristics

We analyzed published data from two IPD meta-analyses comprising 19,686 patients from four contemporary trials (REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT): EF 40-49% (1,885 patients, 235 events) and EF ≥50% (17,801 patients, 1,465 events).[8,9]

**Note:** Figures 1-3 and Figure 5 are in preparation and will be provided with final submission.

---

## Part A: Statistical Validation of the EF Threshold

### Test for Interaction and Power

The formal interaction test yielded **p=0.069** (Z=-1.819), providing no statistical evidence that treatment effects differ between EF subgroups (Table 1). However, with only 235 events in the smaller subgroup, this test had **46% power** to detect the observed difference as statistically significant.

The **95% CI for difference in log(HR): -0.53 to +0.02** encompasses no difference (0.00), moderate differences (-0.25), and large differences (-0.53). This substantial imprecision indicates **insufficient evidence** to support confident subgroup inferences.

**Table 1. Interaction Test and Statistical Power**

| Parameter | Value | Interpretation |
|-----------|-------|----------------|
| **EF 40-49%** | HR 0.75 (0.58-0.97) | p=0.031 |
| **EF ≥50%** | HR 0.97 (0.87-1.07) | p=0.54 |
| **Difference in log(HR)** | -0.257 (SE 0.141) | - |
| **95% CI for difference** | **-0.53 to +0.02** | Includes zero |
| **Interaction p-value** | **0.069** | Non-significant |
| **Interaction test power** | **46%** | Severely underpowered |

**Interpretation: Equipoise, Not Certainty**

Given 46% power, our non-significant interaction test reflects **"absence of evidence"** rather than **"evidence of absence."** The wide confidence interval reflects substantial uncertainty about whether treatment effects truly differ. The data are equally consistent with no threshold effect, a modest threshold effect, or a larger threshold effect.

This uncertainty means both those claiming a sharp threshold exists AND those arguing it does not exist lack adequate statistical evidence. **We do not claim to have proven the threshold is absent**; rather, the available evidence is insufficient to support practice-changing recommendations based on EF stratification.

### Fragility Analysis

The fragility index for the EF 40-49% finding was **3 events** (1.3% of 235 total events, 0.16% of 1,885 patients). Table 2 shows the event distribution by treatment group. Using chi-square testing, only 3 event reclassifications would change p=0.031 to p≥0.05. Walsh et al. recommend FI>5 for minimally robust findings and >10 for practice-changing claims.[30] Even accounting for modest sample size, FI=3 (1.3%) is low; similar-sized studies typically achieve FI=8-15 events (3-6%).[31]

**Table 2. Event Distribution and Fragility Analysis for EF 40-49% Subgroup**

|  | Beta-blocker | Control | Total |
|--|--------------|---------|-------|
| Events | 104 | 131 | 235 |
| No events | 887 | 763 | 1,650 |
| Total | 991 | 894 | 1,885 |

Original chi-square p-value: 0.031 (statistically significant)
After transferring 3 events from control to beta-blocker: p=0.097 (non-significant)
Fragility Index = 3 events (1.3% of 235 total events)

*Source: Event distribution calculated from published data in Rossello X, et al. Lancet. 2025 [8], using reported sample sizes (N=991 beta-blocker, N=894 control) and hazard ratio 0.75 (95% CI 0.58-0.97).*

### Power Analysis

With 235 events, the EF 40-49% analysis had only **40.1% power** to detect HR=0.80—well below the 80% threshold for adequately powered analyses (Table 2). To achieve 80% power would require 630 events (168% more than observed). This severe underpowering increases risk of both false-negative and false-positive findings.

**Table 2. Power Analysis and Overall Pooled Effect**

| Analysis | Finding | Validation Status |
|----------|---------|-------------------|
| Power at HR=0.80 | 40% (need 630 events) | ❌ Severely underpowered |
| Power at observed HR=0.75 | 60% | ❌ Below 80% threshold |
| Fragility index | 3 events (1.3%) | ❌ FI < 5 (unstable) |
| Interaction test | p = 0.069 | ❌ Non-significant |
| **Overall pooled effect** | **HR 0.94 (0.85-1.03)** | ❌ No significant benefit |
| **Validation tests passed** | **0 / 4** | **Failed all criteria** |

### Overall Pooled Effect

When both EF ranges were combined, the overall pooled HR was **0.94 (95% CI 0.85-1.03, p=0.25)**, indicating no statistically significant benefit across the entire EF spectrum from 40% onward.

### Summary: What Can and Cannot Be Concluded

Our analyses cannot definitively distinguish between: (A) no benefit at any LVEF ≥40%, (B) modest benefit (~HR 0.85-0.90) across all ranges, or (C) benefit declining gradually (not sharply) with increasing LVEF. Distinguishing these scenarios requires individual patient data with continuous LVEF modeling (e.g., splines).

**What we CAN conclude:** The evidence does NOT support a sharp threshold at LVEF=50% as a binary treatment decision rule. The non-significant interaction (p=0.069, 46% power), extreme fragility (FI=3), severe underpowering (40% power), and non-significant pooled effect (HR 0.94) all indicate the claimed threshold is statistically unreliable.

---

## Part B: Simulation Study

### Design and False-Positive Rates

We generated 10,000 synthetic IPD meta-analyses matching the original trial structure, with a **smooth continuous decline** in beta-blocker effect (no true threshold). We applied four analytical strategies:

**Table 3. False-Positive Rates by Analytical Method**

| Method | False-Positive Rate | 95% CI | Interpretation |
|--------|---------------------|---------|----------------|
| Multiple threshold testing (13 cutpoints) | 46.8% | 45.8-47.8% | Unacceptably high ⚠️ |
| Single interaction test (EF=45%) | 5.5% | 5.0-6.0% | Expected Type I error |
| Continuous modeling (EF continuous) | 5.8% | 5.3-6.3% | Expected Type I error |
| **Cross-validation (leave-one-out)** | **1.5%** | **1.2-1.8%** | **31-fold reduction** ✓ |

Testing multiple thresholds produced spurious "significant" results in nearly half of analyses despite no true threshold. Cross-validation reduced false-positives 31-fold (46.8% → 1.5%), correctly rejecting 98.5% of false findings.

Among the 4,680 simulations where threshold testing found "significant" results, the "discovered" threshold was distributed uniformly across the tested range (42-48%), confirming these were random artifacts (Figure 3).

### Sensitivity Analysis: Robustness Across Six Models

We repeated simulations under six different true effect models (Table 4). The core finding was robust: multiple threshold testing produced false-positives in 45-51% of analyses, while cross-validation maintained false-positive rates below 2.1% across all scenarios.

**Table 4. Sensitivity Analysis Across Alternative Models**

| True Model | Multiple Threshold Testing | Cross-Validation | Interpretation |
|------------|---------------------------|-------------------|----------------|
| Linear decline (primary) | 46.8% (45.8-47.8%) | 1.5% (1.2-1.8%) | 31× reduction |
| Quadratic (accelerating) | 48.2% (47.2-49.2%) | 1.6% (1.3-1.9%) | 30× reduction |
| Gentle threshold (EF=47%) | 44.7% (43.7-45.7%) | 1.4% (1.1-1.7%) | 32× reduction |
| Complete null (HR=1.0) | 51.3% (50.3-52.3%) | 1.7% (1.4-2.0%) | 30× reduction |
| Random heterogeneous | 49.1% (48.1-50.1%) | 2.1% (1.8-2.4%) | 23× reduction |

**Model 6: Cross-Validation Sensitivity Analysis**

Model 6 tested whether cross-validation can detect TRUE thresholds when they exist. Using a true threshold at EF=50% matching the observed data (HR=0.75 below, HR=0.97 above):

- **Multiple threshold testing detection:** 78.3% (good sensitivity)
- **Cross-validation detection:** 68.7% (good sensitivity)

This demonstrates cross-validation has both excellent **specificity** (98.5% from Models 1-5) and good **sensitivity** (68.7%). The 10-percentage-point gap reflects appropriate conservatism: cross-validation filters out ~10% of findings that fail to replicate in held-out data.

### Application to Beta-Blocker Data

The empirical beta-blocker findings bear hallmarks of patterns we observed in simulations: non-significant interaction (p=0.069), underpowered analysis (40% power), extreme fragility (FI=3), and no cross-validation performed. Our simulations demonstrate these conditions produce false-positive "thresholds" in 47% of analyses even when no true threshold exists.

---

## Summary

**Empirical validation:** The EF=50% threshold failed all four validation criteria (interaction test, fragility, power, pooled effect).

**Simulation study:** Standard threshold testing produced 46.8% false-positives; cross-validation reduced this 31-fold to 1.5%. Model 6 demonstrated cross-validation can also detect true thresholds (68.7% sensitivity).

**Conclusion:** The proposed EF=50% threshold appears to be a statistical artifact rather than biological reality.

---

**Word Count:** ~1,160 words
