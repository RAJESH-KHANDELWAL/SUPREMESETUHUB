import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.integrations.registry import (
    PROVIDER_INTEGRATIONS, get_integration, list_integrations, validate_integration_registry,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.integrations.routes import router
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.integrations.service import get_status

class BadaBusinessIntegrationRegistryTests(unittest.TestCase):
    def test_provider_reference_registry_is_unique_and_populated(self):
        result = validate_integration_registry()
        self.assertEqual(result["integration_count"], 21)
        self.assertTrue(result["structurally_valid"])
        self.assertEqual(result["duplicate_ids"], [])

    def test_catalog_does_not_claim_live_connections(self):
        self.assertTrue(all(item["status"] == "catalog_reference_only" for item in PROVIDER_INTEGRATIONS))
        self.assertEqual(get_status()["live_connection_verified_count"], 0)
        self.assertEqual(get_status()["api_documentation_verified_count"], 0)

    def test_provider_lookup(self):
        self.assertEqual(get_integration("google")["package"], "google_business_api_ecosystem")
        self.assertIsNone(get_integration("not-a-provider"))

    def test_integration_routes_are_registered(self):
        paths = {getattr(route, "path", None) for route in router.routes}
        self.assertIn("/integrations/status", paths)
        self.assertIn("/integrations", paths)
        self.assertIn("/integrations/{integration_id}", paths)

if __name__ == "__main__":
    unittest.main()
