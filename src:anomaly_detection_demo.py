import numpy as np

class SimpleAnomalyDetector:
    def __init__(self, threshold_std=3.0):
        self.threshold_std = threshold_std

    def fit(self, errors):
        self.mean = np.mean(errors)
        self.std = np.std(errors)
        self.threshold = self.mean + self.threshold_std * self.std

    def predict(self, errors):
        return (errors > self.threshold).astype(int)
