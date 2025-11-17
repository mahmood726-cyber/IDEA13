# Introduction

Beta-blocker therapy after myocardial infarction (MI) has been a cornerstone of secondary prevention for decades, based on randomized trials conducted primarily in the pre-reperfusion era among patients with reduced left ventricular ejection fraction (LVEF).[1-3] However, the benefit of beta-blockers in contemporary patients with preserved or mildly reduced ejection fraction following MI—who now represent the majority of post-MI patients—has remained uncertain.[4,5] This uncertainty has prompted intense research interest and recent calls for re-evaluation of long-standing guideline recommendations.[6,7]

## Recent High-Profile Meta-Analyses Suggest a Sharp Threshold Effect

In August and November 2025, two companion individual patient data (IPD) meta-analyses from the same collaborative research group were published in *The Lancet* and the *New England Journal of Medicine* (NEJM), analyzing data from the same pool of contemporary randomized trials (REBOOT, BETAMI, DANBLOCK, and CAPITAL-RCT).[8,9] These analyses stratified patients by LVEF and reported strikingly different findings:

- **EF 40-49% (N=1,885):** Beta-blockers were associated with reduced risk of death, MI, or heart failure (hazard ratio [HR] 0.75, 95% CI 0.58-0.97, p=0.031).[8]

- **EF ≥50% (N=17,801):** Beta-blockers showed no significant benefit (HR 0.97, 95% CI 0.87-1.07, p=0.54).[9]

Based on these findings, the investigators concluded that a sharp efficacy threshold exists at LVEF=50%, with benefit in patients with mildly reduced ejection fraction but not in those with preserved function. Editorials and guideline committees have begun citing this work as evidence for ejection fraction-stratified treatment recommendations, with potential implications for millions of patients worldwide.[10-12]

## The Biological Implausibility of a Sharp Threshold

From a pathophysiological perspective, the claimed threshold is difficult to reconcile with known biology. Beta-blocker mechanisms—including heart rate reduction, anti-arrhythmic effects, and neurohormonal modulation—would be expected to vary gradually, not abruptly, across the ejection fraction spectrum.[13,14] The notion that these medications confer benefit at LVEF 49% but none at 51% lacks mechanistic plausibility and has not been demonstrated in basic or translational research.[15]

Moreover, ejection fraction itself is a continuous physiological variable measured with inherent imprecision (test-retest variability of 5-10%).[16,17] The idea that treatment decisions should pivot on a single percentage point—well within measurement error—raises fundamental questions about the robustness of the claimed threshold.[18]

## The Statistical Challenge: Overfitting in Subgroup Analyses

The divergent findings at EF <50% versus ≥50% exemplify a pervasive methodological challenge in clinical research: the identification of spurious subgroup effects through data-dependent threshold selection.[19-21] When continuous variables are dichotomized post hoc, investigators gain substantial "researcher degrees of freedom" to test multiple cutpoints until a "significant" result emerges.[22,23] This practice—whether intentional or inadvertent—capitalizes on random variation and produces findings that fail to replicate in independent datasets.[24,25]

The statistical hallmarks of such overfitting are well-characterized:[26,27]

1. **Non-significant interaction tests** between subgroups (suggesting the apparent difference may be due to chance)
2. **Underpowered subgroup analyses** (increasing susceptibility to false positives)
3. **Extreme statistical fragility** (findings that hinge on a small number of events)
4. **Failure to validate in held-out data** (cross-validation or external replication)

Despite these known risks, formal validation procedures—such as testing for statistical interaction, assessing fragility, or applying cross-validation—are rarely performed or reported in published subgroup analyses.[28,29] The absence of such checks leaves readers unable to distinguish genuine biological heterogeneity from statistical artifacts.

## Knowledge Gaps and Study Objectives

The beta-blocker ejection fraction threshold represents a critical test case for evaluating subgroup claims in IPD meta-analyses. To our knowledge, no published study has applied formal statistical validation to these findings, despite their potential to alter guideline recommendations and clinical practice worldwide.

**We therefore had three objectives:**

1. **To evaluate the statistical robustness** of the claimed EF=50% threshold using published summary data from both meta-analyses, including formal tests for interaction, power analysis, and fragility assessment.

2. **To quantify the false-positive rate** of spurious threshold detection when analyzing continuous variables through simulation studies matching the structure of the original trials.

