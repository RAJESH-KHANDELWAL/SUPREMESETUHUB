from __future__ import annotations

from fastapi.testclient import TestClient


def test_digital_marketplace_catalog_is_public_and_marks_checkout_disabled():
    from backend.api.app import app

    with TestClient(app) as client:
        response = client.get("/api/v1/digital-marketplace/catalog?market=IN")

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["product_model"] == "FLEXIBLE_DIGITAL_ASSETS_ONLY"
    assert data["checkout_status"] == "DISABLED_UNTIL_PAYMENT_PROVIDER_AND_SIGNED_WEBHOOKS_ARE_CONFIGURED"
    assert data["delivery_status"] == "PRIVATE_PAID_DOWNLOAD_FLOW_NOT_YET_ENABLED"


def test_digital_marketplace_catalog_rejects_unknown_market():
    from backend.api.app import app

    with TestClient(app) as client:
        response = client.get("/api/v1/digital-marketplace/catalog?market=EU")

    assert response.status_code == 422
