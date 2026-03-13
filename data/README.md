# Data instructions

This repository does **not** include raw datasets.

## 1) UCI Water Treatment Plant dataset
Download from the UCI Machine Learning Repository (Water Treatment Plant).
Place files in:

- `data/external/uci_water_treatment/water-treatment.data`
- `data/external/uci_water_treatment/water_treatment.names`

## 2) High-frequency datasets (appendices)
These datasets are referenced in the manuscript and must be obtained from their original sources.
Place them in separate subfolders under `data/external/` and update the notebook paths accordingly.

## Notes
- Do not commit raw data to the repository.
- Notebooks should read from `data/external/...` and optionally write processed artifacts to `data/processed/...`.
