import os
from flask import Flask, jsonify
from dummy_external import fetch_dummy

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/collect")
def collect():
    data = fetch_dummy()
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)