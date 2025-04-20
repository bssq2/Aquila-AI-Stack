from flask import Flask, request, jsonify
from classifier import train_model, predict_model

app = Flask(__name__)
model = train_model()  # "Train" once at startup

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ml_model running"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    """
    Expects JSON: {"features": [0.1, 0.2, 0.3]}
    """
    content = request.json
    if not content or "features" not in content:
        return jsonify({"error": "Missing features"}), 400
    features = content["features"]
    if len(features) != 3:
        return jsonify({"error": "Must have exactly 3 features"}), 400

    pred = predict_model(model, features)
    return jsonify({"prediction": int(pred)}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)