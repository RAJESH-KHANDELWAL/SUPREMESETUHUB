from __future__ import annotations

from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient


def test_logout_revokes_only_authenticated_bearer_token(monkeypatch):
    from backend.api import auth as auth_module

    monkeypatch.setattr(
        auth_module.controller,
        "logout",
        lambda **kwargs: {"called": True, **kwargs},
    )

    result = auth_module.logout(
        auth_module.TokenRequest(token="session-token", session_id="session-1"),
        authorization="Bearer session-token",
        current_user={"username": "alice", "session_id": "session-1"},
    )

    assert result == {"called": True, "token": "session-token"}


def test_logout_rejects_different_session_id(monkeypatch):
    from backend.api import auth as auth_module

    monkeypatch.setattr(
        auth_module.controller,
        "logout",
        lambda **kwargs: pytest.fail("must not revoke a different session"),
    )

    with pytest.raises(HTTPException) as error:
        auth_module.logout(
            auth_module.TokenRequest(session_id="other-session"),
            authorization="Bearer caller-token",
            current_user={"username": "alice", "session_id": "callers-session"},
        )

    assert error.value.status_code == 403
    assert error.value.detail == "CANNOT_REVOKE_ANOTHER_SESSION"


def test_logout_rejects_body_token_different_from_bearer(monkeypatch):
    from backend.api import auth as auth_module

    monkeypatch.setattr(
        auth_module.controller,
        "logout",
        lambda **kwargs: pytest.fail("must not revoke a different session"),
    )

    with pytest.raises(HTTPException) as error:
        auth_module.logout(
            auth_module.TokenRequest(token="other-token"),
            authorization="Bearer caller-token",
            current_user={"username": "alice", "session_id": "callers-session"},
        )

    assert error.value.status_code == 403
    assert error.value.detail == "LOGOUT_TOKEN_MISMATCH"


def test_logout_rejects_missing_bearer_header():
    from backend.api import auth as auth_module

    with pytest.raises(HTTPException) as error:
        auth_module.logout(
            auth_module.TokenRequest(),
            authorization=None,
            current_user={"username": "alice", "session_id": "callers-session"},
        )

    assert error.value.status_code == 401
    assert error.value.detail == "BEARER_TOKEN_REQUIRED"


def test_master_id_only_authentication_is_rejected():
    from backend.api import auth as auth_module

    with pytest.raises(HTTPException) as error:
        auth_module.authenticate(auth_module.AuthenticateRequest(master_id="public-or-guessed-id"))

    assert error.value.status_code == 403
    assert error.value.detail == "MASTER_ID_ONLY_AUTHENTICATION_DISABLED_USE_PASSWORD_SIGNIN"


def test_logout_route_validates_bearer_and_revokes_that_token(monkeypatch):
    from backend.api import app as app_module
    from backend.api import auth as auth_module
    from backend.security import dependencies as security_dependencies

    username = app_module.SUPREME_OWNER_USERNAME
    monkeypatch.setattr(
        app_module.authentication_service,
        "validate_token",
        lambda token: {
            "authenticated": True,
            "username": username,
            "session_id": "integration-session",
        },
    )
    monkeypatch.setattr(
        security_dependencies._authentication_service,
        "validate_token",
        lambda token: {
            "authenticated": True,
            "username": username,
            "session_id": "integration-session",
        },
    )
    monkeypatch.setattr(
        security_dependencies._user_controller,
        "search",
        lambda requested_username: SimpleNamespace(
            username=username,
            user_id="integration-user",
            role="OWNER",
            status="ACTIVE",
        ),
    )
    monkeypatch.setattr(
        auth_module.controller,
        "logout",
        lambda **kwargs: {"success": True, **kwargs},
    )

    with TestClient(app_module.app) as client:
        response = client.post(
            app_module.app.url_path_for("logout"),
            headers={"Authorization": "Bearer integration-token"},
            json={"token": "integration-token", "session_id": "integration-session"},
        )

    assert response.status_code == 200
    assert response.json() == {"success": True, "token": "integration-token"}
