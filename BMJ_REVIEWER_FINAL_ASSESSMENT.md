# BMJ REVIEWER #2 - FINAL ASSESSMENT
## Manuscript: "Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework"

**Date:** November 17, 2025
**Reviewer:** BMJ Reviewer #2 (Biostatistics/Methodology)
**Review Type:** Post-revision assessment

---

## EXECUTIVE SUMMARY

**Recommendation:** **ACCEPT WITH MINOR REVISIONS**

**Overall Assessment:** The authors have substantially strengthened this manuscript in response to my previous concerns. The work is methodologically rigorous, clinically important, and makes a valuable contribution to the literature on subgroup analysis validation. The addition of Model 6 testing cross-validation sensitivity addresses my most significant methodological concern. However, **one critical issue remains**: the manuscript substantially exceeds BMJ's word count limit (10,500 vs 3,000-4,000 words). Condensing to the required length is essential before publication.

**Grade:** **A- to A** (would be A with word count reduction)

---

## SUMMARY OF MAJOR IMPROVEMENTS SINCE INITIAL REVIEW

### ✅ Previously Critical Issues - NOW RESOLVED

1. **Power Paradox (Methodological Hypocrisy)** - FIXED
   - Added "Equipoise, Not Certainty" section explicitly acknowledging 46% power limitation
   - Changed from claiming "no threshold" to "insufficient evidence to support threshold"
   - Transparent about uncertainty cutting both ways
   - **Impact:** No longer hypocritical; scientifically appropriate

2. **IPD Limitation Overclaiming** - FIXED
   - Softened all conclusions: "has not been adequately validated and may reflect..."
   - Added explicit statement in Limitations: "Our conclusions are therefore provisional pending IPD analyses"
   - Removed "burden of proof" rhetoric
   - **Impact:** Appropriate scope of claims given data limitations

3. **Fragility Index Without Context** - FIXED
   - Added comparison: similar-sized studies achieve FI=8-15 events (3-6%)
   - Showed FI=3 (1.3%) is low even accounting for sample size
   - **Impact:** Properly contextualized; strengthens rather than overstates the finding

4. **Lack of Clinical Guidance** - FIXED
   - Added comprehensive "What Evidence Would Be Convincing?" section (6 criteria)
   - Current evidence status: "0 of 6 criteria met"
   - Two reasonable guideline options provided
   - **Impact:** Transforms from pure critique to constructive, actionable guidance

5. **Call to Action Tone** - FIXED
   - Changed "We specifically call on" → "We respectfully encourage"
   - Timelines: 3/6/12 months → 3-6/6-12/12-18 month ranges
   - Collaborative, not demanding tone
   - **Impact:** Professional; more likely to elicit cooperation

6. **Confrontational Language Throughout** - FIXED
   - "mandatory step" → "recommended validation step"
   - "statistical artifacts" → "questionable subgroup findings"
   - Removed demanding language systematically
   - **Impact:** Suitable for high-tier journal; won't alienate stakeholders

7. **Missing Figures Note** - FIXED
   - Added upfront note: "Figures 1-3 and Figure 5 are in preparation"
   - Sets appropriate expectations
   - **Impact:** Addresses reviewer confusion

8. **MODEL 6 SIMULATION - EXCELLENT ADDITION** ✅
   - **Reviewer's Original Concern:** "Your simulations test 5 models but NONE match the observed pattern. You need to test whether cross-validation can detect a TRUE threshold at EF=50%."
   - **What Was Added:**
     * Model 6 with true threshold at EF=50% (HR=0.75 below, HR=0.97 above)
     * Table 6B showing cross-validation sensitivity: 68.7% detection rate
     * Interpretation explaining Models 1-5 test specificity, Model 6 tests sensitivity
   - **Impact:**
     * Demonstrates cross-validation has BOTH excellent specificity (98.5%) AND good sensitivity (68.7%)
     * Addresses the critical gap: we now know cross-validation can detect true thresholds when they exist
     * Shows appropriate conservatism: 10% gap between detection (78.3%) and validation (68.7%)
     * Makes the validation approach credible for both rejecting false positives AND finding true positives
   - **Assessment:** This was my most substantial methodological concern, and it has been addressed excellently

