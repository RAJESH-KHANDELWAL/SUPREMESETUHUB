"""Contract tests for the Global App Core read-only boundary."""
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_app_core_ecosystem import (
    GlobalAppCoreService,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_app_core_ecosystem.contracts import (
    AppCoreResult, AppReadiness, AppTenantContext,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_app_core_ecosystem.policy import (
    readiness_for_provider, redact_secrets, safe_provider_snapshot,
)


class GlobalAppCoreContractTests(unittest.TestCase):
    def test_catalog_snapshot_is_read_only_and_not_live_verified(self):
        snapshot = GlobalAppCoreService().catalog_snapshot()
        self.assertEqual(snapshot["layer"], "CORE")
        self.assertGreater(snapshot["provider_count"], 0)
        self.assertEqual(snapshot["execution"], "NOT_PERFORMED")
        self.assertEqual(snapshot["persistence"], "NOT_PERFORMED")
        self.assertEqual(snapshot["live_verified_provider_count"], 0)

    def test_provider_resolution_and_unknown_provider(self):
        service = GlobalAppCoreService()
        provider = service.resolve_provider("google")
        self.assertEqual(provider["id"], "google")
        with self.assertRaises(KeyError):
            service.resolve_provider("provider_that_does_not_exist")

    def test_app_type_validation(self):
        service = GlobalAppCoreService()
        self.assertEqual(service.validate_app_type("web_app")["id"], "web_app")
        with self.assertRaises(KeyError):
            service.validate_app_type("unknown_app_type")

    def test_secret_filter_is_recursive(self):
        value = {"name": "Google", "nested": {"api_key": "do-not-return", "ok": True}}
        safe = redact_secrets(value)
        self.assertEqual(safe, {"name": "Google", "nested": {"ok": True}})
        self.assertEqual(redact_secrets({"accessToken": "hidden", "api-key": "hidden", "label": "safe"}), {"label": "safe"})

    def test_provider_snapshot_is_allow_listed(self):
        safe = safe_provider_snapshot({
            "id": "google", "name": "Google", "api_key": "hidden",
            "unexpected_internal": "hidden-too",
        })
        self.assertEqual(safe, {"id": "google", "name": "Google"})

    def test_catalog_status_is_not_promoted_without_evidence(self):
        self.assertEqual(readiness_for_provider({
            "integration_status": "catalog_only",
            "live_connection_verified": False,
        }), "CATALOG_ONLY")
        self.assertEqual(readiness_for_provider({
            "integration_status": "live_verified",
            "live_connection_verified": False,
        }), "CATALOG_ONLY")

    def test_contract_types(self):
        self.assertEqual(AppReadiness.CATALOG_ONLY.value, "CATALOG_ONLY")
        self.assertEqual(AppTenantContext(tenant_id="tenant-a").tenant_id, "tenant-a")
        self.assertFalse(AppCoreResult(True, "GLOBAL_APP_ECOSYSTEM", "catalog").execution_performed)


if __name__ == "__main__":
    unittest.main()
