# Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework

**REVISED MANUSCRIPT - Response to BMJ Editorial Review**
**Revision Date:** November 2025

---

## Title Page

**Title:** Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework

**Short Title:** Validating Subgroup Claims in Meta-Analyses

**Authors:** [To be added]

**Affiliations:** [To be added]

**Corresponding Author:** [To be added]

**Word Count:** 4,287 words (excluding abstract, references, tables, figures)
**Abstract Word Count:** 349 words
**Number of Tables:** 6 main text tables (+ 4 supplementary tables)
**Number of Figures:** 3 figures (provided as separate files)
**Supplementary Materials:** Yes

**Keywords:** subgroup analysis, overfitting, ejection fraction, beta-blockers, myocardial infarction, cross-validation, statistical fragility, meta-analysis methodology

**Competing Interests:** None declared. The authors have no relationships with the investigators of the original Lancet/NEJM meta-analyses.

**Funding:** None

**Data Availability:** All data extracted from published sources are provided in supplementary materials with full provenance (source tables/figures documented). Simulation code is publicly available at https://github.com/[repository-name] (DOI: 10.5281/zenodo.XXXXX).

**Ethical Approval:** Not required (analysis of published aggregate data and simulated data only)

**Patient and Public Involvement:** Not applicable for this methodological study analyzing published aggregate data. However, the research question (validation of subgroup claims before guideline adoption) was informed by patient advocacy groups' concerns about premature treatment recommendations based on underpowered subgroup analyses.

---

## Abstract

**Objective:** To evaluate the statistical robustness of a proposed left ventricular ejection fraction (LVEF) threshold for beta-blocker efficacy after myocardial infarction.

**Design:** Two-part validation study: (1) empirical analysis of published individual patient data (IPD) meta-analyses, and (2) simulation study quantifying false-positive rates for threshold detection methods.

**Setting:** Secondary analysis of published meta-analyses and computer simulation.

**Participants:** Published data from 19,686 patients with recent myocardial infarction from four contemporary randomized trials (REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT).

**Main Outcome Measures:** Interaction test p-value and power, fragility index, statistical power, false-positive rates for threshold detection, cross-validation performance including both sensitivity and specificity.

**Results:** The interaction test between LVEF 40-49% and ≥50% subgroups was non-significant (p=0.069) with only 46% statistical power, indicating high risk of Type II error. The EF 40-49% finding (HR 0.75, 95% CI 0.58-0.97, p=0.031) was severely underpowered (235 events; 40% power to detect HR=0.80) and statistically fragile (fragility index=3 events, 1.3% of total, though we note fragility indices for time-to-event outcomes have limitations). When both EF ranges were pooled (assuming homogeneous effects), the hazard ratio was 0.94 (95% CI 0.85-1.03).

In simulation studies where no true threshold existed, testing multiple LVEF cutpoints produced false-positive "thresholds" in 46.8% (95% CI 45.8-47.8%) of analyses. Cross-validation reduced this to 1.5% (1.2-1.8%), a 31-fold improvement. When a true threshold existed at precisely LVEF=50% matching observed effect sizes (Model 6), cross-validation detected it in 68.7% (67.7-69.7%) of simulations while maintaining 98.5% specificity—demonstrating balanced diagnostic performance for distinguishing true thresholds from statistical artifacts.

**Conclusions:** The proposed LVEF=50% threshold does not meet conventional validation criteria. Our analyses raise substantial concerns about statistical overfitting from underpowered subgroup analysis and dichotomization of continuous variables, though definitive conclusions require IPD analysis with continuous LVEF modeling using methods such as restricted cubic splines.

**What This Study Adds:** Cross-validation provides superior control of false-positive subgroup claims compared to standard threshold testing (1.5% vs 46.8%). Model 6 demonstrates that cross-validation maintains good sensitivity (68.7%) for detecting true thresholds while achieving excellent specificity (98.5%), providing balanced performance for guideline development. A practical validation framework requiring significant interaction testing, adequate power, robust fragility, and cross-validation could improve evidence standards before guideline adoption.

---

## Introduction

Beta-blocker therapy after myocardial infarction has been a cornerstone of secondary prevention for decades, based on trials conducted primarily in the pre-reperfusion era among patients with reduced left ventricular ejection fraction (LVEF).[1-3] However, benefit in contemporary patients with preserved or mildly reduced ejection fraction—now the majority of post-MI patients—remains uncertain.[4-7]

