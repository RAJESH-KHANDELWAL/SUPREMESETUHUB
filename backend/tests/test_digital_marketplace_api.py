from __future__ import annotations

from fastapi.testclient import TestClient


def test_digital_marketplace_catalog_is_public_and_marks_checkout_disabled():
    from backend.api.app import app

    with TestClient(app) as client:
        response = client.get("/api/v1/digital-marketplace/catalog?market=IN")

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["product_model"] == "DIGITAL_DOWNLOADS_ONLY"
    assert data["checkout_status"] == "DISABLED_UNTIL_MERCHANT_APPROVAL_AND_PAYMENT_VERIFICATION"
    assert data["delivery_status"] == "PRIVATE_DOWNLOAD_DELIVERY_NOT_YET_IMPLEMENTED"


def test_digital_marketplace_catalog_rejects_unknown_market():
    from backend.api.app import app

    with TestClient(app) as client:
        response = client.get("/api/v1/digital-marketplace/catalog?market=EU")

    assert response.status_code == 422
