#!/usr/bin/env python3
"""
Create Figures 2 and 3 with ACTUAL simulation results
Replaces schematic/illustrative data with empirical results
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import pickle

# Set publication-quality defaults
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 0.8

# Load actual simulation results
with open('simulation_results.pkl', 'rb') as f:
    results = pickle.load(f)

print("="*70)
print("CREATING FIGURES WITH ACTUAL SIMULATION DATA")
print("="*70)
print()

# Extract results for Model 1 (linear - primary analysis)
model1 = results['linear']
fpr = model1['fpr']
ci_lower = model1['ci_lower']
ci_upper = model1['ci_upper']
discovered_thresholds = model1['discovered_thresholds']
p_values = model1['p_values']

print("Actual simulation results (Model 1: Linear Decline):")
print(f"  Multiple Threshold Testing: {fpr[0]:.1f}% ({ci_lower[0]:.1f}-{ci_upper[0]:.1f}%)")
print(f"  Single Interaction Test:    {fpr[1]:.1f}% ({ci_lower[1]:.1f}-{ci_upper[1]:.1f}%)")
print(f"  Continuous Modeling:         {fpr[2]:.1f}% ({ci_lower[2]:.1f}-{ci_upper[2]:.1f}%)")
print(f"  Cross-Validation:            {fpr[3]:.1f}% ({ci_lower[3]:.1f}-{ci_upper[3]:.1f}%)")
print()
print(f"  Fold reduction: {fpr[0]/fpr[3]:.1f}x")
print()

# ============================================================================
# FIGURE 2: FALSE-POSITIVE RATES (WITH ACTUAL DATA)
# ============================================================================

def create_figure2_actual():
    """Create bar chart of false-positive rates with ACTUAL data"""

    fig, ax = plt.subplots(figsize=(10, 6))

    # Actual data from simulations
    methods = ['Multiple\nThreshold\nTesting', 'Single\nInteraction\nTest',
               'Continuous\nModeling', 'Cross-\nValidation']

    # Colors - red for high FPR, green for low
    colors = ['#E63946', '#F4A261', '#F4A261', '#2A9D8F']

    x_pos = np.arange(len(methods))

    # Create bars
    bars = ax.bar(x_pos, fpr, color=colors, alpha=0.8, edgecolor='black', linewidth=1.2)

    # Add error bars (confidence intervals)
    errors = [[fpr[i] - ci_lower[i] for i in range(len(fpr))],
              [ci_upper[i] - fpr[i] for i in range(len(fpr))]]
    ax.errorbar(x_pos, fpr, yerr=errors, fmt='none', ecolor='black', capsize=5, capthick=2, linewidth=1.5)

    # Add value labels on bars
    for i, (x, y) in enumerate(zip(x_pos, fpr)):
        ax.text(x, y + 1, f'{y:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)

    # Add CI labels below bars (not on bars - fixes readability issue)
    for i, x in enumerate(x_pos):
        ax.text(x, -2.5, f'({ci_lower[i]:.1f}-{ci_upper[i]:.1f}%)',
                ha='center', va='top', fontsize=8, color='black')

    # Reference line at 5% (nominal Type I error)
    ax.axhline(y=5.0, color='gray', linestyle='--', linewidth=2, alpha=0.7, label='Expected Type I Error (5%)')
    ax.text(3.5, 5.3, 'Expected 5%', ha='right', va='bottom', fontsize=9, color='gray', style='italic')

    # Highlight the fold reduction
    fold_reduction = fpr[0] / fpr[3]
    ax.annotate('', xy=(3, fpr[3]), xytext=(0, fpr[0]),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(1.5, (fpr[0] + fpr[3])/2, f'{fold_reduction:.1f}-fold\nreduction',
            ha='center', va='center', fontsize=10,
            fontweight='bold', color='red',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='red', linewidth=2))

    # Formatting
    ax.set_ylabel('False-Positive Rate (%)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Analytical Method', fontsize=12, fontweight='bold')
    ax.set_title('False-Positive Rates for Threshold Detection When No True Threshold Exists\n(N=10,000 Actual Simulations per Method)',
                 fontsize=12, fontweight='bold', pad=15)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(methods, fontsize=10)
    ax.set_ylim(-3, max(fpr) + 5)

    # Grid
    ax.yaxis.grid(True, linestyle=':', alpha=0.3)
    ax.set_axisbelow(True)

    # Legend
    ax.legend(loc='upper right', fontsize=9)

    plt.tight_layout()
    plt.savefig('Figure2_FalsePositiveRates_ACTUAL.png', dpi=300, bbox_inches='tight')
    plt.savefig('Figure2_FalsePositiveRates_ACTUAL.pdf', dpi=300, bbox_inches='tight')
    print("✓ Figure 2 (ACTUAL) created: Figure2_FalsePositiveRates_ACTUAL.png and .pdf")
    plt.close()


# ============================================================================
# FIGURE 3: DISTRIBUTION OF DISCOVERED THRESHOLDS (WITH ACTUAL DATA)
# ============================================================================

def create_figure3_actual():
    """Create distribution of discovered thresholds with ACTUAL data"""

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Panel A: Distribution of "discovered" thresholds (ACTUAL DATA)
    thresholds = np.arange(42, 48.5, 0.5)

    # Count how many times each threshold was discovered
    threshold_counts = {}
    for t in thresholds:
        threshold_counts[t] = discovered_thresholds.count(t)

    counts = [threshold_counts[t] for t in thresholds]

    ax1.bar(thresholds, counts, width=0.4, color='#E63946', alpha=0.7, edgecolor='black', linewidth=1)
    mean_count = np.mean(counts)
    ax1.axhline(y=mean_count, color='gray', linestyle='--', linewidth=2, label=f'Mean ({mean_count:.0f})')
    ax1.set_xlabel('EF Threshold (%)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Number of Simulations Finding\n"Significant" Result at This Threshold',
                   fontsize=10, fontweight='bold')
    ax1.set_title('Panel A: Distribution of "Discovered" Thresholds\n(Among 4,070 simulations with false positives)',
                  fontsize=11, fontweight='bold')
    ax1.set_xticks(thresholds)
    ax1.set_ylim(0, max(counts) * 1.2)
    ax1.legend(fontsize=9)
    ax1.grid(axis='y', linestyle=':', alpha=0.3)

    # Add annotation
    # Check if distribution is relatively uniform
    cv = np.std(counts) / np.mean(counts)  # Coefficient of variation
    if cv < 0.3:
        interpretation = 'Approximately uniform:\nNo clustering at any value\n→ Random artifacts, not\nbiological signal'
    else:
        interpretation = f'Non-uniform distribution\n(CV={cv:.2f})\n→ Some clustering may\nreflect simulation noise'

    ax1.text(45, max(counts) * 1.05, interpretation,
             ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5',
             facecolor='#FFF3CD', edgecolor='#856404', linewidth=1.5))

    # Panel B: P-value distributions (ACTUAL DATA)
    bins = np.linspace(0, 1, 21)

    # Method 1 p-values (multiple threshold testing)
    p_method1 = np.array(p_values['method1'])
    # Cross-validation doesn't have continuous p-values, so use Method 2 (single interaction) as comparison
    p_method2 = np.array(p_values['method2'])

    ax2.hist(p_method1, bins=bins, alpha=0.6, color='#E63946',
             label='Multiple Threshold Testing', edgecolor='black')
    ax2.hist(p_method2, bins=bins, alpha=0.6, color='#2A9D8F',
             label='Single Interaction Test', edgecolor='black')

    expected_count = len(p_method1) / len(bins)
    ax2.axhline(y=expected_count, color='gray', linestyle='--', linewidth=2,
                label=f'Expected if uniform ({expected_count:.0f})')

    # Highlight p<0.05 region
    ax2.axvspan(0, 0.05, alpha=0.2, color='red', label='p < 0.05')

    ax2.set_xlabel('P-value', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Frequency', fontsize=11, fontweight='bold')
    ax2.set_title('Panel B: P-value Distributions\n(N=10,000 actual simulations, true null hypothesis)',
                  fontsize=11, fontweight='bold')
    ax2.legend(fontsize=8, loc='upper right')
    ax2.set_xlim(0, 1)
    ax2.grid(axis='y', linestyle=':', alpha=0.3)

    # Add annotations
    pct_below_05_method1 = 100 * np.sum(p_method1 < 0.05) / len(p_method1)
    pct_below_05_method2 = 100 * np.sum(p_method2 < 0.05) / len(p_method2)

    ax2.text(0.25, max(ax2.get_ylim()) * 0.85,
             f'Multiple threshold:\n{pct_below_05_method1:.1f}% p<0.05',
             ha='center', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFE5E5', edgecolor='red', linewidth=1.5))
    ax2.text(0.75, max(ax2.get_ylim()) * 0.85,
             f'Single interaction:\n{pct_below_05_method2:.1f}% p<0.05',
             ha='center', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#E5FFF5', edgecolor='green', linewidth=1.5))

    plt.tight_layout()
    plt.savefig('Figure3_ThresholdDistributions_ACTUAL.png', dpi=300, bbox_inches='tight')
    plt.savefig('Figure3_ThresholdDistributions_ACTUAL.pdf', dpi=300, bbox_inches='tight')
    print("✓ Figure 3 (ACTUAL) created: Figure3_ThresholdDistributions_ACTUAL.png and .pdf")
    plt.close()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == '__main__':

    create_figure2_actual()
    create_figure3_actual()

    print()
    print("="*70)
    print("ACTUAL DATA FIGURES CREATED SUCCESSFULLY")
    print("="*70)
    print()
    print("Files generated:")
    print("  • Figure2_FalsePositiveRates_ACTUAL.png / .pdf")
    print("  • Figure3_ThresholdDistributions_ACTUAL.png / .pdf")
    print()
    print("These replace the schematic figures with empirical results")
    print("from 10,000 actual simulations")
    print()
