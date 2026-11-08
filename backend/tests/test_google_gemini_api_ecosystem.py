from types import SimpleNamespace

import pytest

from backend.api.global_ecosystem.global_api_ecosystem.google_api_ecosystem.google_gemini_api_ecosystem.google_gemini_api_ecosystem import (
    GeminiConfigurationError,
    GoogleGeminiAPIService,
)


def test_gemini_connection_requires_a_key(monkeypatch):
    monkeypatch.delenv("GOOGLE_GEMINI_API_KEY", raising=False)
    with pytest.raises(GeminiConfigurationError, match="GEMINI_API_KEY_REQUIRED"):
        GoogleGeminiAPIService().test_connection()


def test_gemini_connection_does_not_return_or_persist_user_key(monkeypatch):
    class Models:
        def list(self):
            return [object(), object()]

    class Client:
        models = Models()

    monkeypatch.setattr(
        GoogleGeminiAPIService,
        "_client",
        staticmethod(lambda api_key=None: Client()),
    )
    result = GoogleGeminiAPIService().test_connection(api_key="do-not-leak")
    assert result["success"] is True
    assert result["connection_verified"] is True
    assert result["credential_persisted"] is False
    assert result["credential_source"] == "user_supplied"
    assert "do-not-leak" not in repr(result)


def test_gemini_generation_requires_prompt_and_model():
    service = GoogleGeminiAPIService(model="")
    with pytest.raises(ValueError, match="PROMPT_REQUIRED"):
        service.generate_content(" ")
    with pytest.raises(GeminiConfigurationError, match="GEMINI_MODEL_REQUIRED"):
        service.generate_content("Hello", api_key="test-key")


def test_gemini_generation_uses_explicit_model_and_prompt(monkeypatch):
    class Models:
        def generate_content(self, *, model, contents):
            assert model == "test-model"
            assert contents == "Hello"
            return SimpleNamespace(text="Hello back")

    class Client:
        models = Models()

    monkeypatch.setattr(
        GoogleGeminiAPIService,
        "_client",
        staticmethod(lambda api_key=None: Client()),
    )
    result = GoogleGeminiAPIService(model="test-model").generate_content(
        "Hello", api_key="test-key"
    )
    assert result["success"] is True
    assert result["text"] == "Hello back"
    assert result["model"] == "test-model"


def test_core_google_gemini_connection_respects_layer_boundary():
    from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
    result = GlobalEcosystemManager().test_google_gemini_connection(api_key="ephemeral-test-key")
    assert result["success"] is False
    assert result["status"] == "NOT_IMPLEMENTED_IN_CORE"
    assert result["credential_persisted"] is False
    assert result["error"] == "CORE_API_LAYER_ISOLATION"
    assert "ephemeral-test-key" not in repr(result)
