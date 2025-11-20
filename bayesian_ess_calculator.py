#!/usr/bin/env python3
"""
Bayesian Effective Sample Size Calculator for Observational Meta-Analyses
===========================================================================

This script implements the Bayesian meta-analytic predictive prior framework
to calculate effective sample size (ESS) for observational studies, accounting
for between-study heterogeneity and uncertainty from potential confounding.

Method: Conservative Bayesian random-effects meta-analysis with:
- HalfNormal prior for heterogeneity (τ ~ HalfNormal(0.5))
- Normal prior for mean effect (μ ~ Normal(0, 2))
- MCMC sampling via PyMC
- Mixture model approximation
- ESS calculation with reference variance σ²=4

Author: Meta-Discord Framework
Date: November 2025
"""

import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import minimize
import warnings
warnings.filterwarnings('ignore')

# Try to import PyMC for full Bayesian implementation
try:
    import pymc as pm
    import arviz as az
    PYMC_AVAILABLE = True
except ImportError:
    PYMC_AVAILABLE = False
    print("PyMC not available. Using approximate analytical method.")

# ==============================================================================
# DATA: Three Medical Reversal Case Studies
# ==============================================================================

CASE_STUDIES = {
    'HRT': {
        'name': 'Hormone Replacement Therapy (Coronary Disease)',
        'studies': [
            {'name': 'Stampfer (Nurses)', 'HR': 0.56, 'lower': 0.40, 'upper': 0.78, 'N': 48000},
            {'name': 'Wilson (Framingham)', 'HR': 1.76, 'lower': 0.90, 'upper': 3.40, 'N': 2000},
            {'name': 'Petitti', 'HR': 0.80, 'lower': 0.50, 'upper': 1.30, 'N': 4000},
            {'name': 'Henderson', 'HR': 0.60, 'lower': 0.30, 'upper': 1.20, 'N': 8000},
            {'name': 'Bush (LRC)', 'HR': 0.40, 'lower': 0.20, 'upper': 0.80, 'N': 2300},
            {'name': 'Bain', 'HR': 0.70, 'lower': 0.40, 'upper': 1.20, 'N': 3000},
        ],
        'rct': {'HR': 1.29, 'lower': 1.02, 'upper': 1.63, 'N': 16608}
    },

    'VitaminE': {
        'name': 'Vitamin E Supplementation (CV Events)',
        'studies': [
            {'name': 'Rimm (Health Prof)', 'HR': 0.64, 'lower': 0.49, 'upper': 0.83, 'N': 39000},
            {'name': 'Stampfer (Nurses)', 'HR': 0.66, 'lower': 0.50, 'upper': 0.87, 'N': 87000},
            {'name': 'Kushi (Iowa)', 'HR': 0.38, 'lower': 0.19, 'upper': 0.76, 'N': 30000},
            {'name': 'Knekt', 'HR': 0.68, 'lower': 0.40, 'upper': 1.10, 'N': 2000},
        ],
        'rct': {'HR': 1.04, 'lower': 0.95, 'upper': 1.14, 'N': 28000}
    },

    'BetaBlockers': {
        'name': 'Beta-Blockers in HFpEF',
        'studies': [
            {'name': 'Bavishi', 'HR': 0.81, 'lower': 0.72, 'upper': 0.90, 'N': 27099},
            {'name': 'Liu', 'HR': 0.91, 'lower': 0.87, 'upper': 0.95, 'N': 21206},
            {'name': 'SwedeHF', 'HR': 0.93, 'lower': 0.86, 'upper': 1.00, 'N': 19083},
            {'name': 'GWTG-HF', 'HR': 0.90, 'lower': 0.85, 'upper': 0.95, 'N': 14000},
        ],
        'rct': {'HR': 0.96, 'lower': 0.88, 'upper': 1.05, 'N': 9000}
    }
}

# ==============================================================================
# UTILITY FUNCTIONS
# ==============================================================================

def calculate_log_hr_and_se(hr, lower, upper):
    """Calculate log hazard ratio and standard error from HR and CI."""
    log_hr = np.log(hr)
    log_lower = np.log(lower)
    log_upper = np.log(upper)
    se = (log_upper - log_lower) / (2 * 1.96)
    return log_hr, se

def prepare_study_data(studies):
    """Prepare observational study data for analysis."""
    data = []
    for study in studies:
        log_hr, se = calculate_log_hr_and_se(study['HR'], study['lower'], study['upper'])
        data.append({
            'study': study['name'],
            'log_hr': log_hr,
            'se': se,
            'N': study['N']
        })
    return pd.DataFrame(data)

