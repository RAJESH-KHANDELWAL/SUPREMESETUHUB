from __future__ import annotations

import asyncio

import pytest
from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import Response


def _request(path: str, token: str = "test-token") -> Request:
    return Request(
        {
            "type": "http",
            "asgi": {"version": "3.0"},
            "http_version": "1.1",
            "method": "GET",
            "scheme": "http",
            "path": path,
            "raw_path": path.encode("utf-8"),
            "query_string": b"",
            "headers": [(b"authorization", f"Bearer {token}".encode("utf-8"))],
            "client": ("testclient", 123),
            "server": ("testserver", 80),
        }
    )


def test_private_ecosystem_routes_are_not_public_platform_entry_points():
    from backend.api.app import PUBLIC_API_PATHS
    assert "/users/register" in PUBLIC_API_PATHS
    assert "/auth/signin" in PUBLIC_API_PATHS
    assert "/identity/register" not in PUBLIC_API_PATHS
    assert "/api/v1/supreme-ecosystem/auth/signup" not in PUBLIC_API_PATHS
    assert "/api/v1/supreme-ecosystem/auth/signin" not in PUBLIC_API_PATHS


def test_non_owner_cannot_access_private_ecosystem(monkeypatch):
    from backend.api import app as app_module
    monkeypatch.setattr(app_module.authentication_service, "validate_token", lambda token: {"authenticated": True, "username": "REGULAR_CUSTOMER"})
    async def call_next(_request):
        return Response("allowed", status_code=200)
    response = asyncio.run(app_module.private_by_default(_request("/api/v1/supreme-ecosystem/dashboard"), call_next))
    assert response.status_code == 403


def test_owner_can_access_private_ecosystem(monkeypatch):
    from backend.api import app as app_module
    monkeypatch.setattr(app_module.authentication_service, "validate_token", lambda token: {"authenticated": True, "username": app_module.SUPREME_OWNER_USERNAME})
    async def call_next(_request):
        return Response("allowed", status_code=200)
    response = asyncio.run(app_module.private_by_default(_request("/api/v1/supreme-ecosystem/dashboard"), call_next))
    assert response.status_code == 200


def _business(owner_id="user-1", business_id="BUS-000001"):
    from types import SimpleNamespace
    return SimpleNamespace(business_id=business_id, owner_id=owner_id, status="ACTIVE", verified=False, to_dict=lambda: {"business_id": business_id, "owner_id": owner_id, "status": "ACTIVE", "verified": False})


def test_business_create_uses_authenticated_owner_and_safe_defaults(monkeypatch):
    from backend.api import businesses as api
    captured = {}
    monkeypatch.setattr(api.controller, "list", lambda: [])
    monkeypatch.setattr(api.controller, "create", lambda **kwargs: (captured.update(kwargs) or _business()))
    result = api.create_business(api.BusinessCreateRequest(name="Example"), current_user={"user_id": "user-1", "role": "USER"})
    assert result["data"]["owner_id"] == "user-1"
    assert captured["status"] == "ACTIVE"
    assert captured["verified"] is False


def test_user_cannot_read_another_users_business(monkeypatch):
    from backend.api import businesses as api
    monkeypatch.setattr(api.controller, "get", lambda _id: _business("user-2"))
    with pytest.raises(HTTPException) as error:
        api.get_business("BUS-000001", current_user={"user_id": "user-1", "role": "USER"})
    assert error.value.status_code == 404


def test_user_cannot_change_another_users_business_status(monkeypatch):
    from backend.api import businesses as api
    monkeypatch.setattr(api.controller, "get", lambda _id: _business("user-2"))
    with pytest.raises(HTTPException) as error:
        api.update_business_status("BUS-000001", api.BusinessStatusRequest(status="INACTIVE"), current_user={"user_id": "user-1", "role": "USER"})
    assert error.value.status_code == 404


def test_non_admin_cannot_verify_business(monkeypatch):
    from backend.api import businesses as api
    monkeypatch.setattr(api.controller, "verify", lambda _id: _business())
    with pytest.raises(HTTPException) as error:
        api.verify_business("BUS-000001", current_user={"user_id": "user-1", "role": "USER"})
    assert error.value.status_code == 403


def test_regular_owner_cannot_set_privileged_status(monkeypatch):
    from backend.api import businesses as api
    monkeypatch.setattr(api.controller, "get", lambda _id: _business("user-1"))
    with pytest.raises(HTTPException) as error:
        api.update_business_status("BUS-000001", api.BusinessStatusRequest(status="VERIFIED"), current_user={"user_id": "user-1", "role": "USER"})
    assert error.value.status_code == 403


def test_business_list_is_filtered_to_authenticated_owner(monkeypatch):
    from backend.api import businesses as api
    monkeypatch.setattr(api.controller, "list", lambda: [_business("user-1"), _business("user-2", "BUS-000002")])
    result = api.get_businesses(current_user={"user_id": "user-1", "role": "USER"})
    assert result["count"] == 1
    assert [item["owner_id"] for item in result["data"]] == ["user-1"]
