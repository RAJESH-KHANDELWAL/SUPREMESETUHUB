from types import SimpleNamespace

from fastapi.testclient import TestClient


def test_signup_route_is_public_and_accepts_matching_password_confirmation(monkeypatch):
    from backend.api import app as app_module
    from backend.api import users as users_module

    monkeypatch.setattr(
        users_module.controller,
        "signup",
        lambda **kwargs: SimpleNamespace(
            to_dict=lambda: {
                "user_id": "USR-TEST",
                "username": "USR_TEST",
                "full_name": kwargs["full_name"],
                "email": kwargs["email"],
            }
        ),
    )

    with TestClient(app_module.app) as client:
        response = client.post(
            "/users/signup",
            json={
                "full_name": "Test User",
                "email": "test@gmail.com",
                "password": "ExamplePassword123",
                "confirm_password": "ExamplePassword123",
            },
        )

    assert response.status_code == 201
    assert response.json()["data"]["username"] == "USR_TEST"
