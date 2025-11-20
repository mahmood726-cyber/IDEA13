# BMJ EDITORIAL REVIEW
## Manuscript ID: [To be assigned]

---

**Title:** Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework

**Manuscript Type:** Research Article

**Date of Review:** November 20, 2025

**Reviewers:** Senior Statistical Editor + 2 External Peer Reviewers

**Handling Editor:** [Name], Deputy Editor, BMJ

---

## EDITORIAL DECISION: **ACCEPT WITH MAJOR REVISIONS**

---

## OVERALL ASSESSMENT

This manuscript addresses an important and timely methodological question about the validation of subgroup claims from individual patient data (IPD) meta-analyses. The authors critique a recently published ejection fraction threshold for beta-blocker therapy after myocardial infarction (published in *Lancet* and *NEJM*, August-November 2025) and propose a validation framework applicable to all subgroup analyses.

**Strengths:**
- Highly relevant and timely topic addressing recent high-profile publications
- Rigorous dual approach (empirical analysis + simulation studies)
- Novel methodological contribution (Model 6 sensitivity testing)
- Well-written and clearly structured
- Transparent about limitations
- Proposes actionable validation framework

**Weaknesses requiring revision:**
- Lack of access to individual patient data limits definitive conclusions
- Some overstatement of certainty in conclusions
- Missing critical references to original Lancet/NEJM papers
- Figures not provided for review
- Tone occasionally veers toward advocacy rather than neutral scientific reporting
- Several statistical and presentation issues detailed below

**The manuscript has substantial merit but requires significant revisions before it can be accepted for publication in BMJ.**

---

## MAJOR CONCERNS REQUIRING REVISION

### 1. **CRITICAL: Missing References to Original Studies**

**Issue:** References [8] and [9] cite "Rossello et al., *Lancet*, August 2025" and "*NEJM*, November 2025" but do not provide complete citation information (volume, pages, DOI). More critically, **the authors have not verified whether these papers have actually been published as of November 20, 2025.**

**Required action:**
- Provide complete citations with DOI
- If papers are not yet published (or are only available as preprints/early online), this must be explicitly stated and the manuscript timeline adjusted accordingly
- The cover letter claims these are "recent" publications from August/November 2025, but the current date is November 20, 2025, which would make the NEJM paper extraordinarily recent
- **Please verify publication status and provide PMIDs/DOIs**

**Severity:** This is a critical omission that prevents editorial evaluation.

---

### 2. **Overstatement of Conclusions Despite Acknowledged Limitations**

**Issue:** The abstract and discussion draw strong conclusions ("may reflect statistical overfitting", "likely represents a statistical artifact") despite explicitly acknowledging in the limitations that:

- "Lack of IPD access prevented us from performing continuous LVEF modeling with splines, direct cross-validation, or examining trial-specific effects"
- "Our conclusions rest primarily on simulation evidence rather than direct IPD reanalysis and are therefore **provisional**"
- The interaction test had only 46% power, meaning "we cannot definitively rule out true subgroup differences"

**Contradiction:** You cannot simultaneously claim conclusions are "provisional" and that evidence "likely represents" an artifact. The strength of language in conclusions exceeds what the available evidence supports.

**Required revisions:**

**Abstract - Conclusions section (currently):**
> "The LVEF 50% threshold has not been adequately validated and **may reflect** statistical overfitting..."

**Suggested revision:**
> "The LVEF 50% threshold has not been adequately validated. Our analyses raise concerns about statistical overfitting, but definitive conclusions require IPD analysis with continuous modeling."

**Discussion - Principal Findings (currently):**
> "...suggest the EF=50% threshold **likely represents** a statistical artifact from underpowered subgroup analysis..."

**Suggested revision:**
> "...raise substantial concerns that the EF=50% threshold may represent a statistical artifact, though definitive determination requires IPD analysis with continuous LVEF modeling."

