from backend.api.global_ecosystem.global_api_ecosystem.openai_api_ecosystem.openai_api_ecosystem import (
    OPENAI_API_ECOSYSTEM,
    get_openai_api_ecosystem,
    list_openai_api_ecosystems,
)


def test_openai_provider_identity_and_canonical_path():
    assert OPENAI_API_ECOSYSTEM["provider_id"] == "openai"
    assert OPENAI_API_ECOSYSTEM["name"] == "OPENAI API ECOSYSTEM"
    assert OPENAI_API_ECOSYSTEM["folder"].endswith("/openai_api_ecosystem")


def test_openai_capability_catalog_has_seventeen_entries():
    result = list_openai_api_ecosystems()
    assert result["success"] is True
    assert result["live_connection_verified"] is False
    assert result["count"] == 17
    assert len(result["ecosystems"]) == 17


def test_catalog_does_not_claim_production_connection_features():
    result = get_openai_api_ecosystem()
    boundary = result["implementation_boundary"]
    assert boundary["catalog_complete"] is True
    assert boundary["connection_ui_implemented"] is False
    assert boundary["authenticated_connection_routes_implemented"] is False
    assert boundary["encrypted_per_user_secret_storage_implemented"] is False
    assert result["live_connection_verified"] is False


def test_catalog_returns_defensive_child_copies():
    first = list_openai_api_ecosystems()
    first["ecosystems"][0]["name"] = "MUTATED"
    second = list_openai_api_ecosystems()
    assert second["ecosystems"][0]["name"] != "MUTATED"
