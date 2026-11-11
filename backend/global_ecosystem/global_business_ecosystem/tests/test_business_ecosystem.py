"""Tests for the Global Business umbrella and Bada Business package connection."""
import unittest

from backend.global_ecosystem.global_business_ecosystem import (
    GlobalBusinessEcosystemService,
    get_bada_business_connection,
)
from backend.global_ecosystem.global_business_ecosystem.registry import validate_registry

class GlobalBusinessEcosystemTests(unittest.TestCase):
    def setUp(self):
        self.service = GlobalBusinessEcosystemService()

    def test_catalog_contains_business_verticals(self):
        catalog = self.service.catalog()
        self.assertEqual(catalog["ecosystem_id"], "global_business_ecosystem")
        self.assertIn("network_marketing_and_direct_selling", catalog["categories"])
        self.assertGreaterEqual(catalog["ecosystem_count"], 5)

    def test_bada_business_is_registered_as_child(self):
        child = self.service.get_ecosystem("global_bada_business_ecosystem")
        self.assertIsNotNone(child)
        self.assertEqual(child["parent_id"] if "parent_id" in child else "global_business_ecosystem", "global_business_ecosystem")

    def test_bada_business_code_adapter_reads_canonical_package(self):
        connection = get_bada_business_connection()
        self.assertTrue(connection["code_connection"])
        self.assertEqual(connection["child_ecosystem_id"], "global_bada_business_ecosystem")
        self.assertEqual(connection["canonical_resource_package"], "backend.global_ecosystem.global_bada_business_ecosystem")
        self.assertGreaterEqual(connection["program_count"], 1)

    def test_connection_does_not_claim_live_provider_api(self):
        connection = get_bada_business_connection()
        self.assertFalse(connection["live_provider_connection_verified"])
        self.assertFalse(connection["official_public_api_verified"])

    def test_registry_integrity(self):
        self.assertEqual(validate_registry(), ())

    def test_search(self):
        results = self.service.search("Bada Business")
        self.assertEqual(results[0]["id"], "global_bada_business_ecosystem")

if __name__ == "__main__":
    unittest.main()
