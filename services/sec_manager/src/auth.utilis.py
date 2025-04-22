import os
import jwt
from datetime import datetime, timedelta

_SECRET = os.environ.get("JWT_SECRET", "supersecret")

def make_token(username):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, _SECRET, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, _SECRET, algorithms=["HS256"])
    except Exception:
        return None