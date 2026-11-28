import unittest

from .service import GlobalConfigService
from .manager import GlobalConfigManager


class GlobalConfigTests(unittest.TestCase):
    def test_environment_overrides_defaults(self):
        service = GlobalConfigService(defaults={"mode": "dev"}, env_prefix="APP_", environ={"APP_MODE": "prod"})
        self.assertEqual(service.get("mode"), "prod")

    def test_secret_values_are_redacted(self):
        service = GlobalConfigService(defaults={"API_TOKEN": "do-not-show"}, env_prefix="", environ={})
        self.assertEqual(service.snapshot().values["API_TOKEN"], "[REDACTED]")

    def test_required_key_validation(self):
        service = GlobalConfigService(defaults={}, env_prefix="", environ={})
        self.assertFalse(service.snapshot(required_keys=("database_url",)).valid)

    def test_manager_has_platform_defaults(self):
        manager = GlobalConfigManager()
        self.assertEqual(manager.get("app_name"), "SUPREMESETUHUB")


if __name__ == "__main__":
    unittest.main()
