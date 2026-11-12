"""Tests for the isolated Global Database Ecosystem DB configuration."""
import pytest

from backend.database.gde_connection import GDEDatabaseConfig


def test_gde_config_loads_only_gde_environment(monkeypatch):
    monkeypatch.setenv("GDE_DB_HOST", "db.example.test")
    monkeypatch.setenv("GDE_DB_NAME", "global_data")
    monkeypatch.setenv("GDE_DB_USER", "gde_user")
    monkeypatch.setenv("GDE_DB_PASSWORD", "not-a-real-password")
    monkeypatch.setenv("GDE_DB_SSL_REQUIRED", "false")
    monkeypatch.setenv("WORDPRESS_DB_HOST", "wordpress.example.test")
    monkeypatch.setenv("WORDPRESS_DB_NAME", "wordpress_db")
    config = GDEDatabaseConfig.from_environment()
    config.validate()
    assert config.host == "db.example.test"
    assert config.database == "global_data"
    assert config.username == "gde_user"


def test_gde_config_rejects_wordpress_database(monkeypatch):
    monkeypatch.setenv("WORDPRESS_DB_NAME", "wordpress_db")
    monkeypatch.setenv("GDE_DB_SSL_REQUIRED", "false")
    config = GDEDatabaseConfig(
        host="db.example.test",
        database="wordpress_db",
        username="gde_user",
        password="secret",
    )
    with pytest.raises(ValueError, match="WordPress databases"):
        config.validate()


def test_gde_config_requires_own_credentials(monkeypatch):
    for key in (
        "GDE_DB_HOST",
        "GDE_DB_NAME",
        "GDE_DB_USER",
        "GDE_DB_PASSWORD",
    ):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv("GDE_DB_SSL_REQUIRED", "false")
    config = GDEDatabaseConfig.from_environment()
    with pytest.raises(ValueError, match="Missing GDE database settings"):
        config.validate()


def test_gde_config_requires_ca_when_ssl_is_required(monkeypatch):
    monkeypatch.setenv("GDE_DB_SSL_REQUIRED", "true")
    config = GDEDatabaseConfig(
        host="db.example.test",
        database="global_data",
        username="gde_user",
        password="secret",
        ssl_required=True,
        ssl_ca=None,
    )
    with pytest.raises(ValueError, match="GDE_DB_SSL_CA"):
        config.validate()
