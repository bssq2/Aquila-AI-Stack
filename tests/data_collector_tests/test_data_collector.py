import requests

BASE = "http://localhost:6000"

def test_health():
    r = requests.get(f"{BASE}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_collect():
    r = requests.get(f"{BASE}/collect")
    assert r.status_code == 200
    data = r.json()
    assert "foo" in data