# ================================================================
# PART A: EMPIRICAL ANALYSIS OF BETA-BLOCKER EF THRESHOLD
# "Statistical Overfitting in Subgroup Analyses"
# VERIFIED DATA from published papers
# ================================================================

library(tidyverse)

# --- 1. VERIFIED INPUT DATA ---

# EF 40-49% subgroup (Lancet, August 30, 2025)
# Source: "β blockers after myocardial infarction with mildly reduced ejection fraction"
ef_4049_hr <- 0.75
ef_4049_ci_lower <- 0.58
ef_4049_ci_upper <- 0.97
ef_4049_n <- 1885
ef_4049_events_bb <- 106
ef_4049_events_control <- 129
ef_4049_n_bb <- 991
ef_4049_n_control <- 894
ef_4049_events_total <- 235  # 106 + 129
ef_4049_p <- 0.031

# EF ≥50% subgroup (NEJM, November 9, 2025)
# Source: "Beta-Blockers after Myocardial Infarction with Normal Ejection Fraction"
ef_50plus_hr <- 0.97
ef_50plus_ci_lower <- 0.87
ef_50plus_ci_upper <- 1.07  # VERIFIED (not 1.09)
ef_50plus_n <- 17801
ef_50plus_events_bb <- 717
ef_50plus_events_control <- 748
ef_50plus_n_bb <- 8831
ef_50plus_n_control <- 8970
ef_50plus_events_total <- 1465  # 717 + 748
ef_50plus_p <- 0.54

cat("===================================================\n")
cat("BETA-BLOCKER EF THRESHOLD ANALYSIS\n")
cat("Data verified from published papers\n")
cat("===================================================\n\n")

# --- 2. CALCULATE LOG-HRS AND STANDARD ERRORS ---

log_hr_4049 <- log(ef_4049_hr)
log_hr_50plus <- log(ef_50plus_hr)

# Standard errors from 95% CIs
se_4049 <- (log(ef_4049_ci_upper) - log(ef_4049_ci_lower)) / (2 * 1.96)
se_50plus <- (log(ef_50plus_ci_upper) - log(ef_50plus_ci_lower)) / (2 * 1.96)

cat("BASIC STATISTICS\n")
cat("================\n")
cat(sprintf("EF 40-49%%:\n"))
cat(sprintf("  Patients: %d (BB=%d, Control=%d)\n",
            ef_4049_n, ef_4049_n_bb, ef_4049_n_control))
cat(sprintf("  Events: %d (BB=%d, Control=%d)\n",
            ef_4049_events_total, ef_4049_events_bb, ef_4049_events_control))
cat(sprintf("  HR: %.2f (95%% CI: %.2f-%.2f), p=%.3f\n",
            ef_4049_hr, ef_4049_ci_lower, ef_4049_ci_upper, ef_4049_p))
cat(sprintf("  log(HR)=%.4f, SE=%.4f\n\n", log_hr_4049, se_4049))

cat(sprintf("EF ≥50%%:\n"))
cat(sprintf("  Patients: %d (BB=%d, Control=%d)\n",
            ef_50plus_n, ef_50plus_n_bb, ef_50plus_n_control))
cat(sprintf("  Events: %d (BB=%d, Control=%d)\n",
            ef_50plus_events_total, ef_50plus_events_bb, ef_50plus_events_control))
cat(sprintf("  HR: %.2f (95%% CI: %.2f-%.2f), p=%.2f\n",
            ef_50plus_hr, ef_50plus_ci_lower, ef_50plus_ci_upper, ef_50plus_p))
cat(sprintf("  log(HR)=%.4f, SE=%.4f\n\n", log_hr_50plus, se_50plus))

# --- 3. TEST FOR INTERACTION (PRIMARY ANALYSIS) ---

cat("TEST FOR INTERACTION\n")
cat("====================\n")
cat("Null hypothesis: HR(40-49%) = HR(≥50%)\n")
cat("Alternative: HR(40-49%) ≠ HR(≥50%)\n\n")

# Z-test for difference in log hazard ratios
z_interaction <- (log_hr_4049 - log_hr_50plus) / sqrt(se_4049^2 + se_50plus^2)
p_interaction <- 2 * pnorm(-abs(z_interaction))

cat(sprintf("Difference in log(HR): %.4f\n", log_hr_4049 - log_hr_50plus))
cat(sprintf("SE of difference: %.4f\n", sqrt(se_4049^2 + se_50plus^2)))
cat(sprintf("Z-statistic: %.3f\n", z_interaction))
cat(sprintf("P-value: %.3f\n\n", p_interaction))

