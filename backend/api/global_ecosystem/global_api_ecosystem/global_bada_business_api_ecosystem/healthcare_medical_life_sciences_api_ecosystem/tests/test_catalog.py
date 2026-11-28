import unittest

from healthcare_medical_life_sciences_api_ecosystem.catalog import get_domain, list_domains

class HealthcareCatalogTests(unittest.TestCase):
    def test_registry_has_34_domains(self):
        self.assertEqual(len(list_domains()), 34)

    def test_unknown_domain_returns_none(self):
        self.assertIsNone(get_domain("unknown-domain"))

    def test_anatomy_domain_exists(self):
        self.assertIsNotNone(get_domain("human_anatomy_body_systems"))

    def test_veterinary_domain_exists(self):
        self.assertIsNotNone(get_domain("veterinary_animal_body_health_welfare"))

if __name__ == "__main__":
    unittest.main()
