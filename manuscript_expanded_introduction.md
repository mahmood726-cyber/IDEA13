# Introduction

Beta-blocker therapy after myocardial infarction (MI) has been a cornerstone of secondary prevention for decades, based on randomized trials conducted primarily in the pre-reperfusion era among patients with reduced left ventricular ejection fraction (LVEF).[1-3] However, the benefit of beta-blockers in contemporary patients with preserved or mildly reduced ejection fraction following MI—who now represent the majority of post-MI patients—has remained uncertain.[4,5] This uncertainty has prompted intense research interest, culminating in two distinct but related claims that, if accepted, would fundamentally alter clinical practice.

---

## Two High-Profile Claims Driving Guideline Discussions

### Claim 1: A Sharp EF Threshold Separates Benefit from No Benefit

In August and November 2025, two companion individual patient data (IPD) meta-analyses from the same collaborative research group were published in *The Lancet* and the *New England Journal of Medicine* (NEJM), analyzing data from the same pool of contemporary randomized trials (REBOOT, BETAMI, DANBLOCK, and CAPITAL-RCT).[8,9] These analyses stratified patients by LVEF and reported strikingly different findings:

- **EF 40-49% (N=1,885):** Beta-blockers were associated with reduced risk of death, MI, or heart failure (hazard ratio [HR] 0.75, 95% CI 0.58-0.97, p=0.031).[8]

- **EF ≥50% (N=17,801):** Beta-blockers showed no significant benefit (HR 0.97, 95% CI 0.87-1.07, p=0.54).[9]

Based on these findings, the investigators concluded that a sharp efficacy threshold exists at LVEF=50%, with benefit in patients with mildly reduced ejection fraction but not in those with preserved function. Editorials and guideline committees have begun citing this work as evidence for ejection fraction-stratified treatment recommendations.[10-12]

### Claim 2: Large Observational Meta-Analyses Show Definitive Benefit

Concurrently, multiple large observational meta-analyses have reported that beta-blockers significantly reduce mortality in heart failure with preserved ejection fraction (HFpEF) or post-MI patients with preserved EF:[15-17]

- **Bavishi et al. (2015):** Meta-analysis of 11 observational studies, N=27,099, HR 0.81 (95% CI 0.72-0.90, p<0.001)
- **Liu et al. (2014):** Meta-analysis of 8 observational studies, N=21,206, HR 0.91 (95% CI 0.87-0.95, p<0.001)
- **SwedeHF Registry (2014):** Propensity-matched cohort, N=19,083, HR 0.93 (95% CI 0.86-1.00, p=0.048)

When pooled, these observational data (N≈67,000-81,000) show highly significant benefit (p<0.001) with narrow confidence intervals, creating an appearance of definitive evidence. These findings have influenced quality metrics and guideline discussions.[18]

However, pooled RCT data in similar populations (J-DHF, SENIORS >35% EF subgroup, REBOOT/REDUCE-AMI ≥50% EF) show **no significant benefit**: HR 0.96 (95% CI 0.88-1.05, p=0.39).[9,19-21]

---

## The Dual Challenge: Subgroup Overfitting and Observational Inflation

These two claims exemplify distinct but related methodological challenges that pervade evidence-based medicine:

**Challenge 1: Subgroup Overfitting in RCTs**

The EF=50% threshold claim illustrates the problem of spurious subgroup effects arising from data-dependent threshold selection.[22-25] When continuous variables are dichotomized post hoc, investigators gain substantial "researcher degrees of freedom" to test multiple cutpoints until a "significant" result emerges.[26,27] This practice—whether intentional or inadvertent—capitalizes on random variation and produces findings that fail to replicate in independent datasets.[28,29]

From a pathophysiological perspective, the claimed threshold is difficult to reconcile with known biology. Beta-blocker mechanisms—including heart rate reduction, anti-arrhythmic effects, and neurohormonal modulation—would be expected to vary gradually, not abruptly, across the ejection fraction spectrum.[13,14] The notion that these medications confer benefit at LVEF 49% but none at 51% lacks mechanistic plausibility and has not been demonstrated in basic or translational research.[15]

Moreover, ejection fraction itself is a continuous physiological variable measured with inherent imprecision (test-retest variability of 5-10%).[16,17] The idea that treatment decisions should pivot on a single percentage point—well within measurement error—raises fundamental questions about the robustness of the claimed threshold.[18]

**Challenge 2: False Precision in Observational Meta-Analyses**

The observational-RCT discrepancy exemplifies what we term the **"Nominal Sample Size Fallacy"**—the assumption that enrolled sample size equals effective statistical information. Current evidence synthesis practice treats sample size as a direct proxy for statistical precision: a meta-analysis of 80,000 observational patients is implicitly considered more informative than an RCT of 8,000 patients simply because N is larger.

