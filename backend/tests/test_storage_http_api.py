from __future__ import annotations

from fastapi.testclient import TestClient


def test_storage_file_api_uploads_and_downloads_private_file(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_DB_PATH", str(tmp_path / "foundation.db"))
    monkeypatch.setenv("SUPREME_FILE_STORAGE_DIR", str(tmp_path / "files"))

    from backend.api import app as app_module
    from backend.api import storage_routes as storage_module

    app_module.app.dependency_overrides[storage_module.get_current_user] = lambda: {
        "authenticated": True,
        "username": "storage-test",
        "user_id": "USR_STORAGE_TEST",
        "role": "USER",
    }
    monkeypatch.setattr(
        app_module.authentication_service,
        "validate_token",
        lambda token: {"authenticated": True, "username": "storage-test", "session_id": "storage-session"},
    )

    try:
        with TestClient(app_module.app) as client:
            upload = client.post(
                "/api/v1/storage/files",
                headers={"Authorization": "Bearer test-token"},
                data={"area_id": "test-area"},
                files={"file": ("sample.txt", b"private file contents", "text/plain")},
            )
            assert upload.status_code == 201, upload.text
            result = upload.json()["data"]
            assert result["storage_backend"] == "LOCAL_FILESYSTEM"
            assert result["size_bytes"] == len(b"private file contents")

            download = client.get(
                result["download_endpoint"],
                headers={"Authorization": "Bearer test-token"},
            )
            assert download.status_code == 200
            assert download.content == b"private file contents"
            assert download.headers["content-disposition"].startswith("attachment;")
    finally:
        app_module.app.dependency_overrides.pop(storage_module.get_current_user, None)


def test_storage_file_api_requires_authentication():
    from backend.api.app import app

    with TestClient(app) as client:
        response = client.get("/api/v1/storage/health")

    assert response.status_code == 401
