FROM python:3.9-slim

WORKDIR /app

# ---- dependencies -----------------------------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- application ------------------------------------------------------------
COPY src/ ./src

# ---- entry‑point so the API & tests can share the same container ------------
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 6000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "6000"]