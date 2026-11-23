"""Atlassian Core inventory, package structure and safe-boundary tests."""
import json
import unittest
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.atlassian_core_ecosystem.catalog import get_atlassian_core_catalog
from backend.core.global_ecosystem.global_core_ecosystem.atlassian_core_ecosystem.product_catalog import list_atlassian_offerings
from backend.core.global_ecosystem.global_core_ecosystem.atlassian_core_ecosystem.domain_catalog import atlassian_domain_summary
from backend.core.global_ecosystem.global_core_ecosystem.atlassian_core_ecosystem.service import AtlassianCoreEcosystemService

ROOT = Path(__file__).resolve().parents[1]
FAMILIES = ["atlassian_admin_identity_core_ecosystem","atlassian_bitbucket_core_ecosystem","atlassian_confluence_core_ecosystem","atlassian_jira_core_ecosystem","atlassian_jira_service_management_core_ecosystem"]
STANDARD_DIRS = ["authentication", "capabilities", "docs", "events", "lifecycle", "models", "schemas", "security", "services", "tests"]

class TestAtlassianCoreCatalog(unittest.TestCase):
    def test_provider_inventory_and_safe_readiness(self):
        catalog = get_atlassian_core_catalog()
        self.assertEqual(catalog["provider"], "atlassian")
        self.assertEqual(len(catalog["children"]), 5)
        offerings = list_atlassian_offerings()
        self.assertEqual(len(offerings), 5)
        self.assertTrue(all(item["api_available"] is None for item in offerings))
        self.assertTrue(all(item["live_connection_verified"] is False for item in offerings))

    def test_domain_inventory(self):
        summary = atlassian_domain_summary()
        self.assertEqual(summary["domain_count"], 6)
        self.assertEqual(summary["offering_count"], 5)
        self.assertEqual(summary["live_connections_verified"], 0)

    def test_google_style_package_structure_and_manifests(self):
        for family in FAMILIES:
            package = ROOT / family
            self.assertTrue(package.is_dir(), family)
            for folder in STANDARD_DIRS:
                self.assertTrue((package / folder).is_dir(), f"{family}/{folder}")
            manifest = json.loads((package / "ecosystem_manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["provider"], "atlassian")
            self.assertEqual(manifest["core_layer"], "ATLASSIAN_CORE")
            compile((package / "ecosystem_config.py").read_text(encoding="utf-8"), str(package / "ecosystem_config.py"), "exec")

    def test_provider_service_reports_no_live_connections(self):
        status = AtlassianCoreEcosystemService().status()
        self.assertTrue(status["success"])
        self.assertEqual(status["module_count"], 5)
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["connected_modules"], 0)

if __name__ == "__main__":
    unittest.main()
