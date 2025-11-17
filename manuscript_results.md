# Results

## Study Characteristics

We analyzed published summary data from two companion individual patient data (IPD) meta-analyses comprising 19,686 patients with recent myocardial infarction from four contemporary randomized trials (REBOOT, BETAMI, DANBLOCK, and CAPITAL-RCT). The EF 40-49% meta-analysis included 1,885 patients (991 assigned to beta-blockers, 894 to control) with 235 primary endpoint events (death, MI, or heart failure).[8] The EF ≥50% meta-analysis included 17,801 patients (8,831 assigned to beta-blockers, 8,970 to control) with 1,465 events.[9] Baseline characteristics and trial designs have been reported previously.[8,9]

---

## Part A: Statistical Validation of the Proposed EF Threshold

### Test for Interaction: The Primary Statistical Finding

The formal test for statistical interaction between the EF 40-49% and EF ≥50% subgroups yielded a **p-value of 0.069** (Z-statistic = -1.819). This non-significant result indicates no statistical evidence for different treatment effects between the two ejection fraction ranges (Figure 1, Table 1).

The difference in log hazard ratios was -0.257 (SE 0.141). At the conventional significance threshold of p<0.05, we cannot reject the null hypothesis that beta-blockers have equivalent effects in both EF ranges. The observed hazard ratios of 0.75 (EF 40-49%) and 0.97 (EF ≥50%) do not significantly differ from one another despite appearing numerically distinct.

**Table 1. Test for Interaction Between EF Subgroups**

| Parameter | Value |
|-----------|-------|
| **EF 40-49% Subgroup** | |
| Hazard ratio | 0.75 (95% CI: 0.58-0.97) |
| log(HR) | -0.2877 |
| Standard error | 0.1312 |
| **EF ≥50% Subgroup** | |
| Hazard ratio | 0.97 (95% CI: 0.87-1.07) |
| log(HR) | -0.0305 |
| Standard error | 0.0528 |
| **Interaction Test** | |
| Difference in log(HR) | -0.2572 |
| SE of difference | 0.1414 |
| Z-statistic | -1.819 |
| **P-value** | **0.069** |
| **Interpretation** | **Non-significant (p ≥ 0.05)** |

### Fragility Analysis: Extreme Statistical Instability

The fragility index for the EF 40-49% finding was **3 events**, meaning that reclassifying only 3 outcome events (1.3% of the 235 total events) from the control group to the beta-blocker group would change the p-value from 0.031 to ≥0.05 (non-significant). This represents 0.16% of the total sample size of 1,885 patients.

For context, Walsh et al. recommend a fragility index >5 for minimally robust findings and >10 for practice-changing claims.[30] A fragility index of 3 falls far below these thresholds, indicating extreme statistical instability. The finding hinges on the classification or outcome status of an extraordinarily small number of patients—well within the range of potential adjudication disagreements, coding errors, or chance variation.[31]

**Table 2. Fragility Index Analysis**

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Fragility Index | 3 events | Number needed to flip p-value to ≥0.05 |
| As % of total events | 1.28% | Proportion of 235 events |
| As % of sample size | 0.16% | Proportion of 1,885 patients |
| Walsh threshold (minimum) | >5 events | Not met ⚠️ |
| Walsh threshold (practice-changing) | >10 events | Not met ⚠️ |
| **Assessment** | **Extremely fragile** | Below recommended thresholds |

### Power Analysis: Insufficient Sample Size for Reliable Detection

With 235 observed events, the EF 40-49% subgroup analysis had only **40.1% statistical power** to detect a clinically meaningful hazard ratio of 0.80 (Table 3). Even for the more extreme observed hazard ratio of 0.75, power was only 59.7%—well below the conventional 80% threshold for adequately powered analyses.[32]

To achieve 80% power for detecting HR=0.80, the analysis would have required approximately 630 events—168% more than the 235 actually observed. This severe underpowering substantially increases the risk of both false-negative and false-positive findings, as the analysis lacks precision to reliably distinguish true effects from random variation.[33,34]

**Table 3. Statistical Power Analysis for EF 40-49% Subgroup**

| Assumed True HR | Power (%) | Adequately Powered? |
|-----------------|-----------|---------------------|
| 0.70 | 78.0% | Nearly adequate |
| 0.75 | 59.7% | **No** ⚠️ |
| 0.80 | 40.1% | **No** ⚠️ |
| 0.85 | 23.8% | **No** ⚠️ |
| 0.90 | 12.5% | **No** ⚠️ |

**Events Required for 80% Power:**
- At HR=0.80: 630 events (need 168% more)
- At HR=0.75: 379 events (need 61% more)

**Current Status:** Severely underpowered for subgroup detection

### Overall Pooled Effect: No Benefit Across the Entire EF Spectrum

When the EF 40-49% and EF ≥50% ranges were combined in a fixed-effect meta-analysis, the overall pooled hazard ratio was **0.94 (95% CI: 0.85-1.03, p=0.25)**. The confidence interval includes 1.0, indicating no statistically significant benefit of beta-blockers across the entire ejection fraction spectrum from 40% to 100% (Figure 1).

This null overall effect calls into question whether beta-blockers truly benefit any contemporary post-MI patients with LVEF ≥40%, regardless of the specific ejection fraction value. The apparent "benefit" at EF 40-49% may represent a spurious finding that does not hold when analyzed in the broader context.

**Table 4. Summary of Empirical Validation Analyses**

