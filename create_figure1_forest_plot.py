#!/usr/bin/env python3
"""
Figure 1: Forest Plot showing Beta-Blocker Effects by EF Range
with Test for Interaction
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Data from verified sources
data = {
    'subgroup': ['EF 40-49%', 'EF ≥50%', 'Overall Pooled'],
    'hr': [0.75, 0.97, 0.94],
    'ci_lower': [0.58, 0.87, 0.85],
    'ci_upper': [0.97, 1.07, 1.03],
    'n_patients': [1885, 17801, 19686],
    'n_events': [235, 1465, 1700],
    'events_bb': [106, 717, 823],
    'events_ctrl': [129, 748, 877],
    'source': ['Lancet 2025', 'NEJM 2025', 'Fixed-effect MA']
}

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Y positions (reversed so EF 40-49% is at top)
y_positions = [2, 1, 0]
colors = ['#2E86AB', '#A23B72', '#F18F01']

# Plot confidence intervals and point estimates
for i, y_pos in enumerate(y_positions):
    # Confidence interval line
    ax.plot([data['ci_lower'][i], data['ci_upper'][i]],
            [y_pos, y_pos],
            'o-',
            linewidth=2.5 if i == 2 else 2,
            markersize=10 if i == 2 else 8,
            color=colors[i],
            solid_capstyle='round',
            zorder=3)

    # Diamond for pooled estimate
    if i == 2:
        diamond_width = (data['ci_upper'][i] - data['ci_lower'][i]) / 2
        diamond_height = 0.15
        diamond = mpatches.Polygon([
            [data['hr'][i] - diamond_width, y_pos],
            [data['hr'][i], y_pos + diamond_height],
            [data['hr'][i] + diamond_width, y_pos],
            [data['hr'][i], y_pos - diamond_height]
        ], closed=True, facecolor=colors[i], edgecolor='black', linewidth=1.5, zorder=4)
        ax.add_patch(diamond)
    else:
        # Square markers for subgroups
        ax.plot(data['hr'][i], y_pos, 's',
                markersize=12,
                color=colors[i],
                markeredgecolor='black',
                markeredgewidth=1,
                zorder=4)

# Vertical line at HR = 1.0 (no effect)
ax.axvline(x=1.0, color='black', linestyle='--', linewidth=1.5, alpha=0.7, zorder=1)

# Add text annotations on left side
for i, y_pos in enumerate(y_positions):
    # Subgroup name
    ax.text(-0.05, y_pos, data['subgroup'][i],
            fontsize=12, fontweight='bold' if i == 2 else 'normal',
            ha='right', va='center')

    # Sample size and events
    ax.text(-0.05, y_pos - 0.25,
            f"N={data['n_patients'][i]:,}, Events={data['n_events'][i]:,}",
            fontsize=9, ha='right', va='center', style='italic', color='gray')

    # Source
    ax.text(-0.05, y_pos - 0.45,
            data['source'][i],
            fontsize=8, ha='right', va='center', color='#555555')

# Add text annotations on right side (HR and CI)
for i, y_pos in enumerate(y_positions):
    ax.text(1.25, y_pos,
            f"{data['hr'][i]:.2f} ({data['ci_lower'][i]:.2f}-{data['ci_upper'][i]:.2f})",
            fontsize=11, fontweight='bold' if i == 2 else 'normal',
            ha='left', va='center')

# Add headers
ax.text(-0.05, 3.0, 'Subgroup', fontsize=13, fontweight='bold', ha='right', va='center')
ax.text(0.65, 3.0, 'Favors\nBeta-Blocker', fontsize=10, ha='center', va='center', color='#2E5090')
ax.text(1.08, 3.0, 'Favors\nControl', fontsize=10, ha='center', va='center', color='#8B0000')
ax.text(1.25, 3.0, 'HR (95% CI)', fontsize=13, fontweight='bold', ha='left', va='center')

# Add interaction test result in box
interaction_text = "Test for Interaction: p = 0.069"
interpretation_text = "Non-significant (p ≥ 0.05)\nNo evidence for differential effect"

# Box for interaction test
box_props = dict(boxstyle='round,pad=0.6', facecolor='#FFF3CD',
                 edgecolor='#856404', linewidth=2)
ax.text(0.67, -0.8, interaction_text,
        fontsize=13, fontweight='bold',
        bbox=box_props, ha='center', va='top',
        color='#856404')

ax.text(0.67, -1.25, interpretation_text,
        fontsize=10, ha='center', va='top',
        style='italic', color='#856404')

# Styling
ax.set_xlim(0.5, 1.3)
ax.set_ylim(-1.6, 3.3)
ax.set_xlabel('Hazard Ratio (95% Confidence Interval)', fontsize=13, fontweight='bold')
ax.set_title('Beta-Blocker Effect on Death, MI, or Heart Failure by Ejection Fraction\n' +
             'Post-Myocardial Infarction Patients',
             fontsize=14, fontweight='bold', pad=20)

# Remove y-axis
ax.set_yticks([])
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# X-axis ticks
ax.set_xticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3])
ax.set_xticklabels(['0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3'])
ax.tick_params(axis='x', labelsize=11)

# Add grid
ax.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5, zorder=0)

# Add note at bottom
note = ("Note: Interaction test evaluates whether the hazard ratios differ significantly between EF subgroups.\n" +
        "p ≥ 0.05 indicates no statistical evidence for different treatment effects.")
ax.text(0.67, -1.55, note,
        fontsize=8, ha='center', va='top', style='italic',
        color='#666666', wrap=True)

plt.tight_layout()

# Save figure
plt.savefig('Figure1_ForestPlot.pdf', dpi=300, bbox_inches='tight')
plt.savefig('Figure1_ForestPlot.png', dpi=300, bbox_inches='tight')

print("✓ Figure 1 created successfully!")
print("  - Figure1_ForestPlot.pdf")
print("  - Figure1_ForestPlot.png")
print("\nKey findings displayed:")
print("  • EF 40-49%: HR 0.75 (0.58-0.97)")
print("  • EF ≥50%: HR 0.97 (0.87-1.07)")
print("  • Overall: HR 0.94 (0.85-1.03)")
print("  • Interaction test: p = 0.069 (NON-SIGNIFICANT)")
