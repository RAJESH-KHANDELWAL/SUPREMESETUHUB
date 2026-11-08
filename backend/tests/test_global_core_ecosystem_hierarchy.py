"""Tests for the mirrored GLOBAL CORE ECOSYSTEM hierarchy."""

import unittest

from backend.core.global_ecosystem.global_core_ecosystem import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    GlobalEcosystemManager,
    get_module,
    list_modules,
    status as core_ecosystem_status,
    tree as core_ecosystem_tree,
)


class TestGlobalCoreEcosystemHierarchy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = GlobalEcosystemManager()

    def test_health_uses_global_core_ecosystem(self):
        result = self.manager.health()
        self.assertTrue(result["success"])
        self.assertTrue(result["root_exists"])
        self.assertTrue(result["core_exists"])

    def test_public_package_entry_point_uses_canonical_registry_identity(self):
        self.assertEqual(ECOSYSTEM_ID, "GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(ECOSYSTEM_NAME, "GLOBAL CORE ECOSYSTEM")
        result = core_ecosystem_status()
        self.assertEqual(result["ecosystem_id"], "GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(result["ecosystem"], "GLOBAL CORE ECOSYSTEM")
        self.assertTrue(result["success"])

    def test_public_package_lists_and_retrieves_core_modules(self):
        listing = list_modules()
        self.assertTrue(listing["success"])
        self.assertGreater(listing["count"], 0)
        self.assertTrue(listing["items"])

        result = get_module("GLOBAL-CORE-ECOSYSTEM")
        self.assertTrue(result["success"])
        self.assertEqual(
            result["item"]["ecosystem_id"],
            "GLOBAL-CORE-ECOSYSTEM",
        )

    def test_public_package_tree_exposes_core_hierarchy(self):
        result = core_ecosystem_tree()
        self.assertTrue(result["success"])
        self.assertEqual(result["id"], "GLOBAL-CORE-ECOSYSTEM")
        root = result["children"][0]
        core = next(
            child
            for child in root["children"]
            if child["ecosystem_id"] == "GLOBAL-CORE-ECOSYSTEM"
        )
        child_ids = {child["ecosystem_id"] for child in core["children"]}
        self.assertIn("GLOBAL-BUSINESS-CORE-ECOSYSTEM", child_ids)
        self.assertIn("GLOBAL-SERVER-CORE-ECOSYSTEM", child_ids)

    def test_core_ecosystem_is_registered_under_global_root(self):
        result = self.manager.get("GLOBAL-CORE-ECOSYSTEM")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "GLOBAL CORE ECOSYSTEM")
        self.assertEqual(result["parent_id"], "GLOBAL-ECOSYSTEM")

    def test_core_service_ecosystems_are_children_of_core(self):
        expected = {
            "GLOBAL-BUSINESS-CORE-ECOSYSTEM",
            "GLOBAL-SERVER-CORE-ECOSYSTEM",
            "GLOBAL-DATABASE-CORE-ECOSYSTEM",
            "GLOBAL-STORAGE-CORE-ECOSYSTEM",
            "GLOBAL-SECURITY-CORE-ECOSYSTEM",
            "GLOBAL-API-CORE-ECOSYSTEM",
            "GLOBAL-AI-CORE-ECOSYSTEM",
            "GLOBAL-SEARCH-CORE-ECOSYSTEM",
            "GLOBAL-BACKUP-CORE-ECOSYSTEM",
            "GLOBAL-LOGGING-CORE-ECOSYSTEM",
            "GLOBAL-NOTIFICATIONS-CORE-ECOSYSTEM",
            "GLOBAL-SETTINGS-CORE-ECOSYSTEM",
        }
        records = {
            item["ecosystem_id"]: item
            for item in self.manager.list()["ecosystems"]
        }
        self.assertTrue(expected.issubset(records))
        for ecosystem_id in expected:
            self.assertEqual(
                records[ecosystem_id]["parent_id"],
                "GLOBAL-CORE-ECOSYSTEM",
                ecosystem_id,
            )

    def test_google_core_and_all_google_children_are_registered(self):
        from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.catalog import (
            get_google_core_catalog,
        )
        self.assertTrue(self.manager.exists("GOOGLE-CORE-ECOSYSTEM"))
        google = self.manager.get("GOOGLE-CORE-ECOSYSTEM")
        self.assertEqual(google["parent_id"], "GLOBAL-CORE-ECOSYSTEM")
        for child in get_google_core_catalog()["children"]:
            record = self.manager.get(child["ecosystem_id"])
            self.assertIsNotNone(record, child["ecosystem_id"])
            self.assertEqual(record["parent_id"], "GOOGLE-CORE-ECOSYSTEM")

    def test_google_core_family_packages_match_all_registered_children(self):
        import importlib
        from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.catalog import (
            get_google_core_catalog,
        )

        family_folders = {
            "GOOGLE-GMAIL-CORE-ECOSYSTEM": "google_gmail_core_ecosystem",
            "GOOGLE-DRIVE-CORE-ECOSYSTEM": "google_drive_core_ecosystem",
            "GOOGLE-CALENDAR-CORE-ECOSYSTEM": "google_calendar_core_ecosystem",
            "GOOGLE-CONTACTS-CORE-ECOSYSTEM": "google_contacts_core_ecosystem",
            "GOOGLE-SHEETS-CORE-ECOSYSTEM": "google_sheets_core_ecosystem",
            "GOOGLE-DOCS-CORE-ECOSYSTEM": "google_docs_core_ecosystem",
            "GOOGLE-SLIDES-CORE-ECOSYSTEM": "google_slides_core_ecosystem",
            "GOOGLE-FORMS-CORE-ECOSYSTEM": "google_forms_core_ecosystem",
            "GOOGLE-CHAT-CORE-ECOSYSTEM": "google_chat_core_ecosystem",
            "GOOGLE-MEET-CORE-ECOSYSTEM": "google_meet_core_ecosystem",
            "GOOGLE-ADMIN-SDK-CORE-ECOSYSTEM": "google_admin_sdk_core_ecosystem",
            "GOOGLE-PEOPLE-CORE-ECOSYSTEM": "google_people_core_ecosystem",
            "GOOGLE-YOUTUBE-CORE-ECOSYSTEM": "google_youtube_core_ecosystem",
            "GOOGLE-MAPS-CORE-ECOSYSTEM": "google_maps_platform_core_ecosystem",
            "GOOGLE-BUSINESS-PROFILE-CORE-ECOSYSTEM": "google_business_profile_core_ecosystem",
            "GOOGLE-ADS-CORE-ECOSYSTEM": "google_ads_core_ecosystem",
            "GOOGLE-ANALYTICS-CORE-ECOSYSTEM": "google_analytics_core_ecosystem",
            "GOOGLE-SEARCH-CONSOLE-CORE-ECOSYSTEM": "google_search_console_core_ecosystem",
            "GOOGLE-CLOUD-CORE-ECOSYSTEM": "google_cloud_core_ecosystem",
            "GOOGLE-FIREBASE-CORE-ECOSYSTEM": "google_firebase_core_ecosystem",
            "GOOGLE-IDENTITY-OAUTH-CORE-ECOSYSTEM": "google_identity_oauth_core_ecosystem",
            "GOOGLE-GEMINI-CORE-ECOSYSTEM": "google_gemini_core_ecosystem",
            "GOOGLE-VERTEX-AI-CORE-ECOSYSTEM": "google_vertex_ai_core_ecosystem",
        }
        package_root = "backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem"
        catalog_ids = {child["ecosystem_id"] for child in get_google_core_catalog()["children"]}
        self.assertEqual(catalog_ids, set(family_folders))
        for ecosystem_id, folder in family_folders.items():
            package = importlib.import_module(f"{package_root}.{folder}")
            self.assertEqual(package.ECOSYSTEM_ID, ecosystem_id)

    def test_google_gmail_core_facade_uses_existing_api_service(self):
        from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.gmail_core import (
            GoogleGmailCoreService,
        )
        service = GoogleGmailCoreService()
        self.assertEqual(service.ECOSYSTEM_ID, "GOOGLE-GMAIL-CORE-ECOSYSTEM")
        result = service.status()
        self.assertEqual(result["provider"], "google")
        self.assertFalse(result["live_connection_verified"])

    def test_tree_places_core_under_global_ecosystem(self):
        tree = self.manager.tree()["tree"]
        children = {child["ecosystem_id"]: child for child in tree["children"]}
        core = children["GLOBAL-CORE-ECOSYSTEM"]
        core_children = {child["ecosystem_id"] for child in core["children"]}
        self.assertIn("GLOBAL-BUSINESS-CORE-ECOSYSTEM", core_children)
        self.assertIn("GLOBAL-SERVER-CORE-ECOSYSTEM", core_children)


if __name__ == "__main__":
    unittest.main()
