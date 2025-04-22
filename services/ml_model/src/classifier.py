from sklearn.dummy import DummyClassifier

_model = DummyClassifier(strategy="most_frequent")
_model.fit([[0], [1], [2]], [0, 1, 1])

def predict(features):
    # features: list of lists
    return _model.predict(features).tolist()