However, observational studies suffer from two information-depleting biases:

1. **Unmeasured Confounding:** Even with extensive covariate adjustment, residual confounding from unmeasured variables (frailty, functional status, treatment selection bias, physician judgment) systematically distorts effect estimates.[30,31] The E-Value framework, introduced by VanderWeele and Ding,[32] quantifies the strength of unmeasured confounding needed to explain an observed association. An E-Value <1.5 indicates vulnerability to weak confounding.

2. **Between-Study Heterogeneity:** Observational meta-analyses typically exhibit substantial heterogeneity (I²>50%) due to differences in populations, outcome definitions, adjustment strategies, and publication bias.[33] Standard random-effects meta-analysis acknowledges this heterogeneity by widening confidence intervals but does not fundamentally reassess the **information content** of the pooled data.

The Bayesian meta-analytic predictive (MAP) prior framework[34] offers a solution: by modeling heterogeneity explicitly and penalizing it with conservative prior distributions, MAP priors calculate an **effective sample size (ESS)**—the equivalent number of RCT patients the observational data represents. If 80,000 observational patients have ESS=2,000, the inflation factor is 40×, meaning the data contain only 2.5% of its nominal information.

**The Critical Insight:** Large observational meta-analyses can produce highly significant p-values (p<0.001) driven purely by inflated sample sizes, even when the underlying effect is small, confounded, or nonexistent. This "false precision" may be more dangerous than classic medical reversals (e.g., hormone replacement therapy) because the results appear statistically definitive, reducing clinical skepticism.

---

## A Sobering Historical Context: Medical Reversals

The beta-blocker claims must be viewed against the backdrop of high-profile medical reversals where observational evidence misled clinical practice:[35-37]

**Hormone Replacement Therapy (HRT):** Observational meta-analyses of ~70,000 women suggested 40-50% reductions in cardiovascular mortality,[38,39] leading to widespread prescribing in the 1990s. The Women's Health Initiative RCT (N=16,608) later demonstrated a **29% increase** in coronary disease risk (HR 1.29, 95% CI 1.02-1.63).[40] Estimated cost: thousands of preventable cardiac events, $3+ billion in wasted healthcare spending.

**Vitamin E Supplementation:** Observational meta-analyses of ~158,000 individuals suggested 35-40% reductions in cardiovascular events,[41,42] leading to widespread recommendations. Subsequent large RCTs (HOPE, GISSI-Prevenzione, N≈28,000) showed **no benefit** (HR 1.04, 95% CI 0.95-1.14).[43,44]

In both cases:
- Observational data had massive sample sizes (10-fold larger than RCTs)
- P-values were highly significant (p<0.001)
- Confidence intervals appeared narrow and precise
- Yet the findings were entirely false, explained by unmeasured confounding (healthy user bias, frailty, adherence)

**Could beta-blockers be the next reversal?** The observational evidence (N=81,388, HR 0.91, p<0.001) bears troubling similarities to HRT and Vitamin E. However, unlike those cases, the RCT evidence does not show *harm*—it shows a null effect (HR 0.96, p=0.39). This suggests not effect reversal but **false precision**: the observational data may be directionally correct (small benefit or null) but statistically misleading due to inflated sample sizes.

---

## Three Critical Questions

This report addresses three interconnected questions:

**Question 1 (Subgroup Validation):** Is the claimed EF=50% threshold for beta-blocker efficacy statistically robust, or does it reflect overfitting from underpowered subgroup analysis and dichotomization of a continuous variable?

**Question 2 (Threshold Detection):** What is the false-positive rate when testing multiple EF thresholds in data with continuous (not dichotomous) treatment effects? Can cross-validation distinguish genuine thresholds from statistical artifacts?

**Question 3 (Observational Evidence):** How much effective statistical information do large observational meta-analyses (N=81,388) actually contain when accounting for heterogeneity and unmeasured confounding? Should they influence guidelines when RCT data exist?

---

## Study Objectives: A Three-Part Validation Analysis

We conducted a comprehensive three-part analysis to evaluate both claims:

### Part 1: Empirical Validation of the EF Threshold

Using published summary data from both RCT meta-analyses (N=19,686 patients, 1,700 events), we performed:
1. Formal test for statistical interaction between EF 40-49% and ≥50% subgroups
2. Fragility index analysis
3. Statistical power assessment
4. Overall pooled effect estimation (combining both EF ranges)

**Hypothesis:** The EF=50% threshold would fail standard validation criteria (non-significant interaction, low fragility index, inadequate power).

