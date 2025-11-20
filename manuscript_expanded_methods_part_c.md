# Methods - Part C: Forensic Analysis of Observational vs. RCT Evidence

## Overview

Parts 1 and 2 evaluated the robustness of ejection fraction-based subgroup claims within RCT data. Part 3 addresses a complementary question: How should we weigh large observational meta-analyses when RCT data coexist? Specifically, we examined the discrepancy between observational registries suggesting beta-blocker benefit in heart failure with preserved ejection fraction (HFpEF) and RCTs showing no significant effect.

We developed and applied a three-component **bias decomposition framework** to quantify: (1) the magnitude of observational-RCT discordance, (2) vulnerability to unmeasured confounding, and (3) the effective statistical information content of observational data when accounting for heterogeneity and residual confounding.

---

## Data Sources for Obs vs. RCT Comparison

### Observational Evidence

We identified three major observational meta-analyses reporting beta-blocker effects in HFpEF or preserved EF post-MI populations:

1. **Bavishi et al. (2015):** Meta-analysis of 11 observational studies, N=27,099, reporting HR 0.81 (95% CI: 0.72-0.90) for all-cause mortality.¹⁵

2. **Liu et al. (2014):** Meta-analysis of 8 observational studies in HFpEF, N=21,206, reporting HR 0.91 (95% CI: 0.87-0.95) for mortality.¹⁶

3. **SwedeHF Registry (Lund et al. 2014):** Propensity-matched cohort from Swedish Heart Failure Registry, N=19,083, reporting HR 0.93 (95% CI: 0.86-1.00) for mortality.¹⁷

4. **GWTG-HF Registry (approximate):** Get With The Guidelines—Heart Failure registry data, N≈14,000, HR 0.90 (95% CI: 0.85-0.95) for in-hospital and 1-year mortality (estimated from published forest plots).⁴⁰

**Total Observational Evidence:** N=81,388 patients

### RCT Evidence

We identified four RCTs or RCT-based analyses in preserved or mildly reduced EF populations:

1. **J-DHF Trial (2013):** Japanese Diastolic Heart Failure Study, N=245, HR 0.90 (95% CI: 0.55-1.49) for composite endpoint including mortality.¹⁹

2. **SENIORS Trial (2005):** Subgroup analysis of patients with LVEF >35%, N=752, HR 0.81 (95% CI: 0.63-1.04) for all-cause mortality.²⁰

3. **REBOOT Analysis (2024):** Post-MI patients with LVEF ≥50%, N=17,801 (subset of Part 1 data), HR 0.97 (95% CI: 0.87-1.07).⁹

4. **REDUCE-AMI Trial (2024):** Post-MI patients with LVEF ≥50%, N=5,020 (overlaps with REBOOT cohort), HR 0.96 (95% CI: 0.79-1.16).⁴¹

**Total RCT Evidence:** N≈9,000 patients (accounting for overlap)

---

## Component 1: Discordance Index

The **Discordance Index (DI)** is a standardized measure of the disagreement between observational and RCT pooled estimates. It is essentially a Z-score for the difference between two meta-analytic point estimates, accounting for the uncertainty of each.

### Calculation

1. **Pool observational studies** using random-effects meta-analysis (DerSimonian-Laird method) to obtain:
   - Pooled log(HR_obs) and SE_obs

2. **Pool RCT studies** using random-effects meta-analysis to obtain:
   - Pooled log(HR_RCT) and SE_RCT

3. **Calculate the Discordance Index:**

$$DI = \frac{|\log(HR_{obs}) - \log(HR_{RCT})|}{\sqrt{SE_{obs}^2 + SE_{RCT}^2}}$$

where the denominator is the standard error of the difference.

### Interpretation

- **DI < 1.0:** Observational and RCT estimates agree within 1 standard error → Grade A (may cautiously pool)
- **DI 1.0-2.0:** Moderate discordance → Grade B (trust RCTs for inference; observational may be biased)
- **DI > 2.0:** Severe conflict (>2 standard errors apart) → Grade C (exclude observational data; likely confounded)

A DI >2.0 provides statistical evidence of genuine discordance beyond sampling variability, analogous to a two-sample Z-test. This threshold corresponds to p<0.05 for a test of equivalence.

---

## Component 2: E-Value (Confounding Vulnerability)

The **E-Value** framework, developed by VanderWeele and Ding,¹² quantifies the minimum strength of unmeasured confounding needed to explain away an observed association. For hazard ratios, the E-Value is calculated as:

$$E\text{-Value} = HR + \sqrt{HR \times (HR - 1)}$$

