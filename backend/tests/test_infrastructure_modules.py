from __future__ import annotations

from backend.infrastructure.backup.service import BackupService
from backend.infrastructure.security.service import SecurityService
from backend.infrastructure.storage.service import StorageService


def test_storage_metadata_crud(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_DB_PATH", str(tmp_path / "storage.db"))
    service = StorageService()
    record = service.create(
        name="Test object store",
        storage_type="OBJECT",
        provider="LOCAL_TEST",
        capacity_gb=10,
        used_gb=2,
    )
    assert record.storage_id.startswith("STG-")
    loaded = service.get(record.storage_id)
    assert loaded is not None
    assert loaded.name == "Test object store"
    assert loaded.used_gb == 2
    assert service.delete(record.storage_id) is True
    assert service.get(record.storage_id) is None


def test_security_metadata_crud(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_DB_PATH", str(tmp_path / "security.db"))
    service = SecurityService()
    record = service.create(
        name="Test policy record",
        security_type="ACCESS_POLICY",
        enabled=True,
    )
    assert record.security_id.startswith("SEC-")
    loaded = service.get(record.security_id)
    assert loaded is not None
    assert loaded.enabled is True
    updated = service.update_enabled(record.security_id, False)
    assert updated is not None
    assert updated.enabled is False


def test_backup_metadata_crud(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_DB_PATH", str(tmp_path / "backup.db"))
    service = BackupService()
    record = service.create(
        name="Test backup record",
        backup_type="DATABASE",
        source_type="SQLITE",
        status="PLANNED",
    )
    assert record.backup_id.startswith("BKP-")
    loaded = service.get(record.backup_id)
    assert loaded is not None
    assert loaded.name == "Test backup record"
    assert loaded.encrypted is True


def test_core_api_service_reports_module_readiness():
    from backend.api.service import APIService

    service = APIService()
    initialized = service.initialize()
    assert initialized["transport"] == "FastAPI"
    assert initialized["private_routes"] == "AUTHENTICATION_REQUIRED"
    assert service.health()["healthy"] is True
