# Figure 5: Proposed Validation Framework for Subgroup Claims

## Title
**A Validation Framework for Subgroup Claims from Individual Patient Data Meta-Analyses**

## Flowchart Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                    SUBGROUP CLAIM IDENTIFIED                     │
│         "Treatment X works in Subgroup A but not B"              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                  LEVEL 1: MINIMUM REQUIREMENTS                   │
│                  (All must pass to proceed)                      │
└─────────────────────────────────────────────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │                                  │
        ▼                                  ▼
┌─────────────────┐              ┌──────────────────────┐
│  1. PRE-        │              │  2. BIOLOGICAL       │
│  SPECIFICATION  │              │  PLAUSIBILITY        │
├─────────────────┤              ├──────────────────────┤
│ Was subgroup    │              │ Is there mechanistic │
│ defined in      │              │ rationale for        │
│ protocol before │              │ differential effect? │
│ seeing data?    │              │                      │
│                 │              │ Beta-blocker EF:     │
│ ✓ Yes → Pass    │              │ ❌ No clear mechanism│
│ ✗ No → FAIL     │              │ for sharp threshold  │
└────────┬────────┘              └──────────┬───────────┘
         │                                  │
         └────────────────┬─────────────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │  3. INTERACTION     │
                │  TEST SIGNIFICANT   │
                ├─────────────────────┤
                │ p < 0.05 for        │
                │ treatment × subgroup│
                │ interaction?        │
                │                     │
                │ Beta-blocker EF:    │
                │ ❌ p = 0.069        │
                │ NON-SIGNIFICANT     │
                └─────────┬───────────┘
                          │
                 ┌────────┴────────┐
                 │ STOP if p ≥ 0.05│
                 │ INSUFFICIENT    │
                 │ EVIDENCE        │
                 └─────────────────┘
                          │
                          ▼ (if p < 0.05)
┌─────────────────────────────────────────────────────────────────┐
│                  LEVEL 2: ROBUSTNESS CHECKS                      │
│              (Assess reliability of the finding)                 │
└─────────────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                  │
        ▼                 ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌─────────────────┐
│ 4. ADEQUATE  │  │ 5. FRAGILITY │  │ 6. OPTIMAL INFO │
│ POWER        │  │ INDEX        │  │ SIZE (TSA)      │
├──────────────┤  ├──────────────┤  ├─────────────────┤
│ ≥80% power   │  │ FI > 5 for   │  │ Cumulative data │
│ to detect    │  │ robust       │  │ reaches required│
│ meaningful   │  │              │  │ information size│
│ effect in    │  │ FI > 10 for  │  │                 │
│ subgroup?    │  │ practice-    │  │ Beta-blocker:   │
│              │  │ changing     │  │ ❌ Below RIS    │
│ Beta-blocker:│  │              │  │                 │
│ ❌ 40% power │  │ Beta-blocker:│  └────────┬────────┘
│              │  │ ❌ FI = 3    │           │
└──────┬───────┘  └──────┬───────┘           │
       │                 │                   │
       └────────┬────────┴─────────┬─────────┘
                │                  │
                ▼                  ▼
        ┌───────────────┐  ┌──────────────────┐
        │ ALL PASSED?   │  │ ANY FAILED?      │
        │               │  │                  │
        │ ✓ → Proceed   │  │ ⚠️  → Interpret  │
        │ to Level 3    │  │ with CAUTION     │
        └───────┬───────┘  └──────────────────┘
                │
                ▼
┌─────────────────────────────────────────────────────────────────┐
│              LEVEL 3: VALIDATION (GOLD STANDARD)                 │
│           (Required for practice-changing claims)                │
└─────────────────────────────────────────────────────────────────┘
                │
        ┌───────┴───────┐
        │               │
        ▼               ▼
┌──────────────┐  ┌─────────────────┐
│ 7. CROSS-    │  │ 8. INDEPENDENT  │
│ VALIDATION   │  │ REPLICATION     │
├──────────────┤  ├─────────────────┤
│ Effect holds │  │ Finding confirms│
│ in held-out  │  │ in separate     │
│ data?        │  │ dataset?        │
│              │  │                 │
│ • Leave-one- │  │ • External data │
│   trial-out  │  │ • Prospective   │
│ • Split      │  │   validation    │
│   sample     │  │                 │
│              │  │ Beta-blocker:   │
│ Beta-blocker:│  │ ❌ Not performed│
│ ❌ Not done  │  │                 │
└──────┬───────┘  └────────┬────────┘
       │                   │
       └─────────┬─────────┘
                 │
                 ▼
        ┌────────────────┐
        │ AT LEAST ONE   │
        │ VALIDATION     │
        │ PASSED?        │
        ├────────────────┤
        │ ✓ Yes →        │
        │   VALIDATED    │
        │   CLAIM        │
        │                │
        │ ✗ No →         │
        │   UNVALIDATED  │
        │   DO NOT USE   │
        │   FOR GUIDELINES│
        └────────┬───────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                         FINAL DECISION                           │
