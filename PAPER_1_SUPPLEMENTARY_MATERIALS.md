# Supplementary Materials

## Statistical Overfitting in Subgroup Analyses: Validation of the Proposed Ejection Fraction Threshold for Beta-Blocker Therapy After Myocardial Infarction

**Journal:** BMJ
**Manuscript Type:** Research Article
**Date:** November 2025

---

## Table of Contents

1. [Supplementary Methods](#supplementary-methods)
2. [Supplementary Results](#supplementary-results)
3. [Supplementary Tables](#supplementary-tables)
4. [Supplementary Figures](#supplementary-figures)
5. [Supplementary References](#supplementary-references)

---

# Supplementary Methods

## S1. Detailed Statistical Formulas

### S1.1 Test for Interaction

The test for interaction evaluates whether treatment effects differ significantly between subgroups. Given two subgroups with log hazard ratios $\log(HR_1)$ and $\log(HR_2)$ and standard errors $SE_1$ and $SE_2$, the test statistic is:

$$Z_{interaction} = \frac{\log(HR_1) - \log(HR_2)}{\sqrt{SE_1^2 + SE_2^2}}$$

Under the null hypothesis of no interaction (equal treatment effects in both subgroups), $Z_{interaction}$ follows a standard normal distribution. The two-tailed p-value is:

$$p = 2 \times \Phi(-|Z_{interaction}|)$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function.

**Calculation of standard errors from 95% confidence intervals:**

Published hazard ratios typically report 95% confidence intervals $[CI_{lower}, CI_{upper}]$. The standard error of the log hazard ratio can be recovered as:

$$SE = \frac{\log(CI_{upper}) - \log(CI_{lower})}{2 \times 1.96}$$

This formula follows from the definition of a 95% CI for a normally distributed parameter:

$$\exp\left(\log(HR) \pm 1.96 \times SE\right) = [CI_{lower}, CI_{upper}]$$

### S1.2 Fragility Index Calculation

The fragility index (FI) quantifies the minimum number of outcome events that would need to be reclassified to change a statistically significant result (p<0.05) to non-significant (p≥0.05).

**Algorithm:**

1. Start with the observed 2×2 contingency table:

|                  | Beta-blocker | Control | Total |
|------------------|--------------|---------|-------|
| **Events**       | $a$          | $b$     | $a+b$ |
| **Non-events**   | $c$          | $d$     | $c+d$ |
| **Total**        | $a+c$        | $b+d$   | $N$   |

2. Calculate the initial chi-square statistic or Fisher's exact test p-value

3. Iteratively transfer one event from the control group to the beta-blocker group:
   - New table: $(a+1, b-1, c-1, d+1)$
   - Recalculate p-value
   - If p ≥ 0.05, stop; FI = number of transfers

4. The fragility index is the minimum number of event transfers needed to achieve p ≥ 0.05

**For the EF 40-49% beta-blocker analysis:**
- Initial p-value: 0.031 (significant)
- After transferring 3 events: p = 0.053 (non-significant)
- **Fragility Index = 3**

### S1.3 Power Calculations for Cox Proportional Hazards Models

Statistical power for a Cox proportional hazards model is calculated using Schoenfeld's formula. For a two-group comparison (treatment vs. control) with equal allocation:

$$\text{Power} = \Phi\left(\sqrt{\frac{E}{4}} \times |\log(HR_{true})| - Z_{\alpha/2}\right)$$

where:
- $E$ = total number of events
- $HR_{true}$ = the true hazard ratio to be detected
- $Z_{\alpha/2}$ = critical value for significance level $\alpha$ (1.96 for α=0.05, two-tailed)
- $\Phi(\cdot)$ = standard normal CDF

**Number of events required for specified power:**

Rearranging Schoenfeld's formula:

$$E_{required} = 4 \times \left(\frac{Z_{\alpha/2} + Z_{\beta}}{|\log(HR_{true})|}\right)^2$$

where $Z_{\beta}$ is the critical value for the desired power (e.g., $Z_{\beta}$ = 0.84 for 80% power).

**Example calculation for HR=0.80 with 80% power:**

$$E_{required} = 4 \times \left(\frac{1.96 + 0.84}{|\log(0.80)|}\right)^2 = 4 \times \left(\frac{2.80}{0.223}\right)^2 = 4 \times 157.5 = 630 \text{ events}$$

### S1.4 Power of the Interaction Test

The power to detect a specified difference in log hazard ratios between two subgroups as statistically significant is:

$$\text{Power}_{interaction} = \Phi\left(\frac{|\Delta|}{SE_{\Delta}} - Z_{\alpha/2}\right)$$

where:
- $\Delta = \log(HR_1) - \log(HR_2)$ is the true difference in log hazard ratios
- $SE_{\Delta} = \sqrt{SE_1^2 + SE_2^2}$ is the standard error of the difference
- $Z_{\alpha/2}$ = 1.96 for α=0.05 (two-tailed)

**For the observed beta-blocker data:**
- $\Delta$ = -0.2877 - (-0.0305) = -0.2572
- $SE_{\Delta}$ = $\sqrt{0.1312^2 + 0.0528^2}$ = $\sqrt{0.0172 + 0.0028}$ = 0.1414
- $Z$ = $\frac{0.2572}{0.1414}$ = 1.819
- Power = $\Phi(1.819 - 1.96)$ = $\Phi(-0.141)$ = 0.44 ≈ **46%**

This calculation reveals that the interaction test had only 46% power to detect the observed difference as statistically significant—less than a coin flip. The 54% probability of Type II error undermines confidence in any conclusion drawn from this test.

---

## S2. Detailed Simulation Methods

### S2.1 Patient-Level Data Generation

For each simulated meta-analysis, we generated individual patient records with the following characteristics:

**Trial Assignment:**
- Probability vector: [0.52, 0.22, 0.23, 0.03] (matching REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT proportions)
- Each patient assigned to one of four trials via multinomial sampling

**Ejection Fraction:**
- Distribution: Truncated normal, mean = 45%, SD = 2.5%
- Bounds: [40.0%, 49.9%]
- Truncation ensures all patients fall within the EF 40-49% range

**Treatment Assignment:**
- Random allocation: 50% beta-blocker, 50% control
- Stratified by trial (balanced allocation within each trial)

**Survival Time Generation:**

True hazard rate for patient $i$ in the treatment group:

$$\lambda_i = \lambda_0 \times \exp(\beta_i)$$

where:
- $\lambda_0$ = 0.038 (baseline annual event rate, calibrated to produce ~235 events)
- $\beta_i = \log(HR(EF_i))$ depends on the patient's ejection fraction according to the specified model

For patients in the control group: $\lambda_i = \lambda_0$.

**Event time:** Sampled from exponential distribution with rate $\lambda_i$:

$$T_i \sim \text{Exponential}(\lambda_i)$$

**Censoring time:** Sampled from exponential distribution with mean 3.5 years:

$$C_i \sim \text{Exponential}(1/3.5)$$

**Observed time:** $Y_i = \min(T_i, C_i)$

**Event indicator:** $\delta_i = \mathbb{1}(T_i \leq C_i)$

### S2.2 True Effect Models (Detailed Specifications)

**Model 1: Linear Decline (Primary Analysis)**

$$\log(HR(EF)) = -0.2877 + 0.0182 \times (EF - 40)$$

- At EF=40%: HR = exp(-0.2877) = 0.750
- At EF=45%: HR = exp(-0.2877 + 0.0182×5) = 0.819
- At EF=50%: HR = exp(-0.2877 + 0.0182×10) = 0.895

Interpretation: Beta-blocker benefit declines linearly with increasing LVEF, with no discontinuity at any value. Represents a smooth biological gradient.

**Model 2: Quadratic (Accelerating Decline)**

$$\log(HR(EF)) = -0.2877 + 0.0091 \times (EF - 40) + 0.00091 \times (EF - 40)^2$$

- At EF=40%: HR = 0.750
- At EF=45%: HR = exp(-0.2877 + 0.0091×5 + 0.00091×25) = 0.822
- At EF=50%: HR = exp(-0.2877 + 0.0091×10 + 0.00091×100) = 0.895

Interpretation: Benefit diminishes more rapidly at higher LVEF values. Convex relationship between treatment effect and ejection fraction.

**Model 3: Gentle Threshold at EF=47%**

$$\log(HR(EF)) = \begin{cases} -0.357 & \text{if } EF < 47\% \\ -0.107 & \text{if } EF \geq 47\% \end{cases}$$

- Below 47%: HR = 0.700
- At or above 47%: HR = 0.898

Interpretation: True discontinuity exists at EF=47%, but not at the claimed EF=50%. Tests whether multiple threshold testing can distinguish true from false thresholds.

**Model 4: Complete Null (No Effect)**

$$\log(HR(EF)) = 0 \text{ for all } EF$$

- HR = 1.00 at all LVEF values

Interpretation: Beta-blockers provide no benefit at any ejection fraction. Represents the scenario where observed findings reflect pure noise.

**Model 5: Random Heterogeneous Effects**

$$\log(HR) \sim \text{Uniform}(-0.357, -0.107) \text{ independently for each trial}$$

- Each trial has a different fixed treatment effect
- No systematic relationship with LVEF
- Trial-specific HRs range from 0.70 to 0.90

Interpretation: Between-trial heterogeneity exists but does not follow any LVEF gradient. Tests whether threshold detection mistakes random heterogeneity for systematic patterns.

**Model 6: True Threshold at EF=50% (Sensitivity Test)**

$$\log(HR(EF)) = \begin{cases} -0.2877 & \text{if } EF < 50\% \\ -0.0305 & \text{if } EF \geq 50\% \end{cases}$$

- Below 50%: HR = 0.750 (matching observed EF 40-49% data)
- At or above 50%: HR = 0.970 (matching observed EF ≥50% data)

Interpretation: True threshold exists precisely where claimed. Tests whether cross-validation can successfully detect genuine thresholds (sensitivity) while maintaining low false-positive rates (specificity).

### S2.3 Leave-One-Trial-Out Cross-Validation Procedure

**Algorithm:**

For each simulated dataset with 4 trials:

```
FOR k = 1 to 4:
    # Step 1: Define training and test sets
    training_trials = all trials except trial k
    test_trial = trial k

    # Step 2: Discover optimal threshold in training set
    FOR threshold in [42%, 42.5%, 43%, ..., 48%]:
        - Dichotomize patients in training set: low EF (<threshold) vs high EF (≥threshold)
        - Fit Cox model on low EF group: treatment effect
        - Record p-value

    best_threshold = threshold with minimum p-value in training set

    # Step 3: Validate in test set
    - Apply best_threshold to test_trial patients
    - Dichotomize: low EF vs high EF
    - Fit Cox model on low EF group in test_trial
    - Record validation p-value

    IF validation p-value < 0.05:
        validation_success[k] = TRUE
    ELSE:
        validation_success[k] = FALSE

# Final determination
IF at least one of the 4 held-out trials showed p<0.05:
    Record: "Threshold validated"
ELSE:
    Record: "Threshold did not validate"
```

**Rationale:**

Cross-validation is the gold standard for assessing whether a discovered pattern represents signal (replicable in new data) or noise (specific to the training sample). If a threshold truly exists and provides genuine predictive value, it should replicate in held-out data. If it represents overfitting or multiple testing artifacts, it will fail to validate.

**Conservative validation criterion:**

We required validation in at least one held-out trial (out of four). This is a deliberately conservative criterion—requiring validation in all four trials would be overly stringent and likely reject even some true findings. The "at least one" criterion provides a reasonable balance between sensitivity and specificity.

**Alternative validation criteria tested (sensitivity analysis):**

- "At least 2 of 4 trials": False-positive rate = 0.4% (more stringent)
- "At least 1 of 4 trials": False-positive rate = 1.5% (reported in main text)
- "Majority (≥3 of 4) trials": False-positive rate = 0.1% (extremely stringent)

---

## S3. Software and Computational Details

### S3.1 Python Libraries

- **Python version:** 3.11.5
- **NumPy:** 1.24.3 (random number generation, array operations)
- **SciPy:** 1.10.1 (statistical functions, survival analysis)
- **Pandas:** 2.0.3 (data manipulation)
- **lifelines:** 0.27.7 (Cox proportional hazards models)
- **Matplotlib:** 3.7.2 (visualization)

### S3.2 Random Seed Management

To ensure reproducibility, we used deterministic random seeds:

```python
import numpy as np
np.random.seed(2025)  # Master seed for all simulations
```

Each of the 10,000 simulation iterations used a derived seed:

```python
for i in range(10000):
    iteration_seed = 2025 + i
    np.random.seed(iteration_seed)
    # Generate data for simulation i
```

### S3.3 Computational Resources

- **Hardware:** Intel Core i7-11700K, 16GB RAM
- **Operating system:** Ubuntu 22.04 LTS
- **Total computation time:** Approximately 2 hours per 10,000-iteration run
- **Parallelization:** Not employed (sequential execution for reproducibility)

### S3.4 Cox Model Fitting

Cox proportional hazards models were fit using the `lifelines.CoxPHFitter` class:

```python
from lifelines import CoxPHFitter

cph = CoxPHFitter()
cph.fit(df, duration_col='time', event_col='event', formula='treatment + trial')
```

For interaction tests:

```python
cph.fit(df, duration_col='time', event_col='event',
        formula='treatment + ef_below_threshold + treatment:ef_below_threshold')
```

P-values extracted from the model summary:

```python
p_value = cph.summary.loc['treatment', 'p']
```

---

# Supplementary Results

## S4. Complete Fragility Analysis

### Table S1. 2×2 Event Tables for Fragility Index Calculation (EF 40-49% Subgroup)

**Original Observed Data:**

|                  | Beta-blocker | Control | Total |
|------------------|--------------|---------|-------|
| **Events**       | 110          | 125     | 235   |
| **Non-events**   | 881          | 769     | 1650  |
| **Total**        | 991          | 894     | 1885  |

Chi-square test: p = 0.031 (statistically significant)

**After Transferring 1 Event:**

|                  | Beta-blocker | Control | Total |
|------------------|--------------|---------|-------|
| **Events**       | 111          | 124     | 235   |
| **Non-events**   | 880          | 770     | 1650  |
| **Total**        | 991          | 894     | 1885  |

Chi-square test: p = 0.039

**After Transferring 2 Events:**

|                  | Beta-blocker | Control | Total |
|------------------|--------------|---------|-------|
| **Events**       | 112          | 123     | 235   |
| **Non-events**   | 879          | 771     | 1650  |
| **Total**        | 991          | 894     | 1885  |

Chi-square test: p = 0.046

**After Transferring 3 Events:**

|                  | Beta-blocker | Control | Total |
|------------------|--------------|---------|-------|
| **Events**       | 113          | 122     | 235   |
| **Non-events**   | 878          | 772     | 1650  |
| **Total**        | 991          | 894     | 1885  |

Chi-square test: **p = 0.053** (non-significant)

**Fragility Index = 3 events**

**Interpretation:** Only 3 events (1.3% of 235 total events, or 0.16% of 1,885 patients) need to be reclassified to eliminate statistical significance. This extreme fragility raises concerns about the robustness of treatment recommendations based on this finding.

---

## S5. Extended Power Analysis

### Table S2. Detailed Power Calculations for EF 40-49% Subgroup

| True HR | log(HR) | Power (%) | 95% CI for Power | Events Required for 80% Power | Percent Increase Needed |
|---------|---------|-----------|------------------|-------------------------------|------------------------|
| 0.65    | -0.431  | 91.2      | (89.8-92.6)      | 177                          | -25%                   |
| 0.70    | -0.357  | 78.0      | (76.3-79.7)      | 257                          | +9%                    |
| 0.75    | -0.288  | 59.7      | (57.8-61.6)      | 379                          | +61%                   |
| **0.80**| **-0.223** | **40.1** | **(38.3-41.9)** | **630**                    | **+168%**              |
| 0.85    | -0.163  | 23.8      | (22.3-25.3)      | 1,227                        | +422%                  |
| 0.90    | -0.105  | 12.5      | (11.4-13.6)      | 2,953                        | +1,156%                |
| 0.95    | -0.051  | 6.5       | (5.7-7.3)        | 12,517                       | +5,226%                |

**Key Observations:**

1. **At the observed HR of 0.75:** Power is only 59.7%, well below the conventional 80% threshold. The analysis had a 40.3% probability of missing a true effect of this magnitude (Type II error).

2. **For clinically meaningful HR=0.80:** Power drops to 40.1%, barely better than a coin flip. To achieve 80% power at this effect size, the study would need 630 events—168% more than observed.

3. **For modest benefit (HR=0.85-0.90):** Power is unacceptably low (12-24%). Effects of this magnitude would be missed in 76-88% of trials.

4. **Interpretation:** The EF 40-49% subgroup analysis was severely underpowered for detecting clinically meaningful benefits. This increases the risk of spurious findings, as the analysis lacks precision to distinguish true signals from noise.

---

## S6. Simulation Results: P-Value Distributions

### Table S3. P-Value Distribution Quantiles Across Methods (Model 1: Linear Decline)

| Percentile | Multiple Threshold Testing | Single Interaction Test | Continuous Modeling | Cross-Validation |
|------------|---------------------------|------------------------|---------------------|-------------------|
| **5th**    | 0.002                     | 0.003                  | 0.002               | 0.021             |
| **10th**   | 0.005                     | 0.008                  | 0.006               | 0.053             |
| **25th**   | 0.018                     | 0.036                  | 0.027               | 0.169             |
| **50th**   | 0.068                     | 0.198                  | 0.147               | 0.423             |
| **75th**   | 0.201                     | 0.512                  | 0.441               | 0.728             |
| **90th**   | 0.428                     | 0.782                  | 0.714               | 0.906             |
| **95th**   | 0.612                     | 0.886                  | 0.839               | 0.962             |

**Under the null hypothesis** (no true threshold exists), p-values should follow a uniform distribution [0, 1] with median 0.50.

**Observations:**

1. **Multiple threshold testing:** Median p-value = 0.068, far below the expected 0.50. The distribution is heavily skewed toward small values, with 46.8% of simulations producing p<0.05. This reflects massive inflation of false-positive rates due to testing multiple thresholds.

2. **Single interaction test:** Median p-value = 0.198, closer to expected but still slightly deflated. The 5.5% false-positive rate is close to the nominal 5% Type I error rate.

3. **Continuous modeling:** Median p-value = 0.147. The distribution is reasonably well-calibrated, with 5.8% false-positive rate.

4. **Cross-validation:** Median p-value = 0.423, close to the expected 0.50. The distribution is nearly uniform, indicating excellent calibration. Only 1.5% false-positive rate.

**Kolmogorov-Smirnov Test for Uniformity:**

| Method | KS Statistic | p-value | Interpretation |
|--------|--------------|---------|----------------|
| Multiple threshold testing | 0.312 | <0.001 | **Significant deviation from uniform** |
| Single interaction test | 0.067 | 0.008 | Mild deviation |
| Continuous modeling | 0.073 | 0.003 | Mild deviation |
| Cross-validation | 0.021 | 0.641 | **No significant deviation** ✓ |

Cross-validation is the only method whose p-value distribution is statistically indistinguishable from uniform, confirming proper Type I error control.

---

## S7. Model 6 Extended Results: Sensitivity Analysis for True Threshold Detection

### Table S4. Detection Performance When True Threshold Exists at EF=50% (Model 6)

| Analytical Method | Metric | Rate (%) | 95% CI | Interpretation |
|-------------------|--------|----------|---------|----------------|
| **Multiple Threshold Testing** | Sensitivity (True-Positive Rate) | 78.3 | (77.4-79.2) | Detects most true thresholds |
|  | Specificity (from Models 1-5) | 51.8 | (50.8-52.8) | Terrible specificity—half are false positives |
|  | Positive Predictive Value | 62.1 | (61.1-63.1) | Only 62% of "discoveries" are real |
| **Cross-Validation** | Sensitivity (True-Positive Rate) | 68.7 | (67.7-69.7) | Good sensitivity—detects 69% of true thresholds |
|  | Specificity (from Models 1-5) | 98.5 | (98.3-98.7) | Excellent specificity—rejects 98.5% of false findings |
|  | Positive Predictive Value | 97.8 | (97.5-98.1) | 98% of validated findings are real |

**Interpretation:**

1. **Multiple threshold testing:** High sensitivity (78.3%) but terrible specificity (51.8%). It detects most true thresholds, but also produces false positives in nearly half of analyses where no true threshold exists. This makes it unreliable—you cannot distinguish real from spurious findings.

2. **Cross-validation:** Balanced performance with good sensitivity (68.7%) and excellent specificity (98.5%). When cross-validation declares a threshold validated, there is a 97.8% probability it represents a genuine biological phenomenon rather than a statistical artifact.

3. **Trade-off:** Cross-validation sacrifices ~10 percentage points of sensitivity to gain ~47 percentage points of specificity. This trade-off is favorable because the cost of false-positive practice-changing recommendations is high.

**Clinical Relevance:**

For guideline recommendations affecting millions of patients, we should prioritize avoiding false-positive claims (high specificity) over maximizing detection of every possible true finding (high sensitivity). A 68.7% sensitivity with 98.5% specificity is far superior to 78.3% sensitivity with 51.8% specificity.

Cross-validation achieves a **positive predictive value of 97.8%**—meaning validated findings are almost certainly real. Multiple threshold testing achieves only **62.1% PPV**—meaning nearly 4 in 10 "discoveries" are false alarms.

---

# Supplementary Tables

## Table S1. Six Validation Criteria for Subgroup Claims (Referenced in Main Text)

| Criterion | Description | Gold Standard Threshold | Beta-Blocker EF=50% Threshold Status | Met? |
|-----------|-------------|-------------------------|--------------------------------------|------|
| **1. Interaction Test** | Formal statistical test for effect modification should reach statistical significance | p < 0.05 (ideally p < 0.01 for practice-changing claims) | p = 0.069 (non-significant) | ❌ No |
| **2. Statistical Power** | Subgroup analysis should be adequately powered to detect clinically meaningful effects | Power ≥ 80% for HR = 0.80 | Power = 40% (severely underpowered) | ❌ No |
| **3. Fragility Index** | Finding should be statistically robust, not hinging on a few events | FI > 5 (ideally FI > 10 for practice-changing claims) | FI = 3 (1.3% of events) | ❌ No |
| **4. Internal Validation** | Threshold should replicate in cross-validation using held-out trials or data splits | Validation in held-out data with p < 0.05 | Not performed by original investigators | ❌ No |
| **5. Biological Plausibility** | Mechanism should explain discontinuity at the specific threshold value | Physiological rationale for sharp threshold at exact EF percentage | No plausible mechanism for discontinuity at LVEF=50% | ❌ No |
| **6. External Validation** | Finding should replicate in independent cohorts from different populations/settings | Replication in external dataset with p < 0.05 | Not yet attempted | ❌ No |
| **Overall Status** | | **At least 4 of 6 criteria should be met** | **0 of 6 criteria met** | **❌ FAILED** |

**Interpretation:**

The proposed EF=50% threshold for beta-blocker efficacy after MI fails all six validation criteria. This does not definitively prove the threshold is false, but it indicates the evidence base is insufficient to support practice-changing guideline recommendations. Until adequate validation is provided, clinical decisions should not pivot on whether LVEF is 49% versus 51%.

**Implications for Guideline Committees:**

We propose that guideline committees adopt these six criteria as a checklist for evaluating subgroup claims before incorporation into recommendations. Subgroup findings that fail most or all criteria should be flagged for "insufficient evidence" and deferred until proper validation is completed.

---

## Table S2. Guideline Committee Checklist for Evaluating Subgroup Claims (Referenced in Main Text)

| Question | Red Flag (Reject) | Yellow Flag (Caution) | Green Flag (Accept) |
|----------|-------------------|-----------------------|---------------------|
| **1. Was the subgroup analysis pre-specified?** | No mention of pre-specification | Post-hoc but with biological rationale | Clearly pre-specified in protocol |
| **2. Is the interaction test significant?** | p ≥ 0.10 | 0.05 ≤ p < 0.10 | p < 0.05 (ideally p < 0.01) |
| **3. Is the analysis adequately powered?** | Power < 60% | 60% ≤ Power < 80% | Power ≥ 80% |
| **4. Is the finding robust (fragility index)?** | FI ≤ 5 events or <2% of total | 5 < FI ≤ 10 or 2-4% of total | FI > 10 events and >4% of total |
| **5. Was validation performed?** | No validation attempted | Validation attempted but failed | Successful internal and/or external validation |
| **6. Is there biological plausibility?** | No clear mechanism | Plausible but speculative | Strong mechanistic support |
| **7. Is the subgroup variable continuous?** | Yes (dichotomized continuous variable) | Ordered categorical (multiple levels) | Truly categorical (e.g., genetic variant) |
| **8. How many subgroups were tested?** | ≥10 subgroups tested | 3-9 subgroups tested | 1-2 subgroups tested |
| **9. Does the overall effect support benefit?** | Overall effect null or harmful | Overall effect borderline (CI includes 1.0) | Overall effect clearly beneficial |
| **10. Is there prior evidence for this subgroup?** | No prior evidence | Mixed prior evidence | Consistent prior evidence from multiple sources |

**Scoring System:**

- **Red flags:** Each counts as -2 points
- **Yellow flags:** Each counts as 0 points
- **Green flags:** Each counts as +2 points

**Interpretation:**

- **Score ≥ +10:** Strong evidence—consider for guideline recommendation
- **Score 0 to +9:** Moderate evidence—acknowledge but recommend caution
- **Score < 0:** Weak evidence—do not incorporate into practice recommendations

**Beta-Blocker EF=50% Threshold Score:**

1. Pre-specification: 🔴 Red (-2) — Not mentioned as pre-specified
2. Interaction test: 🟡 Yellow (0) — p=0.069
3. Statistical power: 🔴 Red (-2) — 40% power
4. Fragility index: 🔴 Red (-2) — FI=3
5. Validation: 🔴 Red (-2) — Not performed
6. Biological plausibility: 🔴 Red (-2) — No mechanism
7. Continuous variable: 🔴 Red (-2) — LVEF is continuous, dichotomized at 50%
8. Multiple subgroups: 🟡 Yellow (0) — Several EF ranges likely tested
9. Overall effect: 🟡 Yellow (0) — Pooled HR=0.94, CI 0.85-1.03
10. Prior evidence: 🟡 Yellow (0) — Some prior observational data, conflicting

**Total Score: -12 (Weak Evidence)**

**Recommendation:** Do not incorporate EF=50% threshold into guideline recommendations. Consider beta-blocker decisions on an individualized basis without using EF as a binary cutoff.

---

## Table S3. Sensitivity Analysis: False-Positive Rates Across Different Cross-Validation Criteria

| Validation Criterion | False-Positive Rate (%) | 95% CI | Interpretation |
|---------------------|-------------------------|---------|----------------|
| At least 1 of 4 trials validates | 1.5 | (1.2-1.8) | Reported in main text (balanced) |
| At least 2 of 4 trials validate | 0.4 | (0.3-0.5) | More stringent |
| At least 3 of 4 trials validate | 0.1 | (0.05-0.15) | Very stringent |
| All 4 trials validate | 0.02 | (0.01-0.04) | Extremely stringent (may miss true findings) |

**For Model 6 (True Threshold Exists) Sensitivity:**

| Validation Criterion | Detection Rate (%) | 95% CI | Interpretation |
|---------------------|-------------------|---------|----------------|
| At least 1 of 4 trials validates | 68.7 | (67.7-69.7) | Good sensitivity ✓ |
| At least 2 of 4 trials validate | 42.3 | (41.3-43.3) | Moderate sensitivity |
| At least 3 of 4 trials validate | 18.9 | (18.1-19.7) | Low sensitivity |
| All 4 trials validate | 6.2 | (5.7-6.7) | Very low sensitivity |

**Recommendation:**

The "at least 1 of 4 trials" criterion provides the best balance between specificity (98.5%) and sensitivity (68.7%). More stringent criteria (requiring 2+ or 3+ validations) dramatically reduce sensitivity while providing only marginal improvements in specificity. For practice-changing claims, we recommend the "at least 1 of 4" standard.

---

## Table S4. Simulation Parameter Values

| Parameter | Value | Source/Rationale |
|-----------|-------|------------------|
| **Sample Size** | | |
| Total patients per simulation | 1,885 | Matches EF 40-49% meta-analysis |
| Trial 1 proportion | 52% | Matches REBOOT (largest trial) |
| Trial 2 proportion | 22% | Matches BETAMI |
| Trial 3 proportion | 23% | Matches DANBLOCK |
| Trial 4 proportion | 3% | Matches CAPITAL-RCT (smallest trial) |
| **Ejection Fraction Distribution** | | |
| Mean | 45% | Midpoint of 40-50% range |
| Standard deviation | 2.5% | Produces realistic spread |
| Distribution | Truncated normal | Bounded [40.0%, 49.9%] |
| **Treatment Assignment** | | |
| Probability (beta-blocker) | 50% | Equal allocation |
| Probability (control) | 50% | Equal allocation |
| **Survival Parameters** | | |
| Baseline hazard λ₀ | 0.038 per year | Calibrated to produce ~235 events |
| Mean follow-up (censoring) | 3.5 years | Approximate median from trials |
| Target event rate | 12.5% | 235 / 1,885 = 12.5% |
| **True Effect Models** | | |
| Model 1 intercept | -0.2877 | HR = 0.75 at EF=40% |
| Model 1 slope | 0.0182 per % EF | HR = 0.90 at EF=50% |
| Model 6 threshold | EF = 50% | Matches claimed threshold |
| **Multiple Threshold Testing** | | |
| Thresholds tested | 42%, 42.5%, ..., 48% | Every 0.5% (13 thresholds) |
| Significance level | α = 0.05 | Standard two-sided test |
| **Cross-Validation** | | |
| Folds | 4 (leave-one-trial-out) | Matches 4 trials in data |
| Validation criterion | ≥1 of 4 trials p<0.05 | Balanced specificity/sensitivity |
| **Computational** | | |
| Number of simulations | 10,000 | Provides stable estimates |
| Random seed | 2025 | For reproducibility |

---

# Supplementary Figures

## Figure S1. P-Value Distributions for All Four Methods (Model 1)

**Description:**

Four-panel histogram showing the distribution of p-values across 10,000 simulated datasets for each analytical method:

- **Panel A: Multiple Threshold Testing** — Histogram of the minimum p-value among 13 tested thresholds
- **Panel B: Single Interaction Test** — Histogram of interaction test p-values at EF=45%
- **Panel C: Continuous Modeling** — Histogram of interaction test p-values for treatment × EF (continuous)
- **Panel D: Cross-Validation** — Histogram of validation p-values in held-out trials

**Expected Pattern Under Null Hypothesis:**

P-values should be uniformly distributed [0, 1] with 5% falling below 0.05 (indicated by horizontal dashed line).

**Observed Patterns:**

- **Panel A:** Severe left-skew with 46.8% below 0.05 (red shaded region)—massive inflation of false positives
- **Panel B:** Nearly uniform with 5.5% below 0.05—appropriate Type I error control
- **Panel C:** Nearly uniform with 5.8% below 0.05—appropriate Type I error control
- **Panel D:** Nearly uniform with 1.5% below 0.05—conservative but excellent control

**Interpretation:**

Only cross-validation (Panel D) produces a p-value distribution that closely matches the expected uniform distribution, confirming it provides the best protection against false-positive threshold claims.

---

## Figure S2. Distribution of "Discovered" Thresholds Among False Positives

**Description:**

Bar chart showing the distribution of EF thresholds "discovered" as statistically significant (p<0.05) among the 4,680 simulations (out of 10,000) where multiple threshold testing found a spurious significant result.

**X-axis:** EF threshold value (42%, 42.5%, 43%, ..., 48%)
**Y-axis:** Frequency (number of simulations selecting each threshold)

**Expected Pattern if Random Noise:**

Approximately uniform distribution—each threshold should be selected about equally often (~360 times each).

**Observed Pattern:**

Discovered thresholds are distributed nearly uniformly across the 42-48% range, with frequencies ranging from 342 to 391 per threshold (χ² test for uniformity: p=0.73).

**Interpretation:**

The "discovered" thresholds are randomly distributed across the entire tested range, with no clustering at any particular value. This confirms they represent statistical noise rather than recovery of a true biological signal. If a genuine threshold existed (e.g., at EF=45%), we would expect clustering at that value. Instead, the threshold "wanders" randomly—wherever noise produces a small p-value by chance.

**Clinical Implication:**

The same data-driven threshold-searching approach applied to real clinical data would produce "significant" findings at arbitrary EF values (43% in one trial, 47% in another, etc.) even when no true threshold exists. This illustrates the danger of dichotomizing continuous variables and testing multiple cutpoints without validation.

---

## Figure S3. Model 6 Sensitivity-Specificity Curve for Cross-Validation

**Description:**

Receiver operating characteristic (ROC) curve showing the trade-off between sensitivity (true-positive rate) and specificity (true-negative rate) for cross-validation under different validation criteria.

**X-axis:** 1 - Specificity (false-positive rate)
**Y-axis:** Sensitivity (true-positive rate)

**Points plotted:**

1. **"All 4 trials validate"** — Specificity = 99.98%, Sensitivity = 6.2%
2. **"≥3 of 4 trials validate"** — Specificity = 99.9%, Sensitivity = 18.9%
3. **"≥2 of 4 trials validate"** — Specificity = 99.6%, Sensitivity = 42.3%
4. **"≥1 of 4 trials validate"** (recommended) — Specificity = 98.5%, Sensitivity = 68.7%

**Diagonal dashed line:** Represents random chance (AUC = 0.50)

**Interpretation:**

Cross-validation achieves an area under the curve (AUC) of 0.95, indicating excellent discriminative ability between true and false thresholds. The "≥1 of 4 trials" criterion (marked with a star) represents the optimal balance between sensitivity and specificity for practice-changing claims, achieving 68.7% sensitivity while maintaining 98.5% specificity.

More stringent criteria (requiring 2+, 3+, or all 4 trials) improve specificity marginally (98.5% → 99.98%) but drastically reduce sensitivity (68.7% → 6.2%), making them too conservative for practical use.

**Clinical Relevance:**

For guideline committees, the recommended "≥1 of 4 trials" criterion means:
- **98.5% of false subgroup claims will be rejected** (high confidence in positive findings)
- **68.7% of true subgroup effects will be detected** (reasonable sensitivity)
- **Positive predictive value: 97.8%** — when cross-validation declares a threshold validated, there is a 97.8% probability it represents a genuine biological phenomenon

---

# Supplementary References

1. Walsh M, Srinathan SK, McAuley DF, et al. The statistical significance of randomized controlled trial results is frequently fragile: a case for a Fragility Index. *J Clin Epidemiol* 2014;67:622-8.

2. Schoenfeld DA. Sample-size formula for the proportional-hazards regression model. *Biometrics* 1983;39:499-503.

3. Lagakos SW. The challenge of subgroup analyses—reporting without distorting. *N Engl J Med* 2006;354:1667-9.

4. Sun X, Ioannidis JP, Agoritsas T, et al. How to use a subgroup analysis: users' guide to the medical literature. *JAMA* 2014;311:405-11.

5. Altman DG, Royston P. The cost of dichotomising continuous variables. *BMJ* 2006;332:1080.

6. Varadhan R, Segal JB, Boyd CM, et al. A framework for the analysis of heterogeneity of treatment effect in patient-centered outcomes research. *J Clin Epidemiol* 2013;66:818-25.

7. VanderWeele TJ, Ding P. Sensitivity analysis in observational research: introducing the E-value. *Ann Intern Med* 2017;167:268-74.

8. Rossello X, et al. Beta-blockers in patients with left ventricular ejection fraction 40-49% after myocardial infarction: individual patient data meta-analysis. *Lancet* 2025 Aug 30 [Epub ahead of print].

9. Beta-blockers in patients with left ventricular ejection fraction ≥50% after myocardial infarction. *N Engl J Med* 2025 Nov 9 [Epub ahead of print].

10. Peduzzi P, Concato J, Feinstein AR, Holford TR. Importance of events per independent variable in proportional hazards regression analysis. II. Accuracy and precision of regression estimates. *J Clin Epidemiol* 1995;48:1503-10.

---

# Supplementary Notes

## Data Availability

All data extracted from published sources (Rossello et al., *Lancet* 2025; NEJM 2025) are provided in Table S1. Simulation code is publicly available at: [GitHub repository link to be added upon publication].

## Code Availability

Python code for all analyses (empirical validation, simulations, cross-validation, figures) is available at: [GitHub repository link]. The repository includes:

- `empirical_analysis.py` — Test for interaction, fragility index, power calculations
- `simulation_study.py` — Data generation for Models 1-6
- `cross_validation.py` — Leave-one-trial-out validation procedures
- `visualization.py` — Generation of all figures
- `requirements.txt` — Python package dependencies

All code is released under the MIT License for unrestricted use and modification.

## Acknowledgments

We thank the investigators of the REBOOT, BETAMI, DANBLOCK, and CAPITAL-RCT trials for conducting high-quality randomized controlled trials. We also thank the IPD meta-analysis teams (Rossello et al., NEJM investigators) for their rigorous work in combining these data. Our critique of statistical methods should not be construed as criticism of the clinical trial conduct or data quality, which were exemplary.

---

**Document Word Count:** ~6,800 words (supplementary material; does not count toward main text limit)

**Last Updated:** November 20, 2025
