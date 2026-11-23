from pathlib import Path
import unittest

from twilio_core_ecosystem.catalog import get_catalog, list_products
from twilio_core_ecosystem.contracts import TenantContext
from twilio_core_ecosystem.manager import get_manager
from twilio_core_ecosystem.policy import TwilioCorePolicy

class TwilioCoreTests(unittest.TestCase):
    def test_catalog_identity_and_product_families(self):
        catalog = get_catalog()
        self.assertEqual(catalog["ecosystem_id"], "TWILIO-CORE-ECOSYSTEM")
        self.assertEqual(len(list_products()), 5)
        self.assertFalse(catalog["live_connection_verified"])

    def test_catalog_is_defensive_copy(self):
        catalog = get_catalog()
        catalog["product_families"].clear()
        self.assertEqual(len(list_products()), 5)

    def test_tenant_context_is_required(self):
        with self.assertRaises(ValueError):
            TenantContext("", "actor").validate()

    def test_sensitive_operations_fail_closed(self):
        result = TwilioCorePolicy.authorize_metadata_capability(
            "MESSAGING_SEND", TenantContext("tenant-1", "actor-1")
        )
        self.assertFalse(result["allowed"])
        self.assertFalse(result["api_call_performed"])

    def test_metadata_discovery_does_not_call_provider(self):
        manager = get_manager()
        self.assertEqual(manager.status()["status"], "CORE_CATALOG_ONLY")
        self.assertFalse(manager.health()["live_connection_verified"])
        self.assertEqual(len(manager.list_products()), 5)
        self.assertFalse(manager.dependency_map()["api_calls_performed"])

if __name__ == "__main__":
    unittest.main()