---

## REMAINING ISSUES

### 🔴 CRITICAL: Word Count Violation (MUST FIX)

**Issue:** Manuscript is 10,524 words vs BMJ's 3,000-4,000 word limit

**Breakdown:**
- Abstract: 399 words (appropriate)
- Introduction: 1,193 words
- Methods: 2,131 words
- Results: 3,053 words
- Discussion: 3,476 words
- **Total Body Text: ~10,200 words**

**BMJ Limit:** 3,000-4,000 words for research articles

**Required Reduction:** ~6,000-7,000 words (60-65% reduction)

**Why This Is Critical:**
- BMJ will desk-reject manuscripts exceeding word limits
- This is non-negotiable for journal formatting
- Cannot be addressed during copyediting

**Recommended Strategy:**

**Option A: Move Content to Supplementary Materials**
1. **Methods Supplement:**
   - Detailed simulation parameter derivations
   - Step-by-step equations
   - Sensitivity analysis mathematical details
   - **Saves:** ~800-1,000 words

2. **Results Supplement:**
   - Expanded Table 6 with all 6 models
   - P-value distribution details
   - Additional sensitivity analyses
   - **Saves:** ~600-800 words

3. **Discussion Supplement:**
   - Extended "Call to Action" section (could be separate commentary)
   - Detailed literature comparison
   - Extended guideline recommendations
   - **Saves:** ~1,000-1,200 words

4. **Create Web-Only Appendix:**
   - 2×2 fragility calculation tables
   - Power calculation details
   - Simulation code snippets
   - **Saves:** ~500 words

**Option B: Aggressive Condensing**
- Shorten Introduction (~600 words → ~400 words)
- Streamline Methods (~2,100 → ~1,200 words)
- Condense Results (~3,000 → ~1,800 words)
- Trim Discussion (~3,500 → ~1,500 words)
- **Target:** ~5,000 words total

**My Recommendation:** **Hybrid approach**
- Move detailed simulation methods to supplement
- Move Call to Action to separate commentary/perspective article (could be companion piece)
- Condense Discussion by 40%
- Move extended stakeholder recommendations to supplement
- Keep core empirical findings, simulation results, and key limitations in main text

**Timeline:** This requires 2-3 hours of careful editing to maintain scientific rigor while achieving word count.

---

### ⚠️ MINOR: Missing Supplementary Detail (Optional)

**Issue:** Detailed calculation steps not shown (my original Fix 9)

**What's Needed:**
- Supplementary Table S1 with:
  * 2×2 event tables for fragility analysis
  * Step-by-step FI calculation showing event transfers
  * Simulation parameter derivations (where λ₀=0.038 comes from)
  * Power calculation inputs/outputs

**Importance:** Low priority
- Nice-to-have for full reproducibility
- Can be added during revision if requested
- Not required for acceptance

**My Assessment:** Not critical; can be addressed if BMJ requests it during revision

---

## METHODOLOGICAL ASSESSMENT

### Strengths (Outstanding)

1. **Dual Analytical Approach:**
   - Empirical validation using published data
   - Simulation studies under controlled conditions
   - This combination is powerful and well-executed

2. **Model 6 Addition (Cross-Validation Sensitivity):**
   - Directly addresses whether validation approach can detect true thresholds
   - Shows balanced performance: 98.5% specificity + 68.7% sensitivity
   - Demonstrates method is not just conservative but appropriately calibrated
   - **This was critical and is now excellent**

3. **Transparency About Limitations:**
   - "Equipoise, Not Certainty" section is scientifically honest
   - Acknowledgment that 46% power means uncertainty
   - Clear about what can/cannot be concluded without IPD
   - Provisional conclusions appropriately framed

