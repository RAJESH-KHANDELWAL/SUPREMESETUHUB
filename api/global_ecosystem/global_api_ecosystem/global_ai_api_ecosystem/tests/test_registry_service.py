import unittest

from ..registry_service import AIRegistryAPIService


class AIRegistryAPIServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = AIRegistryAPIService()

    def test_lists_provider_registry_without_claiming_live_connectivity(self):
        providers = self.service.list_providers()
        self.assertGreaterEqual(len(providers), 68)
        self.assertTrue(all(item["live_connection_verified"] is False for item in providers))

    def test_adapter_directory_is_explicit(self):
        result = self.service.list_adapters()
        self.assertGreaterEqual(result["count"], 20)
        self.assertFalse(result["live_connections_verified"])

    def test_category_filter_works(self):
        frameworks = self.service.list_providers(category="agent_framework")
        self.assertTrue(frameworks)
        self.assertTrue(all(item["provider_type"] == "agent_framework" for item in frameworks))

    def test_registry_validation_is_returned(self):
        result = self.service.get_registry_validation()
        self.assertIn("valid", result)
        self.assertEqual(result["error_count"], len(result["errors"]))

    def test_adult_policy_precheck_fails_closed(self):
        result = self.service.policy_precheck({
            "domain": "adult_content", "purpose": "lawful_adult_platform_safety",
        })
        self.assertFalse(result["allowed_by_precheck"])
        self.assertIn("age_verified", result["missing_safeguards"])


if __name__ == "__main__":
    unittest.main()