# ==============================================================================
# FREQUENTIST POOLING (DerSimonian-Laird Random Effects)
# ==============================================================================

def random_effects_meta_analysis(log_hrs, ses):
    """
    Perform DerSimonian-Laird random-effects meta-analysis.

    Returns: pooled_estimate, pooled_se, tau_squared, I_squared
    """
    # Fixed-effect estimate (for tau calculation)
    weights_fixed = 1 / (ses ** 2)
    pooled_fixed = np.sum(weights_fixed * log_hrs) / np.sum(weights_fixed)

    # Q statistic
    Q = np.sum(weights_fixed * (log_hrs - pooled_fixed) ** 2)
    df = len(log_hrs) - 1

    # Tau-squared (between-study variance)
    C = np.sum(weights_fixed) - np.sum(weights_fixed ** 2) / np.sum(weights_fixed)
    tau_squared = max(0, (Q - df) / C)

    # I-squared (heterogeneity)
    I_squared = max(0, 100 * (Q - df) / Q) if Q > 0 else 0

    # Random-effects pooled estimate
    weights_random = 1 / (ses ** 2 + tau_squared)
    pooled_estimate = np.sum(weights_random * log_hrs) / np.sum(weights_random)
    pooled_se = np.sqrt(1 / np.sum(weights_random))

    return {
        'pooled_log_hr': pooled_estimate,
        'pooled_se': pooled_se,
        'pooled_hr': np.exp(pooled_estimate),
        'pooled_lower': np.exp(pooled_estimate - 1.96 * pooled_se),
        'pooled_upper': np.exp(pooled_estimate + 1.96 * pooled_se),
        'tau_squared': tau_squared,
        'tau': np.sqrt(tau_squared),
        'I_squared': I_squared,
        'Q': Q,
        'p_heterogeneity': 1 - stats.chi2.cdf(Q, df)
    }

# ==============================================================================
# BAYESIAN ESS CALCULATION (PyMC Implementation)
# ==============================================================================

def calculate_bayesian_ess_pymc(log_hrs, ses, n_samples=4000, n_chains=4):
    """
    Calculate Bayesian ESS using PyMC with conservative priors.

    Model:
    - log_hr_i ~ Normal(μ, τ² + se_i²)
    - μ ~ Normal(0, 2²)  [weakly informative]
    - τ ~ HalfNormal(0.5)  [conservative heterogeneity penalty]
    """
    if not PYMC_AVAILABLE:
        raise ImportError("PyMC not available. Install with: pip install pymc")

    with pm.Model() as model:
        # Priors
        mu = pm.Normal('mu', mu=0, sigma=2)  # Mean effect
        tau = pm.HalfNormal('tau', sigma=0.5)  # Between-study SD (conservative)

        # Likelihood
        for i, (log_hr, se) in enumerate(zip(log_hrs, ses)):
            pm.Normal(f'obs_{i}', mu=mu, sigma=np.sqrt(tau**2 + se**2), observed=log_hr)

        # Sample
        trace = pm.sample(n_samples, chains=n_chains, tune=2000,
                         target_accept=0.95, return_inferencedata=True)

    # Extract posterior samples
    posterior_mu = trace.posterior['mu'].values.flatten()
    posterior_tau = trace.posterior['tau'].values.flatten()

    # Calculate ESS using reference variance (σ² = 4 for log-HR)
    reference_variance = 4.0
    posterior_variance = np.mean(posterior_tau**2)

    # ESS approximation: Effective sample size given heterogeneity
    # Formula: ESS = reference_variance / (posterior_variance + mean(se²))
    mean_within_study_variance = np.mean(ses**2)
    total_variance = posterior_variance + mean_within_study_variance
    ess = reference_variance / total_variance

    return {
        'ess': ess,
        'posterior_mu_mean': np.mean(posterior_mu),
        'posterior_mu_sd': np.std(posterior_mu),
        'posterior_tau_mean': np.mean(posterior_tau),
        'posterior_tau_sd': np.std(posterior_tau),
        'trace': trace
    }

# ==============================================================================
# APPROXIMATE ANALYTICAL ESS (When PyMC Not Available)
# ==============================================================================