**Discussion - Conclusions (currently):**
> "The proposed ejection fraction threshold for beta-blocker therapy does not meet statistical validation criteria and **likely represents** an artifact..."

**Suggested revision:**
> "The proposed ejection fraction threshold for beta-blocker therapy does not meet conventional validation criteria. While our analyses raise serious concerns about statistical overfitting, definitive conclusions require continuous modeling of IPD."

**Rationale:** BMJ requires that the strength of conclusions match the strength of evidence. Your limitations section correctly identifies that you lack IPD access and that conclusions are "provisional"—your abstract and conclusions must reflect this uncertainty.

---

### 3. **Tone: Advocacy vs. Objective Scientific Reporting**

**Issue:** Several passages read more like advocacy for a position than neutral scientific reporting. Examples:

**Introduction (lines 67-68):**
> "The notion that these medications confer benefit at LVEF 49% but none at 51% lacks mechanistic plausibility."

**Comment:** This is a strawman argument. The original authors likely did not claim a "sharp" discontinuity at exactly 50% but rather used it as a pragmatic clinical cutpoint. Your characterization may misrepresent their position.

**Discussion:**
> "We respectfully encourage the beta-blocker IPD investigators to perform internal cross-validation..."

**Comment:** While well-intentioned, BMJ research articles should report findings neutrally. "Encouraging" other investigators is more appropriate for a commentary or editorial than a research article.

**Required revisions:**
- Remove advocacy language ("we encourage", "we call for")
- Present the biological plausibility argument more neutrally: "The biological mechanisms underlying beta-blocker effects would be expected to vary continuously rather than exhibiting sharp discontinuities at specific LVEF values"
- Let the data speak for itself without editorializing

**Suggested new paragraph for Discussion:**
> "Our findings highlight the need for rigorous validation of subgroup claims before guideline incorporation. Continuous modeling of IPD with methods such as restricted cubic splines could clarify whether treatment effects vary gradually or exhibit discontinuities across the LVEF spectrum."

---

### 4. **Figures Not Provided**

**Issue:** The manuscript references "Figure 1", "Figure 2", and "Figure 3" throughout but states "Figures 1-3 and Figure 5 (referenced throughout this manuscript) are in preparation."

**BMJ Policy:** Manuscripts cannot be fully evaluated without figures. Figure quality, clarity, and accuracy are critical for peer review.

**Required action:**
- Provide all 3 main text figures as separate high-resolution files
- Ensure Figure 1 (forest plot) clearly shows the non-significant interaction
- Ensure Figure 2 (false-positive rates) uses colorblind-friendly palette
- Ensure Figure 3 (p-value distributions) includes all panels described in legend
- Remove reference to "Figure 5" (appears to be an error—no Figure 5 exists in the manuscript)

**Note on Results section (line 7):**
> "**Note on Figures:** Figures 1-3 and Figure 5 (referenced throughout this manuscript) are in preparation..."

This note is inappropriate for a submitted manuscript. Figures must be complete at submission.

---

### 5. **Statistical Concern: Fragility Index Interpretation**

**Issue:** The authors correctly calculate the fragility index (FI=3) but may overinterpret its meaning for time-to-event analyses.

**Current statement (Results, lines 251-253):**
> "The fragility index for the EF 40-49% finding was **3 events**—meaning only 3 events (1.3% of 235 total) need reclassification to eliminate statistical significance (p≥0.05)."

**Concern:** The fragility index was developed for binary outcomes in RCTs and its extension to time-to-event meta-analyses is not well-established. The method of "transferring events" from control to treatment group doesn't account for:
- Timing of events
- Censoring patterns
- Competing risks

**Required action:**
- Add caveat: "We note that fragility index methods were developed for binary outcomes; their application to time-to-event analyses may not fully account for censoring and event timing."
- Consider sensitivity analysis using different fragility methods for survival data
- Alternatively, de-emphasize FI and focus more on power analysis and interaction test

**Reference needed:** Add citation to Bertagnolli et al. (2019, JAMA Oncol) who discuss limitations of FI for time-to-event outcomes.

