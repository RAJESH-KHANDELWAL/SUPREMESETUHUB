"""Tests for the global relationship and intimacy catalog routes."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api.global_ecosystem.global_api_ecosystem.global_intimacy_api_ecosystem.routes import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_status_is_catalog_only():
    response = client.get("/api/v1/global-intimacy-ecosystem/status")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["catalog_only"] is True
    assert body["live_connections_verified"] is False
    assert body["category_count"] >= 8


def test_categories_include_relationship_and_adult_business_scopes():
    response = client.get("/api/v1/global-intimacy-ecosystem/categories")
    assert response.status_code == 200
    ids = {item["category_id"] for item in response.json()}
    assert "RELATIONSHIPS" in ids
    assert "INTIMACY_WELLNESS" in ids
    assert "ADULT_INDUSTRY_BUSINESS" in ids
    assert "ADULT_CONTENT_HOSTING" in ids
    assert "CONSENT_AND_SAFETY" in ids


def test_provider_category_filter():
    response = client.get(
        "/api/v1/global-intimacy-ecosystem/providers",
        params={"category_id": "adult_content_hosting"},
    )
    assert response.status_code == 200
    assert all("ADULT_CONTENT_HOSTING" in item["category_ids"] for item in response.json())


def test_unknown_category_returns_404():
    response = client.get(
        "/api/v1/global-intimacy-ecosystem/providers",
        params={"category_id": "NOT_A_CATEGORY"},
    )
    assert response.status_code == 404
