# Methods - Part 2: Simulation Study (CONDENSED)

## Part 2: Simulation Study

### Simulation Design

We generated 10,000 synthetic IPD meta-analyses, each matching the key structural features of the EF 40-49% meta-analysis: 4 trials with sample sizes proportional to the original trials (52%, 22%, 23%, 3%), totaling 1,885 patients with approximately 235 events.

### Data Generation

For each simulated meta-analysis:

**Patient characteristics:**
- **Trial assignment:** Multinomial allocation matching original trial proportions
- **Ejection fraction:** Truncated normal distribution (mean=45%, SD=2.5%, range 40.0-49.9%)
- **Treatment:** Random 50/50 allocation to beta-blocker vs. control

**Survival time generation:**

Event times were generated from exponential distributions with hazard rates depending on treatment assignment and ejection fraction. Crucially, we programmed a smooth, continuous relationship between LVEF and treatment effect with **no threshold at any specific value**:

$$\log(HR(EF)) = -0.287 + 0.0182 \times (EF - 40)$$

This produces HR=0.70 at EF=40%, declining linearly to HR=0.90 at EF=50%, with no discontinuity. Baseline annual event rate (λ₀=0.038) and censoring (mean 3.5 years) were calibrated to produce ~235 events per simulation, matching observed data.

### Sensitivity Analysis: Alternative True Effect Models

To assess robustness, we tested five additional functional forms (detailed equations in Supplementary Methods):

- **Model 1 (Primary):** Linear decline HR 0.70→0.90 (no threshold)
- **Model 2:** Quadratic with accelerating decline
- **Model 3:** Gentle threshold at EF=47% (HR 0.70 below, 0.90 above)
- **Model 4:** Complete null (HR=1.0 at all LVEF values)
- **Model 5:** Random heterogeneous effects across trials
- **Model 6:** True threshold at EF=50% matching observed data (HR 0.75 below, 0.97 above)

Models 1-5 assess **specificity** (rejecting false thresholds when none exist). Model 6 assesses **sensitivity** (detecting true thresholds when they genuinely exist), providing complete evaluation of cross-validation's diagnostic performance.

### Analytical Methods Applied to Simulated Data

We applied four strategies to each simulated dataset:

**Method 1: Multiple Threshold Testing** — Tested 13 thresholds (42.0%, 42.5%, ..., 48.0%) and recorded whether **any** produced p<0.05 in the low-EF group. This mimics exploratory threshold searching without validation.

**Method 2: Single Interaction Test** — Tested for interaction at a single pre-specified threshold (EF=45%), representing best practice when the threshold is predetermined.

**Method 3: Continuous Modeling** — Modeled EF continuously with treatment × EF interaction, testing whether treatment effect varied with LVEF without dichotomization.

**Method 4: Cross-Validation (Gold Standard)** — Leave-one-trial-out validation:
1. **Training:** Combine 3 trials, find threshold (42-48%) with smallest p-value
2. **Testing:** Apply discovered threshold to held-out 4th trial
3. **Validation:** Check if low-EF group in test trial shows p<0.05
4. Repeat leaving out each trial; record "validated" if ≥1 of 4 test trials shows p<0.05

This procedure tests whether discovered thresholds replicate in independent data—the fundamental requirement for distinguishing signal from noise.

### Outcome Measures

For each method, we calculated:
1. **False-positive rate:** Proportion of 10,000 simulations declaring a "significant" threshold despite none existing in the true model
2. **Distribution of discovered thresholds:** Whether "significant" findings cluster at any specific EF value or distribute randomly
3. **Sensitivity (Model 6 only):** Proportion detecting the true threshold when one genuinely exists

### Software

Simulations were conducted in Python 3.11 using NumPy 1.24 (random number generation), SciPy 1.10 (statistical functions), and lifelines 0.27 (Cox models). Random seeds were set for reproducibility (master seed: 2025). Complete code is available at [GitHub repository].

---

**Word Count:** ~590 words (down from ~1,500 words; saves ~910 words) ✓

**Content Preserved:**
- ✅ Simulation design overview
- ✅ Core data generation process with key equation
- ✅ All six models described (including Model 6 rationale)
- ✅ All four analytical methods clearly explained
- ✅ Cross-validation procedure with clear steps
- ✅ Outcome measures
- ✅ Software details

**Content Condensed:**
- Detailed equations for Models 2-6 → "detailed equations in Supplementary Methods"
- Extended survival time formulas → Summarized
- Sensitivity analysis justifications → Streamlined
- Statistical software specifications → Brief mention with supplement reference

**Moved to Supplement:**
- Complete equations for all 6 models (Supplementary Methods S2.2)
- Detailed parameter derivations (Table S4)
- Cross-validation algorithm pseudocode (Supplementary Methods S2.3)
- Computational resources and timing details