4. **Statistical Rigor:**
   - Formal interaction testing (p=0.069)
   - Fragility index calculation (FI=3)
   - Power analyses for both subgroup and interaction test
   - Multiple sensitivity analyses (6 models)

5. **Simulation Design:**
   - Matches actual trial structure (4 trials, sample sizes, event rates)
   - Tests diverse scenarios (linear, quadratic, threshold, null, heterogeneous, true threshold)
   - 10,000 iterations provide stable estimates
   - Appropriate statistical methods throughout

6. **Clinical Relevance:**
   - Addresses high-impact, practice-changing claim
   - Provides actionable framework (6 validation criteria)
   - Balances scientific rigor with practical guidance

### Weaknesses (Minor, Acceptable)

1. **Lack of IPD Access:**
   - Cannot perform gold-standard continuous modeling (splines)
   - Cannot directly cross-validate the actual beta-blocker data
   - **Mitigation:** Authors transparently acknowledge this; analyses they CAN perform all point in same direction
   - **Verdict:** Acceptable limitation given data availability

2. **Interaction Test Power (46%):**
   - Non-significant result could be Type II error
   - **Mitigation:** Authors now acknowledge this explicitly in "Equipoise" section; don't claim to have proven equivalence
   - **Verdict:** Appropriately handled

3. **Simulation Assumptions:**
   - Cannot test every possible functional form
   - **Mitigation:** Tested 6 diverse models; findings remarkably consistent
   - **Verdict:** Robustness adequately demonstrated

4. **Pre-Specification Uncertainty:**
   - Unknown if EF=50% was pre-specified or post-hoc
   - **Mitigation:** Authors acknowledge this; note even pre-specified thresholds need validation
   - **Verdict:** Acknowledged transparently

**Overall Methodological Grade:** **A**

The methodology is rigorous, transparent, and fit for purpose. Model 6 addition completes the validation framework.

---

## SPECIFIC SECTION ASSESSMENTS

### Abstract (Grade: A)

**Strengths:**
- Concise, clear, well-structured
- 399 words (perfect for 400-word limit)
- Appropriately softened conclusions
- Methods clearly described
- Key results highlighted

**Weaknesses:**
- None significant

**Recommendation:** Accept as-is

---

### Introduction (Grade: A-)

**Strengths:**
- Clear motivation and context
- Biological implausibility argument well-made
- Statistical challenges clearly outlined
- Objectives clearly stated

**Weaknesses:**
- Slightly long at 1,193 words
- Could be condensed to ~700-800 words for word count compliance

**Recommendation:** Condense by ~30-40% for word count

---

### Methods (Grade: A)

**Strengths:**
- Comprehensive, reproducible
- All 6 simulation models clearly described
- Statistical equations provided
- Cross-validation methodology well-explained

**Weaknesses:**
- Very detailed (2,131 words)
- Some details could move to supplement (e.g., equation derivations, parameter justifications)

**Recommendation:** Move technical details to supplement; keep core methods in main text (~1,200-1,400 words)

---

### Results (Grade: A)

**Strengths:**
- "Equipoise, Not Certainty" section is excellent
- Fragility index properly contextualized
- Model 6 results clearly presented (Table 6B)
- Interpretation section ("What Can/Cannot Be Concluded") is outstanding
- Tables are clear and informative

**Weaknesses:**
- Long (3,053 words)
- Some tables/details could move to supplement

**Recommendations:**
- Move detailed simulation results to supplement
- Keep empirical findings and key simulation results in main text
- **Target:** ~1,800-2,000 words

---

### Discussion (Grade: A-)

**Strengths:**
- Comprehensive, thoughtful
- "What Evidence Would Be Convincing?" section is excellent (6 criteria framework)
- Limitations transparently discussed
- Call to Action is collaborative, not demanding
- Clinical implications clearly stated

**Weaknesses:**
- **Very long** (3,476 words - nearly a full paper by itself)
- Call to Action could be separate commentary/perspective piece
- Some stakeholder recommendations could move to supplement

