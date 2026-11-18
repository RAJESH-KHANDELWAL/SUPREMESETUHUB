import unittest

from ..contracts import PROVIDER_ID, readiness


class ProviderContractTests(unittest.TestCase):
    def test_provider_identity(self):
        self.assertEqual(PROVIDER_ID, "acme")

    def test_provider_is_not_live(self):
        status = readiness()
        self.assertFalse(status["live_connection_verified"])
        self.assertFalse(status["execution_enabled"])


if __name__ == "__main__":
    unittest.main()
