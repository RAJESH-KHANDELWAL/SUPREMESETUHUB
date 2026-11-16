from backend.integration.provider.meta import MetaProvider


def test_meta_provider_is_registered_and_reports_capabilities():
    from backend.integration.registry import IntegrationRegistry

    registry = IntegrationRegistry()
    provider = registry.get("META")

    assert isinstance(provider, MetaProvider)
    assert "META_GRAPH_API" in provider.metadata()["capabilities"]
    assert "META_WHATSAPP_BUSINESS" in provider.metadata()["capabilities"]


def test_meta_health_requires_server_side_oauth_configuration(monkeypatch):
    for key in ("META_APP_ID", "META_APP_SECRET", "META_REDIRECT_URI"):
        monkeypatch.delenv(key, raising=False)

    health = MetaProvider().health()
    assert health["status"] == "NEEDS_CONFIGURATION"
    assert health["live_connection_verified"] is False
    assert set(health["missing_configuration"]) == {
        "META_APP_ID",
        "META_APP_SECRET",
        "META_REDIRECT_URI",
    }


def test_meta_health_never_claims_live_connection(monkeypatch):
    monkeypatch.setenv("META_APP_ID", "test-app-id")
    monkeypatch.setenv("META_APP_SECRET", "test-app-secret")
    monkeypatch.setenv("META_REDIRECT_URI", "https://example.invalid/meta/callback")

    health = MetaProvider().health()
    assert health["status"] == "CONFIGURED_NOT_VERIFIED"
    assert health["connection"] == "NOT_TESTED"
    assert health["live_connection_verified"] is False
    assert "test-app-secret" not in str(health)
