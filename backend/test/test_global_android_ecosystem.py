"""Integration tests for the Backend and Frontend Android ecosystem managers."""

import unittest

from backend.android.global_ecosystem.global_android_ecosystem import get_manager
from frontend.android.global_ecosystem.global_android_ecosystem import (
    FrontendGlobalAndroidEcosystemManager,
    get_manager as get_frontend_manager,
)


class GlobalAndroidEcosystemIntegrationTests(unittest.TestCase):
    def test_backend_manager_is_structure_ready(self):
        status = get_manager().status()
        self.assertEqual(status["ecosystem"], "GLOBAL_ANDROID_ECOSYSTEM")
        self.assertEqual(status["status"], "STRUCTURE_READY")
        self.assertEqual(status["backend_root"], "backend/android")
        self.assertFalse(status["build_verified"])

    def test_frontend_manager_is_structure_ready(self):
        manager = get_frontend_manager()
        self.assertIsInstance(manager, FrontendGlobalAndroidEcosystemManager)
        status = manager.status()
        self.assertEqual(status["status"], "STRUCTURE_READY")
        self.assertEqual(status["frontend_root"], "frontend/android")
        self.assertFalse(status["build_verified"])


if __name__ == "__main__":
    unittest.main()