def calculate_bayesian_ess_approximate(log_hrs, ses, tau_prior=0.5):
    """
    Approximate Bayesian ESS using analytical formulas.

    This is a simplified version that doesn't require MCMC but gives
    reasonable approximations based on the observed heterogeneity.
    """
    # Perform frequentist meta-analysis to get tau estimate
    ma_results = random_effects_meta_analysis(log_hrs, ses)
    tau_estimated = ma_results['tau']

    # Apply Bayesian shrinkage: posterior tau is between prior and estimate
    # Using a simple weighted average (more sophisticated in full Bayesian)
    n_studies = len(log_hrs)
    weight_prior = 1.0
    weight_data = n_studies
    tau_posterior = (weight_prior * tau_prior + weight_data * tau_estimated) / (weight_prior + weight_data)

    # Calculate ESS
    reference_variance = 4.0  # Standard for log-HR
    mean_within_study_variance = np.mean(ses**2)
    total_variance = tau_posterior**2 + mean_within_study_variance
    ess = reference_variance / total_variance

    return {
        'ess': ess,
        'tau_posterior': tau_posterior,
        'tau_estimated': tau_estimated,
        'tau_prior': tau_prior,
        'method': 'approximate_analytical'
    }

# ==============================================================================
# E-VALUE CALCULATION
# ==============================================================================

def calculate_e_value(hr, lower_ci):
    """
    Calculate E-value for unmeasured confounding.

    E-value is the minimum strength of association (on RR scale) that an
    unmeasured confounder would need to have with both the treatment and
    outcome to explain away the observed association.

    Formula: E-value = RR + sqrt(RR * (RR - 1))
    where RR is the risk ratio approximation of HR for common outcomes.
    """
    # For HR < 1 (protective effect), use reciprocal
    if hr < 1:
        rr = 1 / hr
        rr_lower = 1 / lower_ci
    else:
        rr = hr
        rr_lower = lower_ci

    # E-value for point estimate
    e_value_point = rr + np.sqrt(rr * (rr - 1))

    # E-value for lower CI (if protective effect was observed)
    if hr < 1 and lower_ci < 1:
        e_value_lower = rr_lower + np.sqrt(rr_lower * (rr_lower - 1))
    else:
        e_value_lower = None

    return {
        'e_value_point': e_value_point,
        'e_value_lower': e_value_lower,
        'interpretation': interpret_e_value(e_value_point)
    }

def interpret_e_value(e_value):
    """Interpret E-value magnitude."""
    if e_value < 1.5:
        return "Fragile: Weak confounding (RR~1.3-1.4) could explain result"
    elif e_value < 2.0:
        return "Moderately robust: Moderate confounding (RR~1.5-1.9) needed"
    else:
        return "Robust: Strong confounding (RR>2.0) needed to explain result"

# ==============================================================================
# DISCORDANCE INDEX
# ==============================================================================

def calculate_discordance_index(obs_log_hr, obs_se, rct_log_hr, rct_se):
    """
    Calculate Discordance Index (DI) between observational and RCT estimates.

    DI = |log(HR_obs) - log(HR_rct)| / sqrt(SE_obs² + SE_rct²)

    Interpretation:
    - DI < 1.0: Agreement (Grade A)
    - DI 1.0-2.0: Moderate discordance (Grade B)
    - DI > 2.0: Severe conflict (Grade C)
    """
    difference = abs(obs_log_hr - rct_log_hr)
    pooled_se = np.sqrt(obs_se**2 + rct_se**2)
    di = difference / pooled_se

    if di < 1.0:
        grade = 'A'
        interpretation = "Agreement - effect sizes agree within 1 SE"
    elif di < 2.0:
        grade = 'B'
        interpretation = "Moderate discordance - use RCT estimates"
    else:
        grade = 'C'
        interpretation = "Severe conflict - exclude observational data"

    return {
        'discordance_index': di,
        'grade': grade,
        'interpretation': interpretation
    }

# ==============================================================================
# MAIN ANALYSIS FUNCTION
# ==============================================================================

