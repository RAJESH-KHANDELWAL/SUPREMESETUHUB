"""Tests for the global Agriculture/Food CORE contracts and boundaries."""
import unittest
from ..catalog import get_catalog
from ..domain_catalog import list_domains, get_domain
from ..manager import get_manager
from ..policy import classify_capability, safe_metadata

class AgricultureCoreTests(unittest.TestCase):
    def test_catalog_identity_and_parent(self):
        catalog = get_catalog()
        self.assertEqual(catalog["ecosystem_id"], get_manager().ECOSYSTEM_ID)
        self.assertEqual(catalog["parent_id"], "GLOBAL-CORE-ECOSYSTEM")

    def test_domains_are_unique_and_resolvable(self):
        domains = list_domains()
        ids = [item["domain_id"] for item in domains]
        self.assertEqual(len(ids), len(set(ids)))
        for domain_id in ids:
            self.assertIsNotNone(get_domain(domain_id))

    def test_business_layer_is_separate(self):
        self.assertTrue(get_catalog()["business_layer_id"].startswith("GLOBAL-BADA-BUSINESS-"))

    def test_sensitive_capability_is_flagged(self):
        self.assertTrue(classify_capability("HUMAN_HEALTH_RECORDS").startswith("REQUIRES_EXPLICIT"))

    def test_secrets_are_redacted(self):
        self.assertEqual(safe_metadata({"api_key": "x", "name": "farm"})["api_key"], "[REDACTED]")

    def test_no_live_connection_claim(self):
        health = get_manager().health()
        self.assertFalse(health["provider_connections_verified"])

if __name__ == "__main__":
    unittest.main()