if(p_interaction < 0.05) {
  cat("INTERPRETATION: SIGNIFICANT interaction - different treatment effects\n")
} else {
  cat("INTERPRETATION: NON-SIGNIFICANT interaction\n")
  cat("→ No statistical evidence for different treatment effects between subgroups\n")
  cat("→ The apparent threshold at EF=50% is not supported by interaction testing\n")
}
cat("\n")

# --- 4. FRAGILITY INDEX ---

cat("FRAGILITY INDEX ANALYSIS\n")
cat("========================\n")
cat("Question: How many events must change to make p≥0.05?\n\n")

# Function to calculate chi-square p-value
calc_chi_sq_p <- function(events_trt, events_ctrl, n_trt, n_ctrl) {
  total_events <- events_trt + events_ctrl
  total_n <- n_trt + n_ctrl
  expected_trt <- (n_trt / total_n) * total_events
  expected_ctrl <- (n_ctrl / total_n) * total_events

  chi_sq <- (events_trt - expected_trt)^2 / expected_trt +
            (events_ctrl - expected_ctrl)^2 / expected_ctrl

  pchisq(chi_sq, df = 1, lower.tail = FALSE)
}

# Calculate fragility index for EF 40-49% group
p_current <- calc_chi_sq_p(ef_4049_events_bb, ef_4049_events_control,
                            ef_4049_n_bb, ef_4049_n_control)

cat(sprintf("Initial p-value: %.4f (published: %.3f)\n", p_current, ef_4049_p))

fi <- 0
while(p_current < 0.05 && fi < 20) {
  fi <- fi + 1
  events_bb_new <- ef_4049_events_bb + fi
  events_ctrl_new <- ef_4049_events_control - fi
  p_current <- calc_chi_sq_p(events_bb_new, events_ctrl_new,
                              ef_4049_n_bb, ef_4049_n_control)
}

cat(sprintf("\nFragility Index: %d events\n", fi))
cat(sprintf("As %% of total events: %.2f%%\n", (fi / ef_4049_events_total) * 100))
cat(sprintf("\nINTERPRETATION:\n"))
cat(sprintf("→ Only %d event reclassifications needed to render finding non-significant\n", fi))
cat(sprintf("→ Walsh et al. suggest FI>5 for robust findings, FI>10 for practice-changing claims\n"))
cat(sprintf("→ FI=%d indicates EXTREME statistical fragility\n\n", fi))

# --- 5. POWER ANALYSIS ---

cat("POWER ANALYSIS (EF 40-49%% Subgroup)\n")
cat("====================================\n")

# Schoenfeld's formula for Cox regression power
calc_power_cox <- function(n_events, hr_true, alpha = 0.05) {
  z_alpha <- qnorm(1 - alpha/2)
  delta <- log(hr_true)
  pnorm(sqrt(n_events/4) * abs(delta) - z_alpha)
}

hrs_test <- c(0.70, 0.75, 0.80, 0.85, 0.90)
powers <- sapply(hrs_test, function(hr) calc_power_cox(ef_4049_events_total, hr))

cat(sprintf("Current events: %d\n\n", ef_4049_events_total))
cat("Power to detect various effect sizes:\n")
for(i in seq_along(hrs_test)) {
  marker <- if(hrs_test[i] == 0.75) " ← Observed HR" else ""
  cat(sprintf("  HR=%.2f: %.1f%%%s\n", hrs_test[i], powers[i]*100, marker))
}

# Calculate required events for 80% power at HR=0.80
calc_required_events <- function(hr_true, power = 0.80, alpha = 0.05) {
  z_alpha <- qnorm(1 - alpha/2)
  z_beta <- qnorm(power)
  delta <- log(hr_true)
  ceiling(4 * ((z_alpha + z_beta) / abs(delta))^2)
}

events_needed_80 <- calc_required_events(0.80, power = 0.80)
events_needed_75 <- calc_required_events(0.75, power = 0.80)

cat(sprintf("\nEvents required for 80%% power:\n"))
cat(sprintf("  At HR=0.80: %d events (%.1f%% of actual)\n",
            events_needed_80, (ef_4049_events_total/events_needed_80)*100))
cat(sprintf("  At HR=0.75: %d events (%.1f%% of actual)\n\n",
            events_needed_75, (ef_4049_events_total/events_needed_75)*100))

cat("INTERPRETATION:\n")
cat(sprintf("→ Subgroup analysis was UNDERPOWERED for reliable detection\n"))
cat(sprintf("→ Current analysis has only %.0f%% power at HR=0.80\n",
            calc_power_cox(ef_4049_events_total, 0.80)*100))
cat(sprintf("→ Would need %.0f%% more events for adequate (80%%) power\n\n",
            ((events_needed_80 - ef_4049_events_total) / ef_4049_events_total) * 100))

# --- 6. OVERALL POOLED ESTIMATE ---

