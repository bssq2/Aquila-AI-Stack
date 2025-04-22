import os
from flask import Flask, request, jsonify
from classifier import predict

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/predict", methods=["POST"])
def do_predict():
    payload = request.get_json() or {}
    features = payload.get("features", [])
    preds = predict(features)
    return jsonify(predictions=preds)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))
    app.run(host="0.0.0.0", port=port)