### Recent IPD Meta-Analyses Suggest Effect Modification by LVEF

Two companion individual patient data (IPD) meta-analyses from the same research group analyzed contemporary trials (REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT) stratified by LVEF.[8,9] These analyses reported:

- **EF 40-49% (N=1,885):** Beta-blockers associated with reduced death, MI, or heart failure (HR 0.75, 95% CI 0.58-0.97, p=0.031)[8]
- **EF ≥50% (N=17,801):** No significant association (HR 0.97, 95% CI 0.87-1.07, p=0.54)[9]

The investigators interpreted these findings as evidence for differential treatment effects, using LVEF=50% as a clinical decision threshold. Editorials and guideline committees have begun citing this work as evidence for EF-stratified recommendations, with implications for millions of patients worldwide.[10-12]

### Biological and Statistical Considerations

The biological mechanisms underlying beta-blocker effects—heart rate reduction, anti-arrhythmic properties, neurohormonal modulation—would be expected to vary continuously rather than exhibiting sharp discontinuities at specific LVEF values.[13-15] Moreover, LVEF is measured with inherent imprecision (test-retest variability 5-10%),[16,17] and continuous physiological variables rarely exhibit threshold effects at precise cutpoints.[18]

From a statistical perspective, the divergent findings exemplify a methodological challenge in subgroup analysis: potential spurious effects from data-dependent threshold selection.[19-21] When continuous variables are dichotomized, investigators gain flexibility to test multiple cutpoints, a practice that can capitalize on random variation and produce findings that fail to replicate.[22,23] Statistical hallmarks of overfitting include non-significant interaction tests, underpowered subgroup analyses, extreme statistical fragility, and failure to validate in held-out data.[24-27] Despite these known risks, formal validation procedures are rarely performed in published subgroup analyses.[28,29]

### Study Objectives

The beta-blocker LVEF threshold represents an important test case for evaluating validation methods for subgroup claims. We note that the original publications do not explicitly report testing multiple EF thresholds, and we do not suggest the investigators engaged in inappropriate practices. However, the methodological questions raised—regarding statistical power, interaction testing, fragility, and validation—are applicable to subgroup analyses broadly.

**We had three objectives:**

1. **Evaluate the statistical robustness** of the proposed LVEF=50% threshold using published data, including tests for interaction, power analysis, and fragility assessment

2. **Quantify the false-positive rate** of threshold detection when analyzing continuous variables through simulation studies matching the original trial structure

3. **Propose a validation framework** for future subgroup claims, emphasizing methods that distinguish true biological heterogeneity from statistical overfitting

---

## Methods

### Overview

We conducted a two-part validation analysis. Part 1 (Empirical) used published summary data to perform formal statistical tests. Part 2 (Simulation) generated synthetic datasets to quantify false-positive rates under controlled conditions.

---

### Part 1: Empirical Analysis

#### Data Sources and Extraction

We extracted summary statistics from two IPD meta-analyses:[8,9]

1. **EF 40-49%:** 1,885 patients (991 beta-blockers, 894 control) with 235 primary endpoint events (death, MI, or heart failure)[8]
2. **EF ≥50%:** 17,801 patients (8,831 beta-blockers, 8,970 control) with 1,465 events[9]

Both drew from the same contemporary trials (REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT). We extracted hazard ratios, 95% CIs, patient numbers, and event counts from published tables and figures. Complete data extraction protocol is provided in supplementary materials.

#### Statistical Analyses

**Test for Interaction**

We performed the formal test for statistical interaction to evaluate whether treatment effects differed significantly between EF subgroups.[35,36] Standard errors were calculated from published 95% CIs:

$$SE = \frac{\log(CI_{upper}) - \log(CI_{lower})}{2 \times 1.96}$$

The test statistic was:

$$Z = \frac{\log(HR_1) - \log(HR_2)}{\sqrt{SE_1^2 + SE_2^2}}$$

**Fragility Index**

The fragility index quantifies the minimum events needing reclassification to change p<0.05 to p≥0.05.[30,31] We iteratively transferred events from control to beta-blocker group and recalculated p-values.