└─────────────────────────────────────────────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
┌──────────────┐  ┌──────────────────┐
│ ✓ VALIDATED  │  │ ✗ NOT VALIDATED  │
│              │  │                  │
│ • All Level 1│  │ • Failed ≥1      │
│   passed     │  │   Level 1 test   │
│ • Most Level │  │                  │
│   2 passed   │  │ OR               │
│ • ≥1 Level 3 │  │                  │
│   passed     │  │ • Failed Level 2 │
│              │  │   tests          │
│ → May inform │  │                  │
│   guidelines │  │ AND              │
│              │  │                  │
│              │  │ • No Level 3     │
│              │  │   validation     │
│              │  │                  │
│              │  │ → DO NOT use for │
│              │  │   guidelines     │
└──────────────┘  └──────────────────┘
```

## Beta-Blocker EF Threshold: Scorecard

| Level | Test | Requirement | Result | Pass? |
|-------|------|-------------|--------|-------|
| **Level 1** | | | | |
| | 1. Pre-specification | In protocol | Unclear | ❓ |
| | 2. Biological plausibility | Mechanistic rationale | None | ❌ |
| | 3. Interaction test | p < 0.05 | p = 0.069 | ❌ |
| **Level 2** | | | | |
| | 4. Adequate power | ≥80% power | 40% power | ❌ |
| | 5. Fragility index | FI > 5 | FI = 3 | ❌ |
| | 6. Optimal information size | Reached RIS | Below RIS | ❌ |
| **Level 3** | | | | |
| | 7. Cross-validation | Replicates in held-out | Not performed | ❌ |
| | 8. Independent replication | Confirms in external data | Not performed | ❌ |
| **TOTAL** | | | | **0/8 or 1/8** |

**Final Verdict:** ❌ **NOT VALIDATED** — Do not use for guidelines

## Checklist for Authors and Reviewers

### For Authors Reporting Subgroup Findings:

☐ **Pre-specify** subgroups in protocol before data analysis
☐ **Provide** biological/mechanistic rationale for expected heterogeneity
☐ **Report** formal interaction test (not just separate p-values)
☐ **Calculate** statistical power for subgroup analysis
☐ **Assess** fragility index
☐ **Perform** trial sequential analysis (if meta-analysis)
☐ **Validate** using cross-validation or split-sample methods
☐ **Seek** independent replication before recommending practice changes

### For Guideline Committees Evaluating Subgroup Claims:

☐ **Verify** interaction test is significant (p < 0.05)
☐ **Confirm** adequate power (≥80%)
☐ **Check** fragility index (>5 minimum, >10 for practice-changing)
☐ **Require** validation in held-out data or external cohort
☐ **Assess** biological plausibility
☐ **Delay** guideline changes until validation complete
☐ **Commission** independent replication studies if needed

---

## Figure Legend

**Figure 5. Proposed Validation Framework for Subgroup Claims from Individual Patient Data Meta-Analyses.**

A three-level framework for evaluating the credibility of subgroup effect claims. **Level 1** (Minimum Requirements) includes pre-specification, biological plausibility, and a significant interaction test; failure of any Level 1 criterion indicates insufficient evidence for a subgroup effect. **Level 2** (Robustness Checks) assesses the reliability of findings through power analysis, fragility assessment, and information size requirements. **Level 3** (Validation) requires either cross-validation in held-out data or independent external replication before using findings to inform clinical practice guidelines. The beta-blocker ejection fraction threshold is shown failing all applicable tests (0/8 or 1/8 passed), illustrating how even findings from high-quality IPD meta-analyses can represent statistical artifacts when validation procedures are not applied. Authors should report all framework elements; guideline committees should require passage of all Level 1 tests and at least one Level 3 validation before adopting subgroup-stratified recommendations. FI, fragility index; RIS, required information size; TSA, trial sequential analysis.

---

**Key Messages:**

1. **Three-tier validation**: Minimum requirements → Robustness → Validation
2. **Beta-blocker example**: Failed all 8 tests (or 7/8 if pre-specification unclear)
3. **For guidelines**: Require validation (Level 3) for practice-changing claims
4. **Generalizable**: Applies to any IPD meta-analysis subgroup claim

