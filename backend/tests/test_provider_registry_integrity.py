from backend.integrations.registry import IntegrationRegistry
from backend.integrations.providers.apple import AppleProvider
from backend.integrations.providers.esa import ESAProvider
from backend.engines.integrations.registry import IntegrationRegistry as EngineIntegrationRegistry


def test_provider_registry_imports_and_contains_requested_ecosystems():
    registry = IntegrationRegistry()
    assert {"GOOGLE", "MICROSOFT", "AWS", "APPLE", "ESA"} <= set(registry.providers)


def test_apple_provider_is_implemented_and_does_not_claim_connection():
    provider = AppleProvider()
    assert provider.metadata()["name"] == "APPLE"
    assert provider.health()["connection"] == "NOT_CONNECTED"


def test_esa_provider_is_catalog_only_until_connected():
    provider = ESAProvider()
    metadata = provider.metadata()
    assert metadata["name"] == "ESA"
    assert metadata["integration_mode"] == "CATALOG_ONLY"
    assert provider.health()["connection"] == "NOT_CONNECTED"


def test_engine_registry_includes_esa_and_existing_major_providers():
    registry = EngineIntegrationRegistry()
    definitions = {item["provider"] for item in registry.list()}
    assert {"GOOGLE", "MICROSOFT", "AWS", "APPLE", "ESA"} <= definitions
