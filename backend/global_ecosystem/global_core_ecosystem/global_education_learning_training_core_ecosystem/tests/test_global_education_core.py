import unittest
from ..domain_catalog import list_domains, get_domain, validate_domains
from ..region_catalog import list_regional_frameworks, get_regional_framework
from ..manager import get_manager
from ..policy import is_allowed

class GlobalEducationCoreTests(unittest.TestCase):
    def test_unique_domain_ids(self):
        ids = [item["domain_id"] for item in list_domains()]
        self.assertEqual(len(ids), len(set(ids)))

    def test_broad_global_coverage(self):
        self.assertGreaterEqual(len(list_domains()), 50)
        self.assertIsNotNone(get_domain("medical_healthcare_education"))
        self.assertIsNotNone(get_domain("environment_climate_sustainability_education"))

    def test_bharat_and_global_overlays(self):
        regions = list_regional_frameworks()
        self.assertIn("bharat", regions)
        self.assertIn("global", regions)
        self.assertIn("NEP", " ".join(regions["bharat"]["frameworks"]))
        self.assertEqual(get_regional_framework("GLOBAL")["region_id"], "GLOBAL")

    def test_manager_catalog(self):
        manager = get_manager()
        self.assertEqual(manager.catalog()["layer"], "GLOBAL_CORE")
        self.assertEqual(manager.status()["domain_count"], len(list_domains()))

    def test_search_and_policy(self):
        self.assertTrue(get_manager().search("online"))
        self.assertTrue(is_allowed("GET_DOMAIN"))
        self.assertFalse(is_allowed("ENROLL_LEARNERS"))

    def test_domain_integrity(self):
        self.assertTrue(validate_domains()["valid"])

if __name__ == "__main__":
    unittest.main()