**Recommendations:**
- **Critical:** Condense Discussion to ~1,500-1,800 words
- Consider publishing "Call to Action" as separate BMJ commentary
- Move extended recommendations to supplement
- **This section requires the most aggressive editing**

---

## STATISTICAL VALIDITY ASSESSMENT

### Empirical Analyses

✅ **Interaction Test:** Correctly calculated (p=0.069)
✅ **Fragility Index:** Appropriately calculated and contextualized
✅ **Power Analysis:** Both subgroup and interaction power correctly assessed
✅ **Pooled Effect:** Inverse-variance weighting correctly applied
✅ **Confidence Intervals:** Appropriately emphasized over p-values

**Assessment:** All empirical statistical analyses are valid and appropriate.

### Simulation Studies

✅ **Design:** Matches actual trial structure appropriately
✅ **Sample Size:** 10,000 iterations provides stable estimates
✅ **Models Tested:** 6 models cover diverse scenarios comprehensively
✅ **Model 6 (NEW):** Tests sensitivity; demonstrates cross-validation can detect true thresholds
✅ **Statistical Methods:** Cox models, leave-one-trial-out validation correctly implemented
✅ **False-Positive Rates:** Confidence intervals appropriately calculated

**Assessment:** Simulation methodology is sound, well-designed, and appropriately analyzed.

---

## CLINICAL IMPORTANCE

**Impact:** **HIGH**

This manuscript addresses a high-profile claim that is:
- Being cited in editorials and guideline discussions
- Potentially affecting millions of patients
- From prestigious journals (Lancet, NEJM)
- From high-quality IPD meta-analyses

The authors demonstrate that this claim:
- Fails interaction testing (p=0.069)
- Is extremely fragile (FI=3)
- Is severely underpowered (40%)
- Has 47% chance of being a false positive based on simulations

**Clinical Implication:** This work could prevent adoption of questionable subgroup-based guideline recommendations.

**Methodological Contribution:** The validation framework (6 criteria + cross-validation approach) is generalizable and could improve standards for subgroup claims.

**Verdict:** High-impact contribution to both cardiology and methodological literature.

---

## TONE AND PRESENTATION ASSESSMENT

### Previous Version Issues - NOW RESOLVED ✅

**Before:** Confrontational, demanding, sometimes adversarial
**After:** Professional, collaborative, scientifically balanced

**Specific Improvements:**
- "We specifically call on" → "We respectfully encourage"
- "mandatory" → "recommended"
- "statistical artifacts" → "questionable subgroup findings"
- Realistic timelines (3-6 months instead of 3 months)
- Acknowledgment of effort required ("We recognize this requires substantial effort")

**Assessment:** Tone is now appropriate for BMJ. Will not alienate original investigators or guideline committees. Professional and constructive.

---

## COMPARISON TO SIMILAR PUBLISHED WORK

This manuscript compares favorably to:

1. **Wallach et al. (JAMA 2017)** - Credibility of subgroup claims
   - This work: More focused, includes simulations, proposes validation framework
   - **Advantage:** Deeper methodological contribution

2. **Schandelmaier et al. (BMJ 2020)** - ICEMAN tool
   - This work: Applies principles to specific high-profile case + provides empirical validation
   - **Advantage:** Demonstrates real-world application

3. **Wang et al. (JAMA IM 2021)** - Fragility indices in clinical trials
   - This work: Combines fragility with interaction testing, power analysis, cross-validation
   - **Advantage:** More comprehensive validation approach

**Verdict:** This manuscript makes a novel, important contribution that extends existing literature.

---

## LIKELIHOOD OF ACCEPTANCE (BMJ)

**If Word Count Is Addressed:** 85-90%

**Likely Editorial Decision:** **Accept with minor revisions** (word count reduction)

**Likely Reviewer Comments:**
"The authors have substantially strengthened the manuscript. The equipoise language is appropriate, the clinical guidance is comprehensive, and the simulation robustness is impressive. The addition of Model 6 testing cross-validation sensitivity addresses the major methodological concern. The manuscript requires condensing to meet word count limits, but the scientific content is sound and ready for publication."

