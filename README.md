# Interference Detection and Anomaly Classification – Demonstration Repository

This repository provides a simplified and fully reproducible demonstration of PCA-based interference detection and anomaly classification. It contains synthetic multichannel data and clean example code illustrating the methodology described in the accompanying research paper.

---

 Repository Structure
interference-demo/
├── sample_data.csv # Synthetic example dataset
├── requirements.txt # Python dependencies
├── run_demo.py # Full demonstration pipeline
└── src/
├── generate_data.py # Synthetic data generator
├── pca_pipeline_demo.py # PCA pipeline implementation
└── anomaly_detection_demo.py# Threshold-based anomaly detection

---

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt

unning the Demonstration

Run the full demonstration pipeline:

python run_demo.py


This script performs the following steps:

loads the synthetic dataset

applies PCA for dimensionality reduction

computes reconstruction errors

detects anomalies

evaluates classification performance

Running in Google Colab (Optional)

To reproduce the results interactively in Google Colab:

!git clone https://github.com/sebastiancikovsky/interference-demo.git
%cd interference-demo
!pip install -r requirements.txt


After installation, continue with the analysis steps shown in run_demo.py.

Data & Code Availability

All scripts and synthetic data required to reproduce the results are included in this repository.
No proprietary or sensitive data are used.

