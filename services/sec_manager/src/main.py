import os
from flask import Flask, request, jsonify
from auth_utils import make_token
from middleware import require_auth

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/login", methods=["POST"])
def login():
    creds = request.get_json() or {}
    if creds.get("username") == "admin" and creds.get("password") == "admin":
        token = make_token("admin")
        return jsonify(token=token)
    return jsonify(error="Bad credentials"), 401

@app.route("/secure-data")
def secure():
    auth_resp = require_auth()
    if auth_resp:
        return auth_resp  # middleware found a problem
    return jsonify(secret="42")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9000))
    app.run(host="0.0.0.0", port=port)