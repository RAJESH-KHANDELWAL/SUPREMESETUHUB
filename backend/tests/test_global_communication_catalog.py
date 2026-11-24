"""Contract tests for the read-only Global Communication catalog."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api.global_ecosystem.global_api_ecosystem.global_communication_api_ecosystem import router
from backend.api.global_ecosystem.global_api_ecosystem.global_communication_api_ecosystem.service import (
    get_category,
    list_categories,
)

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_status_is_fail_closed():
    response = client.get("/global-communication/status")
    assert response.status_code == 200
    body = response.json()
    assert body["connected_provider_count"] == 0
    assert body["live_messaging_enabled"] is False
    assert body["provider_count"] == len(body["integrations"])
    assert all(provider["integration_status"] == "not_configured" for provider in body["integrations"])
    assert body["safety_controls"]["adult_access_default"] == "disabled"


def test_categories_include_core_and_restricted_adult_metadata():
    response = client.get("/global-communication/categories")
    assert response.status_code == 200
    categories = response.json()
    assert len(categories) >= 10
    ids = {category["category_id"] for category in categories}
    assert {"messaging", "email", "sms", "video_meetings", "adult_platform_directory", "age_verification_safety"} <= ids


def test_adult_categories_require_safety_controls():
    adult = get_category("adult_platform_directory")
    assert adult is not None
    assert adult["tier"] == "restricted_adult"
    assert "strict_age_verification" in adult["compliance_controls"]
    assert "consent_only" in adult["compliance_controls"]


def test_categories_filter_and_404():
    restricted = client.get("/global-communication/categories", params={"tier": "restricted_adult"})
    assert restricted.status_code == 200
    assert restricted.json()
    assert all(category["tier"] == "restricted_adult" for category in restricted.json())
    assert client.get("/global-communication/categories/missing_category").status_code == 404


def test_catalog_results_are_defensive_copies():
    items = list_categories()
    items[0]["providers"].clear()
    assert list_categories()[0]["providers"]
