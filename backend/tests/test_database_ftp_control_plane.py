from __future__ import annotations

import pytest
from fastapi import HTTPException

from backend.api import infrastructure as api


class FakeDatabase:
    def __init__(self):
        self.closed = False

    def health(self):
        return {"success": True, "status": "HEALTHY", "database": "central-test"}

    def close(self):
        self.closed = True


def test_database_status_is_owner_gated_and_closes_connection(monkeypatch):
    database = FakeDatabase()
    monkeypatch.setattr(api, "require_wordpress_owner", lambda token: None)
    monkeypatch.setattr(api, "GDEDatabaseConnection", lambda: database)

    result = api.central_database_status("Bearer test-owner-token")

    assert result["status"] == "HEALTHY"
    assert database.closed is True


def test_database_status_rejects_unauthorized_request(monkeypatch):
    def reject(_token):
        raise HTTPException(status_code=401, detail="AUTHENTICATION_REQUIRED")

    monkeypatch.setattr(api, "require_wordpress_owner", reject)

    with pytest.raises(HTTPException) as error:
        api.central_database_status(None)

    assert error.value.status_code == 401


def test_ftp_profiles_returns_safe_readiness(monkeypatch):
    class FakeFtp:
        def list_profiles(self):
            return [{"profile_id": "supremesetuhub", "configured": True}]

    monkeypatch.setattr(api, "require_wordpress_owner", lambda token: None)
    monkeypatch.setattr(api, "FtpInfrastructureService", FakeFtp)

    result = api.ftp_profile_status("Bearer test-owner-token")

    assert result["success"] is True
    assert len(result["profiles"]) == 1
    assert result["credentials_returned"] is False
    assert result["mutations_performed"] is False


def test_ftp_check_is_owner_gated_and_read_only(monkeypatch):
    class FakeFtp:
        def check_profile(self, profile_id):
            return {
                "success": True,
                "profile_id": profile_id,
                "mutations_performed": False,
                "credentials_returned": False,
            }

    monkeypatch.setattr(api, "require_wordpress_owner", lambda token: None)
    monkeypatch.setattr(api, "FtpInfrastructureService", FakeFtp)

    result = api.check_ftp_profile("supremesetuhub", "Bearer test-owner-token")

    assert result["success"] is True
    assert result["mutations_performed"] is False
    assert result["credentials_returned"] is False


def test_ftp_check_returns_404_for_unknown_profile(monkeypatch):
    class FakeFtp:
        def check_profile(self, _profile_id):
            raise KeyError("unknown")

    monkeypatch.setattr(api, "require_wordpress_owner", lambda token: None)
    monkeypatch.setattr(api, "FtpInfrastructureService", FakeFtp)

    with pytest.raises(HTTPException) as error:
        api.check_ftp_profile("unknown", "Bearer test-owner-token")

    assert error.value.status_code == 404
