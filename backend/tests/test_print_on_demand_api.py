from __future__ import annotations

from fastapi.testclient import TestClient


def test_print_on_demand_catalog_requires_authentication():
    from backend.api.app import app

    with TestClient(app) as client:
        response = client.get("/api/v1/print-on-demand/catalog")

    assert response.status_code == 401


def test_print_on_demand_quote_route(monkeypatch):
    from backend.api import app as app_module
    from backend.api import print_on_demand as pod_module

    app_module.app.dependency_overrides[pod_module.get_current_user] = lambda: {"user_id": "USR_TEST", "role": "USER"}
    monkeypatch.setattr(
        app_module.authentication_service,
        "validate_token",
        lambda token: {"authenticated": True, "username": "pod-test", "session_id": "pod-session"},
    )
    monkeypatch.setattr(
        pod_module.controller,
        "quote",
        lambda **kwargs: {"product_sku": kwargs["product_sku"], "unit_price": 500, "total_price": 1000, "currency": "INR"},
    )
    with TestClient(app_module.app) as client:
        response = client.post(
            "/api/v1/print-on-demand/quote",
            headers={"Authorization": "Bearer pod-test-token"},
            json={"product_sku": "POD-TEE", "market": "IN", "tier": "STANDARD", "quantity": 2},
        )

    assert response.status_code == 200
    assert response.json()["data"]["total_price"] == 1000