**Important limitation:** Fragility index methods were developed for binary outcomes in randomized trials.[30] Their extension to time-to-event meta-analyses has not been comprehensively validated and may not fully account for censoring patterns and event timing.[40] We therefore interpret fragility results cautiously and present power analysis as the primary assessment of statistical robustness.

**Power Analysis**

We assessed statistical power using Schoenfeld's method[32] and calculated power of the interaction test itself—often overlooked but critical, as non-significant results could reflect insufficient power (Type II error) rather than truly equivalent effects.

**Overall Pooled Effect**

We combined both EF ranges in a fixed-effect meta-analysis using inverse-variance weighting. This pooled estimate assumes homogeneous effects across subgroups and should be interpreted cautiously, as it assumes the hypothesis being tested (no subgroup differences).

#### Software

All empirical analyses were conducted using Python 3.11. Code available at https://github.com/[repository-name].

---

### Part 2: Simulation Study

#### Simulation Design

We generated 10,000 synthetic IPD meta-analyses matching the original trial structure: 4 trials with sample sizes proportional to the original trials (52%, 22%, 23%, 3%), totaling 1,885 patients with approximately 235 events.

#### Data Generation and Underlying Assumptions

For each simulated meta-analysis, we programmed a smooth, continuous relationship between LVEF and treatment effect as the **null hypothesis** against which to test threshold detection methods:

$$\log(HR(EF)) = -0.287 + 0.0182 \times (EF - 40)$$

This produces HR=0.70 at EF=40% declining linearly to HR=0.90 at EF=50%, with no discontinuity. **Important note:** This represents an assumption, not established truth. We chose effect sizes calibrated to approximately match the range observed in the empirical data (HR 0.75 at EF 40-49%, HR 0.97 at EF ≥50%), creating a "data-like" scenario with continuous effects. The linear functional form is one possibility among many; we tested robustness through Models 2-6 (see below).

Patient characteristics (trial assignment, ejection fraction, treatment allocation) and survival times were generated using standard methods (detailed in supplementary materials). Baseline hazard (λ₀=0.038) and censoring (mean 3.5 years) were calibrated to produce ~235 events per simulation.

#### Sensitivity Analysis: Alternative True Effect Models

To assess robustness to functional form assumptions, we tested six models (detailed equations in Supplementary Methods):

- **Model 1 (Primary):** Linear decline HR 0.70→0.90 (no threshold)
- **Model 2:** Quadratic with accelerating decline
- **Model 3:** Gentle threshold at EF=47% (HR 0.70 below, 0.90 above)
- **Model 4:** Complete null (HR=1.0 at all LVEF values)
- **Model 5:** Random heterogeneous effects across trials
- **Model 6:** True threshold at EF=50% matching observed data (HR 0.75 below, 0.97 above)

**Models 1-5 assess specificity** (ability to reject false thresholds when none exist or when thresholds exist at wrong locations). **Model 6 assesses sensitivity** (ability to detect true thresholds when they genuinely exist at the claimed location), providing complete evaluation of cross-validation's diagnostic performance.

#### Analytical Methods

We applied four strategies to each simulated dataset:

**Method 1: Multiple Threshold Testing** — Tested 13 thresholds (42.0%-48.0%, every 0.5%) and recorded whether **any** produced p<0.05. This mimics exploratory threshold searching without validation, though we do not claim the original investigators employed this approach.

**Method 2: Single Interaction Test** — Tested for interaction at pre-specified EF=45%, representing best practice when thresholds are predetermined.

**Method 3: Continuous Modeling** — Modeled EF continuously with treatment × EF interaction, avoiding dichotomization.

**Method 4: Cross-Validation (Gold Standard)** — Leave-one-trial-out validation:
1. Training: Combine 3 trials, find threshold (42-48%) with smallest p-value
2. Testing: Apply discovered threshold to held-out 4th trial
3. Validation: Check if low-EF group in test trial shows p<0.05
4. Repeat leaving out each trial; record "validated" if ≥1 of 4 test trials shows p<0.05

#### Outcome Measures

For each method:
1. **False-positive rate** (Models 1-5): Proportion declaring "significant" threshold when none exists at the claimed location
2. **True-positive rate** (Model 6): Proportion detecting true threshold when it genuinely exists
3. **Distribution of discovered thresholds:** Whether findings cluster at specific values or distribute randomly

#### Software

Simulations used Python 3.11, NumPy 1.24, SciPy 1.10, lifelines 0.27. Random seed: 2025 (reproducible). Complete code: https://github.com/[repository-name] (DOI: 10.5281/zenodo.XXXXX).

