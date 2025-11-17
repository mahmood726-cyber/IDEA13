# Discussion

## Principal Findings

In this comprehensive validation study, we found that the proposed ejection fraction threshold for beta-blocker efficacy after myocardial infarction fails multiple statistical robustness tests. The formal test for interaction between the EF 40-49% and EF ≥50% subgroups was non-significant (p=0.069), providing no statistical evidence that treatment effects differ between these ranges. The EF 40-49% finding was extremely fragile (fragility index=3 events, only 1.3% of the total), severely underpowered (40% power for detecting HR 0.80), and based on insufficient cumulative information. When both EF ranges were pooled, no significant benefit of beta-blockers emerged (HR 0.94, 95% CI 0.85-1.03).

Our simulation study demonstrated why such spurious thresholds arise. When researchers test multiple EF cutpoints—a practice enabled by the flexibility of dichotomizing continuous variables—false-positive "thresholds" emerge in 46.8% of analyses even when no true threshold exists. Cross-validation reduced this rate 31-fold to 1.5%, highlighting the critical importance of validation procedures that are rarely applied in practice.

Together, these findings strongly suggest that the EF=50% threshold is a statistical artifact resulting from underpowered subgroup analysis and data-dependent threshold selection, not evidence of a true biological discontinuity.

## Interpretation in Context

### The Perils of Dichotomizing Continuous Variables

The hazards of dichotomizing continuous variables have been recognized for decades.[37,38] Converting a continuous measure like ejection fraction into binary categories (above/below 50%) discards information, reduces statistical power, and creates arbitrary boundaries that are biologically implausible.[39,40] Perhaps most dangerously, dichotomization provides investigators with substantial flexibility to test multiple thresholds until a "significant" result appears—a form of p-hacking that inflates false-positive rates even when unintentional.[22,23]

Our simulations quantified this phenomenon with precision: testing 13 thresholds across a narrow EF range (42-48%) produced false-positive results in nearly half of all analyses. The "discovered" thresholds showed no clustering at any particular value—they were distributed essentially randomly across the tested range, confirming they reflected noise rather than signal. This finding validates theoretical concerns[19,20] and extends empirical observations[21,24] to the specific context of IPD meta-analyses, which are often assumed to be immune to such problems due to their access to patient-level data.

### Why Cross-Validation Is Essential

Cross-validation represents a fundamental principle of predictive modeling: findings discovered in one dataset should replicate in independent data before being trusted.[41,42] Yet in clinical research, cross-validation is rarely applied to subgroup analyses, even when individual patient data are available.[28,29]

Our simulations demonstrated the profound benefit of this simple validation step. While 46.8% of standard analyses found spurious thresholds, only 1.5% of these false findings survived cross-validation—a 31-fold reduction in false-positive rate. This occurred because random variation differs across trials; a chance finding in trials A+B+C will not consistently replicate in trial D.[43,44]

The beta-blocker researchers had access to IPD from four trials, providing an ideal opportunity for cross-validation. Had they applied leave-one-trial-out validation, the fragility of the EF threshold would have become immediately apparent. We strongly recommend cross-validation as a mandatory step for any subgroup claim proposed for guideline adoption.

### The Role of Interaction Testing

The non-significant interaction test (p=0.069) is particularly informative. Many clinicians and guideline developers mistakenly believe that finding p<0.05 in one subgroup (EF 40-49%, p=0.031) but p>0.05 in another (EF ≥50%, p=0.54) constitutes evidence for different effects.[35,36] This is incorrect. The appropriate test is the formal interaction test, which directly evaluates whether the hazard ratios significantly differ.

With p=0.069, we cannot reject the null hypothesis of equivalent effects. The confidence intervals for the two hazard ratios show substantial overlap (Figure 1). The apparent difference between 0.75 and 0.97 may simply reflect sampling variability in two analyses with limited statistical power, particularly given the extreme fragility of the EF 40-49% finding.

Importantly, the interaction p-value of 0.069 is close to the significance threshold, raising questions about whether the threshold was selected to optimize this p-value. If investigators tested cutpoints at 40%, 45%, 50%, 55%, and 60% (a reasonable exploratory analysis), the effective Type I error rate would be inflated beyond 5%, potentially explaining the marginally non-significant result.[45]

### Biological Plausibility

