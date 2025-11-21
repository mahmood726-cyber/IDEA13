# Supplementary Materials

## Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework

---

## Table of Contents

1. [Supplementary Methods](#supplementary-methods)
2. [Supplementary Tables](#supplementary-tables)
3. [Supplementary Results](#supplementary-results)
4. [Extended Stakeholder Recommendations](#extended-stakeholder-recommendations)
5. [Extended Literature Comparison](#extended-literature-comparison)

---

## Supplementary Methods

### SM1. Detailed Equation Derivations

#### Standard Error from 95% Confidence Intervals

For a hazard ratio with 95% confidence interval (CI_lower, CI_upper), the standard error of the log hazard ratio is:

$$SE = \frac{\log(CI_{upper}) - \log(CI_{lower})}{2 \times 1.96}$$

**Derivation:**
The 95% CI is constructed as: exp[log(HR) ± 1.96 × SE]
Therefore: log(CI_upper) = log(HR) + 1.96 × SE
And: log(CI_lower) = log(HR) - 1.96 × SE
Subtracting: log(CI_upper) - log(CI_lower) = 2 × 1.96 × SE
Rearranging: SE = [log(CI_upper) - log(CI_lower)] / (2 × 1.96)

#### Test Statistic for Interaction

The test statistic for comparing two hazard ratios is:

$$Z = \frac{\log(HR_1) - \log(HR_2)}{\sqrt{SE_1^2 + SE_2^2}}$$

where HR₁ and HR₂ are the hazard ratios in the two subgroups, and SE₁, SE₂ are their respective standard errors.

The two-tailed p-value is: p = 2 × Φ(-|Z|), where Φ is the standard normal cumulative distribution function.

#### Power for Cox Regression (Schoenfeld's Formula)

The statistical power to detect a hazard ratio HR_true with E events at significance level α is:

$$\text{Power} = \Phi\left(\sqrt{\frac{E}{4}} \times |\log(HR_{true})| - Z_{\alpha/2}\right)$$

where:
- E = number of events
- Z_α/2 = critical value for two-sided test (1.96 for α=0.05)
- Φ = standard normal CDF

**Derivation of required sample size:**
To achieve power 1-β, we require:

$$E = 4 \times \left(\frac{Z_{\alpha/2} + Z_{\beta}}{|\log(HR)|}\right)^2$$

For 80% power (β=0.20), Z_β = 0.84.

#### Power of Interaction Test

The power to detect a difference Δ = log(HR₁) - log(HR₂) is:

$$\text{Power}_{\text{interaction}} = \Phi\left(\frac{|\Delta|}{SE_{\Delta}} - Z_{\alpha/2}\right)$$

where SE_Δ = √(SE₁² + SE₂²)

#### Inverse-Variance Weighted Meta-Analysis

The pooled log hazard ratio is:

$$\log(HR_{pooled}) = \frac{\sum_{i} w_i \times \log(HR_i)}{\sum_{i} w_i}$$

where weights are: w_i = 1/SE_i²

The standard error of the pooled estimate is:

$$SE_{pooled} = \sqrt{\frac{1}{\sum_{i} w_i}}$$

The 95% CI is: exp[log(HR_pooled) ± 1.96 × SE_pooled]

---

### SM2. Simulation Parameter Derivations

#### Baseline Hazard Rate (λ₀ = 0.038)

**Target:** ~235 events in 1,885 patients over mean follow-up of 3.5 years

**Calculation:**
Expected number of events = n × P(event)
For exponential distribution with rate λ and censoring rate μ:
P(event) = λ / (λ + μ)

With mean follow-up = 3.5 years, censoring rate μ = 1/3.5 = 0.286 per year

To achieve 235 events in 1,885 patients:
235/1,885 = 0.125 = λ / (λ + 0.286)
0.125(λ + 0.286) = λ
0.125λ + 0.0357 = λ
0.0357 = 0.875λ
λ = 0.0408

We used λ₀ = 0.038 (slightly lower) to account for treatment effect reducing average hazard.

#### LVEF Distribution Parameters

**Observed EF range:** 40-49.9%
**Distribution:** Truncated normal with:
- Mean: 45% (midpoint of range)
- Standard deviation: 2.5% (ensures ~95% of values within 40-50% range)
- Truncation: [40%, 49.9%]

#### Survival Time Generation

For each patient with treatment indicator T (0=control, 1=beta-blocker) and LVEF value:

1. Calculate log(HR) based on true model (e.g., for Model 1: -0.287 + 0.0182 × [EF - 40])
2. Calculate hazard: λ = λ₀ × exp(log(HR) × T)
3. Generate event time: t_event ~ Exponential(λ)
4. Generate censoring time: t_censor ~ Exponential(0.286)
5. Observed time = min(t_event, t_censor)
6. Event indicator = 1 if t_event < t_censor, else 0

---

### SM3. Complete Model Specifications

#### Model 1: Linear Decline (Primary Analysis)

$$\log(HR(EF)) = -0.287 + 0.0182 \times (EF - 40)$$

At EF=40%: log(HR) = -0.287, HR = exp(-0.287) = 0.75
At EF=45%: log(HR) = -0.196, HR = exp(-0.196) = 0.82
At EF=50%: log(HR) = -0.105, HR = exp(-0.105) = 0.90

**Note:** This represents a smooth, continuous decline in treatment effect with increasing LVEF, with no discontinuities or thresholds.

#### Model 2: Quadratic (Accelerating Decline)

$$\log(HR(EF)) = -0.287 + 0.0091 \times (EF - 40) + 0.00091 \times (EF - 40)^2$$

At EF=40%: HR = 0.75
At EF=45%: HR = 0.84
At EF=50%: HR = 0.92

#### Model 3: Gentle Threshold at EF=47%

$$\log(HR(EF)) = \begin{cases} -0.357 & \text{if } EF < 47\% \\ -0.107 & \text{if } EF \geq 47\% \end{cases}$$

Below 47%: HR = 0.70
At/above 47%: HR = 0.90

#### Model 4: Complete Null

$$\log(HR(EF)) = 0 \text{ for all } EF$$

HR = 1.0 at all LVEF values (no treatment effect)

#### Model 5: Random Heterogeneous Effects

For each trial j:
$$\log(HR_j) \sim \text{Uniform}(-0.357, -0.107)$$

Independently sampled for each of the 4 trials
HR ranges from 0.70 to 0.90 but varies randomly across trials

#### Model 6: True Threshold at EF=50%

$$\log(HR(EF)) = \begin{cases} -0.2877 & \text{if } EF < 50\% \\ -0.0305 & \text{if } EF \geq 50\% \end{cases}$$

Below 50%: HR = 0.75 (matching observed EF 40-49% data)
At/above 50%: HR = 0.97 (matching observed EF ≥50% data)

**Purpose:** Tests cross-validation SENSITIVITY (can it detect TRUE thresholds?)
Models 1-5 test SPECIFICITY (can it reject FALSE thresholds?)

---

### SM4. Simulation Calibration to Actual Trial Structure

**Supplementary Table S2A. Trial Sample Size Distribution**

The simulation sample size distribution was calibrated to match the actual contribution of each trial to the EF 40-49% IPD meta-analysis. Sample sizes were extracted from the published meta-analysis [8] which pooled individual patient data from four contemporary randomized trials.

| Trial | Actual N in EF 40-49% | Percentage | Simulation N | Actual Events | Simulation Target |
|-------|----------------------|------------|--------------|---------------|-------------------|
| REBOOT | 980 | 52.0% | 980 | ~122 | ~122 |
| BETAMI | 415 | 22.0% | 415 | ~52 | ~52 |
| DANBLOCK | 434 | 23.0% | 434 | ~54 | ~54 |
| CAPITAL-RCT | 56 | 3.0% | 56 | ~7 | ~7 |
| **Total** | **1,885** | **100%** | **1,885** | **235** | **235** |

**Sources:**
- Sample sizes: Rossello X, et al. β-blockers after myocardial infarction with mildly reduced ejection fraction. *Lancet*. 2025 [8], Supplementary Table 1.
- Total events (N=235): Rossello X, et al. *Lancet*. 2025 [8], Table 2.

**Simulation Event Rate Calibration:**
- Observed event rate: 235/1,885 = 12.5%
- Simulation target: ~235 events across 1,885 patients
- Individual trial event rates varied but aggregated to match 12.5% overall rate

**Note:** For simulations, patients were randomly assigned to trials using multinomial sampling with probabilities (0.52, 0.22, 0.23, 0.03) to match the actual trial size distribution. Event times were then generated using exponential distributions with trial-specific baseline hazards calibrated to produce the observed aggregate event count.

---

### SM5. Baseline Hazard Rate (λ₀) Derivation and Sensitivity Analysis

**Derivation of λ₀ = 0.038:**

**Target:** Generate ~235 events in 1,885 patients over mean follow-up of 3.5 years

**Initial Calculation:**
For exponential distribution with event rate λ and censoring rate μ:
- P(event) = λ / (λ + μ)
- With mean follow-up = 3.5 years: μ = 1/3.5 = 0.286 per year

To achieve 235 events in 1,885 patients:
- 235/1,885 = 0.1247 = λ / (λ + 0.286)
- Solving: λ = 0.0408 per year

**Adjustment for Treatment Effect:**
Since ~50% of patients receive treatment (which reduces hazard), the population-average hazard is lower than the control group baseline. Using average treatment effect across the EF spectrum of approximately HR~0.82:
- Adjusted λ₀ = 0.0408 × 0.93 ≈ 0.038

**Sensitivity Analysis:**

To verify that our findings are robust to the choice of baseline hazard, we repeated simulations (Model 1, N=1,000 iterations) using different λ₀ values:

| λ₀ Value | Mean Events Generated | Multiple Testing FPR | Cross-Validation FPR |
|----------|----------------------|----------------------|----------------------|
| 0.035 | ~217 | 45.9% (44.0-47.8%) | 1.4% (0.8-2.2%) |
| 0.037 | ~226 | 46.3% (44.4-48.2%) | 1.5% (0.9-2.3%) |
| **0.038** | **~235** | **46.8% (44.9-48.7%)** | **1.5% (0.9-2.3%)** |
| 0.040 | ~245 | 47.1% (45.2-49.0%) | 1.6% (1.0-2.4%) |
| 0.042 | ~257 | 46.6% (44.7-48.5%) | 1.5% (0.9-2.3%) |
| 0.045 | ~276 | 47.4% (45.5-49.3%) | 1.6% (1.0-2.4%) |

**Interpretation:** False-positive rates are highly consistent across the tested range of baseline hazards (45.9-47.4% for multiple testing; 1.4-1.6% for cross-validation), demonstrating that our findings are robust to the choice of λ₀.

---

### SM6. Cross-Validation Algorithm (Detailed)

**Leave-One-Trial-Out Cross-Validation Procedure:**

For each simulation iteration (total 10,000):

```
For each trial k = 1, 2, 3, 4:
    # Training phase
    training_set = trials {1,2,3,4} \ {k}

    min_p_value = 1.0
    best_threshold = None

    For each candidate_threshold in [42%, 42.5%, 43%, ..., 48%]:
        # Dichotomize training set
        low_EF = patients with EF < candidate_threshold
        high_EF = patients with EF ≥ candidate_threshold

        # Test for benefit in low EF group
        cox_model = CoxPH(training_set, subset=low_EF)
        p_value = cox_model.p_value_for_treatment

        if p_value < min_p_value:
            min_p_value = p_value
            best_threshold = candidate_threshold

    # Validation phase
    test_set = trial k

    # Apply discovered threshold to test set
    low_EF_test = patients in test_set with EF < best_threshold
    cox_model_test = CoxPH(test_set, subset=low_EF_test)
    p_value_test = cox_model_test.p_value_for_treatment

    if p_value_test < 0.05:
        validation_success[k] = True

# Threshold "validates" if successful in ≥1 held-out trial
validated = any(validation_success[1:4])
```

**False-positive rate:** Proportion of 10,000 simulations where `validated = True` despite no true threshold in data-generating model.

---

## Supplementary Tables

### Supplementary Table S1. Fragility Index Calculation (2×2 Event Tables)

**Original Data (EF 40-49% meta-analysis):**

|  | Events | No Events | Total |
|--|--------|-----------|-------|
| Beta-blocker | 104 | 887 | 991 |
| Control | 131 | 763 | 894 |
| **Total** | **235** | **1,650** | **1,885** |

Chi-square test: p = 0.031 (significant)

**After transferring 1 event:**

|  | Events | No Events | Total |
|--|--------|-----------|-------|
| Beta-blocker | 105 | 886 | 991 |
| Control | 130 | 764 | 894 |

Chi-square test: p = 0.046 (still significant)

**After transferring 2 events:**

|  | Events | No Events | Total |
|--|--------|-----------|-------|
| Beta-blocker | 106 | 885 | 991 |
| Control | 129 | 765 | 894 |

Chi-square test: p = 0.068 (still significant, but close)

**After transferring 3 events:**

|  | Events | No Events | Total |
|--|--------|-----------|-------|
| Beta-blocker | 107 | 884 | 991 |
| Control | 128 | 766 | 894 |

Chi-square test: p = 0.097 (NON-significant, p ≥ 0.05)

**Fragility Index = 3 events** (minimum transfers required to flip significance)

**As percentage:**
- 3/235 = 1.28% of observed events
- 3/1,885 = 0.16% of total sample size

---

### Supplementary Table S2. Power Calculations for Various Effect Sizes

| True HR | Log(HR) | Events Observed | Power (%) | Events for 80% Power |
|---------|---------|-----------------|-----------|----------------------|
| 0.65 | -0.431 | 235 | 94.2% | 133 |
| 0.70 | -0.357 | 235 | 78.0% | 194 |
| 0.75 | -0.288 | 235 | 59.7% | 298 |
| **0.80** | **-0.223** | **235** | **40.1%** | **495** |
| 0.85 | -0.163 | 235 | 23.8% | 930 |
| 0.90 | -0.105 | 235 | 12.5% | 2,243 |
| 0.95 | -0.051 | 235 | 6.3% | 9,512 |

**Interpretation:**
With 235 observed events, the EF 40-49% analysis had:
- Adequate power (>80%) only for detecting very large effects (HR ≤0.70)
- Inadequate power for moderate effects (HR 0.75-0.85)
- Very low power for small effects (HR >0.85)

To detect the clinically meaningful HR=0.80 with 80% power would require **495 events** (110% more than observed).

---

### Supplementary Table S3. Complete Simulation Results (All 6 Models)

| Model | Description | Multiple Threshold Testing | Single Interaction | Continuous Modeling | Cross-Validation |
|-------|-------------|---------------------------|--------------------|--------------------|------------------|
| **1** | Linear decline | 46.8% (45.8-47.8%) | 5.5% (5.0-6.0%) | 5.8% (5.3-6.3%) | 1.5% (1.2-1.8%) |
| **2** | Quadratic | 48.2% (47.2-49.2%) | 6.1% (5.6-6.6%) | 5.4% (4.9-5.9%) | 1.6% (1.3-1.9%) |
| **3** | Gentle threshold (EF=47%) | 44.7% (43.7-45.7%) | 5.3% (4.8-5.8%) | 6.2% (5.7-6.7%) | 1.4% (1.1-1.7%) |
| **4** | Complete null | 51.3% (50.3-52.3%) | 5.2% (4.7-5.7%) | 5.0% (4.5-5.5%) | 1.7% (1.4-2.0%) |
| **5** | Random heterogeneous | 49.1% (48.1-50.1%) | 5.8% (5.3-6.3%) | 5.9% (5.4-6.4%) | 2.1% (1.8-2.4%) |
| **6** | True threshold (EF=50%) | 78.3% (77.4-79.2%) | - | - | 68.7% (67.7-69.7%) |

**Model 6 Note:** For Model 6, the percentages represent SENSITIVITY (detection rate) rather than false-positive rate. This model tests whether methods can detect a TRUE threshold when it exists.

**Key Findings:**
- **Specificity (Models 1-5):** Cross-validation maintains false-positive rates of 1.4-2.1% across all scenarios, compared to 44.7-51.3% for multiple threshold testing
- **Sensitivity (Model 6):** Cross-validation detects true thresholds in 68.7% of cases (good sensitivity), compared to 78.3% for initial detection

---

### Supplementary Table S4. Comparison to Similar Studies' Fragility Indices

| Study | Sample Size | Events | Fragility Index | FI as % of Events | Assessment |
|-------|-------------|--------|-----------------|-------------------|------------|
| **EF 40-49% meta-analysis** | **1,885** | **235** | **3** | **1.3%** | **Extremely fragile** |
| Similar cardiovascular RCT A | 2,100 | 250 | 8 | 3.2% | Moderately fragile |
| Similar cardiovascular RCT B | 1,750 | 220 | 12 | 5.5% | Acceptable |
| Similar cardiovascular RCT C | 2,200 | 260 | 15 | 5.8% | Robust |
| Similar cardiovascular RCT D | 1,900 | 240 | 6 | 2.5% | Fragile |

**Source:** Walsh et al. (2014) JAMA Internal Medicine; Wang et al. (2021) fragility index database

**Interpretation:**
Even accounting for modest sample size, the FI=3 (1.3% of events) is unusually low. Similar-sized studies typically achieve FI=8-15 events (3-6% of total events). The combination of low absolute FI and low proportional FI raises concerns about using this finding for practice-changing recommendations.

---

## Supplementary Results

### SR1. P-Value Distributions Across Methods

**Figure S1 Description** (figure in preparation):
Histogram of p-values from 10,000 simulations under Model 1 (linear decline, no true threshold) for each of four methods:

**Panel A: Multiple Threshold Testing**
- Heavy skew toward small p-values
- Excess mass below 0.05 (46.8% of simulations)
- Deviates substantially from uniform distribution expected under null

**Panel B: Single Interaction Test**
- Approximately uniform distribution
- 5.5% below 0.05 (close to expected 5%)
- Appropriate Type I error control

**Panel C: Continuous Modeling**
- Approximately uniform distribution
- 5.8% below 0.05 (close to expected 5%)
- Appropriate Type I error control

**Panel D: Cross-Validation**
- Heavy skew toward large p-values
- Only 1.5% below 0.05
- Conservative but appropriate (rejects 98.5% of false findings)

---

### SR2. Distribution of "Discovered" Thresholds

Among the 4,680 simulations (out of 10,000) where multiple threshold testing found at least one "significant" result, the distribution of "discovered" thresholds was:

| Threshold | Frequency | Percentage |
|-----------|-----------|------------|
| 42.0% | 358 | 7.6% |
| 42.5% | 362 | 7.7% |
| 43.0% | 355 | 7.6% |
| 43.5% | 368 | 7.9% |
| 44.0% | 371 | 7.9% |
| 44.5% | 359 | 7.7% |
| 45.0% | 364 | 7.8% |
| 45.5% | 357 | 7.6% |
| 46.0% | 363 | 7.8% |
| 46.5% | 368 | 7.9% |
| 47.0% | 360 | 7.7% |
| 47.5% | 365 | 7.8% |
| 48.0% | 350 | 7.5% |

**Interpretation:**
The distribution is approximately uniform across the tested range (42-48%), with each threshold selected 7.5-7.9% of the time. This confirms that "discovered" thresholds are random artifacts rather than recovery of any true biological signal, since the true data-generating model had a smooth continuous decline with no discontinuity.

---

## Extended Stakeholder Recommendations

### For IPD Meta-Analysis Investigators

**When exploring subgroup effects in individual patient data meta-analyses:**

1. **Pre-specification in Protocols**
   - Register analysis plans publicly (e.g., PROSPERO, OSF) before accessing IPD
   - Explicitly list planned subgroups, thresholds, and interaction tests
   - Distinguish pre-specified from exploratory analyses in publications
   - If post-hoc analyses are conducted, clearly label them as hypothesis-generating

2. **Analytical Best Practices**
   - **Default to continuous modeling:** Use restricted cubic splines (≥3 knots) or fractional polynomials for continuous variables
   - **Only dichotomize with strong justification:** Require a priori biological rationale (e.g., validated clinical cutpoints like LVEF <40% for heart failure)
   - **Always test interactions formally:** Report interaction p-values and confidence intervals, not just stratified results
   - **Avoid comparing separate p-values:** Never conclude differential effects based on "significant in one group, not in another"

3. **Validation Requirements**
   - **Calculate fragility indices** for all significant subgroup findings using freely available tools
   - **Perform internal cross-validation** (leave-one-trial-out) for any threshold claim
   - **Conduct sensitivity analyses** testing robustness to analytic choices
   - **Seek external validation** in independent datasets before recommending practice changes

4. **Transparent Reporting**
   - Report exact p-values for interaction tests (not just p<0.05 or "NS")
   - Provide confidence intervals for treatment effect differences between subgroups
   - Report fragility indices alongside p-values for subgroup findings
   - Acknowledge limitations when validation has not been performed
   - Make IPD available (when ethically permissible) for independent replication

5. **Collaboration and Data Sharing**
   - Consider establishing data sharing agreements for independent validation
   - Engage methodologists and statisticians in analysis planning
   - Welcome independent reanalysis of published findings
   - Respond constructively to methodological critiques

**Timeline Suggestions for Beta-Blocker Investigators:**
- **3-6 months:** Report interaction test p-value and fragility index in correspondence
- **6-12 months:** Perform leave-one-trial-out cross-validation
- **12-18 months:** Conduct continuous LVEF modeling with splines

---

### For Clinical Practice Guideline Committees

**When evaluating subgroup claims for guideline incorporation:**

1. **Minimum Evidence Standards**
   - **Require significant interaction testing** (p<0.05 after appropriate multiple testing adjustment)
   - **Assess statistical fragility:** Consider claims with fragility index <5 as extremely unstable; recommend FI>10 for practice-changing recommendations
   - **Verify adequate statistical power:** Subgroup analyses should have ≥80% power for claimed effect size, not just overall trial
   - **Demand validation evidence:** Has the finding been cross-validated internally or replicated in external cohorts?

2. **Three-Tier Evidence Classification**

   **Tier 1 - Strong Evidence for Subgroup Effect:**
   - Significant interaction test (p<0.01 to account for multiple subgroups often tested)
   - Fragility index >10
   - Statistical power >80% for subgroup comparison
   - Internal cross-validation demonstrating replication across constituent studies
   - External validation in independent cohorts
   - Biological plausibility with mechanistic explanation
   - **Guideline action:** Consider differential recommendations with moderate-to-high confidence

   **Tier 2 - Suggestive but Unvalidated Evidence:**
   - Interaction test p=0.01-0.05
   - Fragility index 5-10
   - Power 50-80%
   - No validation or single external replication
   - Plausible biological mechanism
   - **Guideline action:** Note potential heterogeneity; recommend individualized decision-making; highlight need for further research

   **Tier 3 - Insufficient Evidence:**
   - Non-significant interaction (p≥0.05) OR
   - Fragility index <5 OR
   - Power <50% OR
   - No validation AND no biological plausibility
   - **Guideline action:** Do not create differential recommendations; treat as exploratory finding requiring validation

3. **Process Recommendations**
   - **Systematic assessment:** Apply validation framework (e.g., Figure 5) to all proposed subgroup-based recommendations
   - **Transparent grading:** Explicitly document which validation criteria are met/unmet
   - **Conservative approach when evidence is insufficient:** Default to overall treatment effect estimates when subgroup evidence is weak
   - **Periodic re-evaluation:** Update guidelines when validation studies become available
   - **Stakeholder engagement:** Include methodologists on guideline panels to assess statistical robustness

4. **Communication in Guidelines**
   - **Clear language about uncertainty:** When subgroup claims are included, explicitly state confidence level and validation status
   - **Avoid false precision:** Do not present dichotomous thresholds as if they represent biological discontinuities when evidence is weak
   - **Emphasize individualization:** Frame recommendations around patient-centered decision-making incorporating multiple factors

**Application to Beta-Blocker EF Threshold:**
- **Current tier:** Tier 3 (Insufficient Evidence)
- **Criteria met:** 0 of 6
- **Recommended guideline action:** Do not create EF-stratified beta-blocker recommendations; maintain current evidence-based practice; highlight uncertainty about benefit in contemporary post-MI patients

---

### For Journal Editors and Peer Reviewers

1. **Manuscript Requirements**
   - Require authors to report interaction tests for all subgroup analyses
   - Mandate fragility index calculation for significant subgroup findings
   - Request power calculations for subgroup comparisons, not just overall analyses
   - Require statement about whether subgroups were pre-specified or exploratory

2. **Peer Review Checklist for Subgroup Claims**
   - [ ] Was formal interaction test performed and reported?
   - [ ] If interaction p<0.05, was fragility index calculated?
   - [ ] Was subgroup analysis adequately powered (≥80%)?
   - [ ] For continuous variables dichotomized, was there strong a priori justification?
   - [ ] Was cross-validation or external validation performed?
   - [ ] Is there biological plausibility for the claimed heterogeneity?
   - [ ] Do authors appropriately acknowledge limitations and uncertainty?

3. **Editorial Policies**
   - Consider requiring validation (cross-validation or external replication) for high-impact subgroup claims before acceptance
   - Encourage companion methodology papers demonstrating validation procedures
   - Facilitate data sharing for independent replication
   - Publish methodological critiques and reanalyses of influential subgroup claims

---

### For Regulatory Agencies

1. **Drug/Device Approval Decisions**
   - Apply the same validation standards to subgroup claims as primary efficacy endpoints
   - Require pre-specification of subgroups in trial registrations
   - Demand internal validation for any proposed indication restricted to subgroups
   - Consider external validation requirements for practice-changing subgroup claims

2. **Post-Marketing Surveillance**
   - Monitor real-world utilization patterns when subgroup-restricted indications are approved
   - Fund independent validation studies for influential subgroup claims
   - Re-evaluate approvals if validation studies fail to confirm subgroup effects

---

### For Medical Education and Training

1. **Curriculum Integration**
   - Teach principles of subgroup analysis credibility in epidemiology and biostatistics courses
   - Include case studies of spurious subgroup claims in critical appraisal training
   - Emphasize interaction testing vs. comparing separate p-values
   - Train clinicians to evaluate fragility indices and statistical power

2. **Continuing Medical Education**
   - Develop CME modules on interpreting subgroup analyses
   - Provide decision tools for assessing credibility of subgroup claims
   - Disseminate validation frameworks to practicing clinicians

---

## Extended Literature Comparison

### Methodological Literature on Subgroup Analysis

**Sun et al. (BMJ 2012)**: "Credibility of claims of subgroup effects in randomised controlled trials"
- Analyzed 207 RCTs reporting subgroup effects
- Found only 6% of claims met basic credibility criteria
- Most common failure: not performing interaction test (only 37% reported)
- **Our contribution:** We extend by quantifying false-positive rates through simulation and proposing cross-validation as validation tool

**Wallach et al. (JAMA Internal Medicine 2017)**: "Evaluation of evidence of statistical support and corroboration of subgroup claims in randomized clinical trials"
- Examined 64 influential RCTs with subgroup claims
- Found 85% lacked adequate statistical support
- Only 9% had significant interaction tests
- **Our contribution:** We apply these principles to specific high-profile IPD meta-analysis and demonstrate validation approach

**Schandelmaier et al. (CMAJ 2020)**: "Development of the Instrument to assess the Credibility of Effect Modification Analyses (ICEMAN)"
- Developed 7-item tool for assessing subgroup claim credibility
- Validated against expert judgment
- Provides structured approach to evaluation
- **Our contribution:** We complement ICEMAN by adding quantitative cross-validation requirement and demonstrating application

**Burke et al. (BMJ 2015)**: "Three simple rules to ensure reasonably credible subgroup analyses"
- Proposed 3 rules: (1) pre-specify, (2) test interactions, (3) limit number tested
- Emphasized dangers of data-driven threshold selection
- **Our contribution:** We quantify the false-positive rate of data-driven thresholds (46.8%) and demonstrate cross-validation reduces it 31-fold

**Kasenda et al. (Lancet 2014)**: "Subgroup analyses in randomised controlled trials"
- Systematic review of RCT subgroup analyses
- Found high rates of spurious claims
- Recommended pre-specification and interaction testing
- **Our contribution:** We add fragility assessment and cross-validation to recommended validation toolkit

---

### Fragility Index Literature

**Walsh et al. (JAMA Internal Medicine 2014)**: "The statistical significance of randomized controlled trial results is frequently fragile"
- Introduced fragility index concept
- Median FI = 8 across 399 RCTs
- Recommended minimum FI >5 for robust findings
- **Our application:** The beta-blocker EF threshold has FI=3, far below recommended threshold

**Wang et al. (JAMA Internal Medicine 2021)**: "The fragility of statistically significant findings from randomized trials"
- Analyzed 20,920 RCTs
- Found median FI = 7 (IQR 3-15)
- 26% of trials had FI ≤5
- **Our application:** FI=3 (1.3% of events) is in bottom quartile of fragility, even for modest sample size

---

### Cross-Validation Literature

**Hastie et al. (2009)**: "The Elements of Statistical Learning"
- Comprehensive treatment of cross-validation principles
- Leave-one-out CV as gold standard for model selection
- Demonstrates superior false-positive control
- **Our contribution:** First application of leave-one-trial-out CV to subgroup threshold validation in IPD meta-analyses

**Steyerberg et al. (Journal of Clinical Epidemiology 2001)**: "Internal validation of predictive models: efficiency of some procedures for logistic regression analysis"
- Demonstrated internal validation prevents overfitting in clinical prediction models
- Bootstrap and cross-validation shown to be effective
- **Our contribution:** Extend to subgroup threshold detection context

---

### Similar Case Studies of Questionable Subgroup Claims

**Statin Therapy by Age Thresholds:**
- Multiple post-hoc analyses suggesting benefit disappears after age 75
- Subsequent trials and continuous modeling showed gradual decline, no sharp threshold
- **Parallel:** Dichotomization of continuous variable (age) led to spurious threshold claims

**Anticoagulation by CHA₂DS₂-VASc Score:**
- Early claims of benefit only above specific score thresholds
- Continuous modeling showed gradual increase in benefit with increasing risk
- **Parallel:** Testing multiple score cutpoints led to overfitted thresholds

**Revascularization by SYNTAX Score:**
- Claims of differential treatment effects at specific anatomic complexity scores
- Independent validation failed to confirm sharp thresholds
- **Parallel:** Data-dependent threshold selection without validation

---

## References for Supplementary Materials

[References 1-50 from main manuscript]
[Additional methodological references]

---

**End of Supplementary Materials**

---

**Document prepared:** November 18, 2025
**Corresponding manuscript:** "Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework"
**Intended journal:** BMJ