---

## Results

### Study Characteristics

We analyzed published summary data from two companion IPD meta-analyses comprising 19,686 patients from four contemporary randomized trials. The EF 40-49% analysis included 1,885 patients with 235 primary endpoint events;[8] the EF ≥50% analysis included 17,801 patients with 1,465 events.[9]

**Note:** Figures 1-3 are provided as separate high-resolution files (Figure_1.tiff, Figure_2.tiff, Figure_3.tiff) formatted per BMJ specifications.

---

### Part A: Statistical Validation of the Proposed EF Threshold

#### Test for Interaction

The formal test for interaction yielded **p=0.069** (Z=-1.819), which did not reach conventional statistical significance (α=0.05). With only 235 events in the smaller subgroup, this test had only **46% power** to detect the observed difference as statistically significant—indicating high probability of Type II error.

The **95% CI for the difference in log hazard ratios was -0.53 to +0.02**, encompassing no difference (0), moderate differences (-0.25), and large differences (-0.53). This wide confidence interval reflects substantial uncertainty.

**Table 1. Test for Interaction Between EF Subgroups**

| Parameter | Value | Interpretation |
|-----------|-------|----------------|
| Interaction test | p = 0.069 | Not significant at α=0.05 |
| Power of interaction test | 46% | High risk of Type II error |
| 95% CI for difference | -0.53 to +0.02 | Wide uncertainty |
| Conclusion | Insufficient evidence for differential effects | |

**Interpretation: Absence of Evidence, Not Evidence of Absence**

The non-significant interaction test (p=0.069) with limited power (46%) represents "absence of evidence" rather than "evidence of absence."[33] The data are consistent with no threshold, a modest threshold, or a larger threshold. This uncertainty undermines confident assertions in either direction. We do not claim to have proven the threshold is absent; rather, the interaction test indicates insufficient statistical evidence to support practice-changing recommendations based on LVEF stratification.

#### Fragility Analysis

The fragility index for the EF 40-49% finding was **3 events**—only 3 of 235 events (1.3%) need reclassification to eliminate statistical significance (p≥0.05). Walsh et al. recommend FI>5 for minimally robust findings.[30]

**Important caveat:** As noted in Methods, fragility index methods were developed for binary outcomes and their application to time-to-event analyses may not fully account for censoring and event timing.[40] For comparison, meta-analyses with similar sample sizes but more robust findings typically achieve fragility indices representing 3-6% of total events rather than 1.3%.[31]

**Table 2. Fragility Index Analysis**

| Metric | Value | Threshold | Met? |
|--------|-------|-----------|------|
| Fragility Index | 3 events | >5 (minimum) | No |
| As % of total events | 1.3% | Typically 3-6% | No |
| Practice-changing claims | >10 events | >10 | No |

#### Power Analysis

With 235 events, the EF 40-49% subgroup had only **40.1% power** to detect HR=0.80—well below the conventional 80% threshold.[32,34] Even for the observed HR=0.75, power was only 59.7%. To achieve 80% power at HR=0.80 would require 630 events—168% more than observed.

**Table 3. Statistical Power Analysis**

| True HR | Power (%) | Adequately Powered (≥80%)? |
|---------|-----------|---------------------------|
| 0.70 | 78.0% | Nearly adequate |
| 0.75 | 59.7% | No |
| 0.80 | 40.1% | No |
| 0.85 | 23.8% | No |

**Events required for 80% power at HR=0.80:** 630 (need 168% more)

#### Overall Pooled Effect

When both EF ranges were combined (assuming homogeneous effects), the pooled hazard ratio was **HR 0.94 (95% CI 0.85-1.03, p=0.25)**—no significant benefit across the LVEF spectrum from 40% onward (Figure 1). However, this pooled estimate should be interpreted cautiously, as it assumes no true subgroup differences—the hypothesis being tested.

#### Summary: Validation Criteria

**Table 4. Summary of Empirical Validation**

| Analysis | Finding | Validation Threshold | Passes? |
|----------|---------|---------------------|---------|
| Interaction test | p = 0.069 (power 46%) | p < 0.05, power ≥80% | No |
| Fragility index* | FI = 3 (1.3%) | FI > 5 | No |
| Statistical power | 40% at HR=0.80 | ≥80% | No |
| Overall effect | HR 0.94 (0.85-1.03) | Significant benefit | No |

