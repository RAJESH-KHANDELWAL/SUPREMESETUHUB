"""Live provider verification must not expose or persist OAuth tokens."""
from backend.integration.provider.microsoft import MicrosoftProvider
from backend.integration.provider.salesforce import SalesforceProvider
from backend.integration.registry import IntegrationRegistry


class FakeResponse:
    def __init__(self, status_code, payload):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        return self._payload


class FakeClient:
    def __init__(self, *args, **kwargs):
        self.calls = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def post(self, url, data):
        self.calls.append(("POST", url))
        if "login.microsoftonline.com" in url:
            return FakeResponse(200, {"access_token": "do-not-return-this-token"})
        return FakeResponse(200, {
            "access_token": "do-not-return-this-token",
            "instance_url": "https://example.my.salesforce.com",
        })

    def get(self, url, headers):
        self.calls.append(("GET", url))
        if "graph.microsoft.com" in url:
            return FakeResponse(200, {"value": [{"id": "tenant-id", "displayName": "Example Tenant"}]})
        return FakeResponse(200, {"DailyApiRequests": {"Max": 100000, "Remaining": 99999}})


def test_microsoft_verification_requires_server_configuration(monkeypatch):
    for key in ("MICROSOFT_TENANT_ID", "MICROSOFT_CLIENT_ID", "MICROSOFT_CLIENT_SECRET"):
        monkeypatch.delenv(key, raising=False)
    result = MicrosoftProvider().verify_connection()
    assert result["status"] == "NEEDS_CONFIGURATION"
    assert result["live_connection_verified"] is False


def test_microsoft_live_verification_never_returns_token(monkeypatch):
    monkeypatch.setenv("MICROSOFT_TENANT_ID", "tenant-id")
    monkeypatch.setenv("MICROSOFT_CLIENT_ID", "client-id")
    monkeypatch.setenv("MICROSOFT_CLIENT_SECRET", "secret-value")
    monkeypatch.setattr("backend.integration.provider.microsoft.httpx.Client", FakeClient)
    result = MicrosoftProvider().verify_connection()
    assert result["success"] is True
    assert result["tenant_name"] == "Example Tenant"
    assert result["live_connection_verified"] is True
    assert "do-not-return-this-token" not in repr(result)


def test_salesforce_live_verification_never_returns_token(monkeypatch):
    monkeypatch.setenv("SALESFORCE_CLIENT_ID", "client-id")
    monkeypatch.setenv("SALESFORCE_CLIENT_SECRET", "secret-value")
    monkeypatch.setattr("backend.integration.provider.salesforce.httpx.Client", FakeClient)
    result = SalesforceProvider().verify_connection()
    assert result["success"] is True
    assert result["instance_host"] == "example.my.salesforce.com"
    assert result["live_connection_verified"] is True
    assert "do-not-return-this-token" not in repr(result)


def test_salesforce_provider_is_registered():
    registry = IntegrationRegistry()
    assert registry.get("SALESFORCE") is not None
    assert registry.get("SALESFORCE").metadata()["name"] == "SALESFORCE"
