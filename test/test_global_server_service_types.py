from __future__ import annotations
import pytest
from backend.server.global_ecosystem.global_server_ecosystem import (
    EcosystemService, get_provider, get_service_type, list_providers, list_service_types,
)
EXPECTED_SERVICE_NAMES = {"VPN SERVER", "VPS SERVER", "CLOUD SERVER", "WEB SERVER", "CLOUD WEB SERVER"}
def test_service_type_catalog_contains_requested_server_types():
    service_types = list_service_types()
    assert {item["name"] for item in service_types} == EXPECTED_SERVICE_NAMES
    assert all(item["status"] == "catalog_only" for item in service_types)
@pytest.mark.parametrize(("service_type_id", "expected_name"), [
    ("VPN-SERVER", "VPN SERVER"), ("vps-server", "VPS SERVER"),
    ("CLOUD_SERVER", "CLOUD SERVER"), ("web-server", "WEB SERVER"),
    ("cloud-web-server", "CLOUD WEB SERVER"),
])
def test_get_service_type_accepts_stable_id_variants(service_type_id, expected_name):
    assert get_service_type(service_type_id)["name"] == expected_name
def test_unknown_service_type_raises_key_error():
    with pytest.raises(KeyError, match="Unknown server service type"):
        get_service_type("not-a-real-service")
def test_catalog_returns_independent_capability_lists():
    providers, service_types = list_providers(), list_service_types()
    providers[0]["capabilities"].append("test-only")
    service_types[0]["capabilities"].append("test-only")
    assert "test-only" not in get_provider("hostinger")["capabilities"]
    assert "test-only" not in get_service_type("VPN-SERVER")["capabilities"]
def test_service_facade_reports_catalogs_without_live_connection_claims():
    description = EcosystemService().describe()
    assert description["ecosystem"] == "GLOBAL_SERVER_ECOSYSTEM"
    assert {item["name"] for item in description["service_types"]} == EXPECTED_SERVICE_NAMES
    assert description["live_connections_enabled"] is False
