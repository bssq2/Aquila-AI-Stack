from flask import request, jsonify
from auth_utils import verify_token

def require_auth():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify(error="Missing token"), 401
    token = auth.split(" ", 1)[1]
    payload = verify_token(token)
    if not payload:
        return jsonify(error="Invalid token"), 401