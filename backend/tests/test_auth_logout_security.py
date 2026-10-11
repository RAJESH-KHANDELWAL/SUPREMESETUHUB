from __future__ import annotations

import pytest
from fastapi import HTTPException


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
