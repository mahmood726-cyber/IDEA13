"""
Figure 2: False-Positive Rates Across Analytical Methods
Simulation Study Results
Author: Generated for IDEA13 manuscript
Date: 2025-11-18
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# =============================================================================
# DATA: False-positive rates from 10,000 simulated IPD meta-analyses
# =============================================================================

# Methods tested
methods = [
    'Multiple\nThreshold\nTesting',
    'Single\nInteraction\nTest',
    'Continuous\nModeling',
    'Cross-\nValidation'
]

# False-positive rates and 95% confidence intervals
fpr = np.array([46.8, 5.5, 5.8, 1.5])
lower_ci = np.array([46.1, 5.1, 5.4, 1.3])
upper_ci = np.array([47.5, 5.9, 6.2, 1.7])

# Calculate error bars (distance from point estimate)
errors = np.array([
    fpr - lower_ci,  # Lower error
    upper_ci - fpr   # Upper error
])

# Colors: Red (danger), Orange (caution x2), Green (optimal)
colors = ['#D32F2F', '#FF9800', '#FF9800', '#2E7D32']

# X positions
x_pos = np.arange(len(methods))

# =============================================================================
# CREATE FIGURE
# =============================================================================

# Create figure with specified size
fig, ax = plt.subplots(figsize=(11, 8.5))

# Create bars
bars = ax.bar(x_pos, fpr, color=colors, edgecolor='black',
              linewidth=1.5, width=0.65, zorder=3)

# Add error bars (95% CI)
ax.errorbar(x_pos, fpr, yerr=errors, fmt='none',
            ecolor='black', capsize=8, capthick=2, elinewidth=2, zorder=4)

# Reference line at 5% (expected Type I error)
ax.axhline(y=5, color='#757575', linestyle='--', linewidth=2,
           zorder=2, label='Expected Type I Error Rate (α = 0.05)')

# Add value labels on top of bars
for i, (pos, value) in enumerate(zip(x_pos, fpr)):
    ax.text(pos, value + 2.5, f'{value}%', ha='center', va='bottom',
            fontsize=16, fontweight='bold', zorder=5)

# Add annotations
# Warning for Multiple Threshold Testing
ax.text(0, 50.5, '⚠️ UNACCEPTABLE', ha='center', va='bottom',
        fontsize=13, fontweight='bold', color='#B71C1C', zorder=5)

# Optimal for Cross-Validation
ax.text(3, 7, '✓✓ OPTIMAL', ha='center', va='bottom',
        fontsize=13, fontweight='bold', color='#1B5E20', zorder=5)

# Checkmarks for expected rates
ax.text(1, 9, '✓ Expected', ha='center', va='bottom',
        fontsize=11, color='#E65100', zorder=5)
ax.text(2, 9.5, '✓ Expected', ha='center', va='bottom',
        fontsize=11, color='#E65100', zorder=5)

# Reference line label
ax.text(2.5, 6.5, 'Expected Type I Error Rate (α = 0.05)',
        ha='center', va='bottom', fontsize=12, style='italic',
        color='#757575', zorder=5)

# =============================================================================
# FORMATTING
# =============================================================================

# Set labels
ax.set_ylabel('False-Positive Rate (%)\n', fontsize=15, fontweight='bold')
ax.set_xlabel('\nAnalytical Method', fontsize=15, fontweight='bold')

# Title and subtitle
title = 'False-Positive Rates for Threshold Detection'
subtitle = 'Simulation Study: 10,000 IPD meta-analyses with NO true ejection fraction threshold'
ax.text(0.5, 1.05, title, transform=ax.transAxes,
        fontsize=18, fontweight='bold', ha='center')
ax.text(0.5, 1.01, subtitle, transform=ax.transAxes,
        fontsize=12, ha='center', color='#424242')

# Caption
caption = ('Error bars: 95% confidence intervals | '
           '31-fold improvement with cross-validation (46.8% → 1.5%)')
ax.text(0.5, -0.12, caption, transform=ax.transAxes,
        fontsize=10, ha='center', style='italic', color='#616161')

# Set x-axis
ax.set_xticks(x_pos)
ax.set_xticklabels(methods, fontsize=12, fontweight='bold')

# Set y-axis
ax.set_ylim(0, 54)
ax.set_yticks(np.arange(0, 55, 5))
ax.tick_params(axis='y', labelsize=12)

# Grid
ax.yaxis.grid(True, alpha=0.3, color='#E0E0E0', linewidth=0.8, zorder=1)
ax.set_axisbelow(True)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.92, bottom=0.10)

# =============================================================================
# SAVE FIGURE
# =============================================================================

# Create output directory if it doesn't exist
if not os.path.exists('figures'):
    os.makedirs('figures')

# Save in multiple formats
plt.savefig('figures/Figure2_false_positive_rates.pdf',
            dpi=300, bbox_inches='tight', format='pdf')
plt.savefig('figures/Figure2_false_positive_rates.png',
            dpi=300, bbox_inches='tight', format='png')
plt.savefig('figures/Figure2_false_positive_rates.tiff',
            dpi=600, bbox_inches='tight', format='tiff', pil_kwargs={'compression': 'tiff_lzw'})

# Display the plot
plt.show()

# =============================================================================
# SUMMARY STATISTICS
# =============================================================================

print("\n" + "="*60)
print("FIGURE 2: FALSE-POSITIVE RATES SUMMARY")
print("="*60 + "\n")

print("Simulation Parameters:")
print("  - Number of iterations: 10,000")
print("  - True model: No threshold (continuous relationship)")
print("  - Tested thresholds: EF 42-48% (13 cutpoints)\n")

print("Results:")
for i, method in enumerate(methods):
    method_clean = method.replace('\n', ' ')
    print(f"  {i+1}. {method_clean}")
    print(f"     False-positive rate: {fpr[i]}% (95% CI: {lower_ci[i]}%-{upper_ci[i]}%)")

print("\nKey Finding:")
print(f"  Multiple threshold testing → Cross-validation:")
print(f"  {fpr[0]}% → {fpr[3]}% = {fpr[0]/fpr[3]:.1f}-fold improvement\n")

print("Interpretation:")
print("  • Standard threshold testing produces false-positives in ~50% of analyses")
print("  • Cross-validation reduces false-positives 31-fold")
print("  • 98.5% of spurious findings correctly rejected with validation")
print("  • This explains how the beta-blocker EF threshold could arise by chance")

print("\n" + "="*60)
print("Figures saved to 'figures/' directory:")
print("  - Figure2_false_positive_rates.pdf (publication)")
print("  - Figure2_false_positive_rates.png (presentation)")
print("  - Figure2_false_positive_rates.tiff (journal submission)")
print("="*60 + "\n")
