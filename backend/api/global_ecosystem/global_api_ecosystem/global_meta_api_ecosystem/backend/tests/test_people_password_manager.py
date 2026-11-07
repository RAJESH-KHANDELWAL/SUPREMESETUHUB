"""Security tests for the people password manager API."""
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api import people_password_manager as pm


@pytest.fixture
def client(tmp_path, monkeypatch):
    from backend.database.service import DatabaseService

    monkeypatch.setattr(pm, "_db", DatabaseService(str(tmp_path / "people-vaults.db")))
    app = FastAPI()
    app.include_router(pm.router)
    app.dependency_overrides[pm.get_current_user] = lambda: {
        "authenticated": True,
        "user_id": "user-a",
        "username": "user-a",
        "role": "USER",
        "status": "ACTIVE",
    }
    return TestClient(app)


def valid_envelope():
    return {
        "format": "SUPREME-ENCRYPTED-VAULT",
        "version": 1,
        "kdf": "PBKDF2-SHA256-600000",
        "cipher": "AES-256-GCM",
        "salt": "c2FsdA==",
        "iv": "aXY=",
        "ciphertext": "ZW5jcnlwdGVkLWRhdGE=",
    }


def test_status_and_platform_catalog_are_available_to_signed_in_user(client):
    assert client.get("/api/v1/people-password-manager/status").status_code == 200
    catalog = client.get("/api/v1/people-password-manager/platforms").json()["platforms"]
    assert {item["id"] for item in catalog} >= {
        "linksetu", "websetu", "codesetu", "linkhub", "webhub",
        "codehub", "webpress", "codepress", "linkpress",
    }


def test_vault_saves_only_encrypted_envelope(client):
    response = client.put(
        "/api/v1/people-password-manager/vault",
        json={"envelope": valid_envelope()},
    )
    assert response.status_code == 200
    assert response.json()["server_can_decrypt"] is False
    saved = client.get("/api/v1/people-password-manager/vault").json()
    assert saved["exists"] is True
    assert saved["envelope"]["ciphertext"] == "ZW5jcnlwdGVkLWRhdGE="


def test_plaintext_or_unknown_envelope_fields_are_rejected(client):
    envelope = valid_envelope()
    envelope["entries"] = [{"username": "someone", "password": "plaintext"}]
    response = client.put(
        "/api/v1/people-password-manager/vault",
        json={"envelope": envelope},
    )
    assert response.status_code == 422


def test_wrong_cipher_is_rejected(client):
    envelope = valid_envelope()
    envelope["cipher"] = "PLAINTEXT"
    response = client.put(
        "/api/v1/people-password-manager/vault",
        json={"envelope": envelope},
    )
    assert response.status_code == 422


def test_delete_removes_the_current_users_vault(client):
    client.put("/api/v1/people-password-manager/vault", json={"envelope": valid_envelope()})
    response = client.delete("/api/v1/people-password-manager/vault")
    assert response.status_code == 200
    assert client.get("/api/v1/people-password-manager/vault").json()["exists"] is False
