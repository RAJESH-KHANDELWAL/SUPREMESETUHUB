from __future__ import annotations

from fastapi.testclient import TestClient


def test_public_print_on_demand_catalog_is_read_only_and_unauthenticated():
    from backend.api.app import app

    with TestClient(app) as client:
        response = client.get("/api/v1/print-on-demand/public/catalog?market=IN")

    assert response.status_code == 200
    payload = response.json()
    assert payload["success"] is True
    data = payload["data"]
    assert data["market"] == "IN"
    assert data["currency"] == "INR"
    assert len(data["products"]) >= 1
    assert data["trend_data_status"] == "EDITORIAL_STARTERS_NOT_LIVE_TREND_DATA"
    assert "estimate" in data["pricing_notice"].lower()
