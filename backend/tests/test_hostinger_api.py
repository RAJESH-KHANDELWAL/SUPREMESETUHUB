from __future__ import annotations

from types import SimpleNamespace

import pytest

from backend.infrastructure import hostinger_api


def test_connection_status_reports_not_configured_without_token(monkeypatch):
    monkeypatch.delenv("HOSTINGER_API_TOKEN", raising=False)
    monkeypatch.delenv("HOSTINGER_API_KEY", raising=False)

    result = hostinger_api.connection_status()

    assert result["status"] == "NOT_CONFIGURED"
    assert result["live_api_test_performed"] is False
    assert result["secrets_returned"] is False


def test_connection_status_uses_official_read_only_websites_endpoint(monkeypatch):
    monkeypatch.setenv("HOSTINGER_API_TOKEN", "test-token")
    seen = {}

    def fake_get(url, **kwargs):
        seen["url"] = url
        seen["headers"] = kwargs["headers"]
        seen["params"] = kwargs["params"]
        return SimpleNamespace(status_code=200, json=lambda: {"data": []})

    monkeypatch.setattr(hostinger_api.httpx, "get", fake_get)

    result = hostinger_api.connection_status()

    assert result["status"] == "CONNECTED"
    assert result["live_api_test_performed"] is True
    assert result["secrets_returned"] is False
    assert seen["url"] == "https://developers.hostinger.com/api/hosting/v1/websites"
    assert seen["headers"]["Authorization"] == "Bearer test-token"
    assert seen["params"] == {"page": 1}


def test_invalid_token_error_does_not_return_response_body(monkeypatch):
    monkeypatch.setenv("HOSTINGER_API_TOKEN", "test-token")

    def fake_get(url, **kwargs):
        return SimpleNamespace(status_code=401, json=lambda: {"secret": "should-not-leak"})

    monkeypatch.setattr(hostinger_api.httpx, "get", fake_get)

    result = hostinger_api.connection_status()

    assert result["status"] == "CONNECTION_FAILED"
    assert result["error"] == "HOSTINGER_API_UNAUTHORIZED"
    assert "should-not-leak" not in str(result)


def test_vps_inventory_uses_read_only_endpoint(monkeypatch):
    monkeypatch.setenv("HOSTINGER_API_TOKEN", "test-token")
    seen = {}

    def fake_get(url, **kwargs):
        seen["url"] = url
        return SimpleNamespace(status_code=200, json=lambda: {"data": []})

    monkeypatch.setattr(hostinger_api.httpx, "get", fake_get)

    result = hostinger_api.list_vps_instances(page=2)

    assert result["success"] is True
    assert result["resource"] == "vps_instances"
    assert seen["url"] == "https://developers.hostinger.com/api/vps/v1/virtual-machines"