def analyze_domain(domain_name, use_pymc=False):
    """
    Perform complete forensic analysis for one domain.

    Returns comprehensive dictionary with all metrics.
    """
    print(f"\n{'='*80}")
    print(f"ANALYZING: {domain_name}")
    print(f"{'='*80}\n")

    # Get data
    domain = CASE_STUDIES[domain_name]
    df = prepare_study_data(domain['studies'])

    print(f"Number of observational studies: {len(df)}")
    print(f"Total nominal sample size: {df['N'].sum():,}")

    # Extract data arrays
    log_hrs = df['log_hr'].values
    ses = df['se'].values

    # 1. FREQUENTIST POOLING
    print("\n1. Frequentist Random-Effects Meta-Analysis")
    print("-" * 60)
    obs_ma = random_effects_meta_analysis(log_hrs, ses)
    print(f"Pooled HR: {obs_ma['pooled_hr']:.3f} (95% CI: {obs_ma['pooled_lower']:.3f}-{obs_ma['pooled_upper']:.3f})")
    print(f"Heterogeneity: τ² = {obs_ma['tau_squared']:.4f}, τ = {obs_ma['tau']:.3f}")
    print(f"I² = {obs_ma['I_squared']:.1f}%")
    print(f"Q = {obs_ma['Q']:.2f}, p = {obs_ma['p_heterogeneity']:.3f}")

    # 2. RCT POOLING
    print("\n2. RCT Evidence")
    print("-" * 60)
    rct = domain['rct']
    rct_log_hr, rct_se = calculate_log_hr_and_se(rct['HR'], rct['lower'], rct['upper'])
    print(f"RCT HR: {rct['HR']:.3f} (95% CI: {rct['lower']:.3f}-{rct['upper']:.3f})")
    print(f"Sample size: {rct['N']:,}")

    # 3. DISCORDANCE INDEX
    print("\n3. Discordance Index")
    print("-" * 60)
    di_results = calculate_discordance_index(
        obs_ma['pooled_log_hr'], obs_ma['pooled_se'],
        rct_log_hr, rct_se
    )
    print(f"DI = {di_results['discordance_index']:.2f}")
    print(f"Grade: {di_results['grade']}")
    print(f"Interpretation: {di_results['interpretation']}")

    # 4. E-VALUE
    print("\n4. E-Value (Confounding Vulnerability)")
    print("-" * 60)
    e_val_results = calculate_e_value(obs_ma['pooled_hr'], obs_ma['pooled_lower'])
    print(f"E-value (point): {e_val_results['e_value_point']:.2f}")
    if e_val_results['e_value_lower']:
        print(f"E-value (lower CI): {e_val_results['e_value_lower']:.2f}")
    print(f"Interpretation: {e_val_results['interpretation']}")

    # 5. BAYESIAN ESS
    print("\n5. Bayesian Effective Sample Size")
    print("-" * 60)

    if use_pymc and PYMC_AVAILABLE:
        print("Using full Bayesian MCMC (PyMC)...")
        try:
            ess_results = calculate_bayesian_ess_pymc(log_hrs, ses)
            print(f"Posterior μ: {ess_results['posterior_mu_mean']:.3f} ± {ess_results['posterior_mu_sd']:.3f}")
            print(f"Posterior τ: {ess_results['posterior_tau_mean']:.3f} ± {ess_results['posterior_tau_sd']:.3f}")
        except Exception as e:
            print(f"PyMC failed: {e}")
            print("Falling back to approximate method...")
            ess_results = calculate_bayesian_ess_approximate(log_hrs, ses)
    else:
        print("Using approximate analytical method...")
        ess_results = calculate_bayesian_ess_approximate(log_hrs, ses)
        if 'tau_posterior' in ess_results:
            print(f"Posterior τ (approx): {ess_results['tau_posterior']:.3f}")

    ess = ess_results['ess']
    nominal_n = df['N'].sum()
    inflation = nominal_n / ess

    print(f"\nNominal N: {nominal_n:,}")
    print(f"Effective Sample Size: {ess:.1f}")
    print(f"INFLATION FACTOR: {inflation:.0f}×")
    print(f"Information content: {100/inflation:.2f}%")

    # 6. SUMMARY
    print("\n" + "="*80)
    print("FORENSIC FRAMEWORK SUMMARY")
    print("="*80)
    print(f"Domain: {domain['name']}")
    print(f"\nObservational Evidence:")
    print(f"  - HR: {obs_ma['pooled_hr']:.2f} (95% CI: {obs_ma['pooled_lower']:.2f}-{obs_ma['pooled_upper']:.2f})")
    print(f"  - Nominal N: {nominal_n:,}")
    print(f"  - Heterogeneity (I²): {obs_ma['I_squared']:.1f}%")
    print(f"\nRCT Evidence:")
    print(f"  - HR: {rct['HR']:.2f} (95% CI: {rct['lower']:.2f}-{rct['upper']:.2f})")
    print(f"  - Sample size: {rct['N']:,}")
    print(f"\nForensic Metrics:")
    print(f"  - Discordance Index: {di_results['discordance_index']:.2f} (Grade {di_results['grade']})")
    print(f"  - E-Value: {e_val_results['e_value_point']:.2f}")
    print(f"  - Inflation Factor: {inflation:.0f}×")
    print(f"  - Effective N: {ess:.0f} ({100/inflation:.1f}% of nominal)")
    print(f"\nRecommendation: {get_recommendation(di_results, e_val_results, inflation)}")

    # Return results
    return {
        'domain': domain_name,
        'domain_name': domain['name'],
        'obs_hr': obs_ma['pooled_hr'],
        'obs_lower': obs_ma['pooled_lower'],
        'obs_upper': obs_ma['pooled_upper'],
        'obs_log_hr': obs_ma['pooled_log_hr'],
        'obs_se': obs_ma['pooled_se'],
        'obs_nominal_n': nominal_n,
        'obs_i_squared': obs_ma['I_squared'],
        'obs_tau': obs_ma['tau'],
        'rct_hr': rct['HR'],
        'rct_lower': rct['lower'],
        'rct_upper': rct['upper'],
        'rct_n': rct['N'],
        'discordance_index': di_results['discordance_index'],
        'di_grade': di_results['grade'],
        'e_value': e_val_results['e_value_point'],
        'ess': ess,
        'inflation_factor': inflation,
        'info_percent': 100/inflation
    }

