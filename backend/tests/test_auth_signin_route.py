from __future__ import annotations

from fastapi.testclient import TestClient


def test_signin_route_returns_session_for_valid_password(monkeypatch):
    from backend.api import app as app_module
    from backend.api import auth as auth_module

    monkeypatch.setattr(
        auth_module.controller,
        "signin",
        lambda **kwargs: {
            "authenticated": True,
            "username": kwargs["username"],
            "token": "test-session-token",
            "session_id": "test-session-id",
        },
    )

    with TestClient(app_module.app) as client:
        response = client.post(
            "/auth/signin",
            json={"username": "new-user", "password": "correct-password"},
        )

    assert response.status_code == 200
    assert response.json()["authenticated"] is True
    assert response.json()["token"] == "test-session-token"


def test_signin_route_returns_401_for_invalid_password(monkeypatch):
    from backend.api import app as app_module
    from backend.api import auth as auth_module

    monkeypatch.setattr(
        auth_module.controller,
        "signin",
        lambda **kwargs: {
            "authenticated": False,
            "message": "Invalid username or password",
        },
    )

    with TestClient(app_module.app) as client:
        response = client.post(
            "/auth/signin",
            json={"username": "new-user", "password": "wrong-password"},
        )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"
    assert response.headers["www-authenticate"] == "Bearer"
