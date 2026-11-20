"""Focused provider validation tests."""
import unittest

from ..service import DigitalOceanCoreService


class ProviderTests(unittest.TestCase):
    def setUp(self):
        self.service = DigitalOceanCoreService()

    def test_unknown_capability(self):
        with self.assertRaises(ValueError):
            self.service.validate("unknown", {})

    def test_all_capabilities(self):
        for capability in ("cloud", "hosting", "server", "storage", "vps"):
            with self.subTest(capability=capability):
                result = self.service.validate(capability, {"operation": "inspect"})
                self.assertEqual(result["capability"], capability)
                self.assertFalse(result["live_call"])

    def test_secret_fields_rejected(self):
        with self.assertRaises(ValueError):
            self.service.validate("cloud", {"metadata": {"api_key": "secret"}})

    def test_execution_disabled(self):
        with self.assertRaisesRegex(RuntimeError, "LIVE_PROVIDER_CALLS_DISABLED"):
            self.service.execute()


if __name__ == "__main__":
    unittest.main()
