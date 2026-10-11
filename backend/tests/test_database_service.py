from __future__ import annotations

from backend.database.controller import DatabaseController
from backend.database.service import DatabaseService


def test_service_executes_parameterized_queries(tmp_path):
    service = DatabaseService(str(tmp_path / "test.db"))
    try:
        service.execute(
            "CREATE TABLE sample (id INTEGER PRIMARY KEY, label TEXT NOT NULL)"
        )
        service.execute(
            "INSERT INTO sample (label) VALUES (?)",
            ("alpha",),
        )
        row = service.fetchone("SELECT label FROM sample WHERE id = ?", (1,))
        assert row is not None
        assert row["label"] == "alpha"
        assert service.health()["healthy"] is True
    finally:
        service.close()


def test_executemany_and_explicit_rollback(tmp_path):
    service = DatabaseService(str(tmp_path / "transaction.db"))
    try:
        service.execute("CREATE TABLE sample (label TEXT NOT NULL)")
        service.executemany(
            "INSERT INTO sample (label) VALUES (?)",
            [("one",), ("two",)],
        )
        assert len(service.fetchall("SELECT label FROM sample")) == 2

        service.begin()
        service.execute("INSERT INTO sample (label) VALUES (?)", ("temporary",))
        assert service.status()["transaction_active"] is True
        service.rollback()

        rows = service.fetchall("SELECT label FROM sample ORDER BY label")
        assert [row["label"] for row in rows] == ["one", "two"]
        assert service.status()["transaction_active"] is False
    finally:
        service.close()


def test_controller_lifecycle_and_status(tmp_path):
    controller = DatabaseController(DatabaseService(str(tmp_path / "controller.db")))
    connected = controller.connect()
    assert connected["connected"] is True

    result = controller.execute(
        "CREATE TABLE sample (id INTEGER PRIMARY KEY, label TEXT NOT NULL)"
    )
    assert result == -1

    inserted = controller.execute(
        "INSERT INTO sample (label) VALUES (?)",
        ("controller",),
    )
    assert inserted == 1
    assert controller.health()["healthy"] is True

    disconnected = controller.disconnect()
    assert disconnected["connected"] is False
