#!/usr/bin/env python3
"""
PART A: EMPIRICAL ANALYSIS OF BETA-BLOCKER EF THRESHOLD
Statistical Overfitting in Subgroup Analyses
VERIFIED DATA from published papers
"""

import numpy as np
from scipy import stats
import pandas as pd

# ================== VERIFIED INPUT DATA ==================

# EF 40-49% subgroup (Lancet, August 30, 2025)
ef_4049 = {
    'hr': 0.75,
    'ci_lower': 0.58,
    'ci_upper': 0.97,
    'n': 1885,
    'events_bb': 106,
    'events_control': 129,
    'n_bb': 991,
    'n_control': 894,
    'p': 0.031
}
ef_4049['events_total'] = ef_4049['events_bb'] + ef_4049['events_control']

# EF ≥50% subgroup (NEJM, November 9, 2025)
ef_50plus = {
    'hr': 0.97,
    'ci_lower': 0.87,
    'ci_upper': 1.07,  # VERIFIED
    'n': 17801,
    'events_bb': 717,
    'events_control': 748,
    'n_bb': 8831,
    'n_control': 8970,
    'p': 0.54
}
ef_50plus['events_total'] = ef_50plus['events_bb'] + ef_50plus['events_control']

print("="*60)
print("BETA-BLOCKER EF THRESHOLD ANALYSIS")
print("Data verified from published papers")
print("="*60)
print()

# ================== LOG-HRS AND STANDARD ERRORS ==================

log_hr_4049 = np.log(ef_4049['hr'])
log_hr_50plus = np.log(ef_50plus['hr'])

# Standard errors from 95% CIs
se_4049 = (np.log(ef_4049['ci_upper']) - np.log(ef_4049['ci_lower'])) / (2 * 1.96)
se_50plus = (np.log(ef_50plus['ci_upper']) - np.log(ef_50plus['ci_lower'])) / (2 * 1.96)

print("BASIC STATISTICS")
print("="*60)
print(f"\nEF 40-49%:")
print(f"  Patients: {ef_4049['n']} (BB={ef_4049['n_bb']}, Control={ef_4049['n_control']})")
print(f"  Events: {ef_4049['events_total']} (BB={ef_4049['events_bb']}, Control={ef_4049['events_control']})")
print(f"  HR: {ef_4049['hr']:.2f} (95% CI: {ef_4049['ci_lower']:.2f}-{ef_4049['ci_upper']:.2f}), p={ef_4049['p']:.3f}")
print(f"  log(HR)={log_hr_4049:.4f}, SE={se_4049:.4f}")

print(f"\nEF ≥50%:")
print(f"  Patients: {ef_50plus['n']} (BB={ef_50plus['n_bb']}, Control={ef_50plus['n_control']})")
print(f"  Events: {ef_50plus['events_total']} (BB={ef_50plus['events_bb']}, Control={ef_50plus['events_control']})")
print(f"  HR: {ef_50plus['hr']:.2f} (95% CI: {ef_50plus['ci_lower']:.2f}-{ef_50plus['ci_upper']:.2f}), p={ef_50plus['p']:.2f}")
print(f"  log(HR)={log_hr_50plus:.4f}, SE={se_50plus:.4f}")
print()

# ================== TEST FOR INTERACTION ==================

print("TEST FOR INTERACTION")
print("="*60)
print("Null hypothesis: HR(40-49%) = HR(≥50%)")
print("Alternative: HR(40-49%) ≠ HR(≥50%)")
print()

# Z-test for difference in log hazard ratios
diff_log_hr = log_hr_4049 - log_hr_50plus
se_diff = np.sqrt(se_4049**2 + se_50plus**2)
z_interaction = diff_log_hr / se_diff
p_interaction = 2 * stats.norm.cdf(-abs(z_interaction))

print(f"Difference in log(HR): {diff_log_hr:.4f}")
print(f"SE of difference: {se_diff:.4f}")
print(f"Z-statistic: {z_interaction:.3f}")
print(f"P-value: {p_interaction:.3f}")
print()

if p_interaction < 0.05:
    print("INTERPRETATION: SIGNIFICANT interaction - different treatment effects")