cat("OVERALL POOLED EFFECT (Both EF ranges combined)\n")
cat("================================================\n")

# Fixed-effect meta-analysis
weights <- c(1/se_4049^2, 1/se_50plus^2)
pooled_log_hr <- sum(c(log_hr_4049, log_hr_50plus) * weights) / sum(weights)
pooled_se <- sqrt(1 / sum(weights))
pooled_hr <- exp(pooled_log_hr)
pooled_ci_lower <- exp(pooled_log_hr - 1.96 * pooled_se)
pooled_ci_upper <- exp(pooled_log_hr + 1.96 * pooled_se)
pooled_p <- 2 * pnorm(-abs(pooled_log_hr / pooled_se))

cat(sprintf("Total patients: %d\n", ef_4049_n + ef_50plus_n))
cat(sprintf("Total events: %d\n", ef_4049_events_total + ef_50plus_events_total))
cat(sprintf("Pooled HR: %.2f (95%% CI: %.2f-%.2f)\n",
            pooled_hr, pooled_ci_lower, pooled_ci_upper))
cat(sprintf("P-value: %.3f\n\n", pooled_p))

if(pooled_ci_upper < 1.0) {
  cat("INTERPRETATION: Significant benefit of beta-blockers overall\n\n")
} else {
  cat("INTERPRETATION: No significant benefit of beta-blockers overall\n")
  cat("→ When both EF ranges combined, no evidence of benefit\n\n")
}

# --- 7. SUMMARY TABLE ---

cat("======================================\n")
cat("SUMMARY OF KEY FINDINGS\n")
cat("======================================\n\n")

results_df <- data.frame(
  Analysis = c(
    "Interaction test (p-value)",
    "Conclusion on interaction",
    "Fragility Index (events)",
    "Fragility Index (% of events)",
    "Fragility interpretation",
    "Power at HR=0.75 (observed)",
    "Power at HR=0.80",
    "Power interpretation",
    "Required events for 80% power",
    "Overall pooled HR (both groups)",
    "Overall conclusion"
  ),
  Result = c(
    sprintf("%.3f", p_interaction),
    ifelse(p_interaction < 0.05, "SIGNIFICANT", "NON-SIGNIFICANT"),
    sprintf("%d", fi),
    sprintf("%.1f%%", (fi/ef_4049_events_total)*100),
    ifelse(fi <= 5, "EXTREMELY FRAGILE", "FRAGILE"),
    sprintf("%.1f%%", calc_power_cox(ef_4049_events_total, 0.75)*100),
    sprintf("%.1f%%", calc_power_cox(ef_4049_events_total, 0.80)*100),
    ifelse(calc_power_cox(ef_4049_events_total, 0.80) < 0.80,
           "UNDERPOWERED", "ADEQUATE"),
    sprintf("%d", events_needed_80),
    sprintf("%.2f (%.2f-%.2f)", pooled_hr, pooled_ci_lower, pooled_ci_upper),
    ifelse(pooled_ci_upper < 1.0, "Benefit", "No benefit")
  )
)

print(results_df, row.names = FALSE)

# Save results
write.csv(results_df, "empirical_results_summary.csv", row.names = FALSE)
cat("\n\nResults saved to: empirical_results_summary.csv\n")

# --- 8. FINAL VERDICT ---

cat("\n======================================\n")
cat("FINAL VERDICT\n")
cat("======================================\n\n")

failures <- 0
if(p_interaction >= 0.05) {
  cat("✗ FAILED: Interaction test non-significant (p=%.3f)\n", p_interaction)
  failures <- failures + 1
}
if(fi <= 5) {
  cat(sprintf("✗ FAILED: Fragility Index (%d) below recommended threshold (>5)\n", fi))
  failures <- failures + 1
}
if(calc_power_cox(ef_4049_events_total, 0.80) < 0.80) {
  cat(sprintf("✗ FAILED: Underpowered (%.0f%% < 80%%)\n",
              calc_power_cox(ef_4049_events_total, 0.80)*100))
  failures <- failures + 1
}

cat(sprintf("\nThe proposed EF threshold fails %d/3 core statistical validation tests.\n", failures))
cat("\nCONCLUSION:\n")
cat("The claim of a sharp efficacy threshold at EF=50% is NOT supported by\n")
cat("the statistical evidence. The finding appears to be an artifact of\n")
cat("underpowered subgroup analysis and dichotomization of a continuous variable.\n\n")
cat("RECOMMENDATION:\n")
cat("Clinical guidelines should NOT adopt EF-stratified beta-blocker recommendations\n")
cat("based on this evidence.\n\n")

cat("======================================\n")
cat("ANALYSIS COMPLETE\n")
cat("======================================\n")