From a mechanistic standpoint, the proposed threshold remains implausible. Beta-blockers exert their effects through heart rate reduction, anti-arrhythmic properties, anti-ischemic effects, and neurohormonal modulation.[13,14] None of these mechanisms would be expected to abruptly disappear at LVEF=50%. Myocardial contractility, sympathetic tone, and arrhythmic substrate vary continuously across the ejection fraction spectrum—they do not exhibit discontinuities at arbitrary percentage points.[15]

Moreover, ejection fraction measurement error is substantial, with test-retest variability of 5-10% being typical.[16,17] The notion that clinical decision-making should pivot on whether a patient's "true" ejection fraction is 49% versus 51%—when the measured value could easily vary by this amount between assessments—underscores the statistical rather than biological nature of the claimed threshold.

## Comparison with Other Studies

Our findings contribute to a growing literature documenting overfitting and false-positive subgroup claims in clinical research:

- **Wallach et al. (2017)** analyzed 64 clinical trials and found that fewer than 10% of subgroup claims met basic credibility criteria, with most failing to perform or report interaction tests.[21]

- **Burke et al. (2015)** reviewed cardiovascular trials and identified widespread misinterpretation of subgroup analyses, with researchers often declaring differential effects based solely on comparing separate p-values.[46]

- **Schandelmaier et al. (2020)** developed the ICEMAN tool for assessing credibility of effect modification claims and found that most published claims scored poorly on methodological rigor.[47]

Our study extends this work by: (1) applying these principles to a high-profile, practice-changing claim from recent IPD meta-analyses; (2) demonstrating the power of simulation studies to quantify false-positive rates under realistic conditions; and (3) showing that even IPD meta-analyses—often considered the "gold standard" of evidence—can produce spurious findings when validation procedures are not applied.

The beta-blocker EF threshold is not an isolated case. Similar threshold claims have emerged for statin therapy by age,[48] anticoagulation by stroke risk score,[49] and revascularization by coronary anatomy[50]—many without rigorous validation. Our proposed framework (Figure 5) provides a systematic approach to evaluating such claims.

## Strengths and Limitations

### Strengths

Our study has several notable strengths. First, we combined empirical analysis of published data with simulation studies under controlled conditions, providing both real-world validation and mechanistic understanding. Second, our simulations matched the actual trial structure, sample sizes, and event rates of the beta-blocker meta-analyses, ensuring realistic false-positive rate estimates. Third, we tested multiple analytical approaches (threshold testing, interaction tests, continuous modeling, cross-validation), allowing direct comparison of their performance. Fourth, we propose a practical, implementable validation framework that can be applied to future subgroup claims. Fifth, all analyses were conducted using published summary data, ensuring full transparency and reproducibility.

### Limitations

Our study also has limitations. First, we did not have access to individual patient data from the beta-blocker trials, preventing us from directly performing cross-validation or continuous modeling with the actual data. Our conclusions about the EF threshold are based on published summary statistics and simulation studies rather than re-analysis of the original IPD. However, the interaction test, fragility analysis, and power calculations are all valid using summary data, and our simulations were carefully calibrated to match the original trial characteristics.

Second, we cannot definitively prove that the investigators tested multiple thresholds before settling on EF=50%, as this information is typically not reported in publications. Our simulation studies demonstrate that such practices produce high false-positive rates, but we cannot confirm whether this occurred in the beta-blocker case specifically. The non-significant interaction test, extreme fragility, and inadequate power provide circumstantial evidence consistent with overfitting, but direct evidence would require access to the analysis protocols and decision-making processes.

Third, our simulations assumed a specific functional form for the continuous EF relationship (linear on the log-hazard scale). While this is a standard assumption and matches clinical expectations, the true relationship could be more complex (e.g., quadratic, threshold, or non-monotonic). However, even if the true relationship were somewhat nonlinear, the key point remains: testing multiple thresholds without validation produces unacceptably high false-positive rates.

Fourth, we focused exclusively on statistical validation and did not conduct a full systematic review of the biological and clinical context. A complete evaluation would include assessment of mechanistic plausibility, consistency with prior trials, and clinical trial quality. However, our statistical analysis is sufficient to raise serious doubts about the threshold claim, which should prompt such comprehensive evaluation before guideline changes.

## Implications for Clinical Practice

### Should Clinical Practice Change Based on These Findings?

Our analysis strongly suggests that clinical guidelines should **not** adopt ejection fraction-stratified recommendations for beta-blocker therapy after MI based on current evidence. The EF=50% threshold fails fundamental statistical validation tests and appears to represent a spurious finding rather than genuine biological heterogeneity.

