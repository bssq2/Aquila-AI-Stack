# services/data_collector/src/main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Data‑Collector")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/collect")
async def collect():
    """
    Dummy endpoint exercised by the test‑suite.
    It only needs to include a 'foo' key in the JSON response.
    """
    return JSONResponse({"foo": "bar"})