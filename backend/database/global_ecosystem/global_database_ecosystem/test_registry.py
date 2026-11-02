"""Tests for provider registry metadata; tests do not require network credentials."""

from .registry import GlobalDatabaseEcosystemRegistry


def test_registry_lists_expected_provider_ecosystems():
    providers = GlobalDatabaseEcosystemRegistry.list_providers()
    ids = {provider["provider_id"] for provider in providers}
    assert ids == {"google", "aws", "microsoft", "proton", "mega"}
    assert all(provider["connection_status"] == "not_configured" for provider in providers)


def test_registry_returns_provider_by_id():
    provider = GlobalDatabaseEcosystemRegistry.get_provider("google")
    assert provider.describe()["provider_id"] == "google"


def test_registry_rejects_unknown_provider():
    try:
        GlobalDatabaseEcosystemRegistry.get_provider("unknown")
    except KeyError:
        pass
    else:
        raise AssertionError("Unknown providers must raise KeyError")
