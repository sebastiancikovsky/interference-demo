# Interference Detection and Anomaly Classification – Demonstration Repository

This repository provides a concise and fully reproducible demonstration of PCA-based interference detection and anomaly classification. It includes a synthetic multichannel dataset and clean reference implementations that illustrate the core methodology discussed in the related research.

## Contents

- **sample_data.csv** — synthetic multichannel dataset  
- **requirements.txt** — Python dependencies  
- **run_demo.py** — complete demonstration workflow  
- **pca_pipeline_demo.py** — PCA transformation and reconstruction-error pipeline  
- **anomaly_detection_demo.py** — threshold-based anomaly detection  
- **generate_data.py** — synthetic data generator  
- **colab_demo.ipynb** — full Google Colab notebook with plots  

All code is self-contained and purely demonstrational; no proprietary or sensitive datasets are included.

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running the Demonstration

```bash
python run_demo.py
```

This script loads the dataset, applies PCA for dimensionality reduction, computes reconstruction errors, identifies anomalies, and prints evaluation metrics.

---

## Google Colab Notebook

You can run the full reproducible demo (including all plots) directly in Google Colab:

[[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebastiancikovsky/interference-demo/blob/main/colab_demo.ipynb)](https://colab.research.google.com/github/sebastiancikovsky/interference-demo/blob/main/colab_demo.ipynb
)

Alternatively, in a new Google Colab notebook you may execute:

```python
!git clone https://github.com/sebastiancikovsky/interference-demo.git
%cd interference-demo
!pip install -r requirements.txt
!python run_demo.py
```

---

## Reproducibility

All data and code required to reproduce the results are included in this repository.  
The workflow is deterministic and produces consistent outputs across environments.

---

## License

This repository is provided for academic and demonstrational purposes.
