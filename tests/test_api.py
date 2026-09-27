
from fastapi.testclient import TestClient
from app.main import app


def test_health():
    with TestClient(app) as client:
        response = client.get("/health")

        assert response.status_code == 200
        assert response.json()["status"] == "running"


def test_foundation():
    with TestClient(app) as client:
        response = client.get("/api/v1/foundation")

        assert response.status_code == 200

        data = response.json()

        assert data["name"] == "SUPREMESETUHUB MAIN BASE FOUNDATION"
        assert data["version"] == "1.0.0"
        assert data["status"] == "active"
