"""Readiness reporting must be truthful and never expose credentials."""
from backend.integrations.providers.google import GoogleProvider
from backend.integrations.providers.microsoft import MicrosoftProvider
from backend.integrations.providers.aws import AWSProvider
from backend.integrations.providers.apple import AppleProvider


def _clear_provider_env(monkeypatch):
    for key in (
        "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REDIRECT_URI",
        "MICROSOFT_CLIENT_ID", "MICROSOFT_CLIENT_SECRET", "MICROSOFT_TENANT_ID", "MICROSOFT_REDIRECT_URI",
        "AWS_REGION", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_ROLE_ARN", "AWS_WEB_IDENTITY_TOKEN_FILE",
        "APPLE_SERVICES_ID", "APPLE_TEAM_ID", "APPLE_KEY_ID", "APPLE_PRIVATE_KEY", "APPLE_REDIRECT_URI",
        "APPLE_ISSUER_ID", "APPLE_APP_STORE_KEY_ID", "APPLE_APP_STORE_PRIVATE_KEY",
    ):
        monkeypatch.delenv(key, raising=False)


def test_all_providers_are_explicitly_unconfigured_without_secrets(monkeypatch):
    _clear_provider_env(monkeypatch)
    for provider in (GoogleProvider(), MicrosoftProvider(), AWSProvider(), AppleProvider()):
        health = provider.health()
        assert health["status"] == "NEEDS_CONFIGURATION"
        assert health["authentication"] == "NOT_CONFIGURED"
        assert health["connection"] == "NOT_TESTED"
        assert health["live_connection_verified"] is False


def test_google_configuration_does_not_claim_live_connection(monkeypatch):
    _clear_provider_env(monkeypatch)
    monkeypatch.setenv("GOOGLE_CLIENT_ID", "test-client-id")
    monkeypatch.setenv("GOOGLE_CLIENT_SECRET", "test-secret")
    monkeypatch.setenv("GOOGLE_REDIRECT_URI", "https://example.test/oauth/google/callback")
    health = GoogleProvider().health()
    assert health["status"] == "CONFIGURED_NOT_VERIFIED"
    assert health["authentication"] == "CONFIGURED"
    assert health["connection"] == "NOT_TESTED"
    assert "test-secret" not in repr(health)


def test_aws_role_configuration_is_supported(monkeypatch):
    _clear_provider_env(monkeypatch)
    monkeypatch.setenv("AWS_REGION", "ap-south-1")
    monkeypatch.setenv("AWS_ROLE_ARN", "arn:aws:iam::123456789012:role/example")
    monkeypatch.setenv("AWS_WEB_IDENTITY_TOKEN_FILE", "/var/run/secrets/token")
    health = AWSProvider().health()
    assert health["status"] == "CONFIGURED_NOT_VERIFIED"
    assert health["missing_configuration"] == []


def test_apple_app_store_credentials_are_separate_from_sign_in(monkeypatch):
    _clear_provider_env(monkeypatch)
    monkeypatch.setenv("APPLE_ISSUER_ID", "issuer")
    monkeypatch.setenv("APPLE_APP_STORE_KEY_ID", "key-id")
    monkeypatch.setenv("APPLE_APP_STORE_PRIVATE_KEY", "private-key-placeholder")
    health = AppleProvider().health()
    assert health["status"] == "CONFIGURED_NOT_VERIFIED"
    assert health["missing_configuration"] == []
    assert "private-key-placeholder" not in repr(health)
