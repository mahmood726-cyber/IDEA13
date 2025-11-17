# WORD COUNT REDUCTION STRATEGY
## Beta-Blocker EF Threshold Manuscript

**Current word count:** 10,524 words
**Target word count:** 3,000-4,000 words (BMJ limit)
**Required reduction:** ~6,500-7,500 words (60-70% reduction)

**Date:** November 17, 2025
**Status:** Strategic planning document

---

## EXECUTIVE SUMMARY

The manuscript substantially exceeds BMJ's word limit (10,524 vs 3,000-4,000). To achieve publication-ready length while preserving scientific integrity, we recommend a **two-article strategy**:

1. **Main Article** (3,500 words): Focus on beta-blocker case study with essential methodological framework
2. **Methods Companion** (separate submission): Detailed validation framework and simulation methodology

**Alternative:** Single article with extensive online supplementary materials

---

## CURRENT WORD COUNT BREAKDOWN (Estimated)

| Section | Current Words | Target Words | Reduction Needed |
|---------|--------------|--------------|------------------|
| **Abstract** | 350 | 250 | -100 (29%) |
| **Introduction** | 1,200 | 600 | -600 (50%) |
| **Methods** | 2,800 | 800 | -2,000 (71%) |
| **Results** | 2,500 | 1,000 | -1,500 (60%) |
| **Discussion** | 2,800 | 800 | -2,000 (71%) |
| **Tables/Figures** | 500 | 100 | -400 (80%) |
| **References** | 374 | 150 | -224 (60%) |
| **TOTAL** | **10,524** | **3,700** | **-6,824 (65%)** |

---

## STRATEGY 1: TWO-ARTICLE APPROACH (RECOMMENDED)

### Article 1: "Beta-Blocker Ejection Fraction Threshold: A Case Study in Subgroup Overfitting"
**Target Journal:** BMJ (Research)
**Word Count:** 3,500 words
**Focus:** Clinical case study with essential validation framework

#### Content to KEEP in Main Article:

**Introduction** (600 words):
- ✅ ESC guideline recommendation (150 words)
- ✅ REDUCE-HF and TRS-HF trial context (200 words)
- ✅ Problem: threshold not validated (150 words)
- ✅ Brief overview of validation framework (100 words)

**Methods** (800 words):
- ✅ Data sources and extraction (150 words)
- ✅ Interaction test (100 words)
- ✅ Fragility index calculation (100 words)
- ✅ Power analysis (100 words)
- ✅ Simulation study overview (200 words) - HIGH LEVEL ONLY
- ✅ Statistical analysis (150 words)

**Results** (1,000 words):
- ✅ Baseline characteristics (150 words)
- ✅ Interaction test: p=0.069 (200 words)
- ✅ Fragility index: FI=3 (200 words)
- ✅ Power analysis: 40% (150 words)
- ✅ Simulation results summary (300 words) - KEY FINDINGS ONLY

**Discussion** (800 words):
- ✅ Main finding: threshold not validated (200 words)
- ✅ Clinical implications (200 words)
- ✅ Guideline implications (200 words)
- ✅ Limitations (100 words)
- ✅ Conclusions (100 words)

**Figures:**
- ✅ Figure 1: Forest plot
- ✅ Figure 2: False-positive rates (simplified)
- ✅ Figure 4: Validation framework (summary version)
- ❌ Figure 3: MOVE to Supplement

**Tables:**
- ✅ Table 1: Baseline characteristics (condensed)
- ❌ All other tables: MOVE to Supplement

---

### Article 2: "A Statistical Framework for Validating Treatment Effect Heterogeneity Claims"
**Target Journal:** Statistics in Medicine OR Trials (Methods)
**Word Count:** 4,000-5,000 words
**Focus:** Comprehensive methodological framework

#### Content for Methods Article:

**Introduction** (800 words):
- Problem of subgroup overfitting in general
- Prior examples from literature
- Need for validation framework

**Methods** (2,500 words):
- **DETAILED** simulation methodology
- Complete description of all 6 models
- Cross-validation implementation details
- Statistical power calculations
- Fragility index methodology

**Results** (1,000 words):
- Simulation results for all 6 models
- Sensitivity analyses
- Figure 3: Complete threshold distributions
- Supplementary figures

**Discussion** (700 words):
- Methodological recommendations
- Implementation guidance
- Software and code availability

**Benefits of Two-Article Strategy:**
1. Each article stays within word limits
2. Clinical and methodological audiences both served
3. Higher citation potential (two papers)
4. Main article more accessible to clinicians
5. Methods article provides detailed guidance