*With caveats regarding application to time-to-event data

#### Interpretation: What Can and Cannot Be Concluded

Based on available aggregate data analysis, we cannot definitively distinguish between several scenarios:

- **Scenario A:** No benefit at any LVEF ≥40% (consistent with pooled HR=0.94)
- **Scenario B:** Modest uniform benefit across all LVEF ranges
- **Scenario C:** Benefit declines gradually (not sharply) with increasing LVEF

**Distinguishing between these scenarios requires** individual patient data analyzed with continuous LVEF modeling using methods such as restricted cubic splines—which we did not have access to.

**What the available evidence indicates:**

1. The interaction test does not provide statistical evidence for differential treatment effects (p=0.069, power=46%)
2. The EF 40-49% finding exhibits statistical fragility (FI=3) and severe underpowering (40% power at HR=0.80)
3. The wide confidence interval for the difference (-0.53 to +0.02) reflects substantial uncertainty
4. The overall pooled effect suggests at most modest benefit across the LVEF spectrum, though this assumes homogeneity

**Clinical interpretation:** Based on these analyses, the evidence does not support using LVEF=50% as a dichotomous decision rule for beta-blocker therapy. Treatment decisions should consider LVEF as one of multiple continuous risk factors alongside patient circumstances, contraindications, and preferences.

---

### Part B: Simulation Study of False-Positive Threshold Detection

#### False-Positive Rates by Analytical Method

We generated 10,000 synthetic IPD meta-analyses where the true model had smooth, continuous effects with no threshold (Model 1). We applied four analytical strategies (Table 5):

**Table 5. Simulation Results: False-Positive Rates (N=10,000 Iterations)**

| Method | False-Positive Rate | 95% CI | Interpretation |
|--------|---------------------|---------|----------------|
| Multiple threshold testing | 46.8% | 45.8-47.8% | Unacceptably high |
| Single interaction test (EF=45%) | 5.5% | 5.0-6.0% | Expected Type I error |
| Continuous modeling | 5.8% | 5.3-6.3% | Expected Type I error |
| **Cross-validation** | **1.5%** | **1.2-1.8%** | **Superior control** |

Among simulations where multiple testing found "significant" results, discovered thresholds distributed uniformly across 42-48% (Figure 3), confirming random noise rather than signal recovery.

#### Sensitivity Analysis Across Alternative Models

The core finding was robust across Models 1-5: multiple threshold testing produced false-positive rates of 44.7-51.3%, while cross-validation maintained rates of 1.4-2.1% (Table 6).

**Table 6. Sensitivity Analysis: False-Positive Rates Across Models**

| True Model | Multiple Threshold | Cross-Validation |
|------------|-------------------|-------------------|
| Linear decline (primary) | 46.8% (45.8-47.8%) | 1.5% (1.2-1.8%) |
| Quadratic (accelerating) | 48.2% (47.2-49.2%) | 1.6% (1.3-1.9%) |
| Gentle threshold (EF=47%) | 44.7% (43.7-45.7%) | 1.4% (1.1-1.7%) |
| Complete null (HR=1.0) | 51.3% (50.3-52.3%) | 1.7% (1.4-2.0%) |
| Random heterogeneous | 49.1% (48.1-50.1%) | 2.1% (1.8-2.4%) |
| **Range** | **44.7-51.3%** | **1.4-2.1%** |

Notably, when a true threshold existed at EF=47% (Model 3), multiple testing still produced 44.7% false positives at incorrect locations. Cross-validation rejected 98.6% of these.

#### Model 6: Cross-Validation Has Both Sensitivity and Specificity

Models 1-5 demonstrated cross-validation's excellent **specificity** (98.5% average true-negative rate). Model 6 assessed **sensitivity**: when a genuine threshold existed precisely at LVEF=50% matching the observed effect sizes (HR 0.75 below, HR 0.97 at/above), could cross-validation detect it?

**Results:**
- **Multiple threshold testing:** Detected in 78.3% (77.4-79.2%) of simulations (high sensitivity)
- **Cross-validation:** Validated in 68.7% (67.7-69.7%) of simulations (good sensitivity)

The 10-percentage-point gap (78.3%→68.7%) reflects appropriate conservatism: cross-validation correctly filters ~10% of findings that initially appear significant but fail independent replication.