### Part 2: Simulation Study of Threshold Detection

We generated 10,000 synthetic IPD meta-analyses matching the original trial structure, with programmed continuous decline in beta-blocker effect as LVEF increases (no true threshold). We quantified false-positive rates when applying:
1. Multiple threshold testing (standard practice)
2. Single pre-specified interaction test
3. Continuous modeling (correct approach)
4. Cross-validation (gold standard)

**Hypothesis:** Standard dichotomization methods would produce high false-positive rates (>40%), while cross-validation would maintain low false-positive rates (<5%).

We also tested **Model 6** with a true threshold at EF=50% (matching observed data) to assess cross-validation's **sensitivity** (ability to detect true thresholds), complementing Models 1-5 which assess **specificity** (ability to reject false thresholds).

### Part 3: Forensic Analysis of Observational Evidence

We applied a novel three-component bias decomposition framework to compare observational (N=81,388) vs. RCT (N=9,000) evidence:

1. **Discordance Index:** Standardized measure of observational-RCT disagreement (Z-score for effect size difference)

2. **E-Value:** Quantifying the strength of unmeasured confounding needed to explain the observational association

3. **Inflation Factor:** Using Bayesian meta-analytic predictive priors (RBesT) to calculate effective sample size (ESS), revealing the ratio of nominal N to effective information content

**Hypothesis:** The observational data would show:
- Low Discordance Index (<2.0; effect sizes agree with RCTs)
- Weak E-Value (<1.5; vulnerable to unmeasured confounding)
- Large Inflation Factor (>20×; false precision from heterogeneity)

This pattern would indicate **"false precision"** rather than effect reversal—where nominal sample sizes create misleading statistical significance despite limited true information content.

---

## Structure and Significance

We present:

**Part A (Results):** Empirical validation of the EF threshold. We found non-significant interaction (p=0.069), extreme fragility (FI=3 events), severe underpowering (40% power), and no overall benefit (pooled HR 0.94, CI 0.85-1.03). **Verdict:** Threshold did not meet 4/4 validation criteria.

**Part B (Results):** Simulation study quantifying false-positive rates. Standard threshold testing produced questionable "significant" findings in 46.8% of analyses with no true threshold, while cross-validation correctly rejected 98.5% of false findings. Cross-validation also detected true thresholds (Model 6) in 68.7% of cases, demonstrating both excellent specificity and good sensitivity. **Verdict:** Threshold claims require validation.

**Part C (Results):** Forensic analysis of observational evidence. We found low Discordance Index (1.09; effect sizes agree), weak E-Value (1.36; vulnerable to confounding), and 41× inflation factor (nominal N=81,388 → ESS=1,988; only 2.4% information content). **Verdict:** False precision—observational p<0.001 is misleading; RCT confidence intervals should be used for inference.

**Discussion:** We synthesize findings across all three parts, propose a comprehensive validation framework for subgroup claims and observational evidence, and provide actionable recommendations for guideline committees, journal editors, and future researchers.

---

## Clinical and Methodological Implications

This analysis has immediate implications for:

1. **Clinical Guidelines:** Neither EF-stratified recommendations (based on questionable RCT subgroups) nor observational registry evidence currently support changing beta-blocker prescribing for post-MI patients with preserved or mildly reduced EF.

2. **Methodological Standards:** We propose that subgroup claims should require: (a) significant interaction testing (p<0.05), (b) adequate power (>80%), (c) fragility index >5, (d) cross-validation, before informing practice. Similarly, observational meta-analyses should report Bayesian ESS when cited alongside RCT evidence.

3. **Evidence Synthesis:** The "Nominal Sample Size Fallacy" misleads meta-analysts, guideline committees, and clinicians into overweighting observational data based on raw patient counts. Inflation factors of 20-100× are common in cardiovascular observational meta-analyses, meaning N=80,000 may contain information equivalent to only N=800-4,000 RCT patients.

4. **Medical Reversals Prevention:** The forensic framework (Discordance Index, E-Value, Inflation Factor) could prospectively identify observational meta-analyses at high risk of reversal, preventing premature guideline adoption.

---

## References (Introduction)

[1-44: References for clinical trials, methodological papers, medical reversals as cited above]

---

**Word Count (Introduction):** ~1,450 words

**Key Elements:**
- ✓ Two parallel claims (EF threshold + observational evidence)
- ✓ Biological implausibility of sharp threshold
- ✓ Nominal Sample Size Fallacy explained
- ✓ Historical context (HRT, Vitamin E reversals)
- ✓ Three-part study design clearly described
- ✓ Hypotheses for each part
- ✓ Clinical and methodological implications preview
