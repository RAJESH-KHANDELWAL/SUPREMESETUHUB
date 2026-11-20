"""Tests for Cloudflare Core catalog, routing, safety and master-catalog bridge."""
from __future__ import annotations
import unittest
from .domain_catalog import DOMAIN_DEFINITIONS, domain_summary
from .manager import get_manager
from .product_catalog import list_products, list_directory_audit, get_product
from .policy import CloudflareCorePolicy, CloudflarePolicyError

class CloudflareCoreTests(unittest.TestCase):
    def test_domain_taxonomy_and_product_reconciliation(self):
        summary = domain_summary()
        self.assertEqual(summary["domain_count"], len(DOMAIN_DEFINITIONS))
        self.assertEqual(summary["product_count"], len(list_products()))
        self.assertTrue(all(item["product_count"] > 0 for item in summary["domains"]))
    def test_product_lookup_and_domain_filter(self):
        manager = get_manager()
        self.assertIsNotNone(manager.get_product("workers"))
        self.assertIsNone(manager.get_product("not-a-cloudflare-product"))
        self.assertTrue(all(p["domain_id"] == "AI_DEVELOPER_PLATFORM"
                            for p in manager.list_products(domain_id="AI_DEVELOPER_PLATFORM")["products"]))
    def test_existing_directory_audit_does_not_promote_external_names(self):
        audit = {x["directory"]: x["classification"] for x in list_directory_audit()}
        self.assertEqual(audit["onlyfans_cloudflare_core_ecosystem"], "EXTERNAL_OR_UNVERIFIED_PLACEHOLDER")
        self.assertEqual(audit["catalog_cloudflare_core_ecosystem"], "CORE_CATALOG_PACKAGE")
        self.assertNotIn("onlyfans", [p["product_id"] for p in list_products()])
    def test_sensitive_capabilities_require_explicit_authorization(self):
        self.assertEqual(CloudflareCorePolicy.classify_capability("DNS_EDIT"),
                         "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION")
        self.assertEqual(CloudflareCorePolicy.classify_capability("READ_ANALYTICS"),
                         "STANDARD_REQUIRES_TENANT_AUTHORIZATION")
    def test_missing_tenant_context_is_rejected(self):
        with self.assertRaises(CloudflarePolicyError):
            CloudflareCorePolicy.require_tenant_context(None)
    def test_master_catalog_is_read_without_expanding_it(self):
        snapshot = get_manager().master_catalog_snapshot()
        self.assertTrue(snapshot["available"])
        self.assertEqual(snapshot["target_unique_entries"], 2468)
        self.assertEqual(snapshot["current_unique_entries"], 246)
        self.assertEqual(snapshot["remaining_unique_entries"], 2222)
    def test_health_never_claims_live_connectivity(self):
        health = get_manager().health()
        self.assertEqual(health["live_connections_verified"], 0)
        self.assertEqual(health["api_calls_performed"], 0)

if __name__ == "__main__":
    unittest.main()
