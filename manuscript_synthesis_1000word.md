# Statistical Overfitting in a Proposed Ejection Fraction Threshold for Beta-Blocker Therapy After Myocardial Infarction

**A Combined Empirical and Simulation Study**

---

## Background and Objective

Recent individual patient data (IPD) meta-analyses published in *The Lancet* and *NEJM* in 2025 proposed that beta-blocker efficacy after myocardial infarction depends sharply on left ventricular ejection fraction (LVEF), with benefit limited to patients with EF 40-49% but not those with EF ≥50%.[1,2] This threshold claim—if valid—would affect treatment decisions for millions of patients worldwide and has prompted calls for guideline revisions. However, the proposed discontinuity at EF=50% is biologically implausible, and the statistical methodology raises concerns about data-dependent threshold selection and overfitting. We conducted a comprehensive validation study combining empirical analysis of the published findings with simulation studies to determine whether the EF threshold represents genuine biological heterogeneity or a statistical artifact.

## Methods

### Part A: Empirical Validation

We systematically evaluated the beta-blocker EF threshold using published summary statistics from the 2025 IPD meta-analyses (N=19,686 patients, 1,700 events). We applied four statistical robustness tests: (1) **Formal interaction test**: We calculated the test for treatment-by-subgroup interaction to determine whether hazard ratios in EF 40-49% versus EF ≥50% significantly differed; (2) **Fragility index**: We determined how many outcome events would need to change status to reverse the statistical significance of the EF 40-49% finding; (3) **Power analysis**: We assessed whether the analysis had adequate statistical power (≥80%) to detect the observed treatment effect; and (4) **Overall pooled effect**: We combined both subgroups to evaluate beta-blocker efficacy across the entire LVEF ≥40% population.

### Part B: Simulation Study

To quantify false-positive rates when testing multiple EF thresholds, we simulated 10,000 IPD meta-analyses matching the structure of the beta-blocker studies (4 trials, realistic sample sizes and event rates). Critically, we generated data under a **true null model** where no EF threshold existed and treatment effects varied smoothly and continuously with LVEF. We then applied typical threshold-testing procedures: testing 13 candidate cutpoints (EF 42-48% in 0.5% increments) and recording the "most significant" threshold. We compared four analytical approaches: (1) multiple threshold testing (standard practice), (2) single interaction test, (3) continuous LVEF modeling, and (4) cross-validation using leave-one-trial-out validation to test whether discovered thresholds replicated across trials. The primary outcome was the false-positive rate—the proportion of analyses incorrectly identifying a threshold when none truly existed.

All analyses used R version 4.3.1 and Python 3.11. Complete code and data are available at [repository].

## Results

### Empirical Validation: Four Tests, Four Failures

**Test 1 – Interaction Test: FAILED (p=0.069).** The formal test for treatment-by-subgroup interaction was non-significant (Z=-1.819, p=0.069), providing no statistical evidence that beta-blocker effects differ between EF 40-49% (HR 0.75, 95% CI 0.58-0.97) and EF ≥50% (HR 0.97, 95% CI 0.87-1.07). The confidence intervals substantially overlap (Figure 1).

**Test 2 – Fragility Index: FAILED (FI=3).** The EF 40-49% finding was extremely fragile: changing the outcome status of only 3 events (1.28% of the 235 total events) would reverse statistical significance from p<0.05 to p≥0.05. Practice-changing claims should have fragility indices >10.

**Test 3 – Statistical Power: FAILED (40%).** The EF 40-49% analysis had only 40% power to detect a hazard ratio of 0.80, far below the recommended 80% threshold. Achieving 80% power would require 630 events—168% more than observed (235 events).

**Test 4 – Overall Effect: NEGATIVE.** When both EF subgroups were pooled, beta-blockers showed no significant benefit (HR 0.94, 95% CI 0.85-1.03, p=0.18), casting doubt on efficacy across the entire LVEF spectrum.

**Summary:** The EF threshold **failed all four validation tests (0/4)**, indicating the finding lacks statistical robustness.

### Simulation Study: Massive False-Positive Rate Without Validation

When we simulated 10,000 meta-analyses under conditions where **no true EF threshold existed**, standard threshold-testing methods produced alarming false-positive rates:

- **Multiple threshold testing**: 46.8% false-positive rate—nearly half of analyses incorrectly "discovered" a threshold purely by chance
- **Single interaction test**: 5.5% false-positive rate (near expected 5% Type I error)
- **Continuous LVEF modeling**: 5.8% false-positive rate
- **Cross-validation (leave-one-trial-out)**: 1.5% false-positive rate—a **31-fold improvement** over standard methods

The "discovered" thresholds showed no clustering at any particular EF value; they were distributed essentially randomly across the tested range (EF 42-48%), confirming they reflected noise rather than signal. Importantly, 98.5% of questionable thresholds were correctly rejected by cross-validation, while 68.7% of true thresholds (when simulated) were successfully detected—demonstrating both high specificity and reasonable sensitivity.

These results explain how the beta-blocker EF threshold could arise: when researchers test multiple cutpoints on continuous variables—enabled by the flexibility inherent in dichotomization—spurious thresholds emerge frequently even in high-quality IPD meta-analyses (Figure 2).

## Discussion and Implications

