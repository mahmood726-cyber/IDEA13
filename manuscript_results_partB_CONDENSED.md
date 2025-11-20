# Results - Part B: Simulation Study (CONDENSED)

## Part B: Simulation Study of False-Positive Threshold Detection

### False-Positive Rates by Analytical Method

We generated 10,000 synthetic IPD meta-analyses matching the structure of the original trials (4 trials, 1,885 patients, ~235 events), with ejection fraction distributed between 40% and 50%. Crucially, we programmed a smooth, continuous decline in beta-blocker effect as LVEF increased, with **no true threshold at any specific EF value**. The true model produced HR=0.70 at EF=40% declining linearly to HR=0.90 at EF=50% (see Methods).

We applied four analytical strategies to each simulated dataset (Table 5):

**Method 1: Multiple Threshold Testing** — Tested EF cutpoints at every 0.5% from 42-48% (13 thresholds), seeking any "significant" result.
- **Result:** 46.8% false-positive rate (95% CI: 45.8-47.8%)
- **Interpretation:** Nearly half of analyses found spurious significant thresholds

**Method 2: Single Interaction Test** — Tested for interaction at pre-specified EF=45%.
- **Result:** 5.5% false-positive rate (5.0-6.0%)
- **Interpretation:** Appropriate Type I error control when threshold is pre-specified

**Method 3: Continuous Modeling** — Modeled EF continuously (treatment × EF interaction).
- **Result:** 5.8% false-positive rate (5.3-6.3%)
- **Interpretation:** Continuous analysis avoids dichotomization artifacts

**Method 4: Cross-Validation** — Leave-one-trial-out validation of discovered thresholds.
- **Result:** 1.5% false-positive rate (1.2-1.8%)
- **Interpretation:** 98.5% of false findings correctly rejected
- **31-fold reduction** compared to multiple threshold testing (46.8% → 1.5%)

**Table 5. Simulation Results: False-Positive Rates (N=10,000 Iterations)**

| Method | False-Positive Rate | 95% CI | Interpretation |
|--------|---------------------|---------|----------------|
| Multiple threshold testing | 46.8% | 45.8-47.8% | Unacceptably high ⚠️ |
| Single interaction test | 5.5% | 5.0-6.0% | Expected Type I error ✓ |
| Continuous modeling | 5.8% | 5.3-6.3% | Expected Type I error ✓ |
| **Cross-validation** | **1.5%** | **1.2-1.8%** | **Optimal control** ✓ |

Among the 4,680 simulations where multiple threshold testing found a "significant" result, the discovered thresholds were distributed uniformly across 42-48% (Figure 3), confirming they represented random noise rather than recovery of any true signal.

### Sensitivity Analysis Across Alternative Models

We repeated simulations using five alternative true effect models: quadratic decline, gentle threshold at EF=47%, complete null (HR=1.0), and random heterogeneous effects (Table 6). The core finding was robust: multiple threshold testing produced false-positive rates of 44.7-51.3% across all scenarios, while cross-validation maintained rates below 2.1%.

**Table 6. Sensitivity Analysis: False-Positive Rates Across Models**

| True Model | Multiple Threshold | Cross-Validation |
|------------|-------------------|-------------------|
| Linear decline (primary) | 46.8% (45.8-47.8%) | 1.5% (1.2-1.8%) |
| Quadratic (accelerating) | 48.2% (47.2-49.2%) | 1.6% (1.3-1.9%) |
| Gentle threshold (EF=47%) | 44.7% (43.7-45.7%) | 1.4% (1.1-1.7%) |
| Complete null (HR=1.0) | 51.3% (50.3-52.3%) | 1.7% (1.4-2.0%) |
| Random heterogeneous | 49.1% (48.1-50.1%) | 2.1% (1.8-2.4%) |
| **Range** | **44.7-51.3%** | **1.4-2.1%** |

Notably, even when a true threshold existed at EF=47%, multiple testing still produced 44.7% false positives at incorrect locations. Cross-validation correctly rejected 98.6% of these false findings.

### Model 6: Cross-Validation Can Detect True Thresholds

Models 1-5 assessed **specificity** (rejecting false thresholds). Model 6 assessed **sensitivity** (detecting true thresholds). Using a true threshold at EF=50% precisely matching the observed data (HR=0.75 below 50%, HR=0.97 at or above), we tested whether cross-validation could detect genuine discontinuities.

**Results:**
- **Multiple threshold testing:** Detected true threshold in 78.3% of simulations (high sensitivity)
- **Cross-validation:** Validated true threshold in 68.7% of simulations (good sensitivity)

Combined with 98.5% specificity from Models 1-5, cross-validation demonstrates both excellent ability to reject false findings AND good ability to detect true thresholds. The 10-percentage-point gap (78.3% → 68.7%) reflects appropriate conservatism: cross-validation correctly filters out ~10% of findings that initially appear significant but fail independent replication.

**Table 6B. Model 6: Detection of True Threshold at EF=50%**

| Method | Detection Rate | Interpretation |
|--------|---------------|----------------|
| Multiple threshold testing | 78.3% (77.4-79.2%) | High sensitivity, poor specificity (51.8%) |
| **Cross-validation** | **68.7% (67.7-69.7%)** | **Good sensitivity, excellent specificity (98.5%)** |

### Application to Beta-Blocker Data

The empirical beta-blocker findings bear hallmarks of the patterns we observed in simulations:
- Non-significant interaction test (p=0.069)
- Underpowered analysis (40% power)
- Multiple thresholds likely tested (though not explicitly reported)
- No cross-validation performed

Our simulations demonstrate these conditions produce false-positive "thresholds" in 47% of analyses even when no true threshold exists. The claimed EF=50% threshold fits the profile of a potential statistical artifact requiring validation.

---

**Word Count:** ~820 words (down from 1,850 words; saves 1,030 words) ✓

**Content Preserved:**
- ✅ Core false-positive rates (46.8% vs 1.5%)
- ✅ All four methods with interpretations
- ✅ Sensitivity analysis across 5 models
- ✅ Model 6 results demonstrating cross-validation sensitivity
- ✅ Application to beta-blocker data
- ✅ Key tables (Tables 5, 6, 6B)

**Content Condensed:**
- Simulation design details → Referenced in Methods
- P-value distribution analysis → Moved to Supplementary Results
- Extended interpretations → Streamlined
- Detailed 6-model comparison → Summarized in table

**Moved to Supplement:**
- P-value distribution quantiles (Table S3)
- Detailed Model 6 performance metrics (Table S4)
- Figure specifications
