# Methods

## Overview

We conducted a two-part validation analysis to evaluate the statistical robustness of the proposed ejection fraction threshold for beta-blocker efficacy after myocardial infarction. Part 1 (Empirical Analysis) used published summary data from two companion IPD meta-analyses to perform formal statistical tests. Part 2 (Simulation Study) generated synthetic datasets matching the original trial structure to quantify false-positive rates under controlled conditions where no true threshold existed.

---

## Part 1: Empirical Analysis of Published Data

### Data Sources

We extracted summary statistics from two published individual patient data meta-analyses:

1. **EF 40-49% meta-analysis**: Rossello et al., *The Lancet*, August 30, 2025.[8] This analysis included 1,885 patients (991 assigned to beta-blockers, 894 to control) with 235 primary endpoint events (composite of death from any cause, myocardial infarction, or heart failure).

2. **EF ≥50% meta-analysis**: NEJM, November 9, 2025.[9] This analysis included 17,801 patients (8,831 assigned to beta-blockers, 8,970 to control) with 1,465 primary endpoint events (same composite endpoint).

Both meta-analyses drew from the same pool of contemporary randomized trials (REBOOT, BETAMI, DANBLOCK, and CAPITAL-RCT). For each meta-analysis, we extracted the hazard ratio, 95% confidence interval, number of patients, and number of events from the published manuscripts.

### Statistical Analyses

#### Test for Interaction

We performed the formal statistical test for interaction to evaluate whether the treatment effects differed significantly between the EF 40-49% and EF ≥50% subgroups. This is the appropriate test for assessing whether a subgroup effect exists and is superior to comparing p-values from separate analyses.[35,36]

We calculated the standard errors of the log hazard ratios from the published 95% confidence intervals:

$$SE = \frac{\log(CI_{upper}) - \log(CI_{lower})}{2 \times 1.96}$$

The test statistic for interaction was:

$$Z = \frac{\log(HR_1) - \log(HR_2)}{\sqrt{SE_1^2 + SE_2^2}}$$

where $HR_1$ and $HR_2$ are the hazard ratios for the EF 40-49% and EF ≥50% groups, respectively. The two-tailed p-value was calculated as $p = 2 \times \Phi(-|Z|)$, where $\Phi$ is the standard normal cumulative distribution function.

A p-value <0.05 would indicate statistically significant heterogeneity of treatment effect between subgroups, providing evidence for a differential effect. A p-value ≥0.05 indicates no statistical evidence that the treatment effects differ.

#### Fragility Index

The fragility index quantifies the minimum number of outcome events that would need to be reclassified to change a statistically significant result (p<0.05) to non-significant (p≥0.05).[30,31] We calculated the fragility index for the EF 40-49% finding using the method of Walsh et al.[30]

Starting with the observed 2×2 contingency table (events in beta-blocker group vs. control group), we iteratively transferred one event from the control group to the beta-blocker group and recalculated the chi-square p-value after each transfer. The fragility index is the number of events that must be transferred before p≥0.05.

A fragility index ≤5 is considered indicative of extreme statistical instability; values >10 are recommended for practice-changing claims.[30,31]

#### Power Analysis

We assessed the statistical power of the EF 40-49% subgroup analysis to detect clinically meaningful treatment effects. Using Schoenfeld's method for Cox regression,[32] we calculated the power for detecting various true hazard ratios:

$$\text{Power} = \Phi\left(\sqrt{\frac{E}{4}} \times |\log(HR_{true})| - Z_{\alpha/2}\right)$$

where $E$ is the number of events (235), $Z_{\alpha/2}$ is the critical value for a two-sided test at $\alpha=0.05$ (1.96), and $\Phi$ is the standard normal CDF.

We calculated power for assumed true hazard ratios ranging from 0.70 to 0.90. We also determined the number of events required to achieve 80% power for detecting HR=0.80, a commonly cited threshold for clinically meaningful benefit.

The required number of events for 80% power is:

$$E_{required} = 4 \times \left(\frac{Z_{\alpha/2} + Z_{\beta}}{|\log(HR)|}\right)^2$$

where $Z_{\beta}$ = 0.84 for 80% power.

#### Overall Pooled Effect

We combined both EF ranges (40-49% and ≥50%) in a fixed-effect meta-analysis to estimate the overall treatment effect across the entire ejection fraction spectrum from 40% to 100%. We used inverse-variance weighting:

$$\log(HR_{pooled}) = \frac{\sum w_i \times \log(HR_i)}{\sum w_i}$$

where $w_i = 1/SE_i^2$ are the inverse-variance weights. The pooled 95% confidence interval was calculated as:

$$\exp\left(\log(HR_{pooled}) \pm 1.96 \times \sqrt{1/\sum w_i}\right)$$

### Software

All empirical analyses were conducted using Python 3.11 (Python Software Foundation) with standard statistical libraries. Code is available at [GitHub repository to be added upon publication].

---

## Part 2: Simulation Study

### Simulation Design

We generated 10,000 synthetic individual patient data meta-analyses, each designed to match the key structural features of the EF 40-49% meta-analysis:[8]

- **Number of trials**: 4 (matching REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT)
- **Sample size distribution**: Proportional to the original trials (52%, 22%, 23%, 3%)
- **Total patients**: 1,885 per simulated meta-analysis
- **Target events**: Approximately 235 (to match observed event rate of ~12.5%)

