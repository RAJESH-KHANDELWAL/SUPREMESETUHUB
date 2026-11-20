"""Unit tests for Communication Core metadata and safety boundaries."""
from __future__ import annotations
import unittest
from .manager import get_manager
from .policy import CommunicationCorePolicy, CommunicationPolicyError
from .product_catalog import DIRECTORY_INVENTORY, list_products

class CommunicationCoreTests(unittest.TestCase):
    def test_inventory_matches_existing_directory_map(self):
        self.assertEqual(len(DIRECTORY_INVENTORY), 19)
        self.assertEqual(len(list_products()), 19)

    def test_provider_entries_are_catalog_only(self):
        self.assertTrue(all(not item["live_connection_verified"] for item in list_products()))

    def test_manager_health_is_metadata_only(self):
        health = get_manager().health()
        self.assertTrue(health["success"])
        self.assertEqual(health["status"], "CORE_CATALOG_ONLY")
        self.assertEqual(health["live_integrations_verified"], 0)

    def test_master_catalog_is_read_only_and_summary_only(self):
        summary = get_manager().master_catalog_summary()
        self.assertTrue(summary["read_only"])
        self.assertEqual(summary["catalogue_id"], "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM")

    def test_sensitive_capability_requires_explicit_authorization(self):
        with self.assertRaises(CommunicationPolicyError):
            CommunicationCorePolicy.require_explicit_authorization("SEND_MESSAGE", False)

    def test_sensitive_summary_strips_secrets_and_personal_data(self):
        safe = CommunicationCorePolicy.safe_summary({"provider":"x","api_key":"secret","email_address":"a@b.test"})
        self.assertEqual(safe, {"provider":"x"})

if __name__ == "__main__":
    unittest.main()
