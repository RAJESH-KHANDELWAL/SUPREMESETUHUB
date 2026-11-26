"""Contract tests for the Backend Global Android ecosystem manager."""

import unittest

from backend.android.global_ecosystem.global_android_ecosystem import (
    GlobalAndroidEcosystemManager,
    get_manager,
)


class GlobalAndroidEcosystemTests(unittest.TestCase):
    def test_factory_returns_backend_manager(self):
        self.assertIsInstance(get_manager(), GlobalAndroidEcosystemManager)

    def test_manager_exposes_independent_backend_and_frontend_roots(self):
        contract = get_manager().project_contract()
        self.assertEqual(contract["ecosystem"], "GLOBAL_ANDROID_ECOSYSTEM")
        self.assertEqual(contract["backend_root"], "backend/android")
        self.assertEqual(contract["frontend_root"], "frontend/android")
        self.assertEqual(
            contract["backend_ecosystem_path"],
            "backend/android/global_ecosystem/global_android_ecosystem",
        )
        self.assertEqual(
            contract["frontend_ecosystem_path"],
            "frontend/android/global_ecosystem/global_android_ecosystem",
        )
        self.assertFalse(contract["native_build_configured"])

    def test_status_does_not_claim_build_verification(self):
        status = get_manager().status()
        self.assertEqual(status["status"], "STRUCTURE_READY")
        self.assertFalse(status["build_verified"])


if __name__ == "__main__":
    unittest.main()