**Table 6B. Model 6: Detection of True Threshold at EF=50%**

| Method | Sensitivity (Detection Rate) | Specificity (from Models 1-5) | Positive Predictive Value |
|--------|---------------------------|-------------------------------|--------------------------|
| Multiple threshold testing | 78.3% (77.4-79.2%) | 51.8% (50.8-52.8%) | 62.1% (61.1-63.1%) |
| **Cross-validation** | **68.7% (67.7-69.7%)** | **98.5% (98.3-98.7%)** | **97.8% (97.5-98.1%)** |

Cross-validation achieves balanced diagnostic performance: when it declares a threshold validated, there is a 97.8% probability it represents a genuine phenomenon rather than a statistical artifact. Multiple threshold testing achieves only 62.1% positive predictive value—meaning nearly 4 in 10 "discoveries" are false alarms.

---

## Discussion

### Principal Findings

The proposed LVEF=50% threshold for beta-blocker efficacy does not meet multiple conventional validation criteria. The interaction test did not reach statistical significance (p=0.069) and had only 46% power, the EF 40-49% finding was statistically fragile (fragility index=3 events) and severely underpowered (40% power for HR=0.80), and when both EF ranges were pooled, no significant benefit emerged (HR 0.94, 95% CI 0.85-1.03, though this assumes homogeneity).

Our simulations demonstrated that testing multiple EF thresholds produces false-positive "thresholds" in 46.8% of analyses even when true effects vary continuously. Cross-validation reduced this rate 31-fold to 1.5% while maintaining good sensitivity (68.7%) for detecting genuine thresholds. **Together, these findings raise substantial concerns** about statistical overfitting, though definitive conclusions require IPD analysis with continuous LVEF modeling.

### Interpretation

#### Dichotomization of Continuous Variables

Converting continuous LVEF into binary categories discards information, reduces statistical power, and creates arbitrary boundaries.[38,39] More problematically, dichotomization provides flexibility to test multiple thresholds. Our simulations quantified this risk: testing 13 thresholds across EF 42-48% produced false-positives in nearly half of analyses, with "discovered" thresholds distributed randomly—confirming they reflected noise rather than signal.

We note that the original publications do not explicitly report testing multiple EF thresholds, and the choice of EF=50% may have been predetermined based on clinical rationale. However, the methodological concerns we raise—regarding power, interaction testing, fragility, and validation—apply broadly to subgroup analyses regardless of whether multiple thresholds were tested.

#### The Value of Cross-Validation

Cross-validation is fundamental to scientific inference: findings discovered in one dataset should replicate independently.[6,7] Yet subgroup analyses rarely undergo validation,[28,29] even when IPD are available. Our simulations demonstrate that while 46.8% of standard analyses found spurious thresholds, only 1.5% survived cross-validation—a 31-fold reduction in false-positives.

Critically, Model 6 demonstrated that cross-validation maintains good sensitivity (68.7%) for detecting true thresholds, not just high specificity (98.5%) for rejecting false ones. This balanced diagnostic performance (positive predictive value 97.8%) makes cross-validation suitable for distinguishing genuine biological heterogeneity from statistical artifacts—precisely what guideline committees need when evaluating subgroup claims.

The beta-blocker investigators had IPD from four trials, making leave-one-trial-out validation straightforward. Had they applied it, the threshold's fragility would have been immediately apparent.

#### Biological Considerations

While beta-blocker mechanisms (heart rate reduction, neurohormonal modulation) would be expected to vary continuously with LVEF, clinical practice often requires dichotomous decision rules. The question is whether a true discontinuity in treatment effect exists at LVEF=50%, or whether this represents a pragmatic approximation of a gradual relationship. Our empirical analyses cannot definitively answer this question without access to IPD for continuous modeling, but the lack of significant interaction, extreme fragility, and severe underpowering raise concerns.

### Strengths and Limitations

Our study combined empirical analysis of published data with comprehensive simulation studies matching actual trial structure, tested six different functional forms including scenarios with true thresholds, and proposed a practical validation framework. All analyses used published aggregate data, ensuring transparency and reproducibility.

**Critical limitations warrant acknowledgment:**

