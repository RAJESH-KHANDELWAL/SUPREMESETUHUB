from backend.api.dashboard import get_dashboard_metrics
from backend.database.service import DatabaseService


def test_dashboard_metrics_count_real_rows_and_report_source(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "dashboard.db"))
    database.execute("CREATE TABLE users (user_id TEXT PRIMARY KEY)")
    database.execute("INSERT INTO users (user_id) VALUES (?)", ("user-1",))
    database.execute("CREATE TABLE supreme_people (person_id TEXT PRIMARY KEY)")
    database.execute(
        "INSERT INTO supreme_people (person_id) VALUES (?)", ("person-1",)
    )
    database.execute("CREATE TABLE businesses (business_id TEXT PRIMARY KEY)")
    database.execute(
        "INSERT INTO businesses (business_id) VALUES (?)", ("business-1",)
    )

    metrics = get_dashboard_metrics(database)

    assert metrics["users"] == {
        "count": 1,
        "table": "users",
        "available": True,
    }
    assert metrics["people"] == {
        "count": 1,
        "table": "supreme_people",
        "available": True,
    }
    assert metrics["businesses"] == {
        "count": 1,
        "table": "businesses",
        "available": True,
    }
    assert metrics["projects"] == {
        "count": None,
        "table": None,
        "available": False,
    }
    database.close()


def test_dashboard_metrics_report_zero_only_for_existing_empty_tables(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "empty-dashboard.db"))
    database.execute("CREATE TABLE users (user_id TEXT PRIMARY KEY)")
    database.execute("CREATE TABLE supreme_people (person_id TEXT PRIMARY KEY)")

    metrics = get_dashboard_metrics(database)

    assert metrics["users"]["count"] == 0
    assert metrics["users"]["available"] is True
    assert metrics["people"]["count"] == 0
    assert metrics["people"]["available"] is True
    assert metrics["commissions"]["count"] is None
    assert metrics["commissions"]["available"] is False
    database.close()


def test_dashboard_metrics_do_not_create_missing_tables(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "no-tables.db"))

    metrics = get_dashboard_metrics(database)

    assert all(item["available"] is False for item in metrics.values())
    assert database.table_exists("users") is False
    assert database.table_exists("supreme_people") is False
    database.close()
