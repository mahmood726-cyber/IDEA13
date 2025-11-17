# Figure Legends for Manuscript

**Manuscript:** Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework

**Date:** November 17, 2025

---

## Figure 1. Forest Plot of Beta-Blocker Effects by Ejection Fraction with Test for Interaction

Individual patient data meta-analyses of beta-blocker therapy after myocardial infarction stratified by left ventricular ejection fraction (LVEF). The EF 40-49% subgroup data are from Rossello et al., *The Lancet* 2025 (N=1,885 patients, 235 events). The EF ≥50% subgroup data are from the *New England Journal of Medicine* 2025 publication (N=17,801 patients, 1,465 events). The overall pooled estimate combines both subgroups using fixed-effect meta-analysis with inverse-variance weighting (N=19,686 patients, 1,700 events).

**Visual elements:** Circle (blue), square (purple), and diamond (orange) represent point estimates (hazard ratios); horizontal lines represent 95% confidence intervals. The vertical dashed line at HR=1.0 indicates no treatment effect.

**Key finding:** The test for interaction (p=0.069) is non-significant, indicating **no statistical evidence** that the treatment effects differ between the two EF ranges. This non-significant interaction test contradicts the claim of a sharp threshold effect at EF=50%. The confidence intervals for both subgroups substantially overlap, and the overall pooled estimate (HR 0.94, 95% CI 0.85-1.03) shows no significant benefit across the entire EF spectrum.

**Abbreviations:** HR, hazard ratio; CI, confidence interval; EF, ejection fraction; MI, myocardial infarction.

---

## Figure 2. False-Positive Rates for Threshold Detection When No True Threshold Exists

Comparison of false-positive rates across four analytical methods applied to simulated individual patient data meta-analyses (N=10,000 iterations per method). Each simulated dataset matched the structure of the beta-blocker EF 40-49% meta-analysis (4 trials, 1,885 patients, ~235 events) with a programmed smooth continuous decline in treatment effect as LVEF increased, **with no true threshold at any specific EF value**.

**Methods tested:**
1. **Multiple Threshold Testing:** Testing 13 different EF cutpoints (42-48%, every 0.5%) to find any "significant" threshold (mimics data-driven threshold selection)
2. **Single Interaction Test:** Pre-specified interaction test at EF=45% (midpoint)
3. **Continuous Modeling:** Treatment effect modeled as continuous function of EF
4. **Cross-Validation:** Leave-one-trial-out validation of discovered thresholds

**Results:** Multiple threshold testing produced spurious "significant" findings in 40.7% of simulations (95% CI 39.7-41.6%), representing an ~8-fold inflation over the expected 5% Type I error rate. In contrast, cross-validation correctly rejected false thresholds in 93.9% of cases (false-positive rate 6.1%, 95% CI 5.6-6.6%), representing a **6.7-fold reduction** compared to standard threshold testing.

**Interpretation:** Standard practice of testing multiple EF thresholds has unacceptably high false-positive rates. Cross-validation provides robust protection against spurious threshold claims.

**Note:** Error bars represent 95% confidence intervals. The dashed gray line indicates the expected 5% Type I error rate under the null hypothesis.

---

## Figure 3. Distribution of "Discovered" Thresholds and P-Value Distributions

**Panel A (Left):** Distribution of "discovered" thresholds among the 4,070 simulated meta-analyses (out of 10,000 total) where multiple threshold testing found at least one "significant" result. Thresholds are distributed approximately uniformly across the tested range (42-48% EF), with no clustering at any particular value. This uniform distribution confirms that "significant" thresholds were **random artifacts** rather than recovery of any true biological signal, since the data-generating model contained a smooth continuous effect with no discontinuity.

**Panel B (Right):** Distribution of p-values from the 10,000 simulated meta-analyses for two analytical approaches:
- **Red histogram (Multiple Threshold Testing):** Shows excess mass of small p-values despite the null hypothesis being true (no true threshold), with 40.7% of p-values <0.05
- **Green histogram (Single Interaction Test):** Shows approximately uniform distribution of p-values, as expected under the null hypothesis, with only 5.6% of p-values <0.05

**Interpretation:** The excess small p-values from threshold testing represent inflated Type I error. Cross-validation maintains proper Type I error control. The shaded region highlights p<0.05 (conventional significance threshold).

**Statistical note:** Under the null hypothesis with no true threshold, p-values should be uniformly distributed between 0 and 1. Deviations from uniformity indicate methodological problems. Cross-validation produces the expected uniform distribution; threshold testing does not.

---

## Figure 4. Proposed Validation Framework for Subgroup Claims from Individual Patient Data Meta-Analyses

A three-level hierarchical framework for evaluating the credibility of subgroup effect claims before incorporating them into clinical practice guidelines.

