"""Tests for the Frontend Global Android Ecosystem manager."""

import unittest

from frontend.android.global_ecosystem.global_android_ecosystem import (
    FrontendGlobalAndroidEcosystemManager,
    get_manager,
)


class FrontendGlobalAndroidEcosystemTests(unittest.TestCase):
    def test_frontend_manager_factory(self):
        self.assertIsInstance(get_manager(), FrontendGlobalAndroidEcosystemManager)

    def test_frontend_manager_status(self):
        status = get_manager().status()
        self.assertEqual(status["name"], "FRONTEND GLOBAL ANDROID ECOSYSTEM")
        self.assertEqual(status["ecosystem"], "GLOBAL_ANDROID_ECOSYSTEM")
        self.assertEqual(status["frontend_root"], "frontend/android")
        self.assertEqual(status["status"], "STRUCTURE_READY")
        self.assertFalse(status["build_verified"])


if __name__ == "__main__":
    unittest.main()
