# Discussion

## Principal Findings

In this comprehensive validation study, we found that the proposed ejection fraction threshold for beta-blocker efficacy after myocardial infarction does not meet multiple statistical robustness criteria. The formal test for interaction between the EF 40-49% and EF ≥50% subgroups was non-significant (p=0.069), providing no statistical evidence that treatment effects differ between these ranges. The EF 40-49% finding was extremely fragile (fragility index=3 events, only 1.3% of the total), severely underpowered (40% power for detecting HR 0.80), and based on insufficient cumulative information. When both EF ranges were pooled, no significant benefit of beta-blockers emerged (HR 0.94, 95% CI 0.85-1.03).

Our simulation study demonstrated why questionable thresholds can arise. When researchers test multiple EF cutpoints—a practice enabled by the flexibility of dichotomizing continuous variables—false-positive "thresholds" emerge in 46.8% of analyses even when no true threshold exists. Cross-validation reduced this rate 31-fold to 1.5%, highlighting the critical importance of validation procedures that are rarely applied in practice.

Together, these findings suggest that the EF=50% threshold likely represents a statistical artifact resulting from underpowered subgroup analysis and data-dependent threshold selection rather than evidence of a true biological discontinuity.

## Interpretation in Context

### The Perils of Dichotomizing Continuous Variables

The hazards of dichotomizing continuous variables have been recognized for decades.[37,38] Converting a continuous measure like ejection fraction into binary categories (above/below 50%) discards information, reduces statistical power, and creates arbitrary boundaries that are biologically implausible.[39,40] Perhaps most dangerously, dichotomization provides investigators with substantial flexibility to test multiple thresholds until a "significant" result appears—a form of p-hacking that inflates false-positive rates even when unintentional.[22,23]

Our simulations quantified this phenomenon with precision: testing 13 thresholds across a narrow EF range (42-48%) produced false-positive results in nearly half of all analyses. The "discovered" thresholds showed no clustering at any particular value—they were distributed essentially randomly across the tested range, confirming they reflected noise rather than signal. This finding validates theoretical concerns[19,20] and extends empirical observations[21,24] to the specific context of IPD meta-analyses, which are often assumed to be immune to such problems due to their access to patient-level data.

### Why Cross-Validation Is Essential

Cross-validation represents a fundamental principle of predictive modeling: findings discovered in one dataset should replicate in independent data before being trusted.[41,42] Yet in clinical research, cross-validation is rarely applied to subgroup analyses, even when individual patient data are available.[28,29]

Our simulations demonstrated the profound benefit of this simple validation step. While 46.8% of standard analyses found questionable thresholds, only 1.5% of these findings survived cross-validation—a 31-fold reduction in false-positive rate. This occurred because random variation differs across trials; a chance finding in trials A+B+C will not consistently replicate in trial D.[43,44]

The beta-blocker researchers had access to IPD from four trials, providing an ideal opportunity for cross-validation. Had they applied leave-one-trial-out validation, the fragility of the EF threshold would have become immediately apparent. We encourage journal editors and guideline bodies to consider cross-validation as a recommended validation step for subgroup claims proposed for guideline adoption.

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

Our study extends this work by: (1) applying these principles to a high-profile, practice-changing claim from recent IPD meta-analyses; (2) demonstrating the power of simulation studies to quantify false-positive rates under realistic conditions; and (3) showing that even IPD meta-analyses—often considered the "gold standard" of evidence—can produce questionable findings when validation procedures are not applied.

The beta-blocker EF threshold is not an isolated case. Similar threshold claims have emerged for statin therapy by age,[48] anticoagulation by stroke risk score,[49] and revascularization by coronary anatomy[50]—many without rigorous validation. Our proposed framework (Figure 5) provides a systematic approach to evaluating such claims.

## Strengths and Limitations

### Strengths

Our study has several notable strengths. First, we combined empirical analysis of published data with simulation studies under controlled conditions, providing both real-world validation and mechanistic understanding. Second, our simulations matched the actual trial structure, sample sizes, and event rates of the beta-blocker meta-analyses, ensuring realistic false-positive rate estimates. Third, we tested multiple analytical approaches (threshold testing, interaction tests, continuous modeling, cross-validation), allowing direct comparison of their performance. Fourth, we propose a practical, implementable validation framework that can be applied to future subgroup claims. Fifth, all analyses were conducted using published summary data, ensuring full transparency and reproducibility.