when HR <1 (protective effect), the calculation uses the reciprocal: E-Value = 1/HR + √[1/HR × (1/HR - 1)].

For an observed association with HR=0.80 and lower 95% CI limit of 0.70:
- **Point estimate E-Value:** Strength of confounder needed to explain away HR=0.80
- **Lower CI E-Value:** Strength of confounder needed to shift the lower confidence limit to HR=1.0 (null)

### Interpretation

- **E-Value < 1.5:** Weak unmeasured confounding could explain the result → Fragile to bias
- **E-Value 1.5-2.0:** Moderate unmeasured confounding needed → Moderately robust
- **E-Value > 2.0:** Strong unmeasured confounding needed → Robust to likely confounders

For example, an E-Value=1.40 means an unmeasured confounder associated with *both* treatment and outcome at RR=1.40 each could entirely explain the observed HR. Since common unmeasured confounders in observational heart failure studies (frailty, functional status, clinical stability, physician judgment) plausibly have RR=1.3-1.6 for both treatment selection and outcomes,³⁷,³⁸ an E-Value <1.5 indicates vulnerability to these biases.

### Calculation

We calculated E-Values for the pooled observational HR using the `EValue` package in R:

```r
library(EValue)
evalues.HR(est = obs_HR, lo = obs_CI_lower, true = 1, rare = FALSE)
```

We used `rare=FALSE` because heart failure mortality is a common outcome (>10% event rate), which affects the E-Value calculation methodology.¹²

---

## Component 3: Inflation Factor (Bayesian Effective Sample Size)

The most novel component quantifies **information inflation**: the ratio between nominal sample size and effective statistical information when accounting for heterogeneity and bias.

### Conceptual Framework

Standard meta-analysis weights studies by inverse-variance: $w_i = 1 / SE_i^2$. This implicitly treats larger studies as more informative, with weight proportional to sample size. However, observational studies suffer from:

1. **Between-study heterogeneity** (different populations, definitions, adjustment strategies)
2. **Residual confounding** (unmeasured variables systematically biasing results)
3. **Publication bias** (selective reporting of positive findings)

These biases do not simply add noise (wider confidence intervals) but systematically *devalue* the information content of each observation. A study of N=10,000 patients may contain the statistical information equivalent of only N=100 RCT patients.

The **Bayesian meta-analytic predictive (MAP) prior** framework¹⁴,³⁹ provides a principled method to quantify this devaluation by calculating an **effective sample size (ESS)**.

### Bayesian ESS Calculation: Step-by-Step

**Step 1: Fit Bayesian Meta-Analysis (gMAP)**

We fit a Bayesian meta-analysis to the observational studies using the RBesT package in R:¹⁴

```r
library(RBesT)

# Prepare data: log(HR) and SE for each observational study
obs_data <- data.frame(
    Study = c("Bavishi", "Liu", "SwedeHF", "GWTG-HF"),
    TE = log(c(0.81, 0.91, 0.93, 0.90)),  # log hazard ratios
    seTE = c(...),  # standard errors
    N = c(27099, 21206, 19083, 14000)
)

# Fit Bayesian meta-analytic predictive prior
map_mcmc <- gMAP(
    formula = cbind(TE, seTE) ~ 1,
    data = obs_data,
    family = gaussian,  # log-HR is normally distributed
    tau.dist = "HalfNormal",  # Prior for heterogeneity
    tau.prior = 0.5,  # Conservative: penalizes high heterogeneity
    beta.prior = 2    # Weakly informative prior for mean effect
)
```

**Model Specification:**
- **Family:** Gaussian (appropriate for log-hazard ratios)
- **Heterogeneity prior:** τ ~ HalfNormal(0.5), penalizing excessive between-study variability
- **Treatment effect prior:** β ~ Normal(0, 2), weakly informative

The key innovation is the **heterogeneity penalty**: τ_prior=0.5 is conservative, meaning the model heavily discounts studies that are inconsistent with each other. This is appropriate for observational data where heterogeneity often reflects bias rather than genuine population differences.

**Step 2: Fit Mixture Model to Posterior**

The gMAP output is a set of MCMC samples. To calculate ESS, we must approximate the posterior predictive distribution with a parametric mixture model:

```r
# Fit mixture model using EM algorithm
map_mix <- automixfit(map_mcmc)
```

This creates a mixture of normal distributions that closely approximates the posterior distribution while allowing for analytic ESS calculation.

**Step 3: Calculate Effective Sample Size**

