from fastapi.testclient import TestClient

from crypto_pipeline.health_api import app, TOKEN


def test_health_default():
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_health_with_token(monkeypatch):
    import crypto_pipeline.health_api as health_api
    monkeypatch.setattr(health_api, "TOKEN", "secret")
    client = TestClient(health_api.app)
    resp = client.get("/health", headers={"Authorization": "Bearer secret"})
    assert resp.status_code == 200
    resp = client.get("/health", headers={"Authorization": "Bearer wrong"})
    assert resp.status_code == 401
