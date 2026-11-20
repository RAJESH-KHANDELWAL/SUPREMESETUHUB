"""Tests for expanded Global Communication Core metadata."""
from __future__ import annotations
import unittest
from .manager import get_manager
from .policy import CommunicationCorePolicy, CommunicationPolicyError
from .product_catalog import (
    EXISTING_DIRECTORY_INVENTORY, PROVIDER_DIRECTORY, list_products,
    list_providers, inventory_summary,
)
from .domain_catalog import DOMAIN_DEFINITIONS

class CommunicationCoreTests(unittest.TestCase):
    def test_all_existing_directories_are_accounted_for(self):
        self.assertEqual(len(EXISTING_DIRECTORY_INVENTORY), 19)

    def test_expanded_provider_reference_inventory_is_unique(self):
        ids = [item["id"] for item in PROVIDER_DIRECTORY]
        self.assertGreaterEqual(len(ids), 70)
        self.assertEqual(len(ids), len(set(ids)))

    def test_provider_records_are_not_live_integrations(self):
        self.assertTrue(all(not item["live_connection_verified"] for item in PROVIDER_DIRECTORY))
        self.assertTrue(all(item["implementation_status"] == "NOT_IMPLEMENTED" for item in list_products()))

    def test_domains_cover_major_communication_layers(self):
        expected = {
            "TELECOMMUNICATIONS_NETWORKS", "EMAIL_SERVICES", "OTT_MESSAGING",
            "SMS_MMS_RCS", "VOICE_TELEPHONY_VOIP", "VIDEO_CONFERENCING",
            "CPaaS_COMMUNICATION_APIS", "CCaaS_CONTACT_CENTERS",
            "PUSH_NOTIFICATIONS", "AI_CONVERSATIONAL_VOICE",
            "PRIVACY_SECURITY_COMPLIANCE", "INDIA_COMMUNICATION_REGULATORY",
        }
        self.assertTrue(expected.issubset(DOMAIN_DEFINITIONS))

    def test_provider_filtering(self):
        self.assertTrue(all(x["region"] == "INDIA" for x in list_providers(region="INDIA")))
        self.assertTrue(all(x["family"] == "cpaas" for x in list_providers(family="cpaas")))

    def test_inventory_summary_does_not_claim_live_connections(self):
        summary = inventory_summary()
        self.assertEqual(summary["existing_directory_count"], 19)
        self.assertEqual(summary["live_integrations_verified"], 0)

    def test_manager_health_is_metadata_only(self):
        health = get_manager().health()
        self.assertTrue(health["success"])
        self.assertEqual(health["status"], "CORE_CATALOG_ONLY")
        self.assertEqual(health["live_integrations_verified"], 0)

    def test_master_catalog_is_read_only(self):
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
