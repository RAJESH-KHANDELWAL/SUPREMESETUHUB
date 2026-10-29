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
    assert body["category_count"] >= 30
    assert body["provider_count"] >= 25
    assert body["integration_count"] >= 20
    assert body["service_count"] >= 20
    assert body["tool_count"] >= 15


def test_categories_include_relationship_and_adult_business_scopes():
    response = client.get("/api/v1/global-intimacy-ecosystem/categories")
    assert response.status_code == 200
    ids = {item["category_id"] for item in response.json()}
    assert "RELATIONSHIPS" in ids
    assert "INTIMACY_WELLNESS" in ids
    assert "ADULT_INDUSTRY_BUSINESS" in ids
    assert "ADULT_CONTENT_HOSTING" in ids
    assert "CONSENT_AND_SAFETY" in ids
    assert "PORNOGRAPHY_VIDEO_PLATFORMS" in ids
    assert "ADULT_LIVE_STREAMING" in ids
    assert "ADULT_STUDIOS_PRODUCTION" in ids
    assert "EROTIC_AUDIO" in ids
    assert "EROTIC_LITERATURE" in ids
    assert "ADULT_PAYMENTS_PAYOUTS" in ids
    assert "CONTENT_MODERATION" in ids


def test_provider_category_filter():
    response = client.get(
        "/api/v1/global-intimacy-ecosystem/providers",
        params={"category_id": "adult_content_hosting"},
    )
    assert response.status_code == 200
    assert response.json()
    assert all("ADULT_CONTENT_HOSTING" in item["category_ids"] for item in response.json())


def test_unknown_category_returns_404():
    response = client.get(
        "/api/v1/global-intimacy-ecosystem/providers",
        params={"category_id": "NOT_A_CATEGORY"},
    )
    assert response.status_code == 404


def test_subsystem_catalogs_are_registered_and_catalog_only():
    integrations = client.get("/api/v1/global-intimacy-ecosystem/integrations/catalog")
    services = client.get("/api/v1/global-intimacy-ecosystem/services/catalog")
    tools = client.get("/api/v1/global-intimacy-ecosystem/tools/catalog")

    assert integrations.status_code == 200
    assert services.status_code == 200
    assert tools.status_code == 200

    assert len(integrations.json()) >= 20
    assert len(services.json()) >= 20
    assert len(tools.json()) >= 15

    assert all(item["implementation_status"] == "CATALOG_ONLY" for item in integrations.json())
    assert all(item["implementation_status"] == "CATALOG_ONLY" for item in services.json())
    assert all(item["implementation_status"] == "CATALOG_ONLY" for item in tools.json())


def test_subsystem_catalogs_filter_by_category():
    response = client.get(
        "/api/v1/global-intimacy-ecosystem/integrations/catalog",
        params={"category_id": "ADULT_CONTENT_HOSTING"},
    )
    assert response.status_code == 200
    assert response.json()
    assert all("ADULT_CONTENT_HOSTING" in item["category_ids"] for item in response.json())


def test_adult_provider_catalog_includes_research_leads_without_claiming_live_api():
    response = client.get("/api/v1/global-intimacy-ecosystem/providers")
    assert response.status_code == 200
    records = response.json()
    ids = {record["provider_id"] for record in records}
    assert "onlyfans" in ids
    assert "fansly" in ids
    assert "xvideos" in ids
    assert "cloudflare" in ids
    assert all(record["implementation_status"] == "CATALOG_ONLY" for record in records)
    assert all(record["live_connection_verified"] is False for record in records)
