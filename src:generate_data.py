import numpy as np
import pandas as pd

def generate_sample_data(n_samples=1000, n_channels=8):
    mean = np.zeros(n_channels)
    cov = np.eye(n_channels)
    X = np.random.multivariate_normal(mean, cov, size=n_samples)
    anomalies = np.random.multivariate_normal(mean+3, cov*2, size=50)
    labels = np.zeros(n_samples+50)
    labels[-50:] = 1
    X_full = np.vstack([X, anomalies])
    df = pd.DataFrame(X_full, columns=[f"channel_{i}" for i in range(n_channels)])
    df["label"] = labels
    return df

if __name__ == "__main__":
    df = generate_sample_data()
    df.to_csv("../data/sample_data.csv", index=False)