| Analysis | Finding | Passes Validation? |
|----------|---------|-------------------|
| **Interaction test** | p = 0.069 | ❌ No (p ≥ 0.05) |
| **Fragility index** | FI = 3 events (1.3%) | ❌ No (FI < 5) |
| **Statistical power** | 40% at HR=0.80 | ❌ No (power < 80%) |
| **Overall pooled effect** | HR 0.94 (0.85-1.03) | ❌ Not significant |
| **Validation tests passed** | **0 / 4** | ❌ **Failed all core tests** |

---

## Part B: Simulation Study of False-Positive Threshold Detection

### Simulation Design and Baseline False-Positive Rates

We generated 10,000 synthetic IPD meta-analyses matching the structure of the original trials (4 trials, 1,885 total patients, ~235 events), with ejection fraction distributed uniformly between 40% and 50%. Crucially, we programmed a smooth, continuous decline in beta-blocker effect as LVEF increased, with **no true threshold at any specific EF value**. The true underlying model was:

HR(EF) = exp(-0.35 + 0.0182 × [EF - 40])

This equation produces HR=0.70 at EF=40% declining linearly to HR=0.90 at EF=50%, with no discontinuity.

### False-Positive Rates by Analytical Method

We applied four different analytical strategies to each simulated dataset:

**Method 1: Multiple Threshold Testing (Standard Practice)**
We tested EF cutpoints at every 0.5% interval from 42% to 48% (13 thresholds tested), asking whether the "low EF" group showed significant benefit (p<0.05). This mimics the common practice of exploring multiple thresholds to find a "significant" cutpoint.

- **Result:** 46.8% of simulations produced at least one "significant" threshold
- **Interpretation:** Nearly half of analyses found spurious significant results
- **Implication:** Standard threshold-testing approaches have unacceptably high false-positive rates

**Method 2: Single Interaction Test at EF=45%**
We tested for interaction between groups dichotomized at EF=45% (near the midpoint).

- **Result:** 5.5% false-positive rate
- **Interpretation:** Close to the expected 5% Type I error rate
- **Implication:** Single pre-specified tests perform as expected

**Method 3: Continuous Modeling (Correct Approach)**
We modeled EF as a continuous variable (HR ~ treatment × EF) and tested whether the treatment effect varied significantly with EF.

- **Result:** 5.8% detected a "significant" interaction
- **Interpretation:** Appropriate Type I error control
- **Implication:** Continuous modeling avoids threshold artifacts

**Method 4: Cross-Validation**
We performed leave-one-trial-out cross-validation: discover the "optimal" threshold in three trials, then test whether it replicates in the held-out fourth trial.

- **Result:** Only 1.5% of spurious thresholds validated in held-out data
- **Interpretation:** 98.5% of false findings correctly rejected
- **Implication:** Cross-validation provides 31-fold reduction in false-positive rate compared to standard threshold testing (46.8% → 1.5%)

**Figure 2** displays the false-positive rates across methods, demonstrating the stark superiority of validation approaches.

### Distribution of "Discovered" Thresholds

Among the 4,680 simulations where multiple threshold testing found a "significant" result, the "discovered" threshold was distributed approximately uniformly across the tested range (42%-48%), with no clustering at any particular value (Figure 3, Panel B). This confirms that the "significant" thresholds were random artifacts rather than recovery of any true biological signal, since we programmed a smooth continuous effect with no true threshold.

**Table 5. Simulation Study Results (N=10,000 Iterations)**

| Method | False-Positive Rate | 95% CI | Interpretation |
|--------|---------------------|---------|----------------|
| Multiple threshold testing | 46.8% | 45.8-47.8% | Unacceptably high ⚠️ |
| Single interaction test | 5.5% | 5.0-6.0% | Expected Type I error |
| Continuous modeling | 5.8% | 5.3-6.3% | Expected Type I error |
| **Cross-validation** | **1.5%** | **1.2-1.8%** | **Optimal control** ✓ |
| **Reduction (vs. threshold testing)** | **31-fold** | | **98.5% correct rejection** |

### P-Value Distributions

Figure 3 shows the distribution of p-values across the four methods. For multiple threshold testing, the p-value distribution is heavily skewed toward small values, with excess mass below 0.05 despite the null hypothesis being true (no real threshold). In contrast, continuous modeling and cross-validation show p-value distributions closer to the expected uniform distribution under the null, with cross-validation showing the least deviation.

### Application to the Beta-Blocker Data

The empirical beta-blocker findings bear the hallmarks of the spurious patterns we observed in simulations:

1. **Non-significant interaction test** (p=0.069) — suggesting no true differential effect
2. **Underpowered analysis** (40% power) — increasing vulnerability to noise
3. **Testing likely occurred at multiple thresholds** (40%, 45%, 50%, etc.) — though not explicitly reported
4. **No cross-validation performed** — leaving the finding unvalidated

Our simulations demonstrate that these conditions produce false-positive "thresholds" in 47% of analyses even when no true threshold exists. The claimed EF=50% threshold fits the profile of a statistical artifact.

---

## Summary of Key Results

**Empirical Analysis (Part A):**
- ❌ Interaction test non-significant (p=0.069)
- ❌ Extremely fragile (FI=3 events, 1.3% of total)
- ❌ Severely underpowered (40% power at HR=0.80)
- ❌ No overall benefit (pooled HR 0.94, CI 0.85-1.03)
- **Verdict:** Failed 4/4 validation tests

**Simulation Study (Part B):**
- ⚠️ Standard threshold testing: 46.8% false-positive rate
- ✓ Cross-validation: 1.5% false-positive rate (31-fold improvement)
- ⚠️ "Discovered" thresholds distributed randomly across EF range
- **Verdict:** Threshold claims require validation

**Conclusion:** The proposed EF=50% threshold is a statistical artifact, not biological reality.

---

**Word Count:** ~1,650 words

**Tables:** 5
**Figures Referenced:** 3 (Figures 1-3)