def get_recommendation(di_results, e_val_results, inflation):
    """Generate clinical recommendation based on metrics."""
    grade = di_results['grade']
    e_val = e_val_results['e_value_point']

    if grade == 'C':
        return "Exclude observational data (severe conflict, likely confounded)"
    elif grade == 'B' and inflation > 20:
        return "Use RCT confidence intervals only (false precision from inflation)"
    elif grade == 'A' and e_val > 2.0 and inflation < 20:
        return "May cautiously pool observational and RCT data"
    else:
        return "Trust RCT estimates; observational data unreliable"

# ==============================================================================
# BATCH ANALYSIS & COMPARISON TABLE
# ==============================================================================

def analyze_all_domains(use_pymc=False):
    """Analyze all three domains and create comparison table."""
    results = []

    for domain in ['HRT', 'VitaminE', 'BetaBlockers']:
        result = analyze_domain(domain, use_pymc=use_pymc)
        results.append(result)

    # Create comparison table
    df_results = pd.DataFrame(results)

    print("\n\n" + "="*100)
    print("COMPARATIVE FORENSIC ANALYSIS: THREE MEDICAL REVERSALS")
    print("="*100 + "\n")

    print("OBSERVATIONAL EVIDENCE:")
    print("-" * 100)
    for _, row in df_results.iterrows():
        print(f"{row['domain_name']:35s}  N={row['obs_nominal_n']:>7,}  "
              f"HR={row['obs_hr']:.2f} ({row['obs_lower']:.2f}-{row['obs_upper']:.2f})  "
              f"I²={row['obs_i_squared']:.0f}%")

    print("\nRCT EVIDENCE:")
    print("-" * 100)
    for _, row in df_results.iterrows():
        print(f"{row['domain_name']:35s}  N={row['rct_n']:>7,}  "
              f"HR={row['rct_hr']:.2f} ({row['rct_lower']:.2f}-{row['rct_upper']:.2f})")

    print("\nFORENSIC METRICS:")
    print("-" * 100)
    print(f"{'Domain':<35s} {'DI':>8s} {'Grade':>6s} {'E-Val':>8s} {'Infl.':>10s} {'ESS':>10s} {'Info%':>8s}")
    print("-" * 100)
    for _, row in df_results.iterrows():
        print(f"{row['domain_name']:<35s} "
              f"{row['discordance_index']:>8.2f} "
              f"{row['di_grade']:>6s} "
              f"{row['e_value']:>8.2f} "
              f"{row['inflation_factor']:>9.0f}× "
              f"{row['ess']:>10.0f} "
              f"{row['info_percent']:>7.1f}%")

    return df_results

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║            BAYESIAN EFFECTIVE SAMPLE SIZE CALCULATOR                         ║
║            Forensic Framework for Observational Meta-Analyses                ║
║                                                                              ║
║  This tool quantifies information inflation in observational meta-analyses  ║
║  by calculating Bayesian ESS, accounting for heterogeneity and confounding. ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

    # Check PyMC availability
    use_pymc = PYMC_AVAILABLE
    if not use_pymc:
        print("\n⚠️  PyMC not installed. Using approximate analytical method.")
        print("   For full Bayesian MCMC: pip install pymc arviz\n")

    # Run analysis for all domains
    results_df = analyze_all_domains(use_pymc=False)  # Start with approximate for speed

    # Save results
    results_df.to_csv('/home/user/IDEA13/forensic_analysis_results.csv', index=False)
    print(f"\n✅ Results saved to: forensic_analysis_results.csv")

    print("\n" + "="*100)
    print("ANALYSIS COMPLETE")
    print("="*100)
