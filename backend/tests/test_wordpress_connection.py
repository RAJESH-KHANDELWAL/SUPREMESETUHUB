from __future__ import annotations

import pytest

from backend.wordpress.connection import (
    WordPressConnectionConfig,
    WordPressDatabaseConnection,
)


def set_db_env(monkeypatch, prefix="WORDPRESS"):
    monkeypatch.setenv(f"{prefix}_DB_HOST", "mysql.example.test")
    monkeypatch.setenv(f"{prefix}_DB_NAME", "wordpress_db")
    monkeypatch.setenv(f"{prefix}_DB_USER", "wordpress_reader")
    monkeypatch.setenv(f"{prefix}_DB_PASSWORD", "test-password")
    monkeypatch.setenv(f"{prefix}_DB_PORT", "3306")
    monkeypatch.setenv(f"{prefix}_TABLE_PREFIX", "wp_")


def test_config_reads_private_environment_without_changing_password(monkeypatch):
    set_db_env(monkeypatch)
    monkeypatch.setenv("WORDPRESS_DB_PASSWORD", " password with spaces ")

    config = WordPressConnectionConfig.from_environment(
        "rajeshkhandelwalofficial",
        "rajeshkhandelwalofficial.com",
        "WORDPRESS",
    )

    assert config.database_host == "mysql.example.test"
    assert config.database_name == "wordpress_db"
    assert config.database_password == " password with spaces "
    assert config.table_prefix == "wp_"
    assert config.ssl_enabled is True


def test_config_rejects_unknown_environment_prefix(monkeypatch):
    set_db_env(monkeypatch)
    with pytest.raises(ValueError, match="WORDPRESS_ENVIRONMENT_PREFIX_NOT_ALLOWED"):
        WordPressConnectionConfig.from_environment(
            "unknown", "example.test", "UNTRUSTED_PREFIX"
        )


def test_config_rejects_invalid_table_prefix(monkeypatch):
    set_db_env(monkeypatch)
    monkeypatch.setenv("WORDPRESS_TABLE_PREFIX", "wp_; DROP TABLE users;--")

    with pytest.raises(ValueError, match="TABLE_PREFIX_INVALID"):
        WordPressConnectionConfig.from_environment(
            "rajeshkhandelwalofficial",
            "rajeshkhandelwalofficial.com",
            "WORDPRESS",
        )


def test_config_reports_missing_environment_names_only(monkeypatch):
    for name in (
        "WORDPRESS_DB_HOST",
        "WORDPRESS_DB_NAME",
        "WORDPRESS_DB_USER",
        "WORDPRESS_DB_PASSWORD",
    ):
        monkeypatch.delenv(name, raising=False)

    with pytest.raises(RuntimeError, match="WORDPRESS_DB_HOST"):
        WordPressConnectionConfig.from_environment(
            "rajeshkhandelwalofficial",
            "rajeshkhandelwalofficial.com",
            "WORDPRESS",
        )


class FakeCursor:
    def __init__(self):
        self.last_query = ""
        self.last_params = None
        self.closed = False

    def execute(self, query, params=None):
        self.last_query = query
        self.last_params = params

    def fetchone(self):
        if "information_schema.tables" in self.last_query:
            return (1,)
        return (1,)

    def close(self):
        self.closed = True


class FakeConnection:
    def __init__(self):
        self.cursor_instance = FakeCursor()
        self.closed = False

    def is_connected(self):
        return not self.closed

    def ping(self, reconnect=False, attempts=1, delay=0):
        return None

    def cursor(self):
        return self.cursor_instance

    def close(self):
        self.closed = True


def test_health_uses_safe_select_and_closes_cursor(monkeypatch):
    set_db_env(monkeypatch)
    config = WordPressConnectionConfig.from_environment(
        "rajeshkhandelwalofficial",
        "rajeshkhandelwalofficial.com",
        "WORDPRESS",
    )
    connection = WordPressDatabaseConnection(config)
    fake = FakeConnection()
    monkeypatch.setattr(
        "backend.wordpress.connection.mysql.connector.connect",
        lambda **kwargs: fake,
    )

    result = connection.health()

    assert result["success"] is True
    assert result["status"] == "CONNECTED"
    assert fake.cursor_instance.last_query == "SELECT 1"
    assert fake.cursor_instance.closed is True


def test_table_check_uses_parameterized_schema_queries(monkeypatch):
    set_db_env(monkeypatch)
    config = WordPressConnectionConfig.from_environment(
        "rajeshkhandelwalofficial",
        "rajeshkhandelwalofficial.com",
        "WORDPRESS",
    )
    connection = WordPressDatabaseConnection(config)
    fake = FakeConnection()
    monkeypatch.setattr(
        "backend.wordpress.connection.mysql.connector.connect",
        lambda **kwargs: fake,
    )

    result = connection.check_wordpress_tables()

    assert result["success"] is True
    assert result["found_tables"] == [
        "wp_options", "wp_posts", "wp_users", "wp_usermeta"
    ]
    assert "%s" in fake.cursor_instance.last_query
    assert fake.cursor_instance.last_params == ("wordpress_db", "wp_usermeta")
    assert fake.cursor_instance.closed is True


def test_connection_failure_does_not_leak_driver_error(monkeypatch):
    set_db_env(monkeypatch)
    config = WordPressConnectionConfig.from_environment(
        "rajeshkhandelwalofficial",
        "rajeshkhandelwalofficial.com",
        "WORDPRESS",
    )
    connection = WordPressDatabaseConnection(config)

    def fail_connect(**kwargs):
        raise RuntimeError("secret host and password should not appear")

    monkeypatch.setattr(
        "backend.wordpress.connection.mysql.connector.connect",
        fail_connect,
    )

    result = connection.health()
    assert result["success"] is False
    assert result["status"] == "CONNECTION_FAILED"
    assert "error_type" in result
    assert "password" not in str(result).lower()
    assert "secret host" not in str(result).lower()