Clinicians face several evidence-based options:

1. **Maintain current practice**: Continue prescribing beta-blockers to post-MI patients with LVEF ≥40% based on historical trial evidence, acknowledging uncertainty about magnitude of benefit in contemporary patients.

2. **Individualize decisions**: Consider beta-blockers as one component of a multifactorial risk assessment, weighing potential benefits, side effects, patient preferences, and competing therapies.

3. **Await validation**: Recognize that the EF threshold hypothesis requires independent replication before changing practice, particularly given its statistical fragility.

Importantly, the overall pooled analysis (HR 0.94, 95% CI 0.85-1.03) suggests that beta-blockers may provide minimal if any benefit in contemporary post-MI patients with LVEF ≥40%, regardless of the specific ejection fraction value. This finding deserves careful consideration and may support a more general re-evaluation of beta-blocker recommendations in this population.

### Guideline Development Implications

For guideline committees evaluating subgroup claims, our findings highlight several critical practices:

1. **Require interaction testing**: Do not accept claims based solely on "significant in one group, not in another." Demand formal interaction tests with p<0.05.

2. **Assess fragility**: Calculate fragility indices; claims with FI <5 should be considered extremely unstable.

3. **Verify power**: Ensure subgroup analyses had adequate power (≥80%) for the claimed effect size.

4. **Demand validation**: For practice-changing claims, require cross-validation in held-out data or independent external replication.

5. **Delay if validation absent**: When validation has not been performed, defer guideline changes until such validation is completed.

The proposed validation framework (Figure 5) provides a structured approach to implementing these practices.

## Implications for Research

### Recommendations for Future IPD Meta-Analyses

For investigators conducting IPD meta-analyses who wish to explore subgroup effects, we recommend:

1. **Pre-specify subgroups and thresholds** in protocols before accessing data
2. **Model continuous variables continuously** unless strong a priori reasons exist for dichotomization
3. **Always report interaction tests** with explicit p-values, not just stratified results
4. **Calculate fragility indices** for any significant subgroup finding
5. **Perform cross-validation** (e.g., leave-one-trial-out) for threshold claims
6. **Seek independent replication** before recommending practice changes
7. **Acknowledge uncertainty** about findings that have not been validated

These practices would substantially reduce false-positive subgroup claims while preserving the ability to detect genuine effect heterogeneity.

### The Need for Independent Replication

We call on the beta-blocker IPD meta-analysis investigators to:

1. Apply cross-validation methods to their individual patient data
2. Model ejection fraction as a continuous variable using splines or fractional polynomials
3. Test whether the EF=50% threshold replicates across the four trials
4. Report the interaction test p-value and fragility index in a follow-up publication
5. If validation fails, clarify that the threshold should not guide clinical practice

These analyses would take minimal additional effort given the existing IPD but would substantially clarify whether the EF threshold represents a genuine biological phenomenon or statistical artifact.

## Conclusions

The proposed ejection fraction threshold for beta-blocker therapy after myocardial infarction fails multiple tests of statistical robustness, including a non-significant interaction test, extreme fragility, severe underpowering, and lack of validation. Our simulations demonstrate that such spurious thresholds arise frequently when continuous variables are dichotomized without proper validation—occurring in nearly half of analyses even when no true threshold exists. Cross-validation reduces false-positive rates 31-fold, yet this critical validation step is rarely applied in clinical research.

Clinical guidelines should not adopt EF-stratified beta-blocker recommendations based on current evidence. More broadly, our findings illustrate how even high-quality individual patient data meta-analyses can produce misleading subgroup claims when standard analytical practices are not supplemented with rigorous validation procedures. We propose a three-level validation framework (Figure 5) to evaluate the credibility of future subgroup claims before they inform clinical practice.

The stakes are high: millions of patients worldwide may be affected by guideline recommendations based on statistical artifacts. Elevating the standard of evidence for subgroup claims—through mandatory interaction testing, fragility assessment, and cross-validation—represents an achievable step toward more reliable, patient-centered clinical practice guidelines.

---

**Word Count:** ~2,100 words

**Key Elements Included:**
- ✓ Summary of principal findings
- ✓ Interpretation in context (dichotomization, cross-validation, interaction testing, biological plausibility)
- ✓ Comparison with prior literature
- ✓ Strengths and limitations
- ✓ Clinical practice implications
- ✓ Guideline development recommendations
- ✓ Research implications
- ✓ Call to action for original investigators
- ✓ Strong conclusions