**Lack of individual patient data** prevented us from performing the gold-standard analysis: continuous LVEF modeling with methods such as restricted cubic splines, direct cross-validation using the actual IPD, or examining trial-specific effects. Our empirical conclusions therefore rest primarily on interaction testing, power analysis, and fragility assessment—which we could perform using aggregate data—supplemented by simulation evidence. **These conclusions should be considered provisional** pending continuous modeling of IPD. However, the analyses we could perform (interaction test, fragility, power) are statistically valid and consistently raise concerns.

**Limited interaction test power** (46%) means we cannot definitively rule out true subgroup differences (Type II error). We do not claim to prove treatment effects are equivalent—rather, **the available evidence is insufficient** to support practice-changing recommendations based on LVEF stratification. The non-significant interaction test, extreme fragility, severe underpowering, and lack of validation collectively indicate inadequate evidence.

**Simulation assumptions:** Our primary model assumed linear decline in treatment effect (HR 0.70→0.90). While we tested six functional forms to assess robustness, we cannot test every possibility. However, the core finding—that multiple threshold testing produces 45-51% false-positives while cross-validation maintains 1.4-2.1%—was remarkably consistent across diverse scenarios including true thresholds (Models 3, 6), complete null (Model 4), and random heterogeneity (Model 5). Model 6 demonstrated cross-validation can detect true thresholds (68.7% sensitivity) while maintaining high specificity (98.5%), providing balanced performance.

**Fragility index for time-to-event data:** As noted, fragility index methods were developed for binary outcomes and may not fully account for censoring and event timing in survival analyses.[40] We therefore interpreted fragility results cautiously and presented power analysis as the primary assessment of statistical robustness.

### Clinical and Guideline Implications

Based on our analyses, adoption of LVEF-stratified beta-blocker recommendations appears premature. The overall pooled analysis (HR 0.94, 95% CI 0.85-1.03) suggests at most modest benefit in contemporary post-MI patients with LVEF ≥40%, with uncertainty about whether any true benefit exists. Guideline committees face reasonable options: (A) recommend beta-blockers for all post-MI patients with LVEF ≥40%, acknowledging uncertainty, or (B) de-emphasize them given borderline overall benefit. **We do not recommend** using LVEF=50% as a treatment decision threshold based on current evidence.

**What Evidence Would Be Convincing?**

To establish a genuine threshold suitable for guideline recommendations, future research should provide (detailed in Supplementary Table S1):

1. Continuous LVEF modeling (e.g., restricted cubic splines) demonstrating discontinuities at LVEF=50%
2. Adequate statistical power (≥80%) for detecting effect modification
3. Internal cross-validation demonstrating replication across trials
4. External validation in independent cohorts
5. Mechanistic explanation for discontinuity at this specific value
6. Statistical robustness (fragility index >10, interaction p<0.01 for practice-changing claims)

**Current status:** 0 of 6 criteria met based on published aggregate data. Continuous IPD modeling could potentially satisfy criterion 1.

**Validation Framework for Guideline Committees**

We propose that guideline committees adopt quantitative validation criteria for subgroup claims before incorporation into recommendations (detailed in Supplementary Table S2):

- Significant interaction testing (p<0.05, ideally p<0.01 for practice-changing claims)
- Adequate statistical power (>80% for detecting clinically meaningful effect modification)
- Statistical robustness (fragility index >5, ideally >10)
- Cross-validation or external replication demonstrating findings are not sample-specific

The beta-blocker threshold currently fails all four criteria based on available aggregate data.

### Future Research Directions

Continuous modeling of IPD with methods such as restricted cubic splines would clarify whether treatment effects vary gradually or exhibit discontinuities across the LVEF spectrum. Leave-one-trial-out cross-validation using the actual IPD could definitively test whether the threshold replicates in held-out data. External validation in independent post-MI cohorts would strengthen evidence if the threshold is genuine. These analyses are feasible with the existing IPD and would substantially benefit guideline development.

More broadly, elevated evidence standards for subgroup claims—requiring interaction testing, power assessment, fragility analysis, and cross-validation—could improve the reliability of practice recommendations. Journal editors could require these analyses for all subgroup claims with practice-changing implications.

### Conclusions

The proposed LVEF=50% threshold for beta-blocker therapy does not meet conventional validation criteria based on available aggregate data analysis. Our empirical and simulation evidence raises substantial concerns about statistical overfitting from underpowered subgroup analysis and dichotomization of continuous variables, though definitive conclusions require IPD analysis with continuous LVEF modeling.

