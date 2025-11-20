# Cover Letter for BMJ Submission

**Date:** [To be added]

**To:** The Editor, BMJ

**Re:** Submission of Research Article

---

Dear Editor,

We are pleased to submit our manuscript entitled **"Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework"** for consideration as a Research Article in the BMJ.

## Why This Study Matters for BMJ Readers

In August and November 2025, two companion individual patient data (IPD) meta-analyses published in *The Lancet* and *New England Journal of Medicine* concluded that beta-blockers benefit post-myocardial infarction patients with left ventricular ejection fraction (LVEF) 40-49% but not those with LVEF ≥50%, proposing a sharp efficacy threshold at exactly 50%. These findings have sparked calls for ejection fraction-stratified guideline recommendations that would affect millions of patients worldwide.

Our rigorous evaluation reveals that this proposed threshold does not meet basic statistical validation criteria and likely represents a statistical artifact rather than genuine biological heterogeneity. Through empirical analysis of the published data and comprehensive simulation studies, we demonstrate systematic problems with how subgroup effects are identified, validated, and translated into clinical practice recommendations.

## Key Findings

1. **The proposed threshold fails all validation tests:** The interaction test was non-significant (p=0.069, power=46%), the finding was extremely fragile (fragility index=3 events, only 1.3% of total), the analysis was severely underpowered (40% power), and when both EF ranges were pooled, no significant benefit emerged (HR 0.94, 95% CI 0.85-1.03).

2. **Testing multiple thresholds produces false-positives in nearly half of analyses:** Our simulations demonstrate that when continuous variables are dichotomized and multiple thresholds are tested, spurious "significant" findings arise in 46.8% of analyses even when no true threshold exists.

3. **Cross-validation provides a 31-fold reduction in false-positive rates:** Leave-one-trial-out cross-validation—rarely applied despite availability of IPD—correctly rejects 98.5% of false threshold claims while maintaining good sensitivity (68.7%) for detecting true thresholds.

4. **We propose a practical validation framework:** Four criteria (significant interaction test, adequate statistical power, fragility index >5, and cross-validation) should be required before subgroup claims inform guideline recommendations.

## Novelty and Impact

This work makes three distinct contributions:

**Methodological Innovation:** Model 6 in our simulation study is the first to assess cross-validation's **sensitivity** (ability to detect true thresholds) in addition to specificity (ability to reject false thresholds), demonstrating that cross-validation achieves both excellent specificity (98.5%) and good sensitivity (68.7%)—a balanced diagnostic performance crucial for distinguishing signal from noise.

**Immediate Clinical Relevance:** Our findings directly challenge high-profile recent publications in leading journals that are currently informing guideline discussions. Timely publication in BMJ could prevent premature adoption of potentially spurious practice recommendations affecting millions of post-MI patients.

**Generalizable Framework:** While focused on beta-blockers and ejection fraction, our validation criteria apply broadly to any subgroup claim in any clinical area. The framework provides guideline committees with actionable, quantitative criteria for evaluating subgroup evidence.

## Why BMJ?

BMJ is the ideal venue for this work for several reasons:

1. **Readership:** BMJ's broad international readership includes clinicians, guideline developers, and policymakers who directly translate evidence into practice—precisely the audience that needs to see these findings before EF-stratified recommendations are adopted.

2. **Mission Alignment:** This work exemplifies BMJ's commitment to rigorous evaluation of clinical evidence and challenging accepted practices when evidence is insufficient. The manuscript asks difficult questions about how we validate subgroup claims before changing clinical practice.

3. **Prior Coverage:** BMJ has published seminal work on subgroup analysis methodology (Burke et al. 2015, "Three simple rules to ensure reasonably credible subgroup analyses") and continues to lead discussions on evidence quality and guideline development.

4. **Impact and Accessibility:** BMJ's open access model and public health focus would ensure these methodological insights reach the widest possible audience, including guideline committees currently deliberating beta-blocker recommendations.

5. **Timeliness:** The companion *Lancet* and *NEJM* publications appeared in August and November 2025. Rapid BMJ publication would provide timely counterbalance while guideline discussions are active.