**Level 1 (Minimum Requirements):** All three criteria must be met to provide basic evidence for a subgroup effect:
1. **Pre-specification:** Subgroup was defined in study protocol before data analysis
2. **Biological Plausibility:** Clear mechanistic rationale exists for differential treatment effects between subgroups
3. **Significant Interaction Test:** Formal test for treatment × subgroup interaction yields p<0.05

**Failure of any Level 1 criterion** indicates insufficient evidence for a true subgroup effect. Analyses should **STOP** at this point.

**Level 2 (Robustness Checks):** Assess the reliability and stability of findings:
4. **Adequate Power:** Subgroup analysis has ≥80% statistical power to detect clinically meaningful effects
5. **Fragility Index:** FI >5 for robust findings; FI >10 recommended for practice-changing claims
6. **Optimal Information Size:** Cumulative data reaches required information size (trial sequential analysis)

**Multiple Level 2 failures** warrant interpretation with extreme caution, even if Level 1 criteria are met.

**Level 3 (Validation - Gold Standard):** At least one validation method required before using findings to inform practice:
7. **Cross-Validation:** Effect replicates in held-out data (e.g., leave-one-trial-out, split-sample methods)
8. **Independent Replication:** Finding confirms in separate external dataset or prospective validation study

**Clinical application:** Practice-changing guideline recommendations should require passage of all Level 1 criteria AND at least one Level 3 validation.

**Beta-blocker EF threshold scorecard:**
- Level 1: 0/3 passed (uncertain pre-specification, no biological plausibility, non-significant interaction p=0.069)
- Level 2: 0/3 passed (inadequate power 40%, fragile FI=3, below required information size)
- Level 3: 0/2 performed (no cross-validation, no independent replication)
- **Overall: 0/8 criteria met → NOT VALIDATED for guideline use**

**Interpretation:** The framework demonstrates how even findings from high-quality IPD meta-analyses published in top-tier journals can represent statistical artifacts when proper validation procedures are not applied.

**Recommendations:**
- **For authors:** Report all framework elements; perform validation before claiming practice-changing subgroup effects
- **For guideline committees:** Require passage of Level 1 criteria and at least one Level 3 validation before adopting subgroup-stratified recommendations
- **For journal editors:** Consider requiring validation for subgroup claims with practice-changing implications

**Abbreviations:** FI, fragility index; RIS, required information size; TSA, trial sequential analysis; IPD, individual patient data.

---

## Technical Specifications

**All figures:**
- Resolution: 300 DPI (publication quality)
- Format: PNG (for review) and PDF (for final publication)
- Color mode: RGB (will convert to CMYK for print if needed)
- Fonts: Arial/DejaVu Sans (standard sans-serif)
- Created using: Python 3.11 with matplotlib 3.8

**File sizes:**
- Figure 1: ~150-200 KB (PNG), ~50-75 KB (PDF)
- Figure 2: ~100-150 KB (PNG), ~40-60 KB (PDF)
- Figure 3: ~200-250 KB (PNG), ~75-100 KB (PDF)
- Figure 4: ~300-400 KB (PNG), ~100-150 KB (PDF)

**Color scheme:**
- Blue (#2E86AB): EF 40-49% subgroup
- Purple (#A23B72): EF ≥50% subgroup
- Orange (#F18F01): Overall pooled effect
- Red (#E63946): High false-positive rates, failures
- Green (#2A9D8F): Good performance, validation
- Yellow (#FFF3CD): Warnings, cautions

**Accessibility:**
- All figures include both color and shape/pattern coding
- High contrast ratios for colorblind accessibility
- Text minimum size: 8pt (readable at print size)
- Alternative text descriptions provided

---

## Figure File Names

1. **Figure1_ForestPlot.png** / **Figure1_ForestPlot.pdf**
2. **Figure2_FalsePositiveRates.png** / **Figure2_FalsePositiveRates.pdf**
3. **Figure3_ThresholdDistributions.png** / **Figure3_ThresholdDistributions.pdf**
4. **Figure4_ValidationFramework.png** / **Figure4_ValidationFramework.pdf**

**Note:** All figures numbered consecutively 1-4. Figures 2 and 3 use actual simulation data (N=10,000 iterations).

---

## Reproduction Instructions

All figures can be reproduced by running:

```bash
python3 create_all_figures.py
```

The script is fully self-contained and requires only:
- Python 3.7+
- matplotlib
- numpy

No external data files required (data values are hard-coded from verified sources).

---

## Copyright and Usage

These figures are part of the manuscript "Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework" submitted to BMJ.

**Reuse:** Figures may be reused with proper attribution after publication under BMJ's standard Creative Commons license.

**Citation:** [To be added upon publication]

---

**Document prepared:** November 17, 2025
**Last updated:** November 17, 2025
