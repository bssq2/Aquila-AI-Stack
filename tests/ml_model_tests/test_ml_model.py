import requests

BASE = "http://localhost:7000"

def test_health():
    r = requests.get(f"{BASE}/health")
    assert r.json()["status"] == "ok"

def test_predict():
    r = requests.post(f"{BASE}/predict", json={"features": [[0], [1]]})
    assert r.status_code == 200
    assert isinstance(r.json().get("predictions"), list)