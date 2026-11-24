import unittest

from backend.global_ecosystem.atlassian_ecosystem import AtlassianEcosystemService
from backend.global_ecosystem.atlassian_ecosystem.catalog import (
    ATLASSIAN_PRODUCTS, list_capabilities,
)
from backend.global_ecosystem.atlassian_ecosystem.health import readiness_report

class AtlassianEcosystemTests(unittest.TestCase):
    def setUp(self):
        self.service = AtlassianEcosystemService()

    def test_catalog_covers_five_product_families(self):
        self.assertEqual(len(ATLASSIAN_PRODUCTS), 5)
        self.assertIn("jira_cloud", ATLASSIAN_PRODUCTS)
        self.assertIn("bitbucket_cloud", ATLASSIAN_PRODUCTS)

    def test_capability_filter(self):
        rows = list_capabilities("jira_cloud")
        self.assertTrue(rows)
        self.assertTrue(all(row["product_id"] == "jira_cloud" for row in rows))

    def test_catalog_does_not_claim_live_connection(self):
        report = readiness_report()
        self.assertEqual(report["status"], "CATALOG_ONLY")
        self.assertFalse(report["live_connection_verified"])

    def test_request_plan_is_domain_intent_not_execution(self):
        plan = self.service.plan("jira_cloud", "list", "projects")
        self.assertEqual(plan.product_id, "jira_cloud")
        self.assertTrue(plan.metadata["execution_required"])
        self.assertEqual(plan.metadata["transport_owned_by"], "API")

    def test_unknown_product_rejected(self):
        with self.assertRaises(KeyError):
            self.service.plan("unknown", "list", "resources")

    def test_admin_product_requires_consent(self):
        with self.assertRaises(PermissionError):
            self.service.plan("admin_identity", "list", "organizations")
        plan = self.service.plan("admin_identity", "list", "organizations", metadata={"admin_consent": True})
        self.assertEqual(plan.product_id, "admin_identity")

    def test_destructive_operation_requires_confirmation(self):
        with self.assertRaises(PermissionError):
            self.service.plan("jira_cloud", "delete", "issues/ABC-1")
        plan = self.service.plan("jira_cloud", "delete", "issues/ABC-1", metadata={"explicit_confirmation": True})
        self.assertEqual(plan.operation, "delete")

    def test_inline_credentials_rejected(self):
        with self.assertRaises(ValueError):
            self.service.plan("jira_cloud", "create", "issues", {"client_secret": "do-not-store"})

if __name__ == "__main__":
    unittest.main()
