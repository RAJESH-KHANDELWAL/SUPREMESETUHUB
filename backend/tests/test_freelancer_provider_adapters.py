import pytest

from backend.engines.freelancer_ecosystem.provider_adapters import (
    AppleSignInAdapter,
    GoogleDriveAdapter,
    MicrosoftOneDriveAdapter,
    ProviderConfigurationError,
)


def test_google_drive_authorization_url_uses_configured_client(monkeypatch):
    monkeypatch.setenv("GOOGLE_CLIENT_ID", "test-google-client")
    url = GoogleDriveAdapter.authorization_url(
        "opaque-csrf-state",
        "https://example.test/oauth/google/callback",
    )
    assert url.startswith("https://accounts.google.com/o/oauth2/v2/auth?")
    assert "test-google-client" in url
    assert "opaque-csrf-state" in url
    assert "drive.file" in url


def test_microsoft_authorization_url_uses_configured_tenant(monkeypatch):
    monkeypatch.setenv("MICROSOFT_CLIENT_ID", "test-ms-client")
    monkeypatch.setenv("MICROSOFT_TENANT_ID", "organizations")
    url = MicrosoftOneDriveAdapter.authorization_url(
        "opaque-csrf-state",
        "https://example.test/oauth/microsoft/callback",
    )
    assert "login.microsoftonline.com/organizations/" in url
    assert "test-ms-client" in url
    assert "Files.ReadWrite" in url


def test_google_drive_file_listing_calls_real_api_with_bounded_page(monkeypatch):
    class FakeResponse:
        is_error = False

        @staticmethod
        def json():
            return {"files": [{"id": "drive-file-1", "name": "portfolio.pdf"}]}

    def fake_get(url, *, headers, params, timeout):
        assert url == "https://www.googleapis.com/drive/v3/files"
        assert headers["Authorization"] == "Bearer transient-test-token"
        assert params["pageSize"] == 100
        assert timeout == 15.0
        return FakeResponse()

    monkeypatch.setattr("backend.engines.freelancer_ecosystem.provider_adapters.httpx.get", fake_get)
    result = GoogleDriveAdapter.list_files("transient-test-token", page_size=500)
    assert result["files"][0]["name"] == "portfolio.pdf"


def test_apple_identity_validation_requires_token(monkeypatch):
    monkeypatch.setenv("APPLE_CLIENT_ID", "com.example.app")
    with pytest.raises(ValueError, match="APPLE_IDENTITY_TOKEN_REQUIRED"):
        AppleSignInAdapter.verify_identity_token("")


def test_provider_configuration_errors_name_missing_setting_not_secret(monkeypatch):
    monkeypatch.delenv("GOOGLE_CLIENT_ID", raising=False)
    with pytest.raises(ProviderConfigurationError, match="CONFIGURATION_REQUIRED:GOOGLE_CLIENT_ID"):
        GoogleDriveAdapter.authorization_url("state", "https://example.test/callback")