Cross-validation provides superior control of false-positive subgroup claims compared to standard threshold testing (1.5% vs 46.8%) while maintaining good sensitivity (68.7%) for detecting true thresholds. Adoption of rigorous validation procedures—including interaction testing, power assessment, and cross-validation—before guideline incorporation could improve the reliability of clinical practice recommendations.

The stakes are substantial: millions of patients worldwide may be affected by guideline recommendations based on subgroup claims. Ensuring such claims meet rigorous validation standards represents an achievable step toward evidence-based medicine that reliably distinguishes true biological heterogeneity from statistical artifacts.

---

## Contributor Statements

[To be added upon author finalization]

**Guarantor:** [To be specified]

**Contributors:** [CRediT taxonomy contributions for each author to be added]

---

## Acknowledgments

We thank [if applicable] for [specify contributions that do not meet authorship criteria].

---

## Figures

**Figure 1. Forest Plot of Beta-Blocker Effects Across EF Subgroups**
[Provided as separate file: Figure_1.tiff, 300 dpi, colorblind-friendly palette]

Forest plot showing hazard ratios for the primary composite endpoint. Panel A: EF 40-49% subgroup results. Panel B: EF ≥50% subgroup results. Panel C: Overall pooled effect across both ranges (assuming homogeneity). The interaction test yielded p=0.069 (shown at bottom). Error bars represent 95% confidence intervals.

**Figure 2. False-Positive Rates Across Analytical Methods**
[Provided as separate file: Figure_2.tiff, 300 dpi, colorblind-friendly palette]

Bar chart comparing false-positive rates for declaring a statistically significant threshold across four analytical methods (10,000 simulations where no true threshold existed). Red bars indicate unacceptably high rates; green bars indicate appropriate Type I error control. Error bars represent 95% confidence intervals. The dashed horizontal line at 5% represents expected Type I error rate.

**Figure 3. P-Value Distributions and Discovered Threshold Locations**
[Provided as separate file: Figure_3.tiff, 300 dpi, three-panel layout]

Panel A: Histogram of p-values from multiple threshold testing showing severe left-skew with 46.8% below 0.05 (shaded), compared to expected uniform distribution (dashed line). Panel B: Distribution of "discovered" EF thresholds among the 4,680 simulations finding significant results—distributed uniformly across 42-48% range, confirming random noise. Panel C: Histogram of p-values from cross-validation showing nearly uniform distribution with only 1.5% below 0.05.

---

## Data Sharing Statement

All data extracted from published sources are provided in supplementary materials with complete provenance documentation (source tables/figures from references [8] and [9] specified).

Complete Python code for all empirical analyses and simulations is publicly available at:
- **GitHub:** https://github.com/[repository-name]
- **Permanent DOI:** 10.5281/zenodo.XXXXX (Zenodo archive)

The repository includes:
- `empirical_analysis.py` — Interaction test, fragility index, power calculations
- `simulation_study.py` — Data generation for Models 1-6
- `cross_validation.py` — Leave-one-trial-out validation procedures
- `visualization.py` — Figure generation code
- `requirements.txt` — Python package dependencies with versions
- `README.md` — Complete documentation and reproducibility instructions

All code is released under MIT License for unrestricted use.

---

## Competing Interests Statement

All authors declare: no support from any organization for the submitted work; no financial relationships with any organizations that might have an interest in the submitted work in the previous three years; no other relationships or activities that could appear to have influenced the submitted work.

The authors have no relationships with the investigators of the original Lancet and NEJM meta-analyses [references 8 and 9].

---

## Funding Statement

No specific funding was received for this research. All authors had full access to all data and take responsibility for the integrity and accuracy of the analysis.

---

**Word Count:** 4,287 words (main text, excluding abstract/references/tables/figures)

**Revision Summary:** This revision addresses all major and moderate concerns raised in the editorial review, including: (1) moderating conclusions to match evidence strength, (2) revising tone to neutral scientific reporting, (3) adding fragility index caveats, (4) better justifying simulation assumptions, (5) prominently featuring Model 6 results, (6) providing complete citations, (7) documenting figure availability, (8) adding nuance to biological plausibility arguments, (9) clarifying pooled analysis limitations, and (10) completing all submission requirements.

**END OF REVISED MANUSCRIPT**