---

### 6. **Simulation Assumptions Need Justification**

**Issue:** The simulation study programs a "smooth, continuous decline" in treatment effect (HR 0.70 at EF=40% → HR=0.90 at EF=50%). This is an assumption, not an established truth.

**Current Methods (lines 172-176):**
> "Crucially, we programmed a smooth, continuous relationship between LVEF and treatment effect with **no threshold at any specific value**... This produces HR=0.70 at EF=40%, declining linearly to HR=0.90 at EF=50%, with no discontinuity."

**Concern:**
1. Why HR=0.70 at EF=40%? This appears chosen to match the observed data, creating circularity
2. Why linear decline? Could be exponential, logarithmic, step-function, etc.
3. The assumption of "no threshold" is precisely what's being debated—you cannot assume your conclusion

**Required revisions:**
- Acknowledge this is an assumption: "We assumed a smooth continuous relationship as the null hypothesis against which to test threshold detection methods"
- Better justify the choice of HR=0.70→0.90: "We calibrated effect sizes to approximately match the range observed in the empirical data (HR 0.75 at EF 40-49%, HR 0.97 at EF ≥50%)"
- Emphasize that Models 2-6 test robustness to this assumption, including Model 6 where a TRUE threshold exists

**Strength:** You did test multiple functional forms (Models 1-6), which partially addresses this concern. Make this more prominent.

---

### 7. **Model 6 Results Insufficiently Emphasized**

**Issue:** Model 6 is your most important methodological contribution—demonstrating cross-validation has both sensitivity (68.7%) AND specificity (98.5%). Yet it's buried in Results.

**Current placement:**
- Model 6 appears on page [~X] of Results
- Only one table (Table 6B)
- Not mentioned in abstract

**Required revisions:**

**Abstract - Results section:** Add one sentence:
> "When a true threshold existed at EF=50% (Model 6), cross-validation successfully detected it in 68.7% of simulations while maintaining 98.5% specificity, demonstrating balanced diagnostic performance."

**Discussion:** Create dedicated subsection:
> "### Cross-Validation Has Both Sensitivity and Specificity
>
> Our Model 6 sensitivity analysis addresses a critical question: while cross-validation reduces false-positives, could it miss true thresholds? We found that when a genuine threshold existed precisely at EF=50% matching the observed effect sizes, cross-validation detected it in 68.7% of simulations—demonstrating good sensitivity while maintaining excellent specificity (98.5% from Models 1-5). This balanced diagnostic performance (positive predictive value 97.8%) makes cross-validation suitable for distinguishing true biological heterogeneity from statistical artifacts."

**Rationale:** This is genuinely novel and publishable on its own. Previous literature has focused on cross-validation's specificity; demonstrating sensitivity is new.

---

## MODERATE CONCERNS REQUIRING REVISION

### 8. **Interaction Test Interpretation**

**Issue:** p=0.069 is very close to 0.05. While technically non-significant, this is borderline.

**Current interpretation (Results, line 234):**
> "The formal test for interaction... yielded **p=0.069** (Z=-1.819), **failing to reach statistical significance.**"

**Comment:** "Failing" has negative connotation. Also, with only 46% power, this p-value is not reassuring evidence of no difference.

**Suggested revision:**
> "The formal test for interaction yielded p=0.069 (Z=-1.819), which did not reach conventional statistical significance (p<0.05). However, with only 46% power, this test cannot reliably distinguish between no difference and a true moderate difference."

**Your "Equipoise, Not Certainty" section (lines 247-249) handles this well—make sure this balanced interpretation appears consistently.**

---

### 9. **Pooled Analysis Justification**

**Issue:** You pool EF 40-49% and EF ≥50% subgroups to get HR 0.94 (0.85-1.03) and conclude "no significant benefit." But the original investigators separated these groups precisely because they hypothesized differential effects.

