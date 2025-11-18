# Discussion

## Principal Findings

The proposed ejection fraction threshold for beta-blocker efficacy after myocardial infarction does not meet multiple statistical robustness criteria. The interaction test was non-significant (p=0.069), the finding was extremely fragile (FI=3 events, 1.3% of total), the analysis was severely underpowered (40% power), and no overall benefit emerged when EF ranges were pooled (HR 0.94, 95% CI 0.85-1.03).

Our simulations demonstrated that when researchers test multiple EF cutpoints, spurious "thresholds" emerge in 46.8% of analyses even when no true threshold exists. Cross-validation reduced this rate 31-fold to 1.5%, while Model 6 demonstrated cross-validation can also detect true thresholds (68.7% sensitivity). These findings suggest the EF=50% threshold likely represents a statistical artifact from underpowered subgroup analysis and data-dependent threshold selection.

## Interpretation in Context

### Dichotomization and Statistical Overfitting

Converting continuous variables like ejection fraction into binary categories discards information, reduces power, and provides flexibility to test multiple thresholds until a "significant" result appears.[22,23,37-40] Our simulations quantified this precisely: testing 13 thresholds produced false-positives in nearly half of analyses, with "discovered" thresholds distributed randomly across the tested range. This validates theoretical concerns[19,20] and demonstrates that even IPD meta-analyses—often assumed immune to such problems—can produce artifacts without proper validation.

Cross-validation represents a fundamental principle: findings discovered in one dataset should replicate in independent data.[41,42] While 46.8% of standard analyses found spurious thresholds, only 1.5% survived cross-validation—a 31-fold reduction. The beta-blocker researchers had IPD from four trials, providing an ideal opportunity for leave-one-trial-out validation that would have immediately revealed the threshold's fragility.

### Interaction Testing and Biological Plausibility

The non-significant interaction test (p=0.069) is particularly informative. Many mistakenly believe that finding p<0.05 in one subgroup but p>0.05 in another constitutes evidence for different effects—this is incorrect.[35,36] The appropriate test is formal interaction testing. With p=0.069 and substantial CI overlap, we cannot reject equivalent effects. The apparent difference between HR 0.75 and 0.97 may simply reflect sampling variability in underpowered analyses.

From a mechanistic standpoint, the threshold remains implausible. Beta-blocker mechanisms—heart rate reduction, anti-arrhythmic properties, neurohormonal modulation—would not be expected to abruptly disappear at LVEF=50%.[13,14] Ejection fraction measurement error is substantial (5-10% test-retest variability),[16,17] making clinical decisions based on whether EF is 49% versus 51% statistically rather than biologically driven.

## Comparison with Other Studies

Our findings contribute to growing literature documenting overfitting in subgroup claims. Wallach et al. (2017) found fewer than 10% of subgroup claims met basic credibility criteria.[21] Burke et al. (2015) identified widespread misinterpretation of subgroup analyses in cardiovascular trials.[46] Schandelmaier et al. (2020) developed the ICEMAN tool and found most published claims scored poorly on methodological rigor.[47]

Our study extends this work by: (1) applying these principles to a high-profile, practice-changing claim from recent IPD meta-analyses, (2) demonstrating the power of simulation studies to quantify false-positive rates, and (3) showing that even IPD meta-analyses can produce spurious findings without validation procedures.

## Strengths and Limitations

Our study combined empirical analysis with simulations matching actual trial structure, tested multiple analytical approaches, and proposed an implementable validation framework. All analyses used published data, ensuring transparency and reproducibility.

Critical limitations include **lack of individual patient data access**, preventing us from performing gold-standard continuous LVEF modeling with splines, directly cross-validating the actual data, or definitively determining whether multiple thresholds were tested. Our conclusions are therefore **provisional** pending such analyses. However, the analyses we could perform—interaction testing, fragility assessment, and power calculation—are statistically valid and all raise serious concerns.

