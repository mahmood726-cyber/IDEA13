# Figure 1: Forest Plot Specification

## Title
**Beta-Blocker Effect on Death, MI, or Heart Failure by Ejection Fraction**
*Post-Myocardial Infarction Patients*

## Layout

```
Subgroup               0.5   0.6   0.7   0.8   0.9   1.0   1.1        HR (95% CI)
                              Favors BB    |    Favors Control

EF 40-49%              [----●----]         |                         0.75 (0.58-0.97)
N=1,885, Events=235                        |
Lancet 2025                                |

EF ≥50%                            [---■---]---]                     0.97 (0.87-1.07)
N=17,801, Events=1,465                     |
NEJM 2025                                  |

Overall Pooled                      [--◆--]                          0.94 (0.85-1.03)
N=19,686, Events=1,700                     |
Fixed-effect MA                            |

                                           |
                    ┌──────────────────────────────────┐
                    │  Test for Interaction: p = 0.069 │
                    │                                  │
                    │  Non-significant (p ≥ 0.05)      │
                    │  No evidence for differential    │
                    │  effect between subgroups        │
                    └──────────────────────────────────┘
```

## Visual Elements

### Point Estimates
- **EF 40-49%**: Circle (●) at HR = 0.75, Color: Blue (#2E86AB)
- **EF ≥50%**: Square (■) at HR = 0.97, Color: Purple (#A23B72)
- **Overall**: Diamond (◆) at HR = 0.94, Color: Orange (#F18F01)

### Confidence Intervals
- **EF 40-49%**: Line from 0.58 to 0.97 (crosses 1.0 at upper bound)
- **EF ≥50%**: Line from 0.87 to 1.07 (straddles 1.0)
- **Overall**: Line from 0.85 to 1.03 (straddles 1.0)

### Reference Line
- Vertical dashed line at HR = 1.0 (no effect)

### Text Annotations

**Left Side (for each row):**
1. Subgroup name (bold)
2. Sample size and events (italic, gray)
3. Source citation (smaller, gray)

**Right Side:**
- HR with 95% CI in parentheses

### Key Statistical Finding (Highlighted Box)
```
┌─────────────────────────────────────┐
│ Test for Interaction: p = 0.069     │
│                                     │
│ INTERPRETATION:                     │
│ Non-significant (p ≥ 0.05)          │
│ No statistical evidence for         │
│ different treatment effects         │
│ between EF subgroups                │
└─────────────────────────────────────┘
```
- Background: Light yellow (#FFF3CD)
- Border: Dark yellow/brown (#856404)
- Text: Bold for p-value, italic for interpretation

## Data Table

| Subgroup | N | Events | Events (BB) | Events (Ctrl) | HR | 95% CI Lower | 95% CI Upper | Source |
|----------|---|--------|-------------|---------------|----|--------------|--------------| -------|
| EF 40-49% | 1,885 | 235 | 106 | 129 | 0.75 | 0.58 | 0.97 | Lancet 2025 |
| EF ≥50% | 17,801 | 1,465 | 717 | 748 | 0.97 | 0.87 | 1.07 | NEJM 2025 |
| Overall | 19,686 | 1,700 | 823 | 877 | 0.94 | 0.85 | 1.03 | Pooled |

## Statistical Details

### Interaction Test Calculation
```
log(HR₁) = log(0.75) = -0.2877
log(HR₂) = log(0.97) = -0.0305

SE₁ = (log(0.97) - log(0.58)) / (2 × 1.96) = 0.1312
SE₂ = (log(1.07) - log(0.87)) / (2 × 1.96) = 0.0528

Z = (log(HR₁) - log(HR₂)) / √(SE₁² + SE₂²)
  = (-0.2877 - (-0.0305)) / √(0.0172 + 0.0028)
  = -0.2572 / 0.1414
  = -1.819

p = 2 × Φ(-|Z|) = 2 × Φ(-1.819) = 0.069
```

### Interpretation
- **p = 0.069 ≥ 0.05**: Non-significant
- **Conclusion**: The hazard ratios of 0.75 and 0.97 do NOT significantly differ
- **Clinical implication**: No statistical support for an EF threshold at 50%

## Notes for Reproduction

**Software Options:**
1. **R**: Use `forestplot` package or `ggplot2`
2. **Python**: Use `matplotlib` with custom plotting
3. **Excel/PowerPoint**: Manual creation using shapes
4. **GraphPad Prism**: Forest plot function
5. **RevMan**: Cochrane's Review Manager

**Key Design Principles:**
- Clear visual distinction between subgroups
- Prominent display of interaction test
- Reference line at HR = 1.0 clearly marked
- Confidence intervals visually overlap
- Color coding aids interpretation
- Statistical rigor emphasized (p-value in box)

## Figure Legend

**Figure 1. Forest Plot of Beta-Blocker Effects by Ejection Fraction with Test for Interaction.**

Individual patient data meta-analyses of beta-blocker therapy after myocardial infarction stratified by left ventricular ejection fraction (LVEF). The EF 40-49% subgroup data are from Rossello et al., *Lancet* 2025 (N=1,885). The EF ≥50% subgroup data are from the NEJM 2025 publication (N=17,801). The overall pooled estimate combines both subgroups using fixed-effect meta-analysis. Squares and circle represent point estimates (hazard ratios); horizontal lines represent 95% confidence intervals. The vertical dashed line at HR=1.0 indicates no treatment effect. The diamond represents the overall pooled effect. **The test for interaction (p=0.069) is non-significant**, indicating no statistical evidence that the treatment effects differ between the two EF ranges. This non-significant interaction test contradicts the claim of a sharp threshold effect at EF=50%. HR, hazard ratio; CI, confidence interval; BB, beta-blocker; MI, myocardial infarction.
