#!/usr/bin/env python3
"""
PART A: EMPIRICAL ANALYSIS OF BETA-BLOCKER EF THRESHOLD
Pure Python implementation (no dependencies)
"""

import math

# ================== VERIFIED INPUT DATA ==================

# EF 40-49% (Lancet Aug 2025)
ef_4049_hr = 0.75
ef_4049_ci_lower = 0.58
ef_4049_ci_upper = 0.97
ef_4049_events_bb = 106
ef_4049_events_control = 129
ef_4049_events_total = 235
ef_4049_n_bb = 991
ef_4049_n_control = 894
ef_4049_n = 1885

# EF ≥50% (NEJM Nov 2025)
ef_50plus_hr = 0.97
ef_50plus_ci_lower = 0.87
ef_50plus_ci_upper = 1.07  # VERIFIED
ef_50plus_events_bb = 717
ef_50plus_events_control = 748
ef_50plus_events_total = 1465
ef_50plus_n_bb = 8831
ef_50plus_n_control = 8970
ef_50plus_n = 17801

print("="*70)
print("BETA-BLOCKER EF THRESHOLD STATISTICAL ANALYSIS")
print("Data verified from published papers (NEJM & Lancet 2025)")
print("="*70)
print()

# ================== CALCULATIONS ==================

# Log hazard ratios
log_hr_4049 = math.log(ef_4049_hr)
log_hr_50plus = math.log(ef_50plus_hr)

# Standard errors from 95% CIs
se_4049 = (math.log(ef_4049_ci_upper) - math.log(ef_4049_ci_lower)) / (2 * 1.96)
se_50plus = (math.log(ef_50plus_ci_upper) - math.log(ef_50plus_ci_lower)) / (2 * 1.96)

print("VERIFIED DATA")
print("-" * 70)
print("\nEF 40-49% (Lancet, August 30, 2025):")
print(f"  Patients: {ef_4049_n} (BB={ef_4049_n_bb}, Control={ef_4049_n_control})")
print(f"  Events: {ef_4049_events_total} (BB={ef_4049_events_bb}, Control={ef_4049_events_control})")
print(f"  HR: {ef_4049_hr:.2f} (95% CI: {ef_4049_ci_lower:.2f}-{ef_4049_ci_upper:.2f})")
print(f"  log(HR) = {log_hr_4049:.4f}, SE = {se_4049:.4f}")

print("\nEF ≥50% (NEJM, November 9, 2025):")
print(f"  Patients: {ef_50plus_n} (BB={ef_50plus_n_bb}, Control={ef_50plus_n_control})")
print(f"  Events: {ef_50plus_events_total} (BB={ef_50plus_events_bb}, Control={ef_50plus_events_control})")
print(f"  HR: {ef_50plus_hr:.2f} (95% CI: {ef_50plus_ci_lower:.2f}-{ef_50plus_ci_upper:.2f})")
print(f"  log(HR) = {log_hr_50plus:.4f}, SE = {se_50plus:.4f}")
print()

# ================== TEST FOR INTERACTION ==================

print("="*70)
print("ANALYSIS 1: TEST FOR INTERACTION (THE SMOKING GUN)")
print("="*70)
print("\nResearch Question: Do beta-blockers have different effects in")
print("patients with EF 40-49% vs EF ≥50%?")
print("\nNull hypothesis: No difference in treatment effect between subgroups")
print()

# Z-test for difference
diff_log_hr = log_hr_4049 - log_hr_50plus
se_diff = math.sqrt(se_4049**2 + se_50plus**2)
z_interaction = diff_log_hr / se_diff

# Approximate p-value (two-tailed)
# Using approximation: P(|Z| > z) ≈ 2 * 0.5 * erfc(z/sqrt(2))
def norm_cdf(z):
    """Approximation of standard normal CDF"""
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

p_interaction = 2 * (1 - norm_cdf(abs(z_interaction)))

print(f"Difference in log(HR): {diff_log_hr:.4f}")
print(f"SE of difference: {se_diff:.4f}")
print(f"Z-statistic: {z_interaction:.3f}")
print(f"**P-value: {p_interaction:.3f}**")
print()

print("INTERPRETATION:")
if p_interaction < 0.05:
    print("  ✓ SIGNIFICANT interaction (p < 0.05)")
    print("  → Evidence supports different treatment effects")
else:
    print("  ✗ NON-SIGNIFICANT interaction (p ≥ 0.05)")
    print("  → NO statistical evidence for different treatment effects")
    print("  → The claimed threshold at EF=50% is NOT statistically supported")
    print("  → The HRs (0.75 vs 0.97) do NOT significantly differ")
print()

# ================== FRAGILITY INDEX ==================

