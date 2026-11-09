"""Bada Business catalog integration tests."""
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api.bada_business_integration import router
from backend.integration.connector.bada_business import BadaBusinessConnector
from backend.integration.connector.registry import connector_registry
from backend.integration.provider.bada_business import BadaBusinessProvider


def test_bada_business_connector_exposes_canonical_catalog():
    connector = BadaBusinessConnector()
    catalog = connector.catalog()
    assert catalog["link_count"] == 9
    assert catalog["program_count"] == 3
    assert connector.link("digital_dukan")["id"] == "digital_dukan"
    assert connector.program("lfp_digital") is not None
    assert connector.status()["status"] == "CATALOG_ONLY"
    assert connector.status()["connection"] == "NOT_CONNECTED"


def test_bada_business_connector_catalog_is_defensive_copy():
    connector = BadaBusinessConnector()
    catalog = connector.catalog()
    catalog["links"][0]["name"] = "MUTATED"
    assert connector.catalog()["links"][0]["name"] != "MUTATED"


def test_bada_business_connector_search():
    connector = BadaBusinessConnector()
    assert connector.search_links("dukan")[0]["id"] == "digital_dukan"
    assert connector.search_programs("impact")[0]["program_id"] == "bb_impact"


def test_bada_business_is_registered_as_catalog_connector():
    connector = connector_registry.get("bada_business")
    assert connector.display_name == "Bada Business"
    assert connector.handler is None
    assert connector.public_info()["status"] == "CATALOG_ONLY"


def test_bada_business_provider_and_connector_do_not_claim_live_api():
    provider = BadaBusinessProvider()
    assert provider.metadata()["link_count"] == 9
    assert provider.metadata()["program_count"] == 3
    assert provider.health()["connection"] == "NOT_CONNECTED"
    assert provider.health()["live_connection_verified"] is False


def test_bada_business_catalog_api_routes():
    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    status = client.get("/api/v1/bada-business-integration/status")
    assert status.status_code == 200
    assert status.json()["status"] == "CATALOG_ONLY"

    catalog = client.get("/api/v1/bada-business-integration/catalog")
    assert catalog.status_code == 200
    assert catalog.json()["link_count"] == 9
    assert catalog.json()["program_count"] == 3

    link = client.get("/api/v1/bada-business-integration/links/digital_dukan")
    assert link.status_code == 200
    assert link.json()["link"]["id"] == "digital_dukan"

    searched = client.get("/api/v1/bada-business-integration/links?q=dukan")
    assert searched.status_code == 200
    assert searched.json()["count"] == 1

    program = client.get("/api/v1/bada-business-integration/programs?q=impact")
    assert program.status_code == 200
    assert program.json()["count"] == 1

    missing = client.get("/api/v1/bada-business-integration/programs/not-real")
    assert missing.status_code == 404
