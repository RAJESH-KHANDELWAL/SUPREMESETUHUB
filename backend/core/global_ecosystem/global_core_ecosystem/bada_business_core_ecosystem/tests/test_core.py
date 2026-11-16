"""Unit tests for the Bada Business CORE facade and safety boundaries."""
import unittest
from backend.core.global_ecosystem.global_core_ecosystem.bada_business_core_ecosystem import BadaBusinessCoreManager
from backend.core.global_ecosystem.global_core_ecosystem.bada_business_core_ecosystem.policies import BadaBusinessPolicyError, ensure_operation_is_catalog_only

class BadaBusinessCoreTests(unittest.TestCase):
    def setUp(self):
        self.manager = BadaBusinessCoreManager()

    def test_status_reports_catalog_only_connection(self):
        status = self.manager.status()
        self.assertTrue(status["success"])
        self.assertFalse(status["live_connection_verified"])
        self.assertFalse(status["official_public_api_verified"])

    def test_program_catalog_is_readable(self):
        result = self.manager.programs()
        self.assertTrue(result["success"])
        self.assertGreaterEqual(result["count"], 3)

    def test_course_catalog_is_readable(self):
        result = self.manager.courses()
        self.assertTrue(result["success"])

    def test_platform_links_are_readable(self):
        result = self.manager.links()
        self.assertTrue(result["success"])
        self.assertEqual(result["count"], 9)

    def test_registration_validation_does_not_submit(self):
        result = self.manager.validate_registration({"full_name": "Test User", "mobile_number": "+919999999999", "email": "test@example.com", "pincode": "302001"})
        self.assertTrue(result["success"])
        self.assertFalse(result["registration_submitted"])
        self.assertFalse(result["payment_processed"])

    def test_sensitive_operations_are_blocked(self):
        with self.assertRaises(BadaBusinessPolicyError):
            ensure_operation_is_catalog_only("PAYMENT_PROCESS")

if __name__ == "__main__":
    unittest.main()