print("="*70)
print("ANALYSIS 2: FRAGILITY INDEX")
print("="*70)
print("\nQuestion: How fragile is the EF 40-49% finding?")
print("Method: How many events must switch to make p ≥ 0.05?")
print()

def chi_square_p(events_trt, events_ctrl, n_trt, n_ctrl):
    """Chi-square test p-value"""
    total_events = events_trt + events_ctrl
    total_n = n_trt + n_ctrl

    # Expected values
    exp_trt = (n_trt / total_n) * total_events
    exp_ctrl = (n_ctrl / total_n) * total_events

    # Chi-square statistic
    chi_sq = (events_trt - exp_trt)**2 / exp_trt + \
             (events_ctrl - exp_ctrl)**2 / exp_ctrl

    # Approximate p-value for chi-square with df=1
    # P(X > chi_sq) ≈ erfc(sqrt(chi_sq/2))
    if chi_sq < 0.001:
        return 1.0
    p_val = math.erfc(math.sqrt(chi_sq / 2))
    return p_val

# Initial p-value
p_init = chi_square_p(ef_4049_events_bb, ef_4049_events_control,
                      ef_4049_n_bb, ef_4049_n_control)

print(f"Initial p-value (calculated): {p_init:.4f}")
print(f"Published p-value: 0.031")
print()

# Calculate fragility index
fi = 0
p_current = p_init
while p_current < 0.05 and fi < 20:
    fi += 1
    events_bb_new = ef_4049_events_bb + fi
    events_ctrl_new = ef_4049_events_control - fi
    p_current = chi_square_p(events_bb_new, events_ctrl_new,
                             ef_4049_n_bb, ef_4049_n_control)

fi_percent = (fi / ef_4049_events_total) * 100

print(f"**Fragility Index: {fi} events**")
print(f"As % of total events: {fi_percent:.2f}%")
print()

print("INTERPRETATION:")
print(f"  • Only {fi} event reclassifications needed to flip result to non-significant")
print(f"  • This represents just {fi_percent:.1f}% of the {ef_4049_events_total} total events")
print()
print("  Walsh et al. (2014) recommendations:")
print("    - FI > 5 for robust findings")
print("    - FI > 10 for practice-changing claims")
print()
if fi <= 5:
    print(f"  ✗ EXTREMELY FRAGILE: FI={fi} is far below recommended threshold")
    print("  → This finding is statistically unstable")
else:
    print(f"  ⚠ FRAGILE: FI={fi} is below recommended threshold for practice change")
print()

# ================== POWER ANALYSIS ==================

print("="*70)
print("ANALYSIS 3: POWER ANALYSIS")
print("="*70)
print("\nQuestion: Was the EF 40-49% subgroup adequately powered?")
print()

def power_cox(n_events, hr_true, alpha=0.05):
    """Power calculation for Cox regression"""
    z_alpha = 1.96  # For two-sided 5% test
    delta = math.log(hr_true)
    z_power = math.sqrt(n_events / 4) * abs(delta) - z_alpha
    return norm_cdf(z_power)

print(f"Current events: {ef_4049_events_total}")
print()
print("Power to detect various effect sizes:")

hrs_test = [0.70, 0.75, 0.80, 0.85, 0.90]
for hr in hrs_test:
    power = power_cox(ef_4049_events_total, hr)
    marker = " ← Observed HR" if hr == 0.75 else ""
    print(f"  HR = {hr:.2f}: {power*100:5.1f}%{marker}")

# Required events for 80% power
def required_events(hr_true, power=0.80, alpha=0.05):
    """Events needed for specified power"""
    z_alpha = 1.96
    z_beta = 0.84  # For 80% power
    delta = math.log(hr_true)
    return int(math.ceil(4 * ((z_alpha + z_beta) / abs(delta))**2))

events_80_power = required_events(0.80)
events_75_power = required_events(0.75)

print()
print("Events required for 80% power:")
print(f"  At HR=0.80: {events_80_power} events (current: {(ef_4049_events_total/events_80_power)*100:.1f}%)")
print(f"  At HR=0.75: {events_75_power} events (current: {(ef_4049_events_total/events_75_power)*100:.1f}%)")
print()

power_at_80 = power_cox(ef_4049_events_total, 0.80)
shortfall = ((events_80_power - ef_4049_events_total) / ef_4049_events_total) * 100

print("INTERPRETATION:")
if power_at_80 < 0.80:
    print(f"  ✗ UNDERPOWERED: Only {power_at_80*100:.0f}% power at HR=0.80")
    print(f"  → Would need {shortfall:.0f}% more events for 80% power")
    print("  → High risk of false positive/false negative findings")