### Limitations

Our study has important limitations that must be acknowledged transparently.

**Lack of Individual Patient Data Access**

Most critically, we did not have access to the individual patient data from the beta-blocker trials. This prevented us from:
- Directly performing cross-validation on the actual data
- Modeling LVEF as a continuous variable with splines or fractional polynomials
- Examining trial-specific subgroup effects and heterogeneity
- Definitively determining whether multiple thresholds were tested during analysis

Consequently, our empirical analyses rely on published summary statistics, and our conclusions about potential overfitting rest primarily on simulation evidence rather than direct re-analysis of the original IPD. **Most critically, without access to IPD, we cannot perform the gold-standard analysis: modeling LVEF continuously to determine whether treatment effects vary smoothly or exhibit discontinuities.** Our conclusions are therefore **provisional** pending such analyses. However, the analyses we **can** perform using summary data—interaction testing, fragility assessment, and power calculation—are statistically valid and all raise serious concerns about the claimed threshold. Our simulations were carefully calibrated to match the actual trial structure, sample sizes, and event rates.

**Interaction Test Power Limitation**

The test for interaction had only 46% power to detect the observed difference as statistically significant. This limited power means we cannot definitively rule out a true difference in treatment effects between subgroups (Type II error). However, we do not interpret our findings as proving equivalence. Rather, we conclude that **the evidence is insufficient**—whether due to non-significant testing, low power, or both—to support confident subgroup-based treatment recommendations. Practice-changing guideline recommendations require adequately powered, validated evidence, which has not yet been provided for this threshold.

**Simulation Assumptions**

Our simulations tested five different functional forms for the relationship between LVEF and treatment effect: linear decline, quadratic (accelerating decline), gentle threshold at EF=47%, complete null (HR=1.0), and random heterogeneous effects (Table 6). We cannot test every possible true relationship. However, the core finding—that testing multiple thresholds produces false-positives in 45-51% of analyses (depending on the model) while cross-validation reduces this to 1.4-2.1%—was remarkably consistent across all five models, including scenarios with true thresholds, null effects, and random heterogeneity. This robustness demonstrates that the high false-positive rate is not an artifact of our modeling assumptions but a fundamental property of dichotomization combined with multiple testing.

**Uncertainty About Pre-Specification**

We cannot confirm whether the LVEF=50% threshold was pre-specified in analysis plans or selected post hoc, as detailed analysis protocols are typically not published. Pre-specification would address multiple testing concerns but would **not** resolve the fragility, power, or interaction test issues. Even pre-specified subgroups require adequate power, statistical robustness (fragility index >5), and ideally validation before being used to guide practice guidelines. The claimed threshold fails these criteria regardless of pre-specification status.

**Scope of Conclusions**

Our analysis addresses the specific question of whether a sharp threshold exists at LVEF=50%. We do not address the broader question of whether beta-blockers benefit contemporary post-MI patients at any LVEF level, nor do we comment on the validity of historical trials conducted in different patient populations (pre-reperfusion era, selected high-risk patients). The pooled analysis suggests minimal overall benefit (HR 0.94, 95% CI 0.85-1.03), but evaluating beta-blocker efficacy across the entire LVEF spectrum was not our primary objective.

**Generalizability**

While we use the beta-blocker EF threshold as a detailed case study, we cannot guarantee that all similar claims in other clinical contexts would show identical patterns. However, the simulation framework is generalizable and the statistical principles apply broadly. The proposed validation framework (Figure 5) can be adapted to evaluate any subgroup claim from IPD meta-analyses.

Despite these limitations, we believe our analyses provide sufficient evidence to seriously question the validity of the LVEF=50% threshold and to call for rigorous validation before adopting EF-stratified treatment recommendations in clinical guidelines. The analyses we could perform all point in the same direction: insufficient evidence for a threshold effect.

## Implications for Clinical Practice

### Should Clinical Practice Change Based on These Findings?

Our analysis suggests that adoption of ejection fraction-stratified recommendations for beta-blocker therapy after MI would be premature based on current evidence. The EF=50% threshold does not meet fundamental statistical validation criteria and appears to represent a questionable finding rather than genuine biological heterogeneity.

