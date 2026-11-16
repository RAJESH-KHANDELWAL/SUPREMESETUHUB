"""Offline contract tests for the Global Cloud Core control plane."""
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_cloud_core_ecosystem import (
    CloudCoreResult,
    CloudReadiness,
    CloudTenantContext,
    GlobalCloudCoreService,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_cloud_core_ecosystem.policy import (
    readiness_for_provider,
    redact_secrets,
    safe_provider_snapshot,
)


class GlobalCloudCoreContractTests(unittest.TestCase):
    def test_catalog_snapshot_is_read_only_and_catalog_only(self):
        snapshot = GlobalCloudCoreService().catalog_snapshot()
        self.assertEqual(snapshot["layer"], "CORE")
        self.assertEqual(snapshot["provider_count"], 41)
        self.assertEqual(snapshot["live_verified_provider_count"], 0)
        self.assertEqual(snapshot["execution"], "NOT_PERFORMED")
        self.assertEqual(snapshot["persistence"], "NOT_PERFORMED")

    def test_provider_resolution_and_unknown_provider(self):
        service = GlobalCloudCoreService()
        self.assertEqual(service.resolve_provider("google_cloud")["id"], "google_cloud")
        with self.assertRaises(KeyError):
            service.resolve_provider("provider_that_does_not_exist")

    def test_provider_snapshot_is_safe_and_catalog_only(self):
        snapshot = GlobalCloudCoreService().provider_snapshot("aws")
        self.assertEqual(snapshot["provider"]["id"], "aws")
        self.assertEqual(snapshot["readiness"], "CATALOG_ONLY")
        self.assertEqual(snapshot["execution"], "NOT_PERFORMED")

    def test_secret_filter_is_recursive(self):
        value = {"name": "cloud", "nested": {"access_key": "hidden", "ok": True}}
        self.assertEqual(redact_secrets(value), {"name": "cloud", "nested": {"ok": True}})

    def test_provider_snapshot_is_allow_listed(self):
        safe = safe_provider_snapshot({
            "id": "aws", "name": "AWS", "api_key": "hidden",
            "unexpected_internal": "hidden-too",
        })
        self.assertEqual(safe, {"id": "aws", "name": "AWS"})

    def test_readiness_requires_live_evidence(self):
        self.assertEqual(readiness_for_provider({
            "integration_status": "live_verified",
            "live_connection_verified": False,
        }), "CATALOG_ONLY")
        self.assertEqual(readiness_for_provider({
            "integration_status": "live_verified",
            "live_connection_verified": True,
        }), "LIVE_VERIFIED")

    def test_workload_taxonomy_is_read_only(self):
        service = GlobalCloudCoreService()
        snapshot = service.workload_snapshot("agriculture_food")
        self.assertEqual(snapshot["workload"]["id"], "agriculture_food")
        self.assertEqual(snapshot["execution"], "NOT_PERFORMED")
        self.assertEqual(len(service.list_workloads(adult_industry=True)) > 0, True)

    def test_health_and_contract_types(self):
        health = GlobalCloudCoreService().health_snapshot()
        self.assertTrue(health["success"], health)
        self.assertEqual(CloudReadiness.CATALOG_ONLY.value, "CATALOG_ONLY")
        self.assertEqual(CloudTenantContext(tenant_id="tenant-a").tenant_id, "tenant-a")
        self.assertFalse(CloudCoreResult(
            True, "GLOBAL_CLOUD_ECOSYSTEM", "catalog"
        ).execution_performed)


if __name__ == "__main__":
    unittest.main()
