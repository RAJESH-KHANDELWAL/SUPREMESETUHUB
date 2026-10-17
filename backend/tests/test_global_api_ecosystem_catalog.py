from backend.api.global_api_ecosystem_catalog import (
    get_provider_ecosystem,
    list_ai_api_provider_ecosystems,
    list_ecosystems,
    list_provider_ecosystems,
)


def test_global_api_ecosystem_contains_provider_families():
    providers = {item["provider_id"]: item for item in list_provider_ecosystems()}
    assert {"google", "microsoft", "aws", "apple"} <= set(providers)
    assert providers["google"]["name"] == "GOOGLE API ECOSYSTEM"
    assert providers["microsoft"]["name"] == "MICROSOFT API ECOSYSTEM"
    assert providers["aws"]["name"] == "AWS API ECOSYSTEM"
    assert providers["apple"]["name"] == "APPLE API ECOSYSTEM"


def test_provider_catalog_does_not_claim_live_connections():
    for provider in list_provider_ecosystems():
        assert provider["live_connection_verified"] is False


def test_family_filter_and_ai_ecosystem_are_distinct():
    ai = list_provider_ecosystems("AI")
    assert ai
    assert all("AI" in item["families"] for item in ai)
    ai_ids = {item["provider_id"] for item in list_ai_api_provider_ecosystems()}
    assert {"openai", "google", "microsoft", "aws", "anthropic"} <= ai_ids
    assert "apple" not in ai_ids


def test_existing_global_api_ecosystem_modules_are_registered():
    ecosystems = list_ecosystems()
    names = {item["name"] for item in ecosystems}
    assert "GLOBAL AI API ECOSYSTEM" in names
    assert "GLOBAL CLOUD API ECOSYSTEM" in names
    assert "GLOBAL COMPANIES API ECOSYSTEM" in names
    assert len(ecosystems) >= 25


def test_unknown_provider_returns_none():
    assert get_provider_ecosystem("not-a-provider") is None