---

## STRATEGY 2: SINGLE ARTICLE WITH SUPPLEMENT (ALTERNATIVE)

### Main Article (3,700 words)

Use same structure as Strategy 1, Article 1, but move substantial content to online supplement.

### Online Supplement Contents:

**Supplementary Methods:**
- Detailed simulation algorithms (1,500 words)
- All 6 model specifications (500 words)
- Complete statistical formulas (300 words)
- Cross-validation implementation (400 words)

**Supplementary Results:**
- Simulation results for Models 2-6 (800 words)
- Sensitivity analyses (500 words)
- Additional threshold distributions (300 words)

**Supplementary Figures:**
- Figure S1: Threshold distributions (current Figure 3)
- Figure S2: Model 2-6 simulation results
- Figure S3: Power curves
- Figure S4: Sensitivity analyses

**Supplementary Tables:**
- Table S1: Complete baseline characteristics
- Table S2: All simulation results
- Table S3: Sensitivity analyses results

**Supplementary Materials:**
- Complete R and Python code
- Simulation output files
- Data extraction worksheets

**Benefits of Single Article + Supplement:**
1. Maintains unified narrative
2. Standard approach for medical journals
3. All content accessible in one package
4. Lower publication costs

**Drawbacks:**
1. Supplementary materials often ignored
2. Less credit for methodological contribution
3. Methods hidden from statisticians who would benefit

---

## SECTION-BY-SECTION REDUCTION TACTICS

### Abstract (350 → 250 words, -100 words)

**CUT:**
- ❌ Extended background (2-3 sentences)
- ❌ Detailed methods description
- ❌ Specific simulation model details
- ❌ Secondary findings

**KEEP:**
- ✅ One-sentence background
- ✅ Core objective
- ✅ Key methods (interaction test, fragility, simulations)
- ✅ Primary findings (p=0.069, FI=3, 40.7% vs 6.1%)
- ✅ Main conclusion

**Tactic:** Every sentence must justify its inclusion. Remove all "nice to have" context.

---

### Introduction (1,200 → 600 words, -600 words)

**CUT:**
- ❌ Detailed history of beta-blocker trials (save 200 words)
- ❌ Extended discussion of guideline development (save 150 words)
- ❌ Literature review of subgroup analysis problems (save 200 words)
- ❌ Detailed trial descriptions (save 50 words)

**KEEP:**
- ✅ ESC 2023 guideline recommendation (100 words)
- ✅ Source trials (REDUCE-HF, TRS-HF) - brief mention (100 words)
- ✅ Problem statement: threshold not validated (150 words)
- ✅ Study objective (100 words)
- ✅ Brief framework overview (150 words)

**Tactics:**
1. Combine paragraphs: merge related concepts
2. Remove transitional sentences
3. Use active voice (saves words)
4. Cut adjectives and adverbs
5. Remove examples unless critical

**Example Reduction:**

❌ **BEFORE (120 words):**
> "Subgroup analyses are commonly performed in clinical trials to identify patient populations
> who may derive particular benefit from treatment. However, these analyses are prone to
> statistical overfitting, where random variation in small subgroups can be misinterpreted
> as true biological heterogeneity. The problem is exacerbated when multiple subgroups are
> examined without pre-specification, when biological plausibility is questionable, and when
> formal validation procedures are not employed. Previous studies have documented numerous
> examples of subgroup findings that failed to replicate in subsequent trials, leading to
> inappropriate clinical decision-making and wasted research resources."

✅ **AFTER (45 words):**
> "Subgroup analyses commonly identify populations who may benefit from treatment, but are
> prone to overfitting—misinterpreting random variation as true heterogeneity. Without
> pre-specification, biological plausibility, and validation, subgroup findings often fail
> to replicate, leading to inappropriate clinical decisions."

**Savings: 75 words (62% reduction)**

---

### Methods (2,800 → 800 words, -2,000 words)

This requires the most aggressive reduction. Move detailed methods to supplement or companion article.

**CUT (move to supplement):**
- ❌ Detailed simulation algorithms (save 600 words)
- ❌ Complete model specifications for Models 2-6 (save 400 words)
- ❌ Extended mathematical formulas (save 300 words)
- ❌ Detailed cross-validation implementation (save 400 words)
- ❌ Code availability details (save 100 words)
- ❌ Step-by-step calculation procedures (save 200 words)

**KEEP (essential methods only):**
- ✅ Data sources (100 words)
- ✅ Interaction test method (100 words)
- ✅ Fragility index concept (100 words)
- ✅ Power analysis approach (100 words)
- ✅ Simulation study overview (250 words) - SIMPLIFIED
- ✅ Statistical analysis (150 words)

