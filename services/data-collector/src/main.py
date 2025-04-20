from flask import Flask, jsonify
import os
from dummy_external import fetch_dummy_data

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "data_collector running"}), 200

@app.route("/collect", methods=["GET"])
def collect():
    try:
        data = fetch_dummy_data()
        return jsonify({
            "message": "Data collected",
            "data": data
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)