```r
# Calculate ESS with reference variance σ²=4
# (standard for log-hazard ratios, since log(HR) typically ranges ±2)
obs_ess <- ess(map_mix, sigma = 2)
```

The ESS represents the **equivalent number of patients in an idealized RCT** that would provide the same statistical information as the pooled observational data, after accounting for heterogeneity and bias through Bayesian shrinkage.

**Step 4: Calculate Inflation Factor**

```r
total_nominal_n <- sum(obs_data$N)  # 81,388
inflation_factor <- total_nominal_n / obs_ess
```

### Interpretation of Inflation Factor

- **Inflation < 20×:** Reasonable information content → Acceptable quality
- **Inflation 20-100×:** Substantial information devaluation → Use with caution
- **Inflation > 100×:** Massive false precision → Do not trust nominal N

For example, if nominal N=80,000 but ESS=2,000, the inflation factor is 40×, meaning the observational data should be weighted as if it were an RCT of only 2,000 patients, not 80,000.

### Why σ=2 for Log-Hazard Ratios?

The ESS calculation requires a reference variance representing "one unit of information." For log-hazard ratios in cardiovascular outcomes:
- Typical log(HR) values range from -0.3 (HR=0.74, strong benefit) to +0.3 (HR=1.35, moderate harm)
- A standard deviation of σ=2 on the log scale corresponds to HR ranging from ~0.14 to ~7.4
- This represents the plausible range of treatment effects in clinical trials, making σ²=4 a reasonable unit of information¹⁴

### MCMC Settings

To ensure convergence in the presence of heterogeneous observational data, we used stringent MCMC settings:

```r
options(RBesT.MC.control = list(adapt_delta = 0.999))
```

This tightens the Hamiltonian Monte Carlo sampler to avoid divergent transitions when fitting complex posterior distributions.

---

## Integration: The Three-Component Verdict

We integrate the three components into an overall assessment:

| DI | E-Value | Inflation | Grade | Recommendation |
|----|---------|-----------|-------|----------------|
| >2.0 | <1.5 | >100× | **C** | Exclude observational data (confounded) |
| 1-2 | <1.5 | 20-100× | **B-** | Use RCT CIs only (false precision) |
| <1.0 | >2.0 | <20× | **A** | May cautiously pool data |

---

## Software

- **Meta-analysis:** R 4.3.1, `meta` package (frequentist pooling)
- **Bayesian ESS:** R 4.3.1, `RBesT` package version 1.7-3
- **E-Values:** R 4.3.1, `EValue` package version 4.1.3
- **Stan backend:** RStan 2.26.23 for MCMC sampling

All code is available at [GitHub repository].

---

## References

12. VanderWeele TJ, Ding P. Sensitivity analysis in observational research: Introducing the E-value. *Ann Intern Med*. 2017;167(4):268-274.

14. Schmidli H, et al. Robust meta-analytic-predictive priors in clinical trials with historical control information. *Biometrics*. 2014;70(4):1023-1032.

15. Bavishi C, et al. Beta-blockers in heart failure with preserved ejection fraction: a meta-analysis. *Heart Fail Rev*. 2015;20(2):193-201.

16. Liu F, et al. Effects of beta-blockers on heart failure with preserved ejection fraction: a meta-analysis. *PLoS One*. 2014;9(3):e90555.

17. Lund LH, et al. Association between cardiovascular vs. non-cardiovascular co-morbidities and outcomes in heart failure with preserved ejection fraction. *Eur Heart J*. 2014;35(7):428-435.

19. Yamamoto K, et al. Effects of carvedilol on heart failure with preserved ejection fraction: the Japanese Diastolic Heart Failure Study (J-DHF). *Eur J Heart Fail*. 2013;15(1):110-118.

20. Flather MD, et al. Randomized trial to determine the effect of nebivolol on mortality and cardiovascular hospital admission in elderly patients with heart failure (SENIORS). *Eur Heart J*. 2005;26(3):215-225.

37. Groenwold RH, et al. Sensitivity analysis for the effects of multiple unmeasured confounders. *Ann Epidemiol*. 2016;26(9):605-611.

38. Hernán MA, Robins JM. Using big data to emulate a target trial when a randomized trial is not available. *Am J Epidemiol*. 2016;183(8):758-764.

39. Neuenschwander B, et al. Summarizing historical information on controls in clinical trials. *Clin Trials*. 2010;7(1):5-18.

40. [GWTG-HF registry publication - to be added]

41. [REDUCE-AMI reference - to be added]

---

**Word Count (Part C Methods):** ~1,450 words