**Tactics:**
1. Reference established methods, don't re-describe
2. Cite software packages instead of explaining calculations
3. Use phrases like "using standard methods" for well-known approaches
4. Move formulas to supplement, give only conceptual description
5. Provide high-level overview, details in supplement

**Example Reduction:**

❌ **BEFORE (200 words):**
> "We performed a simulation study to quantify false-positive rates for threshold detection
> under different analytical approaches. For each simulation iteration, we generated data
> for 1,885 patients across 4 trials matching the sample size distribution of the actual
> beta-blocker dataset. Ejection fraction was drawn from a truncated normal distribution
> with mean 45% and standard deviation 2.5%, constrained to the range 40-49.9%. Treatment
> allocation was randomly assigned with 1:1 ratio. The true underlying model assumed a
> continuous linear decline in treatment effect with increasing EF, with no threshold.
> Specifically, log(HR) = -0.287 + 0.0182 × (EF - 40), producing HR=0.70 at EF=40% and
> HR=0.90 at EF=50%. We simulated survival times using exponential distributions with
> hazard rates determined by the true model, with baseline annual event rate of 3.8%
> and median follow-up of 3.5 years."

✅ **AFTER (80 words):**
> "We simulated 10,000 datasets (1,885 patients across 4 trials) matching the beta-blocker
> data structure. The true model assumed continuous linear decline in treatment effect
> with EF (no threshold): HR=0.70 at EF=40%, declining to HR=0.90 at EF=50%. We compared
> false-positive rates for four analytical methods: (1) multiple threshold testing,
> (2) single interaction test, (3) continuous modeling, and (4) cross-validation.
> Detailed methods are provided in the Online Supplement."

**Savings: 120 words (60% reduction)**

---

### Results (2,500 → 1,000 words, -1,500 words)

**CUT (move to supplement):**
- ❌ Extended baseline characteristics table (save 300 words)
- ❌ Detailed simulation results for Models 2-6 (save 600 words)
- ❌ Sensitivity analyses (save 400 words)
- ❌ Detailed threshold distribution analysis (save 200 words)

**KEEP:**
- ✅ Key baseline characteristics (150 words)
- ✅ Interaction test result with interpretation (200 words)
- ✅ Fragility index finding (200 words)
- ✅ Power analysis result (150 words)
- ✅ Primary simulation findings (Model 1 only) (300 words)

**Tactics:**
1. Present only primary outcomes
2. Remove sub-analyses
3. Consolidate results into fewer paragraphs
4. Reference supplementary tables instead of describing in text
5. Combine related findings

---

### Discussion (2,800 → 800 words, -2,000 words)

**CUT:**
- ❌ Extended literature review (save 500 words)
- ❌ Detailed policy implications (save 400 words)
- ❌ Extended methodological discussion (save 600 words)
- ❌ Speculation about mechanisms (save 300 words)
- ❌ Future research directions beyond essentials (save 200 words)

**KEEP:**
- ✅ Summary of key finding (150 words)
- ✅ Clinical implications (200 words)
- ✅ Guideline implications (200 words)
- ✅ Essential limitations (150 words)
- ✅ Conclusions (100 words)

**Tactics:**
1. Remove all speculative content
2. Condense each paragraph to core message
3. Eliminate repetition of results
4. Focus on clinical actionability
5. Be directive, not exploratory

---

### Figures and Tables

**Current: 4 figures + multiple tables**
**Target: 3 figures + 1 table**

**KEEP:**
- ✅ Figure 1: Forest plot (essential for showing interaction)
- ✅ Figure 2: False-positive rates (core finding)
- ✅ Figure 4: Validation framework (conceptual contribution)
- ✅ Table 1: Baseline characteristics (CONDENSED)

**MOVE TO SUPPLEMENT:**
- ❌ Figure 3: Threshold distributions → Figure S1
- ❌ All other tables → Online Supplement

**Figure Caption Reduction:**
Reduce captions by 50%. State only what is shown, minimal interpretation.

---

## WRITING TECHNIQUES FOR REDUCTION

### 1. Eliminate Redundancy

❌ **BEFORE:** "We found that the interaction test was not statistically significant (p=0.069)"
✅ **AFTER:** "The interaction test was non-significant (p=0.069)"
**Savings:** 3 words (19%)

---

### 2. Use Active Voice

❌ **BEFORE:** "It was found that cross-validation reduced false positives"
✅ **AFTER:** "Cross-validation reduced false positives"
**Savings:** 3 words (38%)

