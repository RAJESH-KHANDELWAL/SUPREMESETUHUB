import io
import os
import time
import zipfile

from fastapi import FastAPI\nfrom fastapi.testclient import TestClient\n\nfrom backend.api.supreme_updates import router\n\napp = FastAPI()\napp.include_router(router)\n

def _zip_package(main_file: str) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        archive.writestr(main_file, "<?php // test plugin")
    return output.getvalue()


def test_update_server_health_reports_missing_configuration(monkeypatch, tmp_path):
    monkeypatch.setenv("SUPREME_UPDATE_STORAGE_DIR", str(tmp_path))
    monkeypatch.delenv("SUPREME_UPDATE_ADMIN_TOKEN", raising=False)
    monkeypatch.delenv("SUPREME_UPDATE_SIGNING_SECRET", raising=False)
    with TestClient(app) as client:
        response = client.get("/api/v1/supreme-updates/health")
    assert response.status_code == 200
    assert response.json()["status"] == "configuration_required"


def test_publish_requires_admin_token(monkeypatch, tmp_path):
    monkeypatch.setenv("SUPREME_UPDATE_STORAGE_DIR", str(tmp_path))
    monkeypatch.setenv("SUPREME_UPDATE_ADMIN_TOKEN", "test-admin-token")\n    monkeypatch.setenv("SUPREME_UPDATE_STORAGE_DURABILITY_ACKNOWLEDGED", "true")
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/supreme-updates/admin/publish/supremesetuhub",
            data={"version": "1.3.7"},
            files={"package": ("supremesetuhub.zip", _zip_package("supremesetuhub/supremesetuhub.php"), "application/zip")},
        )
    assert response.status_code == 401


def test_publish_and_check_update(monkeypatch, tmp_path):
    monkeypatch.setenv("SUPREME_UPDATE_STORAGE_DIR", str(tmp_path))
    monkeypatch.setenv("SUPREME_UPDATE_ADMIN_TOKEN", "test-admin-token")
    monkeypatch.setenv("SUPREME_UPDATE_SIGNING_SECRET", "x" * 48)\n    monkeypatch.setenv("SUPREME_UPDATE_STORAGE_DURABILITY_ACKNOWLEDGED", "true")
    with TestClient(app) as client:
        published = client.post(
            "/api/v1/supreme-updates/admin/publish/supremesetuhub",
            headers={"Authorization": "Bearer test-admin-token"},
            data={"version": "1.3.8", "notes": "Security and update improvements"},
            files={"package": ("supremesetuhub.zip", _zip_package("supremesetuhub/supremesetuhub.php"), "application/zip")},
        )
        assert published.status_code == 200, published.text
        assert len(published.json()["sha256"]) == 64

        check = client.get(
            "/api/v1/supreme-updates/check/supremesetuhub",
            params={"installed_version": "1.3.6"},
        )
        assert check.status_code == 200
        data = check.json()
        assert data["update_available"] is True
        assert data["latest_version"] == "1.3.8"
        assert data["sha256"] == published.json()["sha256"]

        download = client.get(data["package"])
        assert download.status_code == 200
        assert download.content.startswith(b"PK")

        expired = client.get(
            "/api/v1/supreme-updates/download/supremesetuhub/1.3.8",
            params={"expires": int(time.time()) - 1, "token": "invalid"},
        )
        assert expired.status_code == 403


def test_publish_rejects_wrong_plugin_archive(monkeypatch, tmp_path):
    monkeypatch.setenv("SUPREME_UPDATE_STORAGE_DIR", str(tmp_path))
    monkeypatch.setenv("SUPREME_UPDATE_ADMIN_TOKEN", "test-admin-token")
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/supreme-updates/admin/publish/supremesetuhub",
            headers={"Authorization": "Bearer test-admin-token"},
            data={"version": "1.3.8"},
            files={"package": ("wrong.zip", _zip_package("other-plugin/main.php"), "application/zip")},
        )
    assert response.status_code == 422