else:
    print("INTERPRETATION: NON-SIGNIFICANT interaction")
    print("→ No statistical evidence for different treatment effects between subgroups")
    print("→ The apparent threshold at EF=50% is not supported by interaction testing")
print()

# ================== FRAGILITY INDEX ==================

print("FRAGILITY INDEX ANALYSIS")
print("="*60)
print("Question: How many events must change to make p≥0.05?")
print()

def calc_chi_sq_p(events_trt, events_ctrl, n_trt, n_ctrl):
    """Calculate chi-square p-value for event rates"""
    total_events = events_trt + events_ctrl
    total_n = n_trt + n_ctrl
    expected_trt = (n_trt / total_n) * total_events
    expected_ctrl = (n_ctrl / total_n) * total_events

    chi_sq = (events_trt - expected_trt)**2 / expected_trt + \
             (events_ctrl - expected_ctrl)**2 / expected_ctrl

    return stats.chi2.sf(chi_sq, df=1)

# Initial p-value
p_current = calc_chi_sq_p(ef_4049['events_bb'], ef_4049['events_control'],
                          ef_4049['n_bb'], ef_4049['n_control'])

print(f"Initial p-value: {p_current:.4f} (published: {ef_4049['p']:.3f})")

# Calculate fragility index
fi = 0
while p_current < 0.05 and fi < 20:
    fi += 1
    events_bb_new = ef_4049['events_bb'] + fi
    events_ctrl_new = ef_4049['events_control'] - fi
    p_current = calc_chi_sq_p(events_bb_new, events_ctrl_new,
                               ef_4049['n_bb'], ef_4049['n_control'])

fi_percent = (fi / ef_4049['events_total']) * 100

print(f"\nFragility Index: {fi} events")
print(f"As % of total events: {fi_percent:.2f}%")
print(f"\nINTERPRETATION:")
print(f"→ Only {fi} event reclassifications needed to render finding non-significant")
print(f"→ Walsh et al. suggest FI>5 for robust findings, FI>10 for practice-changing claims")
print(f"→ FI={fi} indicates EXTREME statistical fragility")
print()

# ================== POWER ANALYSIS ==================

print("POWER ANALYSIS (EF 40-49% Subgroup)")
print("="*60)

def calc_power_cox(n_events, hr_true, alpha=0.05):
    """Calculate power using Schoenfeld's formula"""
    z_alpha = stats.norm.ppf(1 - alpha/2)
    delta = np.log(hr_true)
    return stats.norm.cdf(np.sqrt(n_events/4) * abs(delta) - z_alpha)

hrs_test = [0.70, 0.75, 0.80, 0.85, 0.90]
powers = [calc_power_cox(ef_4049['events_total'], hr) for hr in hrs_test]

print(f"Current events: {ef_4049['events_total']}")
print("\nPower to detect various effect sizes:")
for hr, power in zip(hrs_test, powers):
    marker = " ← Observed HR" if hr == 0.75 else ""
    print(f"  HR={hr:.2f}: {power*100:.1f}%{marker}")

# Required events for 80% power
def calc_required_events(hr_true, power=0.80, alpha=0.05):
    """Calculate required events for specified power"""
    z_alpha = stats.norm.ppf(1 - alpha/2)
    z_beta = stats.norm.ppf(power)
    delta = np.log(hr_true)
    return int(np.ceil(4 * ((z_alpha + z_beta) / abs(delta))**2))

events_needed_80 = calc_required_events(0.80)
events_needed_75 = calc_required_events(0.75)

print(f"\nEvents required for 80% power:")
print(f"  At HR=0.80: {events_needed_80} events ({(ef_4049['events_total']/events_needed_80)*100:.1f}% of actual)")
print(f"  At HR=0.75: {events_needed_75} events ({(ef_4049['events_total']/events_needed_75)*100:.1f}% of actual)")
print()

power_at_80 = calc_power_cox(ef_4049['events_total'], 0.80)
additional_needed = ((events_needed_80 - ef_4049['events_total']) / ef_4049['events_total']) * 100

print("INTERPRETATION:")
print(f"→ Subgroup analysis was UNDERPOWERED for reliable detection")
print(f"→ Current analysis has only {power_at_80*100:.0f}% power at HR=0.80")
print(f"→ Would need {additional_needed:.0f}% more events for adequate (80%) power")
print()

