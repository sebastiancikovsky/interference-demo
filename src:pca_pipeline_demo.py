import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

class PCAPipeline:
    def __init__(self, n_components=0.95):
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=n_components)

    def fit(self, X):
        Xs = self.scaler.fit_transform(X)
        self.pca.fit(Xs)

    def transform(self, X):
        Xs = self.scaler.transform(X)
        return self.pca.transform(Xs)

    def reconstruction_error(self, X):
        Xs = self.scaler.transform(X)
        Xp = self.pca.inverse_transform(self.pca.transform(Xs))
        return np.mean((Xs - Xp)**2, axis=1)
