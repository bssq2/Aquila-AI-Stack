#!/usr/bin/env sh
set -e

# ── launch the API in the background ────────────────────────────────────────────
uvicorn src.main:app --host 0.0.0.0 --port 6000 &

# ── then run whatever command the container receives (e.g.  pytest) ────────────
exec "$@"