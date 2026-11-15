import unittest
from ..domain_catalog import DOMAIN_CATEGORIES
from ..domain_models import DomainRecord
from ..domain_registry import DomainRegistry
from ..domain_service import DomainStorageService

class DomainFoundationTests(unittest.TestCase):
    def test_catalog(self):
        self.assertGreaterEqual(len(DOMAIN_CATEGORIES), 8)

    def test_normalization(self):
        self.assertEqual(DomainRecord("d1", "Example.COM.").domain_name, "example.com")

    def test_duplicate_id(self):
        registry = DomainRegistry()
        registry.register(DomainRecord("d1", "example.com"))
        with self.assertRaises(ValueError):
            registry.register(DomainRecord("d1", "example.net"))

    def test_no_false_live_connection(self):
        self.assertFalse(DomainStorageService().health()["external_connections_verified"])

if __name__ == "__main__":
    unittest.main()
