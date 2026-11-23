import unittest
from ..domain_catalog import list_business_domains, get_business_domain, validate_business_domains
from ..manager import get_manager
from ..policy import is_allowed

class EducationBusinessCoreTests(unittest.TestCase):
    def test_unique_domain_ids(self):
        ids = [item["domain_id"] for item in list_business_domains()]
        self.assertEqual(len(ids), len(set(ids)))

    def test_expanded_service_work_business_coverage(self):
        domains = list_business_domains()
        self.assertGreaterEqual(len(domains), 50)
        self.assertTrue(all(item["capabilities"] == ["SERVICE", "WORK", "BUSINESS"] for item in domains))

    def test_core_mapping(self):
        self.assertEqual(get_business_domain("online_courses_lms_edtech_platforms")["core_domain_id"], "digital_online_distance_learning")
        self.assertTrue(validate_business_domains()["valid"])

    def test_manager_filter(self):
        self.assertEqual(len(get_manager().filter_by_capability("SERVICE")), len(list_business_domains()))

    def test_integrity_and_policy(self):
        self.assertTrue(is_allowed("GET_CATALOG"))
        self.assertFalse(is_allowed("PROCESS_PAYMENTS"))

if __name__ == "__main__":
    unittest.main()
