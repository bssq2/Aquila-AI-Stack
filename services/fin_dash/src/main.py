import os
from flask import Flask
from app import app as dash_app

server = Flask(__name__)
server.wsgi_app = dash_app.server

@server.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    server.run(host="0.0.0.0", port=port)