else:
    print(f"  ✓ ADEQUATELY POWERED: {power_at_80*100:.0f}% power")
print()

# ================== POOLED EFFECT ==================

print("="*70)
print("ANALYSIS 4: OVERALL POOLED EFFECT")
print("="*70)
print("\nQuestion: What is the effect when both EF ranges are combined?")
print()

# Fixed-effect meta-analysis
w1 = 1 / se_4049**2
w2 = 1 / se_50plus**2
total_w = w1 + w2

pooled_log_hr = (log_hr_4049 * w1 + log_hr_50plus * w2) / total_w
pooled_se = math.sqrt(1 / total_w)
pooled_hr = math.exp(pooled_log_hr)
pooled_ci_lower = math.exp(pooled_log_hr - 1.96 * pooled_se)
pooled_ci_upper = math.exp(pooled_log_hr + 1.96 * pooled_se)

print(f"Total patients: {ef_4049_n + ef_50plus_n:,}")
print(f"Total events: {ef_4049_events_total + ef_50plus_events_total:,}")
print(f"\n**Pooled HR: {pooled_hr:.2f} (95% CI: {pooled_ci_lower:.2f}-{pooled_ci_upper:.2f})**")
print()

print("INTERPRETATION:")
if pooled_ci_upper < 1.0:
    print("  ✓ Significant benefit of beta-blockers overall")
else:
    print("  ✗ NO significant benefit of beta-blockers overall")
    print("  → When both EF ranges combined, confidence interval includes 1.0")
    print("  → No evidence of benefit across the EF spectrum")
print()

# ================== SUMMARY ==================

print("="*70)
print("SUMMARY OF KEY FINDINGS")
print("="*70)
print()

results = [
    ("Interaction test (p-value)", f"{p_interaction:.3f}"),
    ("Interaction significant?", "NO" if p_interaction >= 0.05 else "YES"),
    ("Fragility Index", f"{fi} events ({fi_percent:.1f}%)"),
    ("Fragility assessment", "EXTREMELY FRAGILE" if fi <= 5 else "FRAGILE"),
    ("Power at HR=0.80", f"{power_at_80*100:.1f}%"),
    ("Adequately powered?", "NO" if power_at_80 < 0.80 else "YES"),
    ("Events needed (80% power)", f"{events_80_power}"),
    ("Pooled HR (both groups)", f"{pooled_hr:.2f} ({pooled_ci_lower:.2f}-{pooled_ci_upper:.2f})"),
    ("Overall benefit?", "NO" if pooled_ci_upper >= 1.0 else "YES"),
]

for analysis, result in results:
    print(f"{analysis:.<50} {result}")

print()

# Save CSV
with open('empirical_results_summary.csv', 'w') as f:
    f.write("Analysis,Result\n")
    for analysis, result in results:
        f.write(f'"{analysis}","{result}"\n')

print("Results saved to: empirical_results_summary.csv")
print()

# ================== FINAL VERDICT ==================

print("="*70)
print("FINAL VERDICT")
print("="*70)
print()

print("The proposed EF 50% threshold FAILS statistical validation:")
print()

failures = []
if p_interaction >= 0.05:
    failures.append("interaction")
    print(f"  ✗ Interaction test NON-SIGNIFICANT (p={p_interaction:.3f} ≥ 0.05)")
    print("     → No evidence the HRs differ between subgroups")

if fi <= 5:
    failures.append("fragility")
    print(f"\n  ✗ Extremely FRAGILE (FI={fi} ≤ 5)")
    print(f"     → Only {fi} events need to change to flip the result")

if power_at_80 < 0.80:
    failures.append("power")
    print(f"\n  ✗ UNDERPOWERED ({power_at_80*100:.0f}% < 80%)")
    print(f"     → Needs {shortfall:.0f}% more events for reliable detection")

print(f"\n{'='*70}")
print(f"FAILED: {len(failures)}/3 core validation tests")
print(f"{'='*70}")
print()

print("CONCLUSION:")
print()
print("  The claim of a sharp efficacy threshold at EF=50% is NOT")
print("  supported by the statistical evidence. The 'finding' appears")
print("  to be an artifact of:")
print()
print("    1. Underpowered subgroup analysis")
print("    2. Statistical fragility")
print("    3. Dichotomization of a continuous variable")
print()
print("RECOMMENDATION:")
print()
print("  Clinical guidelines should NOT adopt EF-stratified beta-blocker")
print("  recommendations based on this evidence.")
print()
print("  The original authors should:")
print("    • Report the interaction test (p=0.069)")
print("    • Model EF as continuous (not dichotomized)")
print("    • Apply cross-validation to their IPD data")
print()
print("="*70)
print("ANALYSIS COMPLETE")
print("="*70)
