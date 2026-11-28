from __future__ import annotations
import importlib
import unittest
from backend.core.global_ecosystem.global_core_ecosystem.paypal_core_ecosystem.catalog import get_paypal_core_catalog
from backend.core.global_ecosystem.global_core_ecosystem.paypal_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.paypal_core_ecosystem.master_catalog import get_master_catalog_status
from backend.core.global_ecosystem.global_core_ecosystem.paypal_core_ecosystem.contracts import TenantContext

class PayPalCoreTests(unittest.TestCase):
    def test_inventory_is_complete_and_unique(self):
        products = get_paypal_core_catalog()["children"]
        self.assertEqual(len(products), 13)
        self.assertEqual(len({p["ecosystem_id"] for p in products}), 13)
        self.assertTrue(all(p["capabilities"] and p["domain_id"] for p in products))
    def test_every_product_manager_is_importable(self):
        for product in get_paypal_core_catalog()["children"]:
            module = importlib.import_module("backend.core.global_ecosystem.global_core_ecosystem.paypal_core_ecosystem." + product["package"] + ".manager")
            manager_class = getattr(module, product["manager_class"])
            self.assertEqual(manager_class().status()["ecosystem_id"], product["ecosystem_id"])
    def test_manager_reports_metadata_not_live_connection(self):
        manager = get_manager()
        status = manager.status()
        self.assertEqual(status["product_count"], 13)
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(manager.health()["api_calls_performed"], 0)
    def test_tenant_context_and_capability_policy(self):
        manager = get_manager()
        result = manager.product_manager("PAYPAL-PAYMENTS-CORE-ECOSYSTEM").evaluate_capability("PAYMENT_METADATA", TenantContext("tenant-1","actor-1"))
        self.assertTrue(result["success"])
        self.assertFalse(result["data"]["provider_api_call_performed"])
        denied = manager.product_manager("PAYPAL-PAYMENTS-CORE-ECOSYSTEM").evaluate_capability("PAYOUT_BATCH_METADATA", TenantContext("tenant-1","actor-1"))
        self.assertFalse(denied["success"])
    def test_master_catalog_is_read_only_and_has_paypal_reference(self):
        status = get_master_catalog_status()
        self.assertTrue(status["available"])
        self.assertTrue(status["paypal_payment_package_registered"])
        self.assertEqual(status["access_mode"], "READ_ONLY_ON_DEMAND")
        self.assertFalse(status["source_modified"])
        self.assertEqual(status["taxonomy_entries_added"], 0)

if __name__ == "__main__": unittest.main()
