import unittest

from ..catalog import get_domain, list_domains

class CatalogTests(unittest.TestCase):
    def test_domain_registry_has_sixteen_entries(self):
        self.assertEqual(len(list_domains()), 16)

    def test_domain_lookup_returns_none_for_unknown_id(self):
        self.assertIsNone(get_domain("not-a-real-domain"))

    def test_known_domain_can_be_loaded(self):
        self.assertIsNotNone(get_domain("agriculture_farming_primary_production"))

if __name__ == "__main__":
    unittest.main()
