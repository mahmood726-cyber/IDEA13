#!/usr/bin/env python3
"""
Create Figure 4 (renamed from Figure 5): Validation Framework Flowchart
FIXED VERSION: Uses standard Unicode symbols instead of emoji for better font compatibility
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Set publication-quality defaults
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 0.8

def create_figure4():
    """Create validation framework flowchart with standard Unicode symbols"""

    fig, ax = plt.subplots(figsize=(12, 16))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 20)
    ax.axis('off')

    # Helper function to create boxes
    def add_box(x, y, width, height, text, facecolor='lightblue', edgecolor='black',
                linewidth=2, fontsize=10, fontweight='normal', align='center'):
        box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1",
                            edgecolor=edgecolor, facecolor=facecolor, linewidth=linewidth)
        ax.add_patch(box)

        # Handle multi-line text
        if align == 'center':
            ax.text(x + width/2, y + height/2, text, ha='center', va='center',
                   fontsize=fontsize, fontweight=fontweight, wrap=True)
        else:
            ax.text(x + 0.2, y + height/2, text, ha='left', va='center',
                   fontsize=fontsize, fontweight=fontweight, wrap=True)

    # Helper function for arrows
    def add_arrow(x1, y1, x2, y2, style='->', color='black', linewidth=2):
        arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                               color=color, linewidth=linewidth, mutation_scale=20)
        ax.add_patch(arrow)

    # Title box
    add_box(0.5, 18.5, 9, 1, 'SUBGROUP CLAIM IDENTIFIED\n"Treatment X works in Subgroup A but not B"',
            facecolor='#E8F4F8', edgecolor='#2E86AB', fontsize=11, fontweight='bold')

    # Level 1 header
    add_box(0.5, 16.8, 9, 0.8, 'LEVEL 1: MINIMUM REQUIREMENTS\n(All must pass to proceed)',
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=10, fontweight='bold')
    add_arrow(5, 18.5, 5, 17.6)

    # Level 1 tests (FIXED: replaced emoji with standard symbols)
    add_box(0.7, 14.5, 2.5, 2, '1. PRE-SPECIFICATION\n\nWas subgroup defined\nin protocol before\nseeing data?\n\n? Unknown for\nBeta-blocker EF',
            facecolor='#FFF9E5', edgecolor='#F4A261', fontsize=8)
    add_box(3.7, 14.5, 2.5, 2, '2. BIOLOGICAL\nPLAUSIBILITY\n\nMechanistic rationale\nfor differential effect?\n\n\u2717 No clear\nmechanism for\nsharp threshold',
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=8)
    add_box(6.7, 14.5, 2.5, 2, '3. INTERACTION\nTEST SIGNIFICANT\n\np < 0.05 for\ntreatment \u00d7 subgroup?\n\n\u2717 p = 0.069\nNON-SIGNIFICANT',
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=8)

    # Arrows from Level 1 header to tests
    add_arrow(2, 16.8, 2, 16.5)
    add_arrow(5, 16.8, 5, 16.5)
    add_arrow(8, 16.8, 8, 16.5)

    # STOP box
    add_box(3.5, 13, 3, 0.8, 'STOP if p \u2265 0.05: INSUFFICIENT EVIDENCE',
            facecolor='#E63946', edgecolor='darkred', fontsize=9, fontweight='bold')
    add_arrow(8, 14.5, 6.5, 13.5)

    # Level 2 header
    add_box(0.5, 11.5, 9, 0.8, 'LEVEL 2: ROBUSTNESS CHECKS\n(Assess reliability of finding)',
            facecolor='#FFF9E5', edgecolor='#F4A261', fontsize=10, fontweight='bold')
    add_arrow(5, 13, 5, 12.3)

    # Level 2 tests (FIXED: replaced emoji with standard symbols)
    add_box(0.7, 8.8, 2.5, 2.3, '4. ADEQUATE POWER\n\n\u226580% power to detect\nmeaningful effect\nin subgroup?\n\n\u2717 Beta-blocker:\n40% power',
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=8)
    add_box(3.7, 8.8, 2.5, 2.3, '5. FRAGILITY INDEX\n\nFI > 5 for robust\nFI > 10 for\npractice-changing\n\n\u2717 Beta-blocker:\nFI = 3',
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=8)
    add_box(6.7, 8.8, 2.5, 2.3, '6. OPTIMAL\nINFORMATION SIZE\n\nCumulative data\nreaches required\ninformation size?\n\n\u2717 Below RIS',
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=8)

    # Arrows from Level 2 header to tests
    add_arrow(2, 11.5, 2, 11.1)
    add_arrow(5, 11.5, 5, 11.1)
    add_arrow(8, 11.5, 8, 11.1)

    # Warning box (FIXED: replaced warning emoji with !)
    add_box(3, 7.3, 4, 0.8, '! ANY FAILED? \u2192 Interpret with CAUTION',
            facecolor='#FFF3CD', edgecolor='#856404', fontsize=9, fontweight='bold')
    add_arrow(5, 8.8, 5, 8.1)

    # Level 3 header
    add_box(0.5, 5.8, 9, 0.8, 'LEVEL 3: VALIDATION (GOLD STANDARD)\n(Required for practice-changing claims)',
            facecolor='#E5FFF5', edgecolor='#2A9D8F', fontsize=10, fontweight='bold')
    add_arrow(5, 7.3, 5, 6.6)

    # Level 3 tests (FIXED: replaced emoji with standard symbols)
    add_box(1.2, 3.3, 3.5, 2.2, '7. CROSS-VALIDATION\n\nEffect holds in\nheld-out data?\n\n\u2022 Leave-one-trial-out\n\u2022 Split sample\n\n\u2717 Beta-blocker:\nNot performed',
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=8)
    add_box(5.3, 3.3, 3.5, 2.2, '8. INDEPENDENT\nREPLICATION\n\nFinding confirms in\nseparate dataset?\n\n\u2022 External data\n\u2022 Prospective\n  validation\n\n\u2717 Not performed',
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=8)

    # Arrows from Level 3 header to tests
    add_arrow(3, 5.8, 3, 5.5)
    add_arrow(7, 5.8, 7, 5.5)

    # Final decision header
    add_box(0.5, 1.8, 9, 0.5, 'FINAL DECISION',
            facecolor='#E8F4F8', edgecolor='#2E86AB', fontsize=11, fontweight='bold')
    add_arrow(5, 3.3, 5, 2.3)

    # Final decision boxes (FIXED: replaced emoji with standard symbols)
    add_box(0.7, 0.2, 4, 1.4, '\u2713 VALIDATED\n\n\u2022 All Level 1 passed\n\u2022 Most Level 2 passed\n\u2022 \u22651 Level 3 passed\n\n\u2192 May inform guidelines',
            facecolor='#E5FFF5', edgecolor='#2A9D8F', fontsize=8, linewidth=3)
    add_box(5.3, 0.2, 4, 1.4, '\u2717 NOT VALIDATED\n\n\u2022 Failed \u22651 Level 1 test OR\n\u2022 Failed Level 2 tests AND\n\u2022 No Level 3 validation\n\n\u2192 DO NOT use for guidelines',
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=8, linewidth=3)

    # Arrows from final decision header
    add_arrow(3.5, 1.8, 2.7, 1.6)
    add_arrow(6.5, 1.8, 7.3, 1.6)

    # Add scorecard in corner (FIXED: replaced emoji with standard symbols)
    scorecard_text = 'Beta-Blocker EF Threshold:\n\n' \
                    'Level 1: 0/3 passed \u2717\n' \
                    'Level 2: 0/3 passed \u2717\n' \
                    'Level 3: 0/2 performed \u2717\n\n' \
                    'TOTAL: 0/8 \u2717\n\n' \
                    'VERDICT: NOT VALIDATED'

    add_box(0.3, 11.8, 2.2, 2.5, scorecard_text,
            facecolor='#FFE5E5', edgecolor='#E63946', fontsize=7,
            fontweight='bold', align='left', linewidth=2)

    plt.tight_layout()
    plt.savefig('Figure4_ValidationFramework.png', dpi=300, bbox_inches='tight')
    plt.savefig('Figure4_ValidationFramework.pdf', dpi=300, bbox_inches='tight')
    print("\u2713 Figure 4 created: Figure4_ValidationFramework.png and .pdf")
    print("  (Fixed emoji rendering issue, renumbered from Figure 5)")
    plt.close()


if __name__ == '__main__':
    print("="*70)
    print("CREATING FIGURE 4: VALIDATION FRAMEWORK (FIXED VERSION)")
    print("="*70)
    print()
    print("Changes from original Figure 5:")
    print("  \u2022 Replaced emoji with standard Unicode symbols")
    print("  \u2022 Renumbered: Figure 5 \u2192 Figure 4")
    print("  \u2022 Fixed font rendering warnings")
    print()

    create_figure4()

    print()
    print("="*70)
    print("FIGURE 4 CREATED SUCCESSFULLY")
    print("="*70)
    print()
