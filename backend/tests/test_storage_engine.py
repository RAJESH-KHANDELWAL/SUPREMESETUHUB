from __future__ import annotations

from backend.engines.storage import StorageEngine


def test_storage_engine_does_not_claim_physical_storage_is_connected(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_DB_PATH", str(tmp_path / "storage-engine.db"))
    engine = StorageEngine()

    connected = engine.connect()
    config = engine.configuration()
    health = engine.health()

    assert connected["connected"] is False
    assert connected["status"] == "METADATA_ONLY"
    assert config["storage_backend_configured"] is False
    assert config["storage_backend"] is None
    assert health["database_registry"] == "READY"
    assert health["physical_storage"] == "NOT_CONFIGURED"
    assert health["health"] == "DEGRADED"


def test_storage_engine_health_checks_registry_tables(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_DB_PATH", str(tmp_path / "storage-health.db"))
    engine = StorageEngine()

    assert engine.health()["database_registry"] == "READY"

    engine.database.execute("DROP TABLE ai_store_audit")

    health = engine.health()
    assert health["database_registry"] == "UNAVAILABLE"
    assert health["health"] == "UNHEALTHY"
