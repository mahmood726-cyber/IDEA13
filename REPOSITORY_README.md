# Beta-Blocker EF Threshold Validation Analysis

**Repository for:** Statistical Overfitting in Subgroup Analyses: Evidence from Beta-Blocker Trials and a Validation Framework

**Manuscript submitted to:** BMJ

**DOI:** 10.5281/zenodo.PENDING (to be assigned upon publication)

---

## Overview

This repository contains all code and data for validating the proposed ejection fraction threshold for beta-blocker efficacy after myocardial infarction. The analysis includes:

1. **Empirical validation** using published summary statistics from two IPD meta-analyses
2. **Simulation studies** (N=10,000 iterations × 6 models) quantifying false-positive rates
3. **Cross-validation framework** for threshold validation

---

## Repository Structure

```
beta-blocker-validation/ef-threshold-analysis/
│
├── README.md                          # This file
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
├── environment.yml                    # Conda environment (alternative)
│
├── data/
│   ├── extracted_data.csv            # Summary statistics from [8,9]
│   ├── ef_40_49_data.csv             # EF 40-49% subgroup data
│   ├── ef_50plus_data.csv            # EF ≥50% subgroup data
│   ├── event_tables.csv              # 2×2 contingency tables
│   └── README_data.md                # Data extraction documentation
│
├── code/
│   ├── empirical_analysis/
│   │   ├── interaction_test.py       # Formal interaction testing
│   │   ├── fragility_index.py        # Fragility index calculation
│   │   ├── power_analysis.py         # Power calculations
│   │   ├── pooled_effect.py          # Inverse-variance pooling
│   │   └── empirical_main.py         # Run all empirical analyses
│   │
│   ├── simulations/
│   │   ├── simulation_model1.py      # Linear decline
│   │   ├── simulation_model2.py      # Quadratic
│   │   ├── simulation_model3.py      # Gentle threshold (EF=47%)
│   │   ├── simulation_model4.py      # Complete null
│   │   ├── simulation_model5.py      # Random heterogeneous
│   │   ├── simulation_model6.py      # True threshold (EF=50%)
│   │   ├── simulation_utils.py       # Shared simulation functions
│   │   └── run_all_simulations.py    # Run all 6 models
│   │
│   ├── validation/
│   │   ├── cross_validation.py       # Leave-one-trial-out CV
│   │   ├── multiple_testing.py       # Test 13 thresholds
│   │   ├── continuous_modeling.py    # Spline modeling
│   │   └── validation_comparison.py  # Compare all methods
│   │
│   └── visualization/
│       ├── figure1_forest_plot.py    # Forest plot of results
│       ├── figure2_fpr_comparison.py # False-positive rate comparison
│       ├── figure3_distributions.py  # P-value distributions
│       └── figure5_framework.py      # Validation framework diagram
│
├── results/
│   ├── empirical_results.csv         # Interaction, fragility, power
│   ├── simulation_results/
│   │   ├── model1_results.csv
│   │   ├── model2_results.csv
│   │   ├── model3_results.csv
│   │   ├── model4_results.csv
│   │   ├── model5_results.csv
│   │   └── model6_results.csv
│   ├── false_positive_rates.csv      # Summary across all models
│   └── figures/
│       ├── figure1_forest_plot.png
│       ├── figure2_fpr_comparison.png
│       ├── figure3_p_distributions.png
│       └── figure5_validation_framework.png
│
├── tests/
│   ├── test_interaction.py           # Unit tests for interaction test
│   ├── test_fragility.py             # Unit tests for fragility index
│   ├── test_simulations.py           # Validation of simulation code
│   └── test_cross_validation.py      # Cross-validation tests
│
└── docs/
    ├── methods_detailed.md           # Extended methods documentation
    ├── simulation_parameters.md      # Calibration parameters
    ├── replication_guide.md          # Step-by-step replication
    └── troubleshooting.md            # Common issues and solutions
```

---

## Installation

### Option 1: Using pip

