from backend.integration.registry import IntegrationRegistry
from backend.integration.provider.apple import AppleProvider
from backend.integration.provider.bada_business import BadaBusinessProvider
from backend.integration.provider.esa import ESAProvider
from backend.engine.integrations.registry import IntegrationRegistry as EngineIntegrationRegistry


def test_provider_registry_imports_and_contains_requested_ecosystems():
    registry = IntegrationRegistry()
    assert {"BADA_BUSINESS", "GOOGLE", "MICROSOFT", "AWS", "APPLE", "ESA", "SALESFORCE"} <= set(registry.providers)


def test_apple_provider_is_implemented_and_does_not_claim_connection():
    provider = AppleProvider()
    assert provider.metadata()["name"] == "APPLE"
    assert provider.health()["connection"] == "NOT_TESTED"


def test_esa_provider_is_catalog_only_until_connected():
    provider = ESAProvider()
    metadata = provider.metadata()
    assert metadata["name"] == "ESA"
    assert metadata["integration_mode"] == "CATALOG_ONLY"
    assert provider.health()["connection"] == "NOT_CONNECTED"


def test_engine_registry_includes_esa_and_existing_major_providers():
    registry = EngineIntegrationRegistry()
    definitions = {item["provider"] for item in registry.list()}
    assert {"GOOGLE", "MICROSOFT", "AWS", "APPLE", "ESA", "SALESFORCE"} <= definitions


def test_bada_business_provider_exposes_catalog_without_claiming_live_connection():
    provider = BadaBusinessProvider()
    metadata = provider.metadata()
    health = provider.health()
    assert metadata["name"] == "BADA_BUSINESS"
    assert metadata["catalog_status"] == "RESOURCE_CATALOG_ONLY"
    assert metadata["official_public_api_verified"] is False
    assert metadata["link_count"] == 9
    assert metadata["program_count"] == 3
    link_ids = {item["id"] for item in metadata["resource_catalog"]["links"]}
    assert {
        "nice_analysis",
        "business_breakthrough_seminar",
        "idea_to_ipo",
        "lfp_digital",
        "bb_coach",
        "digital_daily_event",
        "cash_growth_profit",
        "business_tales",
        "digital_dukan",
    } <= link_ids
    assert health["status"] == "CATALOG_AVAILABLE"
    assert health["connection"] == "NOT_CONNECTED"
    assert health["live_connection_verified"] is False
