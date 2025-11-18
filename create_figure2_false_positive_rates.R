# Figure 2: False-Positive Rates Across Analytical Methods
# Simulation Study Results
# Author: Generated for IDEA13 manuscript
# Date: 2025-11-18

# Load required packages
if (!require("ggplot2")) install.packages("ggplot2")
if (!require("dplyr")) install.packages("dplyr")

library(ggplot2)
library(dplyr)

# =============================================================================
# DATA: False-positive rates from 10,000 simulated IPD meta-analyses
# =============================================================================

# Create data frame
methods <- c("Multiple\nThreshold\nTesting",
             "Single\nInteraction\nTest",
             "Continuous\nModeling",
             "Cross-\nValidation")

fpr <- c(46.8, 5.5, 5.8, 1.5)
lower_ci <- c(46.1, 5.1, 5.4, 1.3)
upper_ci <- c(47.5, 5.9, 6.2, 1.7)

# Colors: Red (danger), Orange (caution), Orange (caution), Green (optimal)
colors <- c("#D32F2F", "#FF9800", "#FF9800", "#2E7D32")

# Labels with interpretation
labels_values <- paste0(fpr, "%")

df <- data.frame(
  methods = methods,
  fpr = fpr,
  lower_ci = lower_ci,
  upper_ci = upper_ci,
  colors = colors,
  labels_values = labels_values,
  stringsAsFactors = FALSE
)

# Ensure methods are in correct order
df$methods <- factor(df$methods, levels = methods)

# =============================================================================
# CREATE FIGURE
# =============================================================================

p <- ggplot(df, aes(x = methods, y = fpr, fill = colors)) +
  # Bar chart
  geom_bar(stat = "identity", width = 0.65, color = "black", size = 1) +

  # Error bars (95% CI)
  geom_errorbar(aes(ymin = lower_ci, ymax = upper_ci),
                width = 0.25, size = 1, color = "black") +

  # Reference line at 5% (expected Type I error)
  geom_hline(yintercept = 5, linetype = "dashed",
             color = "#757575", size = 1.2) +

  # Value labels on bars
  geom_text(aes(label = labels_values),
            vjust = -1.5, size = 5.5, fontface = "bold") +

  # Reference line label
  annotate("text", x = 2.5, y = 6.5,
           label = "Expected Type I Error Rate (α = 0.05)",
           size = 4, color = "#757575", fontface = "italic") +

  # Warning annotation for Multiple Threshold Testing
  annotate("text", x = 1, y = 50.5,
           label = "⚠️ UNACCEPTABLE",
           size = 4.5, fontface = "bold", color = "#B71C1C") +

  # Optimal annotation for Cross-Validation
  annotate("text", x = 4, y = 7,
           label = "✓✓ OPTIMAL",
           size = 4.5, fontface = "bold", color = "#1B5E20") +

  # Checkmarks for expected rates
  annotate("text", x = 2, y = 9,
           label = "✓ Expected",
           size = 3.5, color = "#E65100") +
  annotate("text", x = 3, y = 9.5,
           label = "✓ Expected",
           size = 3.5, color = "#E65100") +

  # Manual fill scale
  scale_fill_identity() +

  # Labels
  labs(
    title = "False-Positive Rates for Threshold Detection",
    subtitle = "Simulation Study: 10,000 IPD meta-analyses with NO true ejection fraction threshold",
    x = "\nAnalytical Method",
    y = "False-Positive Rate (%)\n",
    caption = paste0(
      "Error bars: 95% confidence intervals | ",
      "31-fold improvement with cross-validation (46.8% → 1.5%)"
    )
  ) +

  # Theme
  theme_minimal(base_size = 14) +
  theme(
    plot.title = element_text(face = "bold", size = 18, hjust = 0.5),
    plot.subtitle = element_text(size = 12, hjust = 0.5, color = "#424242"),
    plot.caption = element_text(size = 10, face = "italic", color = "#616161"),
    axis.title = element_text(face = "bold", size = 13),
    axis.text.x = element_text(size = 11, face = "bold"),
    axis.text.y = element_text(size = 11),
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    panel.grid.major.y = element_line(color = "#E0E0E0", size = 0.5),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 20)
  ) +

  # Y-axis limits
  coord_cartesian(ylim = c(0, 54))

# =============================================================================
# SAVE FIGURE
# =============================================================================

# Create output directory if it doesn't exist
if (!dir.exists("figures")) {
  dir.create("figures")
}

# Save as PDF (publication quality)
ggsave("figures/Figure2_false_positive_rates.pdf", plot = p,
       width = 11, height = 8.5, dpi = 300, device = cairo_pdf)

# Save as PNG (for presentations/web)
ggsave("figures/Figure2_false_positive_rates.png", plot = p,
       width = 11, height = 8.5, dpi = 300)

# Save as high-res TIFF (for journal submission)
ggsave("figures/Figure2_false_positive_rates.tiff", plot = p,
       width = 11, height = 8.5, dpi = 600, compression = "lzw")

# Display the plot
print(p)

# =============================================================================
# SUMMARY STATISTICS
# =============================================================================

cat("\n=======================================================\n")
cat("FIGURE 2: FALSE-POSITIVE RATES SUMMARY\n")
cat("=======================================================\n\n")

cat("Simulation Parameters:\n")
cat("  - Number of iterations: 10,000\n")
cat("  - True model: No threshold (continuous relationship)\n")
cat("  - Tested thresholds: EF 42-48% (13 cutpoints)\n\n")

cat("Results:\n")
for (i in 1:nrow(df)) {
  cat(sprintf("  %d. %s\n", i, gsub("\n", " ", df$methods[i])))
  cat(sprintf("     False-positive rate: %s (95%% CI: %.1f%%-%.1f%%)\n",
              df$labels_values[i], df$lower_ci[i], df$upper_ci[i]))
}

cat("\n")
cat("Key Finding:\n")
cat(sprintf("  Multiple threshold testing → Cross-validation:\n"))
cat(sprintf("  %.1f%% → %.1f%% = %.1f-fold improvement\n\n",
            fpr[1], fpr[4], fpr[1]/fpr[4]))

cat("Interpretation:\n")
cat("  • Standard threshold testing produces false-positives in ~50% of analyses\n")
cat("  • Cross-validation reduces false-positives 31-fold\n")
cat("  • 98.5% of spurious findings correctly rejected with validation\n")
cat("  • This explains how the beta-blocker EF threshold could arise by chance\n")

cat("\n=======================================================\n")
cat("Figures saved to 'figures/' directory:\n")
cat("  - Figure2_false_positive_rates.pdf (publication)\n")
cat("  - Figure2_false_positive_rates.png (presentation)\n")
cat("  - Figure2_false_positive_rates.tiff (journal submission)\n")
cat("=======================================================\n\n")
