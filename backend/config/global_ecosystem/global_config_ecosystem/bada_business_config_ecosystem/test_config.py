import unittest

from .service import BadaBusinessConfigService
from .manager import BadaBusinessConfigManager


class BadaBusinessConfigTests(unittest.TestCase):
    def test_safe_defaults(self):
        result = BadaBusinessConfigManager().initialize()
        self.assertFalse(result["values"]["enabled"])
        self.assertTrue(result["values"]["require_approval"])
        self.assertTrue(result["valid"])

    def test_timeout_validation(self):
        service = BadaBusinessConfigService(overrides={"request_timeout_seconds": 500}, environ={})
        self.assertFalse(service.snapshot()["valid"])

    def test_unknown_environment_validation(self):
        service = BadaBusinessConfigService(overrides={"environment": "unknown"}, environ={})
        self.assertFalse(service.snapshot()["valid"])

    def test_sensitive_keys_are_redacted(self):
        service = BadaBusinessConfigService(overrides={"API_TOKEN": "hidden"}, environ={})
        self.assertEqual(service.snapshot()["values"]["API_TOKEN"], "[REDACTED]")


if __name__ == "__main__":
    unittest.main()