```bash
# Clone repository
git clone https://github.com/beta-blocker-validation/ef-threshold-analysis.git
cd ef-threshold-analysis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using conda

```bash
# Clone repository
git clone https://github.com/beta-blocker-validation/ef-threshold-analysis.git
cd ef-threshold-analysis

# Create conda environment
conda env create -f environment.yml
conda activate ef-threshold
```

---

## Dependencies

### Core Requirements

- Python ≥ 3.11
- NumPy ≥ 1.24.0
- SciPy ≥ 1.10.0
- pandas ≥ 2.0.0
- lifelines ≥ 0.27.0 (for Cox proportional hazards models)
- matplotlib ≥ 3.7.0
- seaborn ≥ 0.12.0

### Optional (for testing)

- pytest ≥ 7.3.0
- pytest-cov ≥ 4.1.0

---

## Quick Start

### Run Complete Analysis

```bash
# Empirical analysis (uses published data)
python code/empirical_analysis/empirical_main.py

# Simulations (all 6 models, 10,000 iterations each)
# WARNING: This takes ~2 hours on standard desktop
python code/simulations/run_all_simulations.py

# Generate all figures
python code/visualization/generate_all_figures.py
```

### Run Individual Components

```bash
# Interaction test only
python code/empirical_analysis/interaction_test.py

# Fragility index only
python code/empirical_analysis/fragility_index.py

# Single simulation model (faster for testing)
python code/simulations/simulation_model1.py --iterations 1000

# Cross-validation
python code/validation/cross_validation.py
```

---

## Data Sources

All data were extracted from publicly available published meta-analyses:

1. **Rossello X, et al.** β-blockers after myocardial infarction with mildly reduced ejection fraction. *The Lancet*. 2025. [8]
   - EF 40-49% subgroup: N=1,885 patients, 235 events
   - Hazard ratio: 0.75 (95% CI 0.58-0.97, p=0.031)

2. **Beta-Blockers after Myocardial Infarction with Normal Ejection Fraction.** *New England Journal of Medicine*. 2025. [9]
   - EF ≥50% subgroup: N=17,801 patients, 1,465 events
   - Hazard ratio: 0.97 (95% CI 0.87-1.07, p=0.54)

**Note:** We did not have access to individual patient data. All analyses use published summary statistics.

---

## Empirical Analysis

### 1. Interaction Test

```python
from code.empirical_analysis import interaction_test

result = interaction_test.calculate(
    hr1=0.75, ci1_lower=0.58, ci1_upper=0.97,  # EF 40-49%
    hr2=0.97, ci2_lower=0.87, ci2_upper=1.07   # EF ≥50%
)

print(f"Interaction p-value: {result['p_value']:.3f}")
print(f"95% CI for difference: ({result['ci_lower']:.2f}, {result['ci_upper']:.2f})")
```

**Expected output:**
```
Interaction p-value: 0.069
95% CI for difference: (-0.53, 0.02)
Interpretation: No statistical evidence for differential effects
```

### 2. Fragility Index

```python
from code.empirical_analysis import fragility_index

result = fragility_index.calculate(
    events_treatment=104,
    events_control=131,
    n_treatment=991,
    n_control=894
)

print(f"Fragility Index: {result['fragility_index']}")
print(f"As % of events: {result['percent_of_events']:.1f}%")
```

**Expected output:**
```
Fragility Index: 3
As % of events: 1.3%
Interpretation: Extremely fragile (FI < 5 threshold)
```

### 3. Power Analysis

```python
from code.empirical_analysis import power_analysis

result = power_analysis.calculate(
    n_events=235,
    hr_true=0.80,
    alpha=0.05
)

print(f"Power: {result['power']:.1%}")
print(f"Events needed for 80% power: {result['events_for_80pct']}")
```

**Expected output:**
```
Power: 40.1%
Events needed for 80% power: 630
Interpretation: Severely underpowered
```

---

## Simulation Studies

### Running Simulations

```python
from code.simulations import simulation_model1

# Run 10,000 simulations (Model 1: Linear decline)
results = simulation_model1.run_simulations(
    n_iterations=10000,
    n_patients=1885,
    n_trials=4,
    trial_proportions=[0.52, 0.22, 0.23, 0.03],
    seed=42
)