**Concern:** If a true threshold exists, pooling across it would mask real effects in the EF 40-49% group. Your pooled analysis assumes the conclusion you're trying to test.

**Current statement (Results, line 279):**
> "When both EF ranges were combined, the pooled hazard ratio was **HR 0.94 (95% CI 0.85-1.03, p=0.25)**—no significant benefit across the entire LVEF spectrum from 40% onward..."

**Required revision:**
> "When both EF ranges were combined (assuming homogeneous effects), the pooled hazard ratio was HR 0.94 (95% CI 0.85-1.03, p=0.25). However, this pooled estimate should be interpreted cautiously, as it assumes no true subgroup differences—the hypothesis being tested."

**Better approach:** Present the pooled analysis as exploratory, not definitive. The interaction test is the appropriate statistical test, not the pooled estimate.

---

### 10. **Multiple Testing Adjustment**

**Issue:** You test 13 thresholds (42%, 42.5%, ... 48%) in your simulation "Method 1" and find 46.8% false-positive rate. This is expected without multiple testing adjustment.

**Current interpretation:** You correctly identify this as a problem with "multiple threshold testing."

**Missing:** You don't discuss whether the original Lancet/NEJM investigators tested multiple thresholds. Do you have evidence they did? Or are you assuming they did?

**Required addition to Discussion:**
> "We note that the original publications do not explicitly report testing multiple EF thresholds. However, the choice of EF=50% as the cutpoint—which is a round number and plausible clinical threshold—raises the possibility of data-driven threshold selection, even if unintentional. Transparent reporting of all tested thresholds is essential for interpreting subgroup findings."

**Tone:** Keep this neutral. You're raising a methodological concern, not accusing anyone of misconduct.

---

### 11. **Power Analysis for Fragility Index**

**Issue:** You state FI=3 is "extremely fragile" but don't discuss whether this is unusual given the sample size.

**Current statement (Results, lines 253-263):**
> "Walsh et al. recommend FI>5 for minimally robust findings and >10 for practice-changing claims. A fragility index of 3 indicates extreme statistical instability."

**Missing context:**
- How does FI=3 with N=1,885 and 235 events compare to other meta-analyses of similar size?
- Is the fragility due to small sample size or genuinely questionable finding?

**Suggested addition:**
> "While fragility indices are influenced by sample size, even accounting for the modest event count (N=235), an FI of 3 represents only 1.3% of observed events. For comparison, meta-analyses with similar sample sizes but more robust findings typically achieve fragility indices of 8-15 events (3-6% of total).[reference]"

**Good news:** You have this discussion in the supplementary materials (S4). Move it to main text.

---

### 12. **Biological Plausibility Section Needs Nuance**

**Current statement (Introduction, lines 67-68):**
> "The notion that these medications confer benefit at LVEF 49% but none at 51% lacks mechanistic plausibility."

