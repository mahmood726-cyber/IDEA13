# Results - Part A: Empirical Analysis (CONDENSED)

## Study Characteristics

We analyzed published summary data from two companion IPD meta-analyses comprising 19,686 patients from four contemporary randomized trials (REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT). The EF 40-49% meta-analysis included 1,885 patients with 235 primary endpoint events (death, MI, or heart failure).[8] The EF ≥50% meta-analysis included 17,801 patients with 1,465 events.[9]

---

## Part A: Statistical Validation of the Proposed EF Threshold

### Test for Interaction

The formal test for interaction between EF 40-49% and EF ≥50% subgroups yielded **p=0.069** (Z=-1.819), failing to reach statistical significance. With only 235 events in the smaller subgroup, this test had only **46% power** to detect the observed difference as significant—less than a coin flip.

The **95% CI for the difference in log hazard ratios was -0.53 to +0.02**, encompassing no difference (0), moderate differences (-0.25), and large differences (-0.53). This wide confidence interval reflects substantial uncertainty about whether treatment effects truly differ between subgroups.

**Table 1. Test for Interaction Between EF Subgroups**

| Parameter | Value | Interpretation |
|-----------|-------|----------------|
| **Interaction test** | p = 0.069 | Not significant (p ≥ 0.05) |
| **Power of interaction test** | 46% | High risk of Type II error |
| **95% CI for difference** | -0.53 to +0.02 | Wide uncertainty |
| **Conclusion** | **Insufficient evidence for differential effects** | |

**Interpretation: Equipoise, Not Certainty**

Given the limited power (46%), our non-significant interaction test represents **"absence of evidence"** rather than **"evidence of absence."** The data are equally consistent with no threshold, a modest threshold, or a larger threshold. This uncertainty means that confident assertions either for or against a sharp threshold lack adequate statistical support. **We do not claim to have proven the threshold is absent**; rather, evidence is insufficient to support practice-changing recommendations based on EF stratification.

### Fragility Analysis

The fragility index for the EF 40-49% finding was **3 events**—meaning only 3 events (1.3% of 235 total) need reclassification to eliminate statistical significance (p≥0.05). Walsh et al. recommend FI>5 for minimally robust findings and >10 for practice-changing claims.[30] A fragility index of 3 indicates extreme statistical instability.

**Table 2. Fragility Index Analysis**

| Metric | Value | Threshold | Met? |
|--------|-------|-----------|------|
| Fragility Index | 3 events | >5 (minimum) | ❌ No |
| As % of total events | 1.3% | | |
| As % of sample size | 0.16% | | |
| Practice-changing claims | >10 events | >10 | ❌ No |

### Power Analysis

With 235 events, the EF 40-49% subgroup had only **40.1% power** to detect HR=0.80—well below the conventional 80% threshold.[32] Even for the more extreme observed HR=0.75, power was only 59.7%. To achieve 80% power at HR=0.80 would require 630 events—168% more than observed.

**Table 3. Statistical Power Analysis**

| True HR | Power (%) | Adequately Powered (≥80%)? |
|---------|-----------|---------------------------|
| 0.70 | 78.0% | Nearly adequate |
| 0.75 | 59.7% | **No** ⚠️ |
| 0.80 | 40.1% | **No** ⚠️ |

**Events required for 80% power at HR=0.80:** 630 (need 168% more)

### Overall Pooled Effect

When both EF ranges were combined, the pooled hazard ratio was **HR 0.94 (95% CI 0.85-1.03, p=0.25)**—no significant benefit across the entire LVEF spectrum from 40% onward (Figure 1). This null overall effect questions whether beta-blockers benefit any contemporary post-MI patients with LVEF ≥40%, regardless of specific EF value.

### Summary: Validation Criteria

**Table 4. Summary of Empirical Validation**

| Analysis | Finding | Passes? |
|----------|---------|---------|
| Interaction test | p = 0.069 | ❌ No |
| Fragility index | FI = 3 (1.3%) | ❌ No |
| Statistical power | 40% at HR=0.80 | ❌ No |
| Overall pooled effect | HR 0.94 (0.85-1.03) | ❌ Not significant |
| **Validation tests passed** | **0 / 4** | **❌ Failed** |

**What Can and Cannot Be Concluded**

Our analyses address a focused question: Is there sufficient statistical evidence for a sharp treatment effect threshold at LVEF=50%? Based on available evidence, **we cannot support this claim**.

However, we cannot definitively distinguish between several scenarios:
- **Scenario A:** No benefit at any LVEF ≥40% (consistent with pooled HR=0.94)
- **Scenario B:** Modest benefit across all LVEF ranges (approximately HR 0.85-0.90)
- **Scenario C:** Benefit declines gradually (not sharply) with increasing LVEF

Distinguishing between these would require individual patient data with continuous LVEF modeling (e.g., restricted cubic splines).

**What we CAN conclude:**

1. Evidence does **NOT support a sharp threshold at LVEF=50%** as a binary treatment decision rule
2. Non-significant interaction (p=0.069, 46% power), extreme fragility (FI=3), and underpowering (40% power) indicate the threshold is **statistically unreliable**
3. Wide confidence interval (-0.53 to +0.02) reflects **insufficient precision** for confident subgroup inferences
4. Overall pooled effect (HR 0.94, 0.85-1.03) suggests **at most modest benefit** across the LVEF spectrum, possibly no benefit at all

**Clinical recommendation:** LVEF should **not** be used as a dichotomous decision rule for beta-blocker therapy after MI. Treatment decisions should be individualized, incorporating LVEF as one of multiple continuous risk factors. The decision should not pivot on whether LVEF is 49% versus 51%.

---

**Word Count:** ~810 words (estimated original ~1,500 words; saves ~690 words) ✓

**Content Preserved:**
- ✅ Study characteristics
- ✅ Test for interaction (p=0.069, power=46%)
- ✅ "Equipoise, Not Certainty" interpretation
- ✅ Fragility analysis (FI=3)
- ✅ Power analysis (40% at HR=0.80)
- ✅ Overall pooled effect (HR=0.94)
- ✅ Summary validation table
- ✅ What can/cannot be concluded
- ✅ Clinical recommendation

**Content Condensed:**
- Extended power calculations → Table with key values only
- Detailed interpretations → Streamlined
- Repetitive phrasing → Tightened
- Extended scenario discussions → Brief bullet points

**Moved to Supplement:**
- Complete 2×2 fragility tables → Table S1
- Extended power calculations table → Table S2
- Detailed mathematical derivations → Supplementary Methods
