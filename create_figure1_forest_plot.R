# Figure 1: Forest Plot with Interaction Test
# Publication-quality forest plot for beta-blocker EF threshold paper

library(forestplot)
library(grid)

# Data
subgroups <- c("EF 40-49%", "EF ≥50%", "Overall Pooled")
hrs <- c(0.75, 0.97, 0.94)
ci_lower <- c(0.58, 0.87, 0.85)
ci_upper <- c(0.97, 1.07, 1.03)
n_patients <- c(1885, 17801, 19686)
n_events <- c(235, 1465, 1700)
sources <- c("Lancet 2025", "NEJM 2025", "Fixed-effect MA")

# Create text matrix for left side of plot
text_matrix <- cbind(
  c("Subgroup", subgroups),
  c("N Patients", format(n_patients, big.mark=",")),
  c("Events", n_events),
  c("Source", sources)
)

# Create data for forest plot
mean_values <- c(NA, hrs)
lower_values <- c(NA, ci_lower)
upper_values <- c(NA, ci_upper)

# Create HR text for right side
hr_text <- c(
  "HR (95% CI)",
  sprintf("%.2f (%.2f-%.2f)", hrs[1], ci_lower[1], ci_upper[1]),
  sprintf("%.2f (%.2f-%.2f)", hrs[2], ci_lower[2], ci_upper[2]),
  sprintf("%.2f (%.2f-%.2f)", hrs[3], ci_lower[3], ci_upper[3])
)

# Open PDF device
pdf("Figure1_ForestPlot.pdf", width=12, height=8)

# Create forest plot
forestplot(
  labeltext = text_matrix,
  mean = mean_values,
  lower = lower_values,
  upper = upper_values,
  new_page = TRUE,

  # Title
  title = "Beta-Blocker Effect on Death, MI, or Heart Failure by Ejection Fraction",

  # Aesthetics
  boxsize = 0.3,
  lineheight = unit(8, "mm"),
  colgap = unit(3, "mm"),

  # Reference line
  zero = 1,
  xlog = FALSE,

  # X-axis
  xticks = seq(0.5, 1.3, 0.1),
  xlab = "Hazard Ratio (95% CI)",

  # Colors
  col = fpColors(
    box = c("blue", "purple", "orange"),
    line = c("blue", "purple", "orange"),
    summary = "orange",
    zero = "black"
  ),

  # Line types
  lty.ci = c(1, 1, 1),

  # Graph position
  graphwidth = unit(60, "mm"),

  # Clip limits
  clip = c(0.5, 1.3),

  # Text formatting
  txt_gp = fpTxtGp(
    label = gpar(cex=0.9),
    ticks = gpar(cex=0.8),
    xlab = gpar(cex=1.0, fontface="bold"),
    title = gpar(cex=1.1, fontface="bold")
  ),

  # Is summary (for diamond shape)
  is.summary = c(FALSE, FALSE, FALSE, TRUE),

  # Align
  align = c("l", "c", "c", "l"),

  # Header
  hrzl_lines = list(
    "1" = gpar(lty=1, lwd=2),
    "5" = gpar(lty=1, lwd=2)
  )
)

# Add interaction test annotation
grid.text(
  "Test for Interaction: p = 0.069 (Non-significant)\nNo statistical evidence for differential effect between EF subgroups",
  x = 0.5,
  y = 0.12,
  just = "center",
  gp = gpar(
    fontsize = 11,
    fontface = "italic",
    col = "#856404"
  )
)

# Add box around interaction test
grid.rect(
  x = 0.5,
  y = 0.12,
  width = 0.6,
  height = 0.08,
  just = "center",
  gp = gpar(
    col = "#856404",
    fill = "#FFF3CD",
    lwd = 2
  )
)

dev.off()

# Also create PNG version
png("Figure1_ForestPlot.png", width=12, height=8, units="in", res=300)

forestplot(
  labeltext = text_matrix,
  mean = mean_values,
  lower = lower_values,
  upper = upper_values,
  new_page = TRUE,
  title = "Beta-Blocker Effect on Death, MI, or Heart Failure by Ejection Fraction",
  boxsize = 0.3,
  lineheight = unit(8, "mm"),
  colgap = unit(3, "mm"),
  zero = 1,
  xlog = FALSE,
  xticks = seq(0.5, 1.3, 0.1),
  xlab = "Hazard Ratio (95% CI)",
  col = fpColors(
    box = c("blue", "purple", "orange"),
    line = c("blue", "purple", "orange"),
    summary = "orange",
    zero = "black"
  ),
  lty.ci = c(1, 1, 1),
  graphwidth = unit(60, "mm"),
  clip = c(0.5, 1.3),
  txt_gp = fpTxtGp(
    label = gpar(cex=0.9),
    ticks = gpar(cex=0.8),
    xlab = gpar(cex=1.0, fontface="bold"),
    title = gpar(cex=1.1, fontface="bold")
  ),
  is.summary = c(FALSE, FALSE, FALSE, TRUE),
  align = c("l", "c", "c", "l"),
  hrzl_lines = list(
    "1" = gpar(lty=1, lwd=2),
    "5" = gpar(lty=1, lwd=2)
  )
)

grid.text(
  "Test for Interaction: p = 0.069 (Non-significant)\nNo statistical evidence for differential effect between EF subgroups",
  x = 0.5,
  y = 0.12,
  just = "center",
  gp = gpar(fontsize = 11, fontface = "italic", col = "#856404")
)

grid.rect(
  x = 0.5,
  y = 0.12,
  width = 0.6,
  height = 0.08,
  just = "center",
  gp = gpar(col = "#856404", fill = "#FFF3CD", lwd = 2)
)

dev.off()

cat("\n✓ Figure 1 created successfully!\n")
cat("  - Figure1_ForestPlot.pdf\n")
cat("  - Figure1_ForestPlot.png\n\n")
cat("Key findings displayed:\n")
cat("  • EF 40-49%: HR 0.75 (0.58-0.97)\n")
cat("  • EF ≥50%: HR 0.97 (0.87-1.07)\n")
cat("  • Overall: HR 0.94 (0.85-1.03)\n")
cat("  • Interaction test: p = 0.069 (NON-SIGNIFICANT)\n")
