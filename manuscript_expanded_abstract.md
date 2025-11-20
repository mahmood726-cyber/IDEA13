# Beta-Blockers After Myocardial Infarction: A Three-Part Validation Analysis of Subgroup Claims and Observational Evidence

## Abstract

**Background:** Recent individual-patient data (IPD) meta-analyses published in *The Lancet* and *NEJM* suggest beta-blockers benefit post-myocardial infarction patients with left ventricular ejection fraction (LVEF) 40-49% (hazard ratio [HR] 0.75, 95% CI 0.58-0.97, p=0.031) but not those with LVEF ≥50% (HR 0.97, 95% CI 0.87-1.07, p=0.54), leading to calls for ejection fraction-stratified treatment guidelines. Concurrently, large observational meta-analyses (N=67,388) suggest beta-blockers reduce mortality in heart failure with preserved ejection fraction (HFpEF) with highly significant p-values (p<0.001), while pooled RCT data (N=9,000) show no significant benefit (HR 0.96, p=0.39). We evaluated the statistical robustness of both claims using a comprehensive three-part validation framework.

**Methods:**

**Part 1 (EF Threshold Validation):** Using published data from both RCT meta-analyses (N=19,686 patients, 1,700 events), we calculated the formal test for statistical interaction between EF subgroups, assessed statistical power and fragility of the EF 40-49% finding, and determined the overall pooled treatment effect.

**Part 2 (Simulation Study):** We generated 10,000 synthetic IPD meta-analyses matching the original trial structure, with a true continuous decline in beta-blocker effect as LVEF increases (no sharp threshold). We quantified false-positive rates when applying standard dichotomization methods versus cross-validation approaches.

**Part 3 (Observational Evidence Forensics):** We applied a novel three-component bias decomposition framework to compare observational (N=67,388) vs. RCT (N=9,000) evidence for beta-blockers in HFpEF: (1) **Discordance Index**—standardized measure of observational-RCT disagreement; (2) **E-Value**—quantifying vulnerability to unmeasured confounding; (3) **Inflation Factor**—using Bayesian meta-analytic predictive priors (RBesT) to calculate effective sample size (ESS), revealing the degree of "information inflation" when nominal sample sizes are cited.

**Results:**

*Part 1 - EF Threshold Analysis:* The test for interaction between EF subgroups was non-significant (p=0.069), providing no statistical evidence for different treatment effects. The EF 40-49% subgroup analysis was severely underpowered (235 events; 40% power to detect HR 0.80) and extremely fragile (fragility index=3 events, representing only 1.3% of total events). When both EF ranges were pooled, the overall HR was 0.94 (95% CI 0.85-1.03), indicating no significant benefit across the entire EF spectrum.

*Part 2 - Simulation Study:* When testing multiple EF thresholds in data with smooth, continuous effects (no true threshold), standard dichotomization methods produced questionable "significant" thresholds in 46.8% of simulations. In contrast, cross-validation correctly rejected false thresholds in 98.5% of cases, representing a 31-fold reduction in false-positive rates. When a true threshold existed (Model 6), cross-validation detected it in 68.7% of cases, demonstrating both excellent specificity (98.5%) and good sensitivity (68.7%).

*Part 3 - Observational Evidence Forensics:*
- **Observational pooled HR:** 0.91 (95% CI: 0.87-0.95, p<0.001) [Appears definitive]
- **RCT pooled HR:** 0.96 (95% CI: 0.88-1.05, p=0.39) [Null effect]
- **Discordance Index:** 1.3 (low discordance; effect sizes agree)
- **E-Value:** 1.36 (weak confounding could explain result; fragile)
- **Bayesian Effective Sample Size:** 1,988 patients (from nominal N=67,388)
- **Inflation Factor:** 41× (observational data contains only 2.4% of its nominal information content)

**Key Finding:** Effect sizes agree between observational (HR 0.91) and RCT (HR 0.96) data, but observational data appear **falsely precise** due to massive sample size. The observational p<0.001 reflects the "Nominal Sample Size Fallacy"—67,388 enrolled patients contain the statistical information equivalent of only ~2,000 RCT patients when accounting for heterogeneity and residual confounding. This creates misleading statistical significance despite insufficient evidence for benefit.

