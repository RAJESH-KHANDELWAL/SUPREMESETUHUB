"""Contract tests for the Backend Global Android ecosystem adapter."""

import unittest

from backend.android.global_ecosystem.global_android_ecosystem import (
    GlobalAndroidEcosystemManager,
    get_manager,
)
from backend.foundation.global_ecosystem.global_foundation_ecosystem.android import (
    AndroidFoundationManager,
)


class GlobalAndroidEcosystemTests(unittest.TestCase):
    def test_manager_delegates_to_canonical_foundation_component(self):
        component = AndroidFoundationManager()
        manager = GlobalAndroidEcosystemManager(component)

        self.assertIs(manager.get_component(), component)
        self.assertEqual(manager.project_contract(), component.project_contract())

    def test_factory_returns_manager_with_existing_project_contract(self):
        manager = get_manager()
        contract = manager.project_contract()

        self.assertEqual(contract["project_path"], "backend/mobile/android")
        self.assertEqual(contract["app_module_path"], "backend/mobile/android/app")
        self.assertEqual(contract["application_id"], "com.mainbasefoundation.android")
        self.assertEqual(contract["compile_sdk"], 36)
        self.assertEqual(contract["min_sdk"], 26)
        self.assertEqual(contract["java_version"], 17)
        self.assertEqual(contract["release_task"], ":app:bundleRelease")

    def test_status_does_not_claim_build_verified(self):
        status = get_manager().status()

        self.assertEqual(status["status"], "INTEGRATED")
        self.assertFalse(status["build_verified"])


if __name__ == "__main__":
    unittest.main()