3. **To propose a validation framework** for future subgroup claims from IPD meta-analyses, emphasizing methods that distinguish true biological heterogeneity from statistical overfitting.

We hypothesized that the EF=50% threshold would fail standard statistical validation tests and that simulation studies would demonstrate high false-positive rates for threshold detection when continuous variables are dichotomized without proper validation. Our findings have direct implications for the ongoing revision of clinical practice guidelines for beta-blocker therapy after MI.

---

## References (Placeholder)

[1] β-Blocker Heart Attack Trial Research Group. A randomized trial of propranolol in patients with acute myocardial infarction. *JAMA*. 1982.

[2] Norwegian Multicenter Study Group. Timolol-induced reduction in mortality and reinfarction in patients surviving acute myocardial infarction. *N Engl J Med*. 1981.

[3] CAPRICORN Investigators. Effect of carvedilol on outcome after myocardial infarction in patients with left-ventricular dysfunction. *Lancet*. 2001.

[4] Dahl Aarvik M, et al. Health outcomes with and without β-blocker therapy after myocardial infarction. *Eur Heart J*. 2024.

[5] Bangalore S, et al. β-Blocker use and clinical outcomes in stable outpatients with and without coronary artery disease. *JAMA*. 2012.

[6] Nauta ST, et al. Contemporary clinical practice of β-blocker use after myocardial infarction. *JACC*. 2024.

[7] Puymirat E, et al. β-Blockers and mortality after myocardial infarction in patients without heart failure. *JACC*. 2016.

[8] Rossello X, et al. β-blockers after myocardial infarction with mildly reduced ejection fraction. *Lancet*. 2025.

[9] Beta-Blockers after Myocardial Infarction with Normal Ejection Fraction. *N Engl J Med*. 2025.

[10] [Editorial reference]

[11] [Guideline committee statement]

[12] [Commentary]

[13] Freemantle N, et al. Beta blockade after myocardial infarction. *BMJ*. 1999.

[14] Packer M. Do β-blockers prevent or cause heart failure? *JACC*. 2013.

[15] [Mechanistic study reference]

[16] Otterstad JE, et al. Accuracy and reproducibility of biplane two-dimensional echocardiographic measurements of left ventricular dimensions and function. *Eur Heart J*. 1997.

[17] Wood PW, et al. Left ventricular ejection fraction and volumes. *JACC Cardiovasc Imaging*. 2014.

[18] Konstam MA, et al. Ejection fraction: misunderstood and overrated. *Circulation*. 2017.

[19] Burke JF, et al. Three simple rules to ensure reasonably credible subgroup analyses. *BMJ*. 2015.

[20] Sun X, et al. Credibility of claims of subgroup effects in randomised controlled trials. *BMJ*. 2012.

[21] Wallach JD, et al. Evaluation of evidence of statistical support and corroboration of subgroup claims in randomized clinical trials. *JAMA Intern Med*. 2017.

[22] Simmons JP, et al. False-positive psychology: undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychol Sci*. 2011.

[23] Gelman A, Loken E. The garden of forking paths. *Am Sci*. 2014.

[24] Yusuf S, et al. Analysis and interpretation of treatment effects in subgroups of patients in randomized clinical trials. *JAMA*. 1991.

[25] Assmann SF, et al. Subgroup analysis and other (mis)uses of baseline data in clinical trials. *Lancet*. 2000.

[26] Lagakos SW. The challenge of subgroup analyses. *N Engl J Med*. 2006.

[27] Wang R, et al. Statistics in medicine—reporting of subgroup analyses in clinical trials. *N Engl J Med*. 2007.

[28] Schandelmaier S, et al. Development of the Instrument to assess the Credibility of Effect Modification Analyses (ICEMAN). *CMAJ*. 2020.

[29] Kasenda B, et al. Subgroup analyses in randomised controlled trials. *Lancet*. 2014.

---

**Word Count:** ~1,050 words

**Key Elements Included:**
- ✓ Clinical context and stakes
- ✓ Description of the two 2025 meta-analyses
- ✓ Biological implausibility argument
- ✓ Statistical overfitting framework
- ✓ Study objectives (3 aims)
- ✓ Hypothesis statement
- ✓ Significance and implications
