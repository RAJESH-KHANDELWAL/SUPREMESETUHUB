"""Compatibility tests for the central SUPREMESETUHUB database config."""
import pytest

from backend.database.gde_connection import GDEDatabaseConfig, SupremeDatabaseConfig


def test_legacy_gde_name_is_alias_for_central_config():
    assert GDEDatabaseConfig is SupremeDatabaseConfig


def test_config_loads_only_central_environment(monkeypatch):
    monkeypatch.setenv("SUPREMESETUHUB_DB_HOST", "db.example.test")
    monkeypatch.setenv("SUPREMESETUHUB_DB_NAME", "supreme_main")
    monkeypatch.setenv("SUPREMESETUHUB_DB_USER", "supreme_user")
    monkeypatch.setenv("SUPREMESETUHUB_DB_PASSWORD", "not-a-real-password")
    monkeypatch.setenv("SUPREMESETUHUB_DB_SSL_REQUIRED", "false")
    monkeypatch.setenv("GDE_DB_HOST", "ignored.example.test")
    monkeypatch.setenv("GDE_DB_NAME", "legacy_gde_db")
    monkeypatch.setenv("GDE_DB_USER", "legacy_gde_user")
    monkeypatch.setenv("GDE_DB_PASSWORD", "ignored-password")

    config = GDEDatabaseConfig.from_environment()
    config.validate()

    assert config.host == "db.example.test"
    assert config.database == "supreme_main"
    assert config.username == "supreme_user"


def test_config_rejects_wordpress_database(monkeypatch):
    monkeypatch.setenv("WORDPRESS_DB_NAME", "wordpress_db")
    config = SupremeDatabaseConfig(
        host="db.example.test",
        database="wordpress_db",
        username="supreme_user",
        password="secret",
    )
    with pytest.raises(ValueError, match="primary WordPress database"):
        config.validate()


def test_config_requires_central_credentials(monkeypatch):
    for key in ("SUPREMESETUHUB_DB_HOST", "SUPREMESETUHUB_DB_PASSWORD"):
        monkeypatch.delenv(key, raising=False)
    config = SupremeDatabaseConfig.from_environment()
    with pytest.raises(ValueError, match="Missing central database settings"):
        config.validate()


def test_config_requires_ca_when_ssl_is_required():
    config = SupremeDatabaseConfig(
        host="db.example.test",
        database="supreme_main",
        username="supreme_user",
        password="secret",
        ssl_required=True,
        ssl_ca=None,
    )
    with pytest.raises(ValueError, match="SUPREMESETUHUB_DB_SSL_CA"):
        config.validate()


def test_central_database_can_be_separate_from_wordpress_database(monkeypatch):
    monkeypatch.setenv("WORDPRESS_DB_NAME", "primary_wordpress_db")
    config = SupremeDatabaseConfig(
        host="db.example.test",
        database="supreme_main_db",
        username="supreme_user",
        password="secret",
        ssl_required=False,
    )
    config.validate()
    assert config.database != "primary_wordpress_db"
