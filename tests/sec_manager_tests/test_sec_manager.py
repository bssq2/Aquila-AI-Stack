import requests

BASE = "http://localhost:9000"

def test_health():
    r = requests.get(f"{BASE}/health")
    assert r.json()["status"] == "ok"

def test_login_and_secure():
    r = requests.post(f"{BASE}/login", json={"username":"admin","password":"admin"})
    assert "token" in r.json()
    token = r.json()["token"]
    r2 = requests.get(f"{BASE}/secure-data", headers={"Authorization": f"Bearer {token}"})
    assert r2.status_code == 200
    assert r2.json()["secret"] == "42"