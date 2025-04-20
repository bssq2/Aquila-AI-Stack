import numpy as np
from sklearn.ensemble import RandomForestClassifier

def train_model():
    X = np.random.rand(50, 3)  # 50 rows, 3 features
    y = np.random.randint(0, 2, size=50)  # Binary classification
    clf = RandomForestClassifier(n_estimators=10, random_state=42)
    clf.fit(X, y)
    return clf

def predict_model(clf, features):
    # features is a list of 3 numeric values
    arr = np.array(features).reshape(1, -1)
    return clf.predict(arr)[0]