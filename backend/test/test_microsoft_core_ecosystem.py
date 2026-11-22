"""Tests for the Microsoft Core ecosystem metadata control plane."""
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.microsoft_core_ecosystem import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.microsoft_core_ecosystem.domain_catalog import DOMAIN_DEFINITIONS
from backend.core.global_ecosystem.global_core_ecosystem.microsoft_core_ecosystem.manager import (
    get_microsoft_core_catalog,
    list_microsoft_products,
    microsoft_offerings_summary,
)


class MicrosoftCoreEcosystemTests(unittest.TestCase):
    def test_manager_health_and_domain_coverage(self):
        manager = get_manager()
        health = manager.health()
        self.assertEqual(health["ecosystem_id"], "MICROSOFT-CORE-ECOSYSTEM")
        self.assertEqual(health["domain_count"], 19)
        self.assertEqual(health["product_family_count"], 16)
        self.assertEqual(health["registered_product_domain_count"], 16)

    def test_all_products_have_known_domain(self):
        products = get_manager().list_products()["products"]
        self.assertEqual(len(products), 16)
        self.assertTrue(all(product["domain_id"] in DOMAIN_DEFINITIONS for product in products))
        self.assertEqual(len({product["ecosystem_id"] for product in products}), len(products))

    def test_canonical_manager_owns_catalog_and_inventory_helpers(self):
        catalog = get_microsoft_core_catalog()
        self.assertEqual(catalog["ecosystem_id"], "MICROSOFT-CORE-ECOSYSTEM")
        self.assertEqual(len(list_microsoft_products()), 16)
        self.assertEqual(len(list_microsoft_products(enabled_only=True)), 16)
        self.assertEqual(microsoft_offerings_summary()["count"], 16)
        catalog["children"].clear()
        self.assertEqual(len(get_microsoft_core_catalog()["children"]), 16)

    def test_unknown_product_and_domain(self):
        self.assertIsNone(get_manager().get_product("not-a-product"))
        with self.assertRaises(ValueError):
            get_manager().get_domain_manager("NOT_A_DOMAIN")

    def test_catalog_does_not_claim_live_connectivity(self):
        status = get_manager().status()
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["api_calls_performed"], 0)


if __name__ == "__main__":
    unittest.main()