**Probability of Major Revision:** <10% (only if word count not addressed)

**Probability of Rejection:** <5% (methodology is strong, topic is important)

---

## SPECIFIC RECOMMENDATIONS FOR AUTHORS

### 🔴 REQUIRED FOR ACCEPTANCE

**1. Address Word Count (CRITICAL - Non-Negotiable)**
   - **Current:** 10,524 words
   - **Target:** 3,000-4,000 words
   - **Strategy:**
     * Move simulation details to supplement (~1,000 words saved)
     * Consider Call to Action as separate commentary (~800 words saved)
     * Condense Discussion by 40% (~1,400 words saved)
     * Streamline Introduction (~300 words saved)
     * Move stakeholder recommendations to supplement (~500 words saved)
   - **Timeline:** 2-3 hours of careful editing
   - **Priority:** **MANDATORY**

### ✅ OPTIONAL (NICE-TO-HAVE)

**2. Create Supplementary Materials**
   - Supplementary Table S1: Detailed calculations (2×2 tables, FI steps, parameter derivations)
   - Supplementary Methods: Extended simulation details
   - Supplementary Results: Complete 6-model comparison tables
   - **Priority:** Low (can add if BMJ requests)

**3. Consider Companion Commentary**
   - Publish "Call to Action" as separate BMJ perspective/commentary piece
   - Would be high-visibility, allow full development of stakeholder recommendations
   - Could cite main manuscript and expand on practical implementation
   - **Priority:** Optional but recommended

---

## BOTTOM LINE

### What Has Been Accomplished

The authors have transformed this manuscript from vulnerable (Grade B+) to publication-ready (Grade A-). Specifically:

✅ **9 of 10 critical issues resolved**
✅ **Model 6 added - excellent work**
✅ **Tone transformed to professional/collaborative**
✅ **Limitations transparently acknowledged**
✅ **Clinical guidance comprehensive**
✅ **Methodology rigorous and complete**

### What Remains

🔴 **Word count reduction (CRITICAL)**
⚠️ Supplementary details (optional)

### Recommendation

**ACCEPT WITH MINOR REVISIONS**

**Required Revisions:**
1. Condense manuscript to 3,000-4,000 words (move content to supplement)

**Optional Revisions:**
2. Add supplementary calculation details if requested by editors

**Timeline for Revision:** 1 week (2-3 hours for word count editing + time for author review)

**Likelihood of Acceptance After Revision:** 90-95%

---

## FINAL VERDICT

**Scientific Quality:** A
**Methodological Rigor:** A
**Clinical Importance:** High
**Writing Quality:** A-
**Word Count Compliance:** F (must fix)

**Overall Recommendation:** **ACCEPT WITH MINOR REVISIONS** (word count reduction required)

**Expected Publication Decision:** **Accept** after word count addressed

**Impact Potential:** High - will influence guideline development and methodological standards for subgroup analyses

---

**Reviewer Signature:** BMJ Reviewer #2 (Biostatistics/Methodology)
**Date:** November 17, 2025
**Conflicts of Interest:** None

---

## MESSAGE TO AUTHORS

You have done excellent work addressing my previous concerns. The manuscript is now methodologically rigorous, clinically important, and publication-worthy. The Model 6 addition was exactly what was needed - it demonstrates that cross-validation has both the specificity to reject false thresholds AND the sensitivity to detect true ones. This completeness makes your proposed validation framework credible and implementable.

The one remaining hurdle is word count. BMJ is strict about this, and at 10,500 words (vs 3,000-4,000 required), you'll need to condense substantially. However, the scientific content is strong - this is purely a formatting issue, not a scientific one.

I recommend:
1. Move detailed methods to supplement
2. Consider publishing the Call to Action as a separate BMJ commentary (it's excellent and deserves full development)
3. Condense Discussion by ~40%
4. Streamline Introduction slightly

With these changes, this will be a high-impact BMJ publication. Congratulations on the rigorous, important work.
