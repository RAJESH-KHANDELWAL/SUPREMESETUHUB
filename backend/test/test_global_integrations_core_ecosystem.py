from backend.core.global_ecosystem.global_core_ecosystem.global_integrations_core_ecosystem import (
    GlobalIntegrationsCoreOrchestrator, GlobalIntegrationsCoreService,
    get_integration, get_integrations_catalog, get_provider_catalog,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_integrations_core_ecosystem.policy import redact_sensitive_metadata

def test_catalog_has_expected_domains_and_provider_metadata_only():
    assert len(get_integrations_catalog()) == 31
    assert all(x["live_connection_verified"] is False for x in get_integrations_catalog())
    assert all(x["live_connection_verified"] is False for x in get_provider_catalog())

def test_catalog_lookup_returns_independent_data():
    first = get_integrations_catalog()
    first[0]["display_name"] = "changed"
    assert get_integrations_catalog()[0]["display_name"] != "changed"
    assert get_integration("NOT-A-DOMAIN") is None

def test_age_restricted_domains_require_consent():
    for item in get_integrations_catalog():
        if item["age_restricted"]:
            assert item["consent_required"] is True

def test_metadata_redacts_credentials_and_personal_data():
    value = {"provider":"google","api_key":"do-not-return","nested":{"access_token":"x","region":"asia-south1"}}
    cleaned = redact_sensitive_metadata(value)
    assert "api_key" not in cleaned
    assert "access_token" not in cleaned["nested"]
    assert cleaned["nested"]["region"] == "asia-south1"

def test_service_and_orchestrator_are_read_only():
    service = GlobalIntegrationsCoreService()
    assert service.health()["success"] is True
    assert service.health()["live_connections_verified"] is False
    assert service.describe()["provider_execution_enabled"] is False
    assert GlobalIntegrationsCoreOrchestrator().health()["execution_enabled"] is False
