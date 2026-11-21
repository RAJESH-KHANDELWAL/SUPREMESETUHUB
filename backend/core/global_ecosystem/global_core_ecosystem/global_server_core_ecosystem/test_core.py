"""Offline tests for GLOBAL SERVER CORE domain contracts and metadata."""
import unittest

from .models import ServerIdentity
from .registry import ServerCoreRegistry
from .service import ServerCoreService
from .policy import ServerPolicy
from .manager import get_manager, validate_master_alignment


class ServerCoreTests(unittest.TestCase):
    def payload(self, server_id="node-1"):
        return {
            "server_id": server_id, "provider_id": "AWS", "server_type": "VPS",
            "server_role": "application", "country": "in", "region": "ap-south-1",
            "environment": "test", "metadata": {"zone": "a"},
        }

    def test_identity_registration_normalizes_and_copies(self):
        service = ServerCoreService()
        result = service.register_identity(self.payload())
        self.assertTrue(result["success"])
        result["identity"]["metadata"]["zone"] = "mutated"
        stored = service.get_identity("node-1")["identity"]
        self.assertEqual(stored["provider_id"], "aws")
        self.assertEqual(stored["metadata"]["zone"], "a")

    def test_missing_and_duplicate_identity_rejected(self):
        registry = ServerCoreRegistry()
        with self.assertRaises(ValueError):
            registry.register(ServerIdentity("", "aws", "vps", "app", "IN", "west", "test"))
        item = ServerIdentity("one", "aws", "vps", "app", "IN", "west", "test")
        registry.register(item)
        with self.assertRaises(ValueError):
            registry.register(item)

    def test_policy_requires_approval_by_default(self):
        policy = ServerPolicy()
        with self.assertRaises(PermissionError):
            policy.validate(environment="production")
        policy.validate(environment="production", authorized=True)
        with self.assertRaises(ValueError):
            policy.validate(environment="sandbox", authorized=True)

    def test_service_reports_core_boundary(self):
        info = ServerCoreService().describe()
        self.assertEqual(info["layer"], "CORE")
        self.assertFalse(info["remote_operations_enabled"])
        self.assertIn("aws", info["provider_domains"])

    def test_registry_and_all_domain_manifests_are_consistent(self):
        status = get_manager().status()
        self.assertEqual(status["provider_count"], 7)
        self.assertEqual(status["core_domain_count"], 16)
        self.assertEqual(status["domain_manifest_count"], 16)
        self.assertEqual(status["control_area_count"], 96)
        self.assertEqual(status["workload_profile_count"], 20)
        self.assertEqual(status["service_tier_count"], 7)
        self.assertFalse(status["remote_operations_enabled"])

    def test_master_catalog_references_are_valid_and_read_only(self):
        result = validate_master_alignment()
        self.assertTrue(result["success"])
        self.assertEqual(result["unknown_references"], 0)
        self.assertFalse(result["counts_as_new_master_entries"])
        self.assertEqual(result["target_unique_entries"], 2468)

    def test_domain_discovery_is_case_insensitive(self):
        manager = get_manager()
        self.assertIsNotNone(manager.get_domain("availability"))
        self.assertIsNone(manager.get_domain("NOT_A_SERVER_DOMAIN"))

    def test_provider_inventory_is_metadata_only(self):
        providers = get_manager().list_providers()
        self.assertEqual(len(providers), 7)
        self.assertTrue(all(item.get("provider_id") for item in providers))
        self.assertFalse(get_manager().status()["live_provider_connections_verified"])


if __name__ == "__main__":
    unittest.main()
