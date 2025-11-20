# Discussion (CONDENSED VERSION FOR BMJ SUBMISSION)

## Principal Findings

The proposed ejection fraction threshold for beta-blocker efficacy after myocardial infarction does not meet multiple statistical validation criteria. The interaction test was non-significant (p=0.069, with only 46% power), the EF 40-49% finding was extremely fragile (fragility index=3 events, 1.3% of total), the subgroup analysis was severely underpowered (40% power for detecting HR 0.80), and when both EF ranges were pooled, no significant benefit emerged (HR 0.94, 95% CI 0.85-1.03).

Our simulations demonstrated that testing multiple EF thresholds—a practice enabled by dichotomizing continuous variables—produces false-positive "thresholds" in 46.8% of analyses even when no true threshold exists. Cross-validation reduced this rate 31-fold to 1.5%. Together, these findings suggest the EF=50% threshold likely represents a statistical artifact from underpowered subgroup analysis rather than genuine biological heterogeneity.

## Interpretation

### The Hazards of Dichotomization

Converting continuous ejection fraction into binary categories discards information, reduces power, and creates arbitrary boundaries.¹⁻³ More dangerously, dichotomization provides flexibility to test multiple thresholds until a "significant" result appears—a form of p-hacking that inflates false-positive rates.⁴⁻⁵ Our simulations quantified this: testing 13 thresholds across EF 42-48% produced false-positives in nearly half of analyses, with "discovered" thresholds distributed randomly across the range—confirming they reflected noise rather than signal.

### Why Cross-Validation Matters

Cross-validation is fundamental: findings discovered in one dataset should replicate independently.⁶⁻⁷ Yet subgroup analyses rarely undergo this validation,⁸⁻⁹ even when IPD are available. While 46.8% of standard analyses found questionable thresholds, only 1.5% survived cross-validation—a 31-fold reduction. When a true threshold existed (Model 6), cross-validation detected it in 68.7% of cases, demonstrating both excellent specificity (98.5%) and good sensitivity.

The beta-blocker researchers had IPD from four trials, ideal for leave-one-trial-out validation. Had they applied it, the threshold's fragility would have been immediately apparent.

### Biological Implausibility

From a mechanistic standpoint, the threshold remains implausible. Beta-blocker effects (heart rate reduction, anti-arrhythmic properties, neurohormonal modulation) would not abruptly disappear at LVEF=50%.¹⁰⁻¹¹ Myocardial contractility and sympathetic tone vary continuously—they exhibit no discontinuities at arbitrary percentage points. Moreover, ejection fraction measurement error is substantial (5-10% test-retest variability),¹²⁻¹³ making 49% versus 51% clinically indistinguishable.

##Strengths and Limitations

Our study combined empirical analysis with simulation studies matching actual trial structure, tested multiple analytical approaches, and proposes a practical validation framework. All analyses used published data, ensuring transparency.

**Critical limitations warrant acknowledgment:**

**Lack of IPD access** prevented us from performing continuous LVEF modeling with splines, direct cross-validation, or examining trial-specific effects. Our conclusions rest primarily on simulation evidence rather than direct IPD reanalysis and are therefore **provisional** pending gold-standard continuous modeling. However, analyses we could perform—interaction testing, fragility assessment, power calculation—are statistically valid and consistently raise concerns.

**Limited interaction test power** (46%) means we cannot definitively rule out true subgroup differences (Type II error). We do not claim to prove equivalence—rather, **evidence is insufficient** to support practice-changing recommendations. The non-significant test, extreme fragility, severe underpowering, and lack of validation collectively indicate inadequate evidence for the threshold.

**Simulation assumptions:** We tested six functional forms (linear, quadratic, threshold, null, heterogeneous, true threshold matching observed data). While we cannot test every possibility, the core finding—that multiple threshold testing produces 45-51% false-positives while cross-validation reduces this to 1.4-2.1%—was remarkably consistent across diverse scenarios. Model 6 demonstrated cross-validation can detect true thresholds (68.7% sensitivity) while maintaining high specificity (98.5%).

## Clinical and Guideline Implications

Adoption of EF-stratified beta-blocker recommendations would be premature. The overall pooled analysis (HR 0.94, 95% CI 0.85-1.03) suggests minimal if any benefit in contemporary post-MI patients with LVEF ≥40%, regardless of specific EF value. Until adequate validation is provided, guideline committees face two reasonable options: (A) recommend beta-blockers for all post-MI patients with LVEF ≥40%, acknowledging uncertainty, or (B) de-emphasize them given borderline overall benefit. **We do not recommend using EF=50% as a treatment decision threshold.**

**What Evidence Would Be Convincing?** To establish a genuine threshold suitable for guidelines, future research should provide (Table S1): (1) continuous LVEF modeling with splines showing discontinuities at EF=50%, (2) adequate power (≥80%) for effect modification, (3) internal cross-validation demonstrating replication across trials, (4) external validation in independent cohorts, (5) mechanistic explanation for the discontinuity, and (6) statistical robustness (fragility index >10, interaction p<0.01). **Current status: 0 of 6 criteria met.**

For guideline committees evaluating any subgroup claim, we propose requiring: significant interaction testing (p<0.05), fragility index >5, adequate power (>80%), and cross-validation or external replication before adoption (Table S2). The beta-blocker threshold fails all criteria.

## Recommendations

We respectfully encourage the beta-blocker IPD investigators to perform internal cross-validation and continuous LVEF modeling to clarify whether the threshold represents genuine biology or statistical artifact. These analyses would substantially benefit the clinical community.

More broadly, journal editors should require reporting of interaction tests, fragility indices, and power calculations for all subgroup analyses. When subgroup claims have practice-changing implications but lack validation, guideline committees should defer recommendations until validation is completed.

## Conclusions

The proposed ejection fraction threshold for beta-blocker therapy does not meet statistical validation criteria and likely represents an artifact from underpowered analysis and dichotomization of continuous variables. Our simulations demonstrate questionable thresholds arise in nearly half of analyses without proper validation. Cross-validation reduces false-positive rates 31-fold yet is rarely applied.

Adoption of EF-stratified recommendations would be premature. Even high-quality IPD meta-analyses can produce questionable findings without rigorous validation procedures. The stakes are high: millions of patients worldwide may be affected by guideline recommendations based on inadequately validated subgroup claims. Elevating evidence standards—through interaction testing, fragility assessment, and cross-validation—represents an achievable step toward more reliable clinical practice guidelines.

---

**Word Count:** ~980 words

**References:** Condensed inline citations (full list in main manuscript)

---

## Notes for Production

**Content preserved:**
- ✅ Principal findings
- ✅ Core interpretations (dichotomization, cross-validation, biological implausibility)
- ✅ Strengths and limitations (transparent about IPD access)
- ✅ Clinical implications
- ✅ Validation framework (referenced as Table S1-S2)
- ✅ Brief recommendations
- ✅ Strong conclusions

**Content condensed:**
- Extended stakeholder recommendations → Brief paragraph
- Detailed "What Evidence Would Be Convincing?" → Referenced table
- Extended literature comparisons → Removed (covered in Introduction)
- Repetitive interpretations → Streamlined

**Moved to supplement:**
- Table S1: Six validation criteria with detailed explanations
- Table S2: Guideline committee checklist
- Extended call to action with timelines
- Detailed comparisons to prior literature

**Savings:** 3,476 → 980 words (saves 2,496 words) ✅
