"""Contract and inventory tests for Global Developer Core."""
import json
import unittest
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.global_developer_core_ecosystem.catalog import (
    PROVIDER_PACKAGES, get_developer_core_catalog, get_developer_core_provider,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_developer_core_ecosystem.policy import (
    adult_provider_enabled, validate_metadata,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_developer_core_ecosystem.service import (
    GlobalDeveloperCoreService,
)

ROOT = Path(__file__).resolve().parents[1]
API_ROOT = Path("backend/api/global_ecosystem/global_api_ecosystem/global_developer_api_ecosystem")
TEN_FOLDERS = {"authentication","capabilities","docs","events","lifecycle","models","schemas","security","services","tests"}

class TestGlobalDeveloperCore(unittest.TestCase):
    def test_catalog_identity_and_provider_count(self):
        catalog = get_developer_core_catalog()
        self.assertEqual(catalog["ecosystem_id"], "GLOBAL-DEVELOPER-CORE-ECOSYSTEM")
        self.assertEqual(catalog["parent_id"], "GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(catalog["provider_count"], 29)
        self.assertEqual(len(catalog["providers"]), 29)

    def test_core_provider_inventory_matches_api_package_directories(self):
        api_ids = {
            p.name.removesuffix("_api_ecosystem")
            for p in API_ROOT.iterdir()
            if p.is_dir() and p.name.endswith("_api_ecosystem")
        }
        self.assertEqual(set(PROVIDER_PACKAGES), api_ids)

    def test_all_provider_packages_follow_google_ten_folder_standard(self):
        self.assertEqual(len(PROVIDER_PACKAGES), 29)
        for provider_id in PROVIDER_PACKAGES:
            package = ROOT / f"{provider_id}_core_ecosystem"
            self.assertTrue((package / "README.md").is_file(), provider_id)
            self.assertTrue((package / "ecosystem_manifest.json").is_file(), provider_id)
            self.assertTrue((package / "ecosystem_config.py").is_file(), provider_id)
            self.assertTrue((package / "contracts.py").is_file(), provider_id)
            manifest = json.loads((package / "ecosystem_manifest.json").read_text())
            self.assertEqual(set(manifest["folders"]), TEN_FOLDERS, provider_id)
            for folder in TEN_FOLDERS:
                self.assertTrue((package / folder / "README.md").is_file(), f"{provider_id}/{folder}")
            self.assertTrue((package / "authentication/contract.php").is_file(), provider_id)

    def test_every_provider_is_catalog_only_and_not_live_verified(self):
        for provider in get_developer_core_catalog()["providers"]:
            self.assertEqual(provider["status"], "CORE_CATALOG_ONLY")
            self.assertFalse(provider["connected"])
            self.assertFalse(provider["live_connection_verified"])
            self.assertIsNone(provider["api_available"])

    def test_provider_lookup_accepts_canonical_id(self):
        record = get_developer_core_provider("github_developer")
        self.assertIsNotNone(record)
        self.assertEqual(record["api_catalog_ref"], f"{API_ROOT}/github_developer_api_ecosystem")

    def test_secret_material_is_rejected_recursively(self):
        self.assertTrue(validate_metadata({"tenant_id": "t1", "filters": {"api_key": "do-not-store"}})["errors"])
        self.assertTrue(validate_metadata({"metadata": [{"refresh_token": "x"}]})["errors"])
        self.assertTrue(validate_metadata({"tenant_id": "t1"})["allowed"])

    def test_adult_only_provider_requires_all_review_gates(self):
        self.assertFalse(adult_provider_enabled("adult_creator_business"))
        self.assertFalse(adult_provider_enabled("adult_creator_business", explicit_review=True, age_assurance_verified=True, consent_controls_verified=True))
        self.assertTrue(adult_provider_enabled("adult_creator_business", explicit_review=True, age_assurance_verified=True, consent_controls_verified=True, jurisdiction_reviewed=True))
        self.assertTrue(adult_provider_enabled("github_developer"))

    def test_service_reports_catalog_only_without_external_calls(self):
        status = GlobalDeveloperCoreService().status()
        self.assertEqual(status["provider_count"], 29)
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["external_api_calls"], 0)

    def test_global_core_parent_registry_contains_developer_core(self):
        from backend.core.global_ecosystem.global_core_ecosystem.catalog import get_category_catalog
        records = {x["ecosystem_id"]: x for x in get_category_catalog()}
        record = records["GLOBAL-DEVELOPER-CORE-ECOSYSTEM"]
        self.assertEqual(record["parent_id"], "GLOBAL-CORE-ECOSYSTEM")

if __name__ == "__main__":
    unittest.main()
