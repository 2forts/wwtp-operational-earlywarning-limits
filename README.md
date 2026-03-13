# Operational limits of early-warning models for wastewater treatment plants

This repository contains the code and notebooks used to generate the results and figures for the manuscript:

**“Operational limits of early-warning models for wastewater treatment plants under realistic false-alarm constraints”**

The study investigates whether data-driven early-warning models for wastewater treatment plants (WWTPs) admit an **operationally viable regime** when evaluated under explicit false-alarm constraints and event-based metrics.

---

## Key message

Although weak predictive signal is detectable in multivariate WWTP data using standard discrimination metrics (ROC-AUC, PR-AUC), **this signal does not translate into actionable early warning** under realistic operating conditions.

Across multiple datasets, models fail to anticipate events at conservative alarm rates (≈ one false alarm per 30 days). Meaningful detection only emerges at alarm frequencies that are incompatible with routine plant operation.

---

## What this repository contains

```
├─ notebooks/    # Jupyter notebooks used to generate results and figures
├─ src/          # Reusable utilities (event definition, labels, evaluation)
├─ figures/      # Final figures used in the manuscript
├─ data/         # Instructions for obtaining datasets (no raw data included)
├─ paper/        # Optional manuscript-related materials
```

Raw datasets are **not** included in this repository.

---

## Evaluation philosophy

This work departs from point-wise classification evaluation and adopts an **operational perspective**, based on:

- Horizon-based early-warning formulation
- Event-level objectives (not sample-level accuracy)
- Explicit false-alarm constraints
- Rolling-origin (strictly chronological) validation
- Operational curves:  
  **event hit-rate vs. false alarms per 30 days**

This framework directly reflects how early-warning systems are used in practice.

---

## Datasets analysed

1. **UCI Water Treatment Plant dataset**  
   Daily multivariate process data (527 days)

2. **High-frequency N₂O emission dataset**  
   Minute-resolution biological process measurements (Appendix A)

3. **High-frequency industrial control dataset (Agtrup, 2-minute resolution)**  
   Independent industrial WWTP monitoring data (Appendix B)

Across all datasets, the absence of a conservative operational regime persists.

---

## Models included

- Logistic regression (transparent baseline)
- Temporal Convolutional Network (sequence model)
- Gradient-boosted trees (XGBoost) for robustness analysis

The observed operational limits are **not architecture-dependent**.

---

## Reproducing the results

1. Create the Python environment (recommended):

```
conda env create -f environment.yml
conda activate wwtp-ew-operational
```

or using pip:

```
pip install -r requirements.txt
```

2. Download the datasets following the instructions in `data/README.md`.

3. Run the notebooks in order:

```
01_uci_exploration_baselines.ipynb
02_uci_tcn_model.ipynb
03_uci_main_results.ipynb
04_uci_operational_robustness.ipynb
05_n2o_highfreq_operational_robustness.ipynb
06_agtrup_2min_operational_robustness.ipynb
04b_uci_xgboost_operational_limits.ipynb (optional but recommended)
```

Figures used in the manuscript will be saved to the `figures/` directory.

---

## License

This repository is released under the MIT License.