print(f"Multiple testing FPR: {results['fpr_multiple']:.1%}")
print(f"Cross-validation FPR: {results['fpr_cv']:.1%}")
```

**Expected output (Model 1):**
```
Multiple testing FPR: 46.8% (95% CI: 45.8-47.8%)
Cross-validation FPR: 1.5% (95% CI: 1.2-1.8%)
Reduction: 31-fold
```

### Simulation Parameters

All simulations are calibrated to match actual trial structure:

```python
SIMULATION_PARAMS = {
    'n_patients': 1885,
    'n_trials': 4,
    'trial_proportions': [0.52, 0.22, 0.23, 0.03],  # REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT
    'target_events': 235,
    'event_rate': 0.125,  # 12.5%
    'baseline_hazard': 0.038,  # λ₀ per year
    'mean_followup': 3.5,  # years
    'lvef_mean': 45,  # percent
    'lvef_sd': 2.5,  # percent
    'lvef_range': (40, 49.9)  # Models 1-5
}
```

For Model 6 (sensitivity analysis), LVEF range is extended to (40, 60) with mean=50, SD=5.

---

## Cross-Validation

### Leave-One-Trial-Out Validation

```python
from code.validation import cross_validation

# Generate test data
simulated_data = generate_simulated_ipd(...)  # Your data here

# Run cross-validation
cv_results = cross_validation.leave_one_trial_out(
    data=simulated_data,
    thresholds=range(42, 49, 0.5),  # Test 42.0%, 42.5%, ..., 48.0%
    alpha=0.05
)

print(f"Discovered threshold: EF={cv_results['best_threshold']}%")
print(f"Validated in held-out trial: {cv_results['validated']}")
```

---

## Reproducing Manuscript Figures

### Figure 1: Forest Plot

```bash
python code/visualization/figure1_forest_plot.py
```

Generates forest plot showing:
- EF 40-49%: HR 0.75 (0.58-0.97)
- EF ≥50%: HR 0.97 (0.87-1.07)
- Pooled: HR 0.94 (0.85-1.03)

### Figure 2: False-Positive Rate Comparison

```bash
python code/visualization/figure2_fpr_comparison.py
```

Compares false-positive rates across 4 analytical methods.

### Figure 3: P-Value Distributions

```bash
python code/visualization/figure3_distributions.py
```

Shows p-value distributions for multiple testing vs. cross-validation.

### Figure 5: Validation Framework

```bash
python code/visualization/figure5_framework.py
```

Displays the proposed 6-criteria validation framework.

---

## Testing

Run unit tests to verify code correctness:

```bash
# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=code tests/

# Run specific test file
pytest tests/test_interaction.py -v
```

---

## Performance Notes

### Computational Requirements

- **Empirical analyses:** < 1 second (uses summary statistics only)
- **Single simulation (1,000 iterations):** ~1 minute
- **Full simulation suite (10,000 × 6 models):** ~2 hours
- **Memory usage:** < 2 GB RAM

### Parallelization

For faster simulations on multi-core machines:

```python
from code.simulations import run_all_simulations

results = run_all_simulations.run_parallel(
    n_iterations=10000,
    n_cores=8  # Use 8 CPU cores
)
```

---

## Citation

If you use this code, please cite:

```
[Authors]. Statistical Overfitting in Subgroup Analyses: Evidence from
Beta-Blocker Trials and a Validation Framework. BMJ. 2025. [In press]
```

---

## License

MIT License - see LICENSE file for details.

---

## Contact

For questions or issues:
- Open an issue on GitHub
- Email: [corresponding author email]

---

## Acknowledgments

This work was conducted independently without specific funding. We thank the original investigators of the REBOOT, BETAMI, DANBLOCK, and CAPITAL-RCT trials for making their IPD meta-analysis results publicly available.

---

## Version History

- **v1.0.0** (2025-11-18): Initial release accompanying manuscript submission
- **v1.1.0** (TBD): Post-peer-review revisions
- **v2.0.0** (TBD): Final version accompanying publication

---

**Last updated:** November 18, 2025