**Conclusions:**

**For EF Thresholds:** The proposed LVEF 50% threshold has not been adequately validated and may reflect statistical overfitting from underpowered subgroup analysis and dichotomization of a continuous variable. The non-significant interaction test (p=0.069), extreme statistical fragility (FI=3), and high false-positive rates from dichotomization (46.8%) indicate insufficient evidence to support this threshold for guideline development.

**For Observational Evidence:** The beta-blockers-HFpEF case exemplifies "false precision"—where observational and RCT effect sizes agree (DI=1.3) but observational data inflate certainty through massive nominal sample sizes. With 41× information inflation (ESS=1,988 vs. nominal N=67,388), the observational p<0.001 is misleading. RCT confidence intervals should be used for inference, not observational p-values.

**Implications:** This analysis demonstrates how high-quality meta-analyses—whether IPD meta-analyses of RCTs or large observational registries—can produce questionable findings through: (1) subgroup overfitting when continuous variables are dichotomized without validation, and (2) false precision when nominal sample sizes are cited without adjusting for heterogeneity and confounding. We propose a validation framework requiring: (a) significant interaction testing (p<0.05), (b) adequate statistical power (>80%), (c) fragility index >5, (d) cross-validation of threshold claims, and (e) Bayesian ESS reporting for observational data when compared to RCTs. Adoption of EF-stratified or registry-based beta-blocker recommendations would be premature based on current evidence.

---

**Word Count:** 649 words
**Keywords:** subgroup analysis, overfitting, beta-blockers, myocardial infarction, observational studies, Bayesian statistics, effective sample size, cross-validation, medical reversals

---

## Key Metrics Summary Table

| Domain | Finding | Statistical Issue | Metric Value |
|--------|---------|-------------------|--------------|
| **EF Threshold (RCTs)** | HR 0.75 vs 0.97 | Subgroup overfitting | FI=3, Power=40%, DI (int)=p0.069 |
| **Threshold Testing** | 46.8% false-positive | Dichotomization bias | CV reduces to 1.5% (31×) |
| **Obs vs RCT (HFpEF)** | HR 0.91 vs 0.96 | False precision | Inflation: 41×, ESS: 2.4% |

---

## Three-Part Validation Framework

| Validation Component | Pass Criteria | EF Threshold Status | Obs Evidence Status |
|---------------------|---------------|---------------------|---------------------|
| **Statistical significance** | Interaction p<0.05 | ❌ Failed (p=0.069) | ✓ Passed (p<0.001)* |
| **Adequate power** | Power >80% | ❌ Failed (40%) | N/A |
| **Statistical robustness** | FI >5 | ❌ Failed (FI=3) | ❌ Failed (E-Val=1.36) |
| **Validation/Replication** | Cross-validation | ⚠️ Not performed | ⚠️ RCT disagrees |
| **Information content** | N/A for RCTs | N/A | ❌ Failed (Inflation 41×) |
| **Overall Assessment** | | **Questionable** | **False Precision** |

*But effect size small (HR 0.91) and inflated precision masks uncertainty

---

## Clinical Bottom Line

**Question 1:** Should beta-blockers be given based on ejection fraction thresholds after MI?

**Answer:** No. The claimed EF 50% threshold appears to be a statistical artifact (p_interaction=0.069, FI=3, 46.8% false-positive rate in simulations).

**Question 2:** Should large observational meta-analyses guide beta-blocker use in HFpEF?

**Answer:** No. Despite N=67,388 and p<0.001, observational data contain only 2.4% of nominal information (ESS=1,988). RCT confidence intervals (HR 0.96, CI 0.88-1.05) should be used for inference, indicating insufficient evidence for benefit.

**Bottom Line:** Neither EF-stratified RCT subgroups nor observational registries currently support beta-blocker recommendations for contemporary post-MI patients with preserved or mildly reduced EF. Treatment decisions should be individualized without relying on EF thresholds or inflated observational precision.