**Issues:**
1. Strawman argument (see Major Concern #3 above)
2. Many biological processes DO exhibit thresholds (e.g., ischemic threshold for chest pain, glucose threshold for diabetes diagnosis)
3. While LVEF itself is continuous, it may be a marker for underlying categorical states (e.g., presence/absence of myocardial scar)

**Suggested revision:**
> "While beta-blocker mechanisms (heart rate reduction, neurohormonal modulation) would be expected to vary continuously with LVEF, clinical practice often requires dichotomous decision rules. The question is whether a sharp discontinuity in treatment effect exists at a specific LVEF value, or whether any threshold represents a pragmatic approximation of a gradual relationship."

**Rationale:** More balanced, acknowledges legitimate reasons for thresholds in clinical practice.

---

## MINOR CONCERNS AND SUGGESTIONS

### 13. **Abstract Structure**

**Current:** The abstract uses bold subheadings (**Background**, **Methods**, **Results**, **Conclusions**, **Implications**).

**BMJ style:** Check whether BMJ prefers structured abstracts with these exact headings. If so, this is correct. If BMJ uses different headings (e.g., "Objective", "Design", "Setting", "Participants", "Main Outcome Measures"), please reformat.

**Word count:** 329 words is within the 350-word limit. ✓

---

### 14. **Tables**

**Table 1:** Excellent. Clear and interpretable.

**Table 2:** Excellent. The "Met?" column with ❌ is helpful but may not render in all PDF converters. Suggest using "No" instead of emoji.

**Table 3:** Good. Consider adding one more row:
| 0.95 | [calculate] | No |

to show that even for tiny effects, power is inadequate.

**Table 4:** The "Passes?" column with ❌ is clear. Same emoji concern as Table 2.

**Table 5:** Excellent. Central finding clearly presented.

**Table 6:** Good. Consider combining Tables 6 and 6B into one comprehensive table.

**Overall:** Tables are high quality. Ensure all render correctly as PDF.

---

### 15. **Discussion Structure**

**Current structure:**
- Principal Findings
- Interpretation (with subsections)
- Strengths and Limitations
- Clinical and Guideline Implications
- Recommendations
- Conclusions

**Suggestion:** Consider BMJ's preferred discussion structure:
1. Statement of principal findings
2. Strengths and weaknesses of the study
3. Comparison with other studies
4. Meaning of the study (implications for clinicians and policymakers)
5. Unanswered questions and future research

**Your current structure is good, but check BMJ author guidelines.**

---

### 16. **References**

**Issue:** Reference list is marked as "Placeholder" and incomplete.

**Required action:**
- Provide complete reference list formatted per BMJ Vancouver style
- Ensure all in-text citations [1-36] have corresponding references
- Add missing references:
  - References [10-12] (editorials/guideline statements)
  - Reference [15] (mechanistic study)
  - All references in supplementary materials

**Critical:** References [8] and [9] MUST have complete citations (see Major Concern #1).

---

### 17. **Supplementary Materials**

**Strengths:**
- Comprehensive (6,800 words)
- Well-organized
- Tables S1 and S2 are excellent practical tools

**Suggestions:**
- Table S1 (Six Validation Criteria): Consider moving to main text. This is central to your framework and shouldn't be hidden in supplement.
- Table S2 (Guideline Committee Checklist): Same comment. This is highly actionable for guideline committees.
- Figure S3 (ROC curve): This might be worth promoting to main text. Shows sensitivity/specificity trade-off clearly.

**If word count allows, move Tables S1-S2 to main text.** They are too important for supplement.

---

### 18. **Code Availability**

**Current statement:**
> "Simulation code is publicly available at [GitHub repository to be added upon publication]."

**BMJ policy:** Code should be available at time of review, not just publication.

**Required action:**
- Deposit code in GitHub or Zenodo NOW
- Provide link to reviewers (can be anonymized repository if needed for blinding)
- Update manuscript with permanent link

**Rationale:** Reviewers need to evaluate reproducibility.

---

## SPECIFIC EDITORIAL QUERIES

### Q1: Author Contributions
The manuscript lists "[To be added]" for author contributions. BMJ requires:
- CRediT taxonomy contributions for each author
- Guarantor identified
- All authors must approve submission

**Action:** Complete before resubmission.

---

### Q2: Conflicts of Interest
You declare "None." Please confirm:
- No financial relationships with organizations that might have an interest in the submitted work
- No other relationships or activities that could appear to have influenced the submitted work
- No relationships with the original Lancet/NEJM investigators that could be perceived as conflicts

**Action:** Confirm in cover letter.

---

### Q3: Patient and Public Involvement
You state "Not applicable (analysis of published aggregate data only)."

**BMJ's stance:** Even for secondary analyses, patient and public involvement is encouraged. Did you consult patients about:
- The importance of this research question?
- Interpretation of findings?
- Dissemination plans?

**Action:** If no PPI, explain why not. If yes, describe briefly.

---

### Q4: Data Sharing
You state all data are from published sources. Please confirm:
- Exact source of all extracted data (which tables/figures from references [8] and [9])
- Whether you contacted original authors for any additional data
- Whether your extracted data matches what original investigators would provide if asked

**Action:** Add data extraction protocol to supplementary methods.

---

## PRESENTATION AND STYLE

### P1: Writing Quality
**Overall:** Excellent. Clear, concise, well-organized.

**Minor issues:**
- Line 7 (Results): "Figure 5" appears in error (should be Figure 3)
- Line 247: "Equipoise, Not Certainty" is a nice subsection title but not standard academic style. Consider "Interpretation of the Non-Significant Interaction Test"
- Avoid first person plural ("We do not claim...") when possible. Use passive voice: "This analysis does not demonstrate..."

---

### P2: Abbreviations
First use of abbreviations is correct (e.g., "left ventricular ejection fraction (LVEF)").

**Check:** Ensure all abbreviations defined at first use in:
- Abstract (separately from main text)
- Main text
- Each table footnote if used in table

---

### P3: Numbers and Statistics
**Current:** p-values reported as p=0.069 (correct, not p<0.05).

**Good practices observed:**
- CIs always provided with point estimates ✓
- Standard errors reported ✓
- Two-tailed tests specified ✓

**One issue:**
Line 235: "less than a coin flip" is informal. Suggest: "indicating high probability of Type II error."

---

## STATISTICAL REVIEW

The statistical methods are generally sound. The statistician reviewer raised these points:

### S1: Interaction Test
✓ Correctly performed
✓ Appropriate interpretation of p=0.069
✓ Power calculation correctly identifies low power

**Minor:** Consider adding heterogeneity test (I²) to quantify between-subgroup variability.

---

### S2: Simulation Design
✓ Well-designed with 10,000 iterations
✓ Multiple sensitivity analyses (Models 1-6)
✓ Appropriate statistical tests

**Minor concerns:**
- Assumption of exponential event times (discussed above in Major Concern #6)
- Calibration of parameters to match observed data creates some circularity
- Cross-validation criterion (≥1 of 4 trials) is somewhat arbitrary; sensitivity analysis with different criteria would strengthen

**Note:** You have cross-validation sensitivity analysis in Table S3. Consider promoting to main text.

---

### S3: Power Calculations
✓ Schoenfeld's formula correctly applied
✓ Range of true HRs tested (0.70-0.90)

**Excellent:** You calculated power of the interaction test itself—often overlooked.

---

### S4: Fragility Index
⚠️ Extension to survival outcomes not well-established (see Major Concern #5)

**Recommendation:** Either:
- Add strong caveats about FI for time-to-event data, OR
- De-emphasize FI and focus on power analysis

---

## REVIEWER COMMENTS

### Reviewer 1 (Statistician): **Accept with Major Revisions**

"This is an important contribution to the literature on subgroup analysis validation. The simulation study is well-designed and the Model 6 sensitivity analysis is genuinely novel. However, the authors overstate their conclusions given lack of IPD access. The tone is occasionally more advocacy than science. With revisions addressing the statistical concerns (particularly fragility index for survival data) and moderating the conclusions to match the strength of evidence, this would be an excellent BMJ paper."

**Key points:**
- Reduce certainty in conclusions
- Address fragility index concerns
- Promote Model 6 findings more prominently

---

### Reviewer 2 (Clinical Trialist): **Accept with Major Revisions**

"The authors make a valuable contribution by highlighting the lack of validation for the EF=50% threshold. However, I'm concerned about the biological implausibility argument, which seems to mischaracterize the original authors' claims. The original Lancet/NEJM papers likely did not claim a sharp discontinuity at exactly 50% but rather used it as a pragmatic clinical cutpoint. The simulation assuming 'no threshold' then tests this strawman. Despite this concern, the empirical analyses (interaction test, power, fragility) are valid and the call for better validation methods is warranted."

**Key points:**
- Revise biological implausibility section
- Clarify what original authors actually claimed
- Focus on empirical findings, not strawman arguments

---

## RECOMMENDATIONS FOR REVISION

### Required Changes (Major Revisions):

1. **Provide complete citations** for references [8] and [9] with DOI/PMID
2. **Provide all 3 figures** as separate high-resolution files
3. **Moderate conclusions** to match strength of evidence (see Major Concern #2)
4. **Revise tone** to neutral scientific reporting (remove advocacy language)
5. **Address fragility index** concerns for time-to-event data
6. **Better justify simulation assumptions** (why HR 0.70→0.90, why linear)
7. **Promote Model 6 findings** to abstract and give dedicated discussion subsection
8. **Complete author information** and contributions
9. **Provide GitHub repository link** with code (for reviewer evaluation)
10. **Format complete reference list** per BMJ Vancouver style

---

### Strongly Recommended Changes:

11. Add context for fragility index interpretation (comparison to similar-sized studies)
12. Revise biological implausibility section to be more balanced
13. Clarify pooled analysis limitations
14. Discuss whether original authors tested multiple thresholds
15. Consider moving Tables S1-S2 to main text (validation framework is central)
16. Add data extraction protocol to supplementary methods

---

### Optional Improvements:

17. Replace emoji symbols (❌, ⚠️) with text for PDF compatibility
18. Add heterogeneity statistics (I²) to interaction test
19. Consider combining Tables 6 and 6B
20. Add more comparison with existing subgroup analysis literature

---

## TIMELINE FOR RESUBMISSION

Given the extent of revisions required, we request resubmission within **6 weeks** (by January 1, 2026).

If you anticipate needing more time, please contact the editorial office.

---

## EDITOR'S SUMMARY

This manuscript makes an important and timely contribution to the literature on validating subgroup claims from IPD meta-analyses. The empirical analyses are sound, the simulation study is well-designed, and the proposed validation framework (Tables S1-S2) is practical and actionable. The Model 6 sensitivity analysis represents a genuine methodological advance.

However, several significant issues must be addressed before publication:

1. **Overstatement of conclusions** despite acknowledged limitations
2. **Figures not provided** for review
3. **Missing/incomplete references** (critical for evaluation)
4. **Tone occasionally too advocacy-oriented** rather than neutral reporting
5. **Statistical concerns** about fragility index for survival data

**With major revisions addressing these concerns, this manuscript would make an excellent contribution to BMJ and would likely be cited extensively by guideline developers and methodologists.**

The authors have done rigorous work on an important question. We encourage revision and resubmission.

---

## NEXT STEPS

1. Carefully review all major and moderate concerns listed above
2. Prepare detailed point-by-point response to reviewers
3. Revise manuscript addressing all required changes
4. Provide all 3 figures as high-resolution files
5. Complete reference list with full citations
6. Complete author information and contributions
7. Upload revised manuscript with track changes version

Please submit:
- Revised manuscript (clean version)
- Revised manuscript (track changes version)
- Point-by-point response to reviewers
- All figure files (separate, high-resolution)
- Supplementary materials (updated if needed)
- Cover letter addressing major concerns

---

**Decision:** ACCEPT WITH MAJOR REVISIONS

**Anticipated outcome if revisions satisfactory:** Accept for publication

**Potential impact:** High (challenges recent high-profile publications, proposes actionable framework, likely to be cited by guideline committees)

---

Sincerely,

**[Editor Name]**
Deputy Editor, BMJ
[Contact information]

---

**Date of Decision:** November 20, 2025
**Manuscript ID:** [To be assigned]
**Revision Due:** January 1, 2026

---

## EDITORIAL CHECKLIST

- ✅ Manuscript reviewed by 2 external peer reviewers
- ✅ Statistical review completed
- ✅ Editorial assessment completed
- ✅ Decision letter prepared
- ⏳ Awaiting author revisions
- ⏳ Re-review after revision
- ⏳ Final acceptance decision

**END OF EDITORIAL REVIEW**
