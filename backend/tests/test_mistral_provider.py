"""Mistral provider configuration and live verification tests."""
from backend.integration.provider.mistral import MistralProvider
from backend.integration.registry import IntegrationRegistry

class FakeResponse:
    status_code = 200
    def raise_for_status(self): return None
    def json(self): return {"data": [{"id": "mistral-small-latest"}, {"id": "mistral-large-latest"}]}

class FakeClient:
    def __init__(self, *args, **kwargs): self.calls = []
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def get(self, url, headers):
        self.calls.append((url, headers))
        return FakeResponse()

def test_mistral_health_requires_server_side_key(monkeypatch):
    monkeypatch.delenv("MISTRAL_API_KEY", raising=False)
    result = MistralProvider().health()
    assert result["status"] == "NEEDS_CONFIGURATION"
    assert result["live_connection_verified"] is False

def test_mistral_verify_without_key_does_not_make_request(monkeypatch):
    monkeypatch.delenv("MISTRAL_API_KEY", raising=False)
    result = MistralProvider().verify_connection()
    assert result["status"] == "NEEDS_CONFIGURATION"
    assert result["live_connection_verified"] is False

def test_mistral_live_verification_lists_models_without_returning_key(monkeypatch):
    monkeypatch.setenv("MISTRAL_API_KEY", "test-secret-key")
    monkeypatch.setattr("backend.integration.provider.mistral.httpx.Client", FakeClient)
    result = MistralProvider().verify_connection()
    assert result["success"] is True
    assert result["status"] == "CONNECTED"
    assert result["available_model_count"] == 2
    assert result["live_connection_verified"] is True
    assert "test-secret-key" not in repr(result)

def test_mistral_provider_is_registered():
    provider = IntegrationRegistry().get("MISTRAL")
    assert provider is not None
    assert provider.metadata()["provider_id"] == "mistral"

def test_mistral_service_family_catalog_has_nine_entries():
    from backend.api.global_ecosystem.global_api_ecosystem.mistral_api_ecosystem.mistral_api_ecosystem import PROVIDER_API_ECOSYSTEM
    assert PROVIDER_API_ECOSYSTEM["service_family_count"] == 9
