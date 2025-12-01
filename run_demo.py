import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from pca_pipeline_demo import PCAPipeline
from anomaly_detection_demo import SimpleAnomalyDetector

def main():
    df = pd.read_csv("data/sample_data.csv")
    X = df.drop("label", axis=1).values
    y = df["label"].values

    pca_pipe = PCAPipeline()
    pca_pipe.fit(X)

    Z = pca_pipe.transform(X)
    errors = pca_pipe.reconstruction_error(X)

    detector = SimpleAnomalyDetector()
    detector.fit(errors)
    anomaly_flags = detector.predict(errors)

    clf = LogisticRegression(max_iter=1000)
    clf.fit(Z, y)
    y_pred = clf.predict(Z)

    print(classification_report(y, y_pred))
    print("Detected anomalies:", sum(anomaly_flags))

if __name__ == "__main__":
    main()
