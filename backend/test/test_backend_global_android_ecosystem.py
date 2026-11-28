"""Tests for the Backend Global Android Ecosystem manager."""

import unittest

from backend.android.global_ecosystem.global_android_ecosystem import (
    GlobalAndroidEcosystemManager,
    get_manager,
)


class BackendGlobalAndroidEcosystemTests(unittest.TestCase):
    def test_backend_manager_factory(self):
        self.assertIsInstance(get_manager(), GlobalAndroidEcosystemManager)

    def test_backend_manager_contract(self):
        manager = get_manager()
        contract = manager.project_contract()
        self.assertEqual(contract["ecosystem"], "GLOBAL_ANDROID_ECOSYSTEM")
        self.assertEqual(contract["backend_root"], "backend/android")
        self.assertEqual(
            contract["backend_ecosystem_path"],
            "backend/android/global_ecosystem/global_android_ecosystem",
        )

    def test_backend_manager_status(self):
        status = get_manager().status()
        self.assertEqual(status["name"], "GLOBAL ANDROID ECOSYSTEM")
        self.assertEqual(status["status"], "STRUCTURE_READY")
        self.assertFalse(status["build_verified"])


if __name__ == "__main__":
    unittest.main()