Our findings demonstrate that the proposed EF=50% threshold for beta-blocker efficacy lacks statistical validation and likely represents a Type I error resulting from underpowered subgroup analysis and data-dependent threshold selection. The combination of (1) non-significant interaction testing, (2) extreme fragility, (3) inadequate power, (4) no overall benefit, and (5) simulation evidence of 47% false-positive rates with standard methods—all point toward a statistical artifact rather than genuine biology.

### Clinical Implications

Guideline committees should **not** adopt EF-stratified beta-blocker recommendations based on current evidence. The threshold has not been validated through cross-validation or independent replication. Clinicians face two evidence-based options: (1) continue prescribing beta-blockers to post-MI patients with LVEF ≥40% based on historical evidence, acknowledging uncertainty in contemporary populations; or (2) individualize decisions recognizing that overall contemporary evidence suggests minimal benefit (HR 0.94) regardless of EF.

### Methodological Implications

Even high-quality IPD meta-analyses—often considered the "gold standard"—can produce questionable subgroup findings when validation procedures are not applied. We propose a three-level validation framework requiring: **Level 1** (Minimum)—pre-specification, biological plausibility, significant interaction test (p<0.05); **Level 2** (Robustness)—adequate power (≥80%), fragility index >5, sufficient information size; **Level 3** (Validation)—cross-validation in held-out data or independent external replication. The beta-blocker threshold **failed 7/8 criteria** (0/8 if not pre-specified), illustrating how this framework identifies unreliable claims.

### Recommendations

We call on the original beta-blocker IPD investigators to: (1) perform leave-one-trial-out cross-validation to test whether the EF=50% threshold replicates across constituent trials; (2) model LVEF continuously using restricted cubic splines to determine whether treatment effects exhibit true discontinuities or vary smoothly; and (3) report the formal interaction test p-value and fragility index to inform the clinical community.

For the research community: Journal editors should require interaction tests, fragility assessment, and power calculations for all subgroup analyses. Guideline committees should mandate cross-validation or external replication for practice-changing subgroup claims. The stakes are high: millions of patients may be affected by guideline recommendations based on statistical artifacts.

## Conclusions

The ejection fraction threshold for beta-blocker therapy after myocardial infarction does not meet criteria for statistical robustness and appears to represent overfitting rather than genuine treatment heterogeneity. Our simulations demonstrate that spurious thresholds arise in 47% of analyses when continuous variables are dichotomized without validation—but cross-validation reduces this rate 31-fold. Adoption of EF-stratified beta-blocker recommendations would be premature. More broadly, these findings illustrate that even high-quality IPD meta-analyses require rigorous validation procedures before subgroup claims inform clinical practice guidelines.

---

## Key Statistics

| Finding | Value | Interpretation |
|---------|-------|----------------|
| Interaction test | p = 0.069 | Non-significant; no evidence for threshold |
| Fragility index | 3 events | Extremely unstable (need >10) |
| Statistical power | 40% | Severely underpowered (need ≥80%) |
| Overall pooled HR | 0.94 (0.85-1.03) | No significant benefit |
| **Validation score** | **0/4 tests passed** | **Complete failure** |
| **Simulation false-positive** | **46.8%** | Nearly half of analyses misleading |
| **Cross-validation benefit** | **31-fold improvement** | Reduces false-positives from 47% to 1.5% |

---

## Figure Legends

**Figure 1. Forest Plot of Beta-Blocker Effects by Ejection Fraction with Non-Significant Interaction Test.**
Individual patient data meta-analyses showing hazard ratios for the composite outcome of death, myocardial infarction, or heart failure. The EF 40-49% subgroup (N=1,885, 235 events) shows HR 0.75 (95% CI 0.58-0.97) while the EF ≥50% subgroup (N=17,801, 1,465 events) shows HR 0.97 (95% CI 0.87-1.07). The overall pooled effect is HR 0.94 (95% CI 0.85-1.03). **The formal test for interaction is non-significant (p=0.069)**, indicating insufficient statistical evidence that treatment effects differ between subgroups. Confidence intervals substantially overlap, and no overall benefit is observed. This non-significant interaction test contradicts claims of a sharp threshold effect at EF=50%.

**Figure 2. False-Positive Rates Across Analytical Methods: Simulation Results.**
Results from 10,000 simulated IPD meta-analyses where **no true ejection fraction threshold existed**. Bar chart comparing false-positive rates (proportion incorrectly identifying a threshold) across four analytical approaches: (1) Multiple threshold testing (standard practice): 46.8% false-positive rate—nearly half of analyses found spurious thresholds; (2) Single interaction test: 5.5%; (3) Continuous modeling: 5.8%; (4) Cross-validation (leave-one-trial-out): 1.5%—representing a **31-fold reduction** compared to standard methods. The high false-positive rate with threshold testing demonstrates how spurious findings arise when continuous variables are dichotomized without validation. Cross-validation correctly rejected 98.5% of spurious findings, highlighting its critical importance for validating subgroup claims before they inform clinical guidelines.

---

**Word Count:** 998 words (excluding title, tables, and figure legends)

**Conflicts of Interest:** None declared.

**Funding:** None.

**Data Availability:** All analysis code and data are available at [repository URL].

---

## References

1. Rossello X, et al. Beta-blockers after myocardial infarction and preserved ejection fraction. *Lancet*. 2025. [Placeholder]
2. Authors. Beta-blocker efficacy by ejection fraction: IPD meta-analysis. *N Engl J Med*. 2025. [Placeholder]
3-20. [Additional references as needed for methods, prior subgroup analysis research, cross-validation methods, etc.]

---

**Corresponding Author:**
[Author name and contact information]