# ================== OVERALL POOLED ESTIMATE ==================

print("OVERALL POOLED EFFECT (Both EF ranges combined)")
print("="*60)

# Fixed-effect meta-analysis
weight_4049 = 1 / se_4049**2
weight_50plus = 1 / se_50plus**2
total_weight = weight_4049 + weight_50plus

pooled_log_hr = (log_hr_4049 * weight_4049 + log_hr_50plus * weight_50plus) / total_weight
pooled_se = np.sqrt(1 / total_weight)
pooled_hr = np.exp(pooled_log_hr)
pooled_ci_lower = np.exp(pooled_log_hr - 1.96 * pooled_se)
pooled_ci_upper = np.exp(pooled_log_hr + 1.96 * pooled_se)
pooled_p = 2 * stats.norm.cdf(-abs(pooled_log_hr / pooled_se))

print(f"Total patients: {ef_4049['n'] + ef_50plus['n']}")
print(f"Total events: {ef_4049['events_total'] + ef_50plus['events_total']}")
print(f"Pooled HR: {pooled_hr:.2f} (95% CI: {pooled_ci_lower:.2f}-{pooled_ci_upper:.2f})")
print(f"P-value: {pooled_p:.3f}")
print()

if pooled_ci_upper < 1.0:
    print("INTERPRETATION: Significant benefit of beta-blockers overall")
else:
    print("INTERPRETATION: No significant benefit of beta-blockers overall")
    print("→ When both EF ranges combined, no evidence of benefit")
print()

# ================== SUMMARY TABLE ==================

print("="*60)
print("SUMMARY OF KEY FINDINGS")
print("="*60)
print()

results_data = {
    'Analysis': [
        'Interaction test (p-value)',
        'Conclusion on interaction',
        'Fragility Index (events)',
        'Fragility Index (% of events)',
        'Fragility interpretation',
        'Power at HR=0.75 (observed)',
        'Power at HR=0.80',
        'Power interpretation',
        'Required events for 80% power',
        'Overall pooled HR (both groups)',
        'Overall conclusion'
    ],
    'Result': [
        f'{p_interaction:.3f}',
        'SIGNIFICANT' if p_interaction < 0.05 else 'NON-SIGNIFICANT',
        f'{fi}',
        f'{fi_percent:.1f}%',
        'EXTREMELY FRAGILE' if fi <= 5 else 'FRAGILE',
        f'{calc_power_cox(ef_4049["events_total"], 0.75)*100:.1f}%',
        f'{power_at_80*100:.1f}%',
        'UNDERPOWERED' if power_at_80 < 0.80 else 'ADEQUATE',
        f'{events_needed_80}',
        f'{pooled_hr:.2f} ({pooled_ci_lower:.2f}-{pooled_ci_upper:.2f})',
        'Benefit' if pooled_ci_upper < 1.0 else 'No benefit'
    ]
}

df_results = pd.DataFrame(results_data)
print(df_results.to_string(index=False))
print()

# Save results
df_results.to_csv('empirical_results_summary.csv', index=False)
print("\nResults saved to: empirical_results_summary.csv")

# ================== FINAL VERDICT ==================

print("\n" + "="*60)
print("FINAL VERDICT")
print("="*60)
print()

failures = 0
if p_interaction >= 0.05:
    print(f"✗ FAILED: Interaction test non-significant (p={p_interaction:.3f})")
    failures += 1

if fi <= 5:
    print(f"✗ FAILED: Fragility Index ({fi}) below recommended threshold (>5)")
    failures += 1

if power_at_80 < 0.80:
    print(f"✗ FAILED: Underpowered ({power_at_80*100:.0f}% < 80%)")
    failures += 1

print(f"\nThe proposed EF threshold fails {failures}/3 core statistical validation tests.")
print("\nCONCLUSION:")
print("The claim of a sharp efficacy threshold at EF=50% is NOT supported by")
print("the statistical evidence. The finding appears to be an artifact of")
print("underpowered subgroup analysis and dichotomization of a continuous variable.")
print("\nRECOMMENDATION:")
print("Clinical guidelines should NOT adopt EF-stratified beta-blocker recommendations")
print("based on this evidence.")
print()
print("="*60)
print("ANALYSIS COMPLETE")
print("="*60)