## Transparency and Rigor

We have ensured complete transparency throughout:

- All analyses used published aggregate data only (no privileged access to unpublished data)
- Complete Python code for all empirical analyses and simulations will be publicly available via GitHub
- We explicitly acknowledge limitations (lack of individual patient data for continuous modeling)
- Our tone is collaborative rather than confrontational—we call for the original investigators to apply cross-validation to their IPD, which would definitively resolve the question
- We do not claim to have proven the threshold is false; rather, we argue evidence is insufficient for practice-changing recommendations

## Compliance with BMJ Policies

We confirm:
- The manuscript has not been published elsewhere and is not under consideration by another journal
- All authors have approved the manuscript and agree with submission to BMJ
- We declare no competing interests
- No specific funding was received for this research
- All data and code will be made publicly available
- Ethical approval was not required (analysis of published aggregate data and simulated data only)

## Format and Word Count

- **Main text:** 4,129 words (close to BMJ's ~4,000-word target for research articles)
- **Abstract:** 329 words (within 350-word limit)
- **Tables:** 6 main text tables, 4 supplementary tables
- **Figures:** 3 main figures, 3 supplementary figures
- **Supplementary materials:** Comprehensive 6,800-word supplement with detailed methods, results, and complete validation framework

We have carefully condensed the manuscript while preserving all essential scientific content, with detailed methodological specifications provided in supplementary materials.

## Suggested Reviewers

We respectfully suggest the following potential reviewers with relevant expertise (no conflicts of interest):

1. **Dr. Joshua Wallach** (Yale University) - Expert on credibility of subgroup claims in randomized trials
2. **Dr. John Ioannidis** (Stanford University) - Leader in meta-research and evidence evaluation
3. **Dr. Stephen Senn** (Consultant Statistician) - Expert on interaction testing and subgroup analyses
4. **Dr. Frank Harrell** (Vanderbilt University) - Expert on continuous variable modeling and dichotomization hazards
5. **Dr. Sara Schroter** (BMJ) - Expert on reporting quality and research integrity

We are open to any reviewers the editors deem appropriate.

## Conclusion

This manuscript addresses a critical gap in how subgroup claims from IPD meta-analyses are validated before influencing clinical practice. The beta-blocker ejection fraction threshold serves as a timely, high-impact case study, but the implications extend far beyond this single example. We demonstrate that even rigorous IPD meta-analyses can produce questionable subgroup findings without proper validation procedures, and we provide practical, actionable solutions.

Given the immediate clinical stakes (guideline recommendations currently under discussion), the broad methodological implications (applicable to subgroup claims across all clinical areas), and BMJ's leadership in evidence-based medicine, we believe this work would be of great interest to your readership and would contribute meaningfully to ongoing discussions about evidence standards for guideline development.

We would be honored to have this work published in BMJ and look forward to your consideration.

Thank you for your time and attention.

Sincerely,

[Lead Author Name]
[Title and Affiliation]
[Email]
[ORCID]

On behalf of all co-authors:
[List all co-authors with affiliations]

---

## Contact Information

**Corresponding Author:**
[Name]
[Institution]
[Department]
[Address]
[Email]
[Phone]

---

## Manuscript Details

**Title:** Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework

**Manuscript Type:** Research Article

**Word Count:** 4,129 words (main text)

**Number of Tables:** 6 (main text), 4 (supplementary)

**Number of Figures:** 3 (main text), 3 (supplementary)

**Supplementary Materials:** Yes (comprehensive methods, results, tables, figures)

**Competing Interests:** None declared

**Funding:** None

---

**Attachments:**
1. Main manuscript (PAPER_1_FINAL_SUBMISSION.md)
2. Supplementary materials (PAPER_1_SUPPLEMENTARY_MATERIALS.md)
3. Figure files (Figures 1-3) [to be created]
4. Supplementary figure files (Figures S1-S3) [to be created]
5. STROBE checklist [if applicable]
6. Author contribution forms [to be completed]

---

**END OF COVER LETTER**
