from __future__ import annotations

import asyncio

import pytest
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

    monkeypatch.setattr(
        app_module.authentication_service,
        "validate_token",
        lambda token: {
            "authenticated": True,
            "username": "REGULAR_CUSTOMER",
        },
    )

    async def call_next(_request):
        return Response("allowed", status_code=200)

    response = asyncio.run(
        app_module.private_by_default(
            _request("/api/v1/supreme-ecosystem/dashboard"),
            call_next,
        )
    )
    assert response.status_code == 403


def test_owner_can_access_private_ecosystem(monkeypatch):
    from backend.api import app as app_module

    monkeypatch.setattr(
        app_module.authentication_service,
        "validate_token",
        lambda token: {
            "authenticated": True,
            "username": app_module.SUPREME_OWNER_USERNAME,
        },
    )

    async def call_next(_request):
        return Response("allowed", status_code=200)

    response = asyncio.run(
        app_module.private_by_default(
            _request("/api/v1/supreme-ecosystem/dashboard"),
            call_next,
        )
    )
    assert response.status_code == 200