### Data Generation Process

For each simulated meta-analysis:

1. **Trial assignment**: Each patient was randomly assigned to one of four trials with probabilities matching the original meta-analyses.

2. **Ejection fraction**: Each patient's LVEF was sampled from a truncated normal distribution with mean 45%, standard deviation 2.5%, bounded between 40% and 49.9% (matching the EF 40-49% range).

3. **Treatment assignment**: Each patient was randomly assigned to beta-blocker or control with equal probability (50/50).

4. **True underlying effect model**: Crucially, we programmed a smooth, continuous decline in beta-blocker effect as LVEF increased, with **no sharp threshold at any specific value**:

$$\log(HR(EF)) = -0.287 + 0.0182 \times (EF - 40)$$

This equation produces HR=0.70 at EF=40%, declining linearly to HR=0.90 at EF=50%. The model has no discontinuities and represents a gradual, continuous relationship—the biological null hypothesis that no sharp threshold exists.

5. **Survival time generation**: Event times were generated from an exponential distribution with hazard rate $\lambda = \lambda_0 \times \exp(\beta \times treatment)$, where $\lambda_0 = 0.038$ (baseline annual rate) and $\beta = \log(HR(EF))$ varies continuously with each patient's ejection fraction. Censoring times were generated from an exponential distribution with mean 3.5 years (matching median follow-up).

### Analytical Methods Applied to Simulated Data

We applied four different analytical strategies to each of the 10,000 simulated datasets:

#### Method 1: Multiple Threshold Testing (Standard Practice)

We tested for treatment benefit in the "low EF" group using 13 different thresholds: 42%, 42.5%, 43%, ..., 48% (every 0.5% from 42% to 48%). For each threshold, we dichotomized patients into "low EF" (below threshold) and "high EF" (at or above threshold), then tested whether the low EF group showed significant benefit (two-sided p<0.05) using a Cox proportional hazards model.

We recorded whether **any** of the 13 thresholds produced a "significant" result (p<0.05). This mimics the common practice of testing multiple cutpoints to identify a "significant" threshold, whether explicitly reported or not.

**False-positive rate**: Proportion of the 10,000 simulations where at least one threshold yielded p<0.05, despite the true model having no threshold.

#### Method 2: Single Interaction Test (Pre-Specified Threshold)

We tested for interaction between treatment and EF group using a single pre-specified threshold at EF=45% (the midpoint of the 40-50% range). We fit a Cox model including the interaction term `treatment × (EF<45)` and recorded the p-value for the interaction coefficient.

**False-positive rate**: Proportion of simulations with interaction p<0.05.

#### Method 3: Continuous Modeling (Correct Approach)

We modeled EF as a continuous variable and tested whether treatment effect varied with EF. We fit a Cox model including the interaction term `treatment × EF` (continuous) and recorded the p-value for the interaction coefficient.

**False-positive rate**: Proportion of simulations with interaction p<0.05. Under correct specification (EF truly continuous), this should detect the non-zero slope, but in our simulations, we varied the strength of the continuous relationship to include truly null scenarios as well.

#### Method 4: Cross-Validation (Gold Standard)

We performed leave-one-trial-out cross-validation:

1. **Training set**: Combine three of the four trials
2. **Discovery**: Find the threshold (42-48%, tested every 0.5%) that produces the smallest p-value in the "low EF" group in the training set
3. **Test set**: Apply the discovered threshold to the held-out fourth trial
4. **Validation**: Test whether the low EF group in the test set also shows significant benefit (p<0.05)

We repeated this procedure four times, leaving out each trial in turn. A spurious threshold "validates" if it shows p<0.05 in at least one held-out trial.

**False-positive rate**: Proportion of simulations where the discovered threshold validated in held-out data.

### Outcome Measures

For each method, we calculated:

1. **False-positive rate**: Proportion of 10,000 simulations declaring a "significant" threshold despite none existing in the true data-generating model
2. **Distribution of discovered thresholds**: Among simulations where a threshold was found, what EF values were selected? (Should be uniform if purely noise)
3. **P-value distributions**: Distribution of the smallest p-values across methods

### Statistical Software

Simulations were conducted in Python 3.11 using NumPy 1.24 for random number generation, SciPy 1.10 for statistical functions, and lifelines 0.27 for survival analysis. Each simulation run took approximately 2 hours on a standard desktop computer (Intel Core i7, 16GB RAM). Reproducibility was ensured by setting random seeds.

All code and simulation results are publicly available at [GitHub repository].

---

## Ethical Approval

This study used only published summary data and simulated data. No individual patient data were accessed. Ethical approval was not required.

---

## Data Availability

All data extracted from published sources are provided in the supplementary materials. Simulation code and complete results are available at [repository link].

---

## Role of the Funding Source

No specific funding was received for this study. The authors had full access to all data and take responsibility for the integrity and accuracy of the analysis.

---

**Word Count:** ~1,550 words

**Key Elements:**
- ✓ Clear description of data sources
- ✓ Detailed statistical methods with equations
- ✓ Simulation design fully specified
- ✓ All four analytical methods explained
- ✓ Software and reproducibility details
- ✓ Ethical considerations