---

### 3. Remove Hedging

❌ **BEFORE:** "Our results suggest that it may be possible that threshold testing could potentially lead to false discoveries"
✅ **AFTER:** "Threshold testing leads to false discoveries"
**Savings:** 13 words (76%)

---

### 4. Combine Sentences

❌ **BEFORE:** "The fragility index was 3 events. This indicates that the finding is fragile."
✅ **AFTER:** "The fragility index of 3 events indicates finding fragility."
**Savings:** 5 words (38%)

---

### 5. Remove Filler Phrases

**Delete these:**
- "It is important to note that..."
- "As shown in Figure X..."
- "In order to..."
- "Due to the fact that..."
- "It has been shown that..."
- "A number of..."
- "It is well known that..."

**Replace with:**
- Nothing (just state the fact)
- "(Figure X)"
- "To..."
- "Because..."
- Direct statement
- "Several..." or "Many..."
- Direct statement

---

### 6. Abbreviate After First Use

❌ **BEFORE:** "Ejection fraction... ejection fraction... ejection fraction..."
✅ **AFTER:** "Ejection fraction (EF)... EF... EF..."
**Savings:** 2 words per subsequent use

---

### 7. Use Numerals

❌ **BEFORE:** "three trials, five methods"
✅ **AFTER:** "3 trials, 5 methods"
**Savings:** 2 words

---

## REFERENCE REDUCTION (374 → 150, -224 references)

**Current:** ~75 references (assuming ~5 words per reference)
**Target:** ~30 references

**KEEP:**
- ✅ Source trials (REDUCE-HF, TRS-HF, Lancet, NEJM)
- ✅ ESC guidelines
- ✅ Key methodological citations (fragility index, interaction tests)
- ✅ 2-3 examples of failed subgroup findings
- ✅ Cross-validation methodology references

**CUT:**
- ❌ Historical background references
- ❌ Tangential citations
- ❌ Multiple citations where one suffices
- ❌ "Review" type references (cite primary sources)

**Tactic:** Every reference must be directly relevant to a specific claim in the manuscript.

---

## IMPLEMENTATION TIMELINE

### Week 1: Major Structural Changes
- Day 1-2: Create two-article outline OR decide on supplement strategy
- Day 3-4: Move content to supplement/second article
- Day 5: Verify main article structure

### Week 2: Sentence-Level Editing
- Day 1: Abstract and Introduction reduction
- Day 2: Methods reduction
- Day 3: Results reduction
- Day 4: Discussion reduction
- Day 5: Final polish

### Week 3: Quality Assurance
- Day 1-2: Read for flow and coherence
- Day 3: Verify all essential content retained
- Day 4: Co-author review
- Day 5: Final word count verification

**Total time:** 3 weeks

---

## QUALITY ASSURANCE CHECKLIST

After reduction, verify:

- [ ] Word count ≤ 4,000 words
- [ ] All essential findings preserved
- [ ] Core argument intact
- [ ] Clinical implications clear
- [ ] Methods sufficient for replication (or in supplement)
- [ ] Figures support main findings
- [ ] References support all major claims
- [ ] No critical information lost
- [ ] Manuscript still readable and flows well
- [ ] Abstract accurately reflects content

---

## WHAT MUST BE PRESERVED

**Non-negotiable content** (must remain in main article):

1. ✅ ESC guideline recommendation
2. ✅ Interaction test: p=0.069 (non-significant)
3. ✅ Fragility index: 3 events
4. ✅ Power: 40% (underpowered)
5. ✅ Simulation finding: 40.7% vs 6.1% (6.7-fold reduction)
6. ✅ Conclusion: Threshold not validated, should not guide practice
7. ✅ Validation framework concept

**Everything else is negotiable.**

---

## RECOMMENDED DECISION

**RECOMMENDATION:** Strategy 2 (Single Article + Supplement)

**Rationale:**
1. Faster to implement (one submission vs two)
2. Maintains unified narrative
3. Standard approach for clinical journals
4. Preserves all methodological detail in supplement
5. Lower publication costs

**Next Steps:**
1. Move detailed methods to Online Supplement
2. Condense Introduction and Discussion by 50%
3. Present only Model 1 simulation results in main text
4. Create Figure S1-S4 for supplementary material
5. Reduce references to top 30
6. Implement sentence-level reduction techniques

**Target completion:** 2-3 weeks

---

**Document prepared:** November 17, 2025
**Author:** Word count reduction strategic planning
**Status:** Ready for implementation
**Decision required:** Choose Strategy 1 (two articles) or Strategy 2 (supplement)
