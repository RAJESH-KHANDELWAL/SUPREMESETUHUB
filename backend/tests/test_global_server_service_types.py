from __future__ import annotations

import pytest

from backend.SERVER.GLOBAL_ECOSYSTEM.GLOBAL_SERVER_ECOSYSTEM import (
    EcosystemService,
    get_provider as get_canonical_provider,
    get_service_type as get_canonical_service_type,
    list_providers as list_canonical_providers,
    list_service_types as list_canonical_service_types,
)
from backend.server.global_ecosystem.global_server_ecosystem import (
    get_provider,
    get_service_type,
    list_providers,
    list_service_types,
)


EXPECTED_SERVICE_NAMES = {
    "VPN SERVER",
    "VPS SERVER",
    "CLOUD SERVER",
    "WEB SERVER",
    "CLOUD WEB SERVER",
}


def test_service_type_catalog_contains_requested_server_types():
    service_types = list_service_types()
    assert {item["name"] for item in service_types} == EXPECTED_SERVICE_NAMES
    assert all(item["status"] == "catalog_only" for item in service_types)


@pytest.mark.parametrize(
    ("service_type_id", "expected_name"),
    [
        ("VPN-SERVER", "VPN SERVER"),
        ("vps-server", "VPS SERVER"),
        ("CLOUD_SERVER", "CLOUD SERVER"),
        ("web-server", "WEB SERVER"),
        ("cloud-web-server", "CLOUD WEB SERVER"),
    ],
)
def test_get_service_type_accepts_stable_id_variants(service_type_id, expected_name):
    assert get_service_type(service_type_id)["name"] == expected_name


def test_unknown_service_type_raises_key_error():
    with pytest.raises(KeyError, match="Unknown server service type"):
        get_service_type("not-a-real-service")


def test_catalog_returns_independent_capability_lists():
    providers = list_providers()
    service_types = list_service_types()
    providers[0]["capabilities"].append("test-only")
    service_types[0]["capabilities"].append("test-only")

    assert "test-only" not in get_provider("hostinger")["capabilities"]
    assert "test-only" not in get_service_type("VPN-SERVER")["capabilities"]


def test_uppercase_canonical_and_lowercase_compatibility_paths_match():
    assert list_canonical_providers() == list_providers()
    assert list_canonical_service_types() == list_service_types()
    assert get_canonical_provider("hostinger") == get_provider("hostinger")
    assert get_canonical_service_type("VPN-SERVER") == get_service_type("VPN-SERVER")


def test_service_facade_reports_catalogs_without_live_connection_claims():
    description = EcosystemService().describe()
    assert description["ecosystem"] == "GLOBAL_SERVER_ECOSYSTEM"
    assert {item["name"] for item in description["service_types"]} == EXPECTED_SERVICE_NAMES
    assert description["live_connections_enabled"] is False