The interaction test had only 46% power, meaning we cannot definitively rule out a true difference (Type II error). However, we do not claim to have proven equivalence. Rather, we conclude the **evidence is insufficient** to support confident subgroup-based treatment recommendations. Practice-changing guideline recommendations require adequately powered, validated evidence, which has not been provided for this threshold.

Our simulations tested six functional forms (Models 1-6), with remarkably consistent findings: threshold testing produced 45-51% false-positives while cross-validation maintained 1.4-2.1% rates across all scenarios. Model 6 demonstrated cross-validation has both excellent specificity (98.5%) and good sensitivity (68.7%), confirming the approach can detect genuine discontinuities while rejecting spurious ones.

## Clinical and Research Implications

### Clinical Practice

Adoption of EF-stratified beta-blocker recommendations would be premature. The EF=50% threshold does not meet fundamental validation criteria and appears to represent a spurious finding. Clinicians should: (1) maintain current evidence-based practice, (2) individualize decisions considering multiple factors, and (3) await independent validation before changing practice. Importantly, the pooled analysis (HR 0.94, 95% CI 0.85-1.03) suggests beta-blockers may provide minimal benefit in contemporary post-MI patients with LVEF ≥40% regardless of specific EF value—deserving careful consideration.

### What Evidence Would Be Convincing?

To establish a genuine LVEF threshold for guideline development, future research should provide:

1. **Continuous LVEF modeling** with splines (≥3 knots) to assess whether effects vary smoothly or exhibit discontinuities
2. **Adequate power** (≥80%) for effect modification; for the observed difference, this requires ~630 events
3. **Internal cross-validation** (leave-one-trial-out) demonstrating threshold replicates across trials
4. **External validation** in independent cohorts from different populations
5. **Biological plausibility** with mechanistic explanation for discontinuity at LVEF=50%
6. **Statistical robustness**: FI>10, significant interaction (p<0.01), sensitivity analyses

The beta-blocker EF threshold meets **0 of 6** criteria. Until such evidence emerges, we do not recommend using EF=50% as a treatment decision threshold.

### Guideline Development and Research Standards

For guideline committees evaluating subgroup claims: (1) require formal interaction testing (p<0.05), (2) assess fragility (consider FI<5 extremely unstable), (3) verify adequate power (≥80%), and (4) demand validation evidence before guideline incorporation.

For investigators conducting IPD meta-analyses: (1) pre-specify subgroups in protocols, (2) model continuous variables continuously unless strong a priori rationale exists for dichotomization, (3) always report interaction tests, (4) calculate fragility indices, (5) perform cross-validation for threshold claims, and (6) seek independent replication before recommending practice changes.

We encourage the beta-blocker IPD investigators to: (1) apply cross-validation methods to their data, (2) model ejection fraction continuously using splines, (3) test whether the EF=50% threshold replicates across trials, and (4) report interaction test p-values and fragility indices. These analyses would substantially clarify whether the threshold represents genuine biological heterogeneity or statistical artifact. (Detailed stakeholder recommendations provided in supplementary materials)

## Conclusions

The proposed LVEF=50% threshold for beta-blocker therapy after MI does not meet criteria for statistical robustness, including non-significant interaction testing, extreme fragility, severe underpowering, and lack of validation. Simulations demonstrate spurious thresholds arise in nearly half of analyses when continuous variables are dichotomized without validation. Cross-validation reduces false-positives 31-fold yet is rarely applied in clinical research.

Adoption of EF-stratified beta-blocker recommendations would be premature. More broadly, our findings illustrate how even high-quality IPD meta-analyses can produce questionable subgroup claims when standard analytical practices are not supplemented with rigorous validation. We propose a validation framework (Figure 5) to evaluate credibility of future subgroup claims before they inform clinical practice.

The stakes are high: millions of patients worldwide may be affected by guideline recommendations based on spurious subgroup findings. Elevating standards—through requirements for interaction testing, fragility assessment, and cross-validation—represents an achievable step toward more reliable, patient-centered clinical practice guidelines.

---

**Word Count:** ~1,240 words

**Note:** Extended stakeholder recommendations, detailed literature comparisons, and implementation guidance provided in supplementary materials.
