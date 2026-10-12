from __future__ import annotations

import sqlite3

import pytest

from backend.engines.database import DatabaseEngine


def test_connect_enables_foreign_keys_and_supports_in_memory_database():
    engine = DatabaseEngine("sqlite:///:memory:")
    try:
        status = engine.connect()
        assert status["connected"] is True
        assert engine.connection is not None
        assert engine.connection.execute("PRAGMA foreign_keys").fetchone()[0] == 1
        engine.execute("CREATE TABLE parent (id INTEGER PRIMARY KEY)")
        engine.execute(
            "CREATE TABLE child (parent_id INTEGER REFERENCES parent(id))"
        )
        with pytest.raises(sqlite3.IntegrityError):
            engine.execute("INSERT INTO child (parent_id) VALUES (999)")
    finally:
        engine.disconnect()


def test_fetch_methods_and_ping_work_for_sqlite(tmp_path):
    engine = DatabaseEngine(f"sqlite:///{tmp_path / 'engine.db'}")
    try:
        assert engine.ping()["reachable"] is True
        engine.execute("CREATE TABLE sample (id INTEGER PRIMARY KEY, name TEXT)")
        engine.execute("INSERT INTO sample (name) VALUES (?)", ("Rajesh",))
        assert engine.fetch_one("SELECT name FROM sample WHERE id = ?", (1,)) == {
            "name": "Rajesh"
        }
        assert engine.fetch_all("SELECT name FROM sample") == [{"name": "Rajesh"}]
        assert engine.health()["health"] == "HEALTHY"
    finally:
        engine.disconnect()


def test_unsupported_driver_is_reported_truthfully_and_url_is_redacted():
    engine = DatabaseEngine("postgresql://admin:supersecret@db.example.test/app?token=private")
    config = engine.configuration()
    assert config["supported"] is False
    assert config["driver"] == "UNSUPPORTED"
    assert config["requested_driver"] == "POSTGRESQL"
    assert "supersecret" not in config["database_url"]
    assert "private" not in config["database_url"]
    assert engine.ping()["reachable"] is False
    with pytest.raises(NotImplementedError):
        engine.connect()


def test_disconnect_is_idempotent(tmp_path):
    engine = DatabaseEngine(f"sqlite:///{tmp_path / 'disconnect.db'}")
    engine.connect()
    assert engine.disconnect()["connected"] is False
    assert engine.disconnect()["connected"] is False
