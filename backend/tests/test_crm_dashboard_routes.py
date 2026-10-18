from fastapi.testclient import TestClient

from backend.api.app import app


def test_supreme_dashboard_static_assets_load_before_sign_in():
    client = TestClient(app)
    paths = [
        "/api/v1/frontend/supreme-dashboard/",
        "/api/v1/frontend/supreme-dashboard/index.html",
        "/api/v1/frontend/supreme-dashboard/signin.html",
        "/api/v1/frontend/supreme-dashboard/signin.js",
        "/api/v1/frontend/supreme-dashboard/crm.html",
        "/api/v1/frontend/supreme-dashboard/crm.css",
        "/api/v1/frontend/supreme-dashboard/crm.js",
    ]

    for path in paths:
        response = client.get(path)
        assert response.status_code == 200, (
            f"{path} should load without an existing session; "
            f"received {response.status_code}: {response.text[:200]}"
        )


def test_crm_api_rejects_requests_without_a_bearer_session():
    client = TestClient(app)

    response = client.get("/api/v1/crm/status")

    assert response.status_code == 401
    assert response.json()["detail"] == "AUTHENTICATION_REQUIRED"