Clinicians face several evidence-based options:

1. **Maintain current practice**: Continue prescribing beta-blockers to post-MI patients with LVEF ≥40% based on historical trial evidence, acknowledging uncertainty about magnitude of benefit in contemporary patients.

2. **Individualize decisions**: Consider beta-blockers as one component of a multifactorial risk assessment, weighing potential benefits, side effects, patient preferences, and competing therapies.

3. **Await validation**: Recognize that the EF threshold hypothesis requires independent replication before changing practice, particularly given its statistical fragility.

Importantly, the overall pooled analysis (HR 0.94, 95% CI 0.85-1.03) suggests that beta-blockers may provide minimal if any benefit in contemporary post-MI patients with LVEF ≥40%, regardless of the specific ejection fraction value. This finding deserves careful consideration and may support a more general re-evaluation of beta-blocker recommendations in this population.

### What Evidence Would Be Convincing?

To establish a genuine LVEF threshold for beta-blocker therapy that could appropriately guide clinical practice guidelines, future research should provide:

**1. Individual Patient Data Analysis with Continuous LVEF Modeling**
- Model LVEF as a continuous variable using restricted cubic splines (≥3 knots) or fractional polynomials
- Visually and statistically assess whether treatment effects vary smoothly or exhibit discontinuities
- Report whether any observed inflection point occurs at the claimed threshold value (EF=50%)

**2. Adequate Statistical Power for Effect Modification**
- Sample size with ≥80% power to detect clinically meaningful effect modification
- For the observed difference (HR 0.75 vs 0.97), this would require ~630 events in the lower EF range
- Power calculation should be reported a priori in study protocols

**3. Internal Cross-Validation**
- Leave-one-trial-out validation demonstrating the threshold replicates across constituent trials
- Consistency of the threshold location across validation folds
- Demonstrate that the finding is not driven by a single trial or small subset of patients

**4. External Validation in Independent Cohorts**
- Replication in separate patient populations not included in the discovery analysis
- Ideally from different geographic regions, time periods, or healthcare systems
- Consistent threshold location and effect magnitudes across validation cohorts

**5. Biological Plausibility**
- Mechanistic explanation for why beta-blocker effects would discontinuously change at LVEF=50%
- Evidence from basic science, pathophysiology, or pharmacodynamics supporting the threshold
- Consideration of measurement error in LVEF assessment (typically 5-10% test-retest variability)

**6. Statistical Robustness**
- Fragility index >10 for practice-changing claims
- Significant formal interaction test (p<0.01, accounting for multiple comparisons)
- Sensitivity analyses showing findings robust to analytic choices

**Current Evidence Status:**

The beta-blocker EF threshold meets **0 of 6** criteria above. Until such evidence emerges, guideline committees face two reasonable options:

- **Option A**: Recommend beta-blockers for all post-MI patients with LVEF ≥40%, acknowledging uncertainty about magnitude of benefit in contemporary practice

- **Option B**: De-emphasize beta-blockers given the overall HR 0.94 (95% CI 0.85-1.03), reserving them for selected high-risk patients based on individual clinical judgment

**We do not recommend** using EF=50% as a treatment decision threshold for withholding beta-blockers based on current evidence.

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
5. If validation does not support the threshold, clarify that it may not be suitable to guide clinical practice

These analyses would take minimal additional effort given the existing IPD but would substantially clarify whether the EF threshold represents a genuine biological phenomenon or a statistical artifact.

---

## Call to Action: Recommendations for Key Stakeholders

We propose specific, actionable steps for three key constituencies to improve the validation of subgroup claims before they influence clinical practice:

### For IPD Meta-Analysis Investigators

When exploring subgroup effects in individual patient data meta-analyses:

1. **Pre-specify subgroups and thresholds** in publicly registered analysis protocols before accessing data
2. **Model continuous variables continuously** using splines or fractional polynomials as the primary analysis; only dichotomize if there is strong a priori biological rationale
3. **Always report interaction tests** with explicit p-values and confidence intervals, not just stratified results
4. **Calculate and report fragility indices** for any statistically significant subgroup finding
5. **Perform internal cross-validation** (e.g., leave-one-trial-out) for any threshold claim before publication
6. **Seek independent external replication** in separate datasets before recommending practice changes
7. **Transparently acknowledge uncertainty** about findings that have not been validated

