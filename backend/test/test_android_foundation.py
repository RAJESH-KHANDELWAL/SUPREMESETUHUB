"""Tests for Android Foundation project contract and ecosystem adapter."""

import unittest

from backend.foundation.global_ecosystem.global_foundation_ecosystem.android import AndroidFoundationManager
from backend.foundation.global_ecosystem.global_foundation_ecosystem.android.global_ecosystem.global_android_ecosystem import (
    GlobalAndroidEcosystemManager,
)


class AndroidFoundationTests(unittest.TestCase):
    def test_android_project_contract_matches_existing_app_configuration(self):
        android = AndroidFoundationManager()
        contract = android.project_contract()

        self.assertEqual(contract["project_path"], "backend/mobile/android")
        self.assertEqual(contract["app_module_path"], "backend/mobile/android/app")
        self.assertEqual(contract["application_id"], "com.mainbasefoundation.android")
        self.assertEqual(contract["namespace"], "com.mainbasefoundation.android")
        self.assertEqual(contract["compile_sdk"], 36)
        self.assertEqual(contract["min_sdk"], 26)
        self.assertEqual(contract["target_sdk"], 36)
        self.assertEqual(contract["java_version"], 17)
        self.assertEqual(contract["release_task"], ":app:bundleRelease")
        self.assertEqual(
            contract["release_artifact"],
            "backend/mobile/android/app/build/outputs/bundle/release/app-release.aab",
        )

    def test_android_ecosystem_wraps_and_delegates_to_original_manager(self):
        component = AndroidFoundationManager()
        ecosystem = GlobalAndroidEcosystemManager(component)

        self.assertIs(ecosystem.get_component(), component)
        self.assertEqual(ecosystem.project_contract(), component.project_contract())
        status = ecosystem.status()
        self.assertEqual(status["status"], "INTEGRATED")
        self.assertEqual(status["ecosystem"], "GLOBAL_ANDROID_ECOSYSTEM")
        self.assertEqual(status["component_key"], "android")

    def test_android_ecosystem_rejects_missing_component(self):
        with self.assertRaisesRegex(ValueError, "Foundation component is required"):
            GlobalAndroidEcosystemManager(None)

    def test_android_status_does_not_claim_build_success(self):
        status = AndroidFoundationManager().status()
        self.assertEqual(status["status"], "CONFIGURED")
        self.assertFalse(status["build_verified"])


if __name__ == "__main__":
    unittest.main()
