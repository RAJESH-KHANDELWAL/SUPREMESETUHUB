from __future__ import annotations

import pytest

from backend.wordpress import (
    WordPressConnectionConfig,
    WordPressController,
    WordPressDatabaseConnection,
    WordPressRegistry,
    WordPressService,
    WordPressSite,
)
from backend.wordpress.rest_api import WordPressRestConfig, WordPressRestClient
from backend.wordpress.service import WordPressService as Service


def test_wordpress_public_package_exports_expected_components():
    assert WordPressConnectionConfig is not None
    assert WordPressDatabaseConnection is not None
    assert WordPressController is not None
    assert WordPressRegistry is not None
    assert WordPressService is Service
    assert WordPressSite is not None


def test_rest_config_uses_registered_site_environment(monkeypatch):
    monkeypatch.setenv("WORDPRESS_SITE_URL", "https://example.com/")
    monkeypatch.setenv("WORDPRESS_USERNAME", "api-user")
    monkeypatch.setenv("WORDPRESS_APPLICATION_PASSWORD", "private-app-password")

    config = WordPressRestConfig.from_environment("rajeshkhandelwalofficial")

    assert config.base_url == "https://example.com"
    assert config.username == "api-user"
    assert config.application_password == "private-app-password"


def test_rest_config_rejects_unregistered_site():
    with pytest.raises(ValueError, match="WORDPRESS_SITE_NOT_REGISTERED"):
        WordPressRestConfig.from_environment("unknown-site")


def test_rest_config_requires_https(monkeypatch):
    monkeypatch.setenv("WORDPRESS_SITE_URL", "http://example.com")
    monkeypatch.setenv("WORDPRESS_USERNAME", "api-user")
    monkeypatch.setenv("WORDPRESS_APPLICATION_PASSWORD", "private-app-password")

    with pytest.raises(RuntimeError, match="must use HTTPS"):
        WordPressRestConfig.from_environment("rajeshkhandelwalofficial")


def test_rest_config_reports_missing_environment_names(monkeypatch):
    for name in (
        "WORDPRESS_SITE_URL",
        "WORDPRESS_USERNAME",
        "WORDPRESS_APPLICATION_PASSWORD",
    ):
        monkeypatch.delenv(name, raising=False)

    with pytest.raises(RuntimeError, match="WORDPRESS_SITE_URL"):
        WordPressRestConfig.from_environment("rajeshkhandelwalofficial")


def test_service_reports_unknown_site_without_opening_database():
    class EmptyRegistry:
        def get(self, site_id):
            return None

        def list_sites(self):
            return []

    service = Service(registry=EmptyRegistry())

    result = service.connect_site("missing-site", "WORDPRESS")

    assert result == {
        "success": False,
        "status": "SITE_NOT_FOUND",
        "site_id": "missing-site",
    }


def test_service_health_reports_not_connected_without_live_connection():
    class EmptyRegistry:
        def get(self, site_id):
            return None

        def list_sites(self):
            return []

    service = Service(registry=EmptyRegistry())

    assert service.health("missing-site") == {
        "success": False,
        "status": "NOT_CONNECTED",
        "site_id": "missing-site",
    }
    assert service.check_wordpress("missing-site") == {
        "success": False,
        "status": "NOT_CONNECTED",
        "site_id": "missing-site",
    }