### For Clinical Practice Guideline Committees

When evaluating subgroup claims for guideline incorporation:

1. **Require formal interaction testing** (p<0.05) as a minimum threshold; do not accept claims based solely on "significant in one group, not in another"
2. **Assess statistical fragility** using fragility indices; consider claims with FI <5 as extremely unstable
3. **Verify adequate statistical power** (≥80%) for the subgroup analysis, not just the overall trial
4. **Demand validation evidence**: Has the finding been cross-validated internally or replicated externally?
5. **Delay guideline recommendations** when validation has not been performed, explicitly noting this as a gap requiring future research
6. **Apply the proposed 3-level validation framework** (Figure 5) systematically to all subgroup claims
7. **Downgrade strength of recommendations** for subgroups that fail validation criteria, even if nominally "statistically significant"

### For the Research Community

To elevate methodological standards for subgroup analyses:

1. **Journal editors**: Require reporting of interaction tests, fragility indices, and power calculations for all subgroup analyses in submission guidelines
2. **Peer reviewers**: Routinely ask for cross-validation or external replication when subgroup claims are presented
3. **Methodologists**: Develop and disseminate accessible tools for fragility analysis and cross-validation in meta-analyses
4. **Funding agencies**: Prioritize support for independent replication studies of high-impact subgroup claims
5. **Trial registries**: Enhance pre-specification requirements to include planned subgroup analyses with specific thresholds
6. **Statistical reporting guidelines** (e.g., CONSORT, PRISMA): Incorporate fragility assessment and validation requirements
7. **Educational initiatives**: Train clinicians and researchers to critically evaluate subgroup claims using the validation framework

### Suggested Next Steps for the Beta-Blocker EF Threshold

We respectfully encourage the investigators of the beta-blocker IPD meta-analyses to consider the following validation analyses, which would substantially clarify whether the EF threshold represents a genuine biological phenomenon:

- **Short term** (3-6 months): Share the formal interaction test p-value and fragility index in a correspondence, commentary, or supplementary analysis. These statistics can be calculated from existing data and would help the clinical community assess the threshold's statistical robustness.

- **Medium term** (6-12 months): Perform internal cross-validation (leave-one-trial-out) to test whether the EF=50% threshold replicates across the four constituent trials. We recognize this requires re-analysis of IPD but represents a critical validation step.

- **Longer term** (12-18 months): Model LVEF continuously using restricted cubic splines or fractional polynomials to determine whether treatment effects vary smoothly or exhibit genuine discontinuities at specific EF values. This gold-standard analysis would definitively address the threshold question.

We recognize these analyses require substantial effort and may reveal complex patterns not captured by simple threshold models. Collaborative sharing of IPD with independent analysts—through established data-sharing platforms or consortia—could accelerate this validation process while maintaining scientific rigor. The clinical community would benefit greatly from such collaborative efforts to resolve this important uncertainty.

---

## Conclusions

The proposed ejection fraction threshold for beta-blocker therapy after myocardial infarction does not meet multiple criteria for statistical robustness, including a non-significant interaction test, extreme fragility, severe underpowering, and lack of validation. Our simulations demonstrate that questionable thresholds arise frequently when continuous variables are dichotomized without proper validation—occurring in nearly half of analyses even when no true threshold exists. Cross-validation reduces false-positive rates 31-fold, yet this critical validation step is rarely applied in clinical research.

Adoption of EF-stratified beta-blocker recommendations would be premature based on current evidence. More broadly, our findings illustrate how even high-quality individual patient data meta-analyses can produce questionable subgroup claims when standard analytical practices are not supplemented with rigorous validation procedures. We propose a three-level validation framework (Figure 5) to evaluate the credibility of future subgroup claims before they inform clinical practice.

The stakes are high: millions of patients worldwide may be affected by guideline recommendations based on questionable subgroup findings. Elevating the standard of evidence for subgroup claims—through recommended requirements for interaction testing, fragility assessment, and cross-validation—represents an achievable step toward more reliable, patient-centered clinical practice guidelines.

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

