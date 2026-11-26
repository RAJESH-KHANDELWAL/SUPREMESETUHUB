"""Structural tests for the Backend and Frontend Android roots."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


class AndroidStructureTests(unittest.TestCase):
    def test_backend_android_entry_point_exists(self):
        package = ROOT / "backend/android/global_ecosystem/global_android_ecosystem"
        self.assertTrue((ROOT / "backend/android/README.md").is_file())
        self.assertTrue((package / "README.md").is_file())
        self.assertTrue((package / "__init__.py").is_file())
        self.assertTrue((package / "manager.py").is_file())

    def test_frontend_android_entry_point_exists(self):
        package = ROOT / "frontend/android/global_ecosystem/global_android_ecosystem"
        self.assertTrue((ROOT / "frontend/android/README.md").is_file())
        self.assertTrue((package / "README.md").is_file())
        self.assertTrue((package / "__init__.py").is_file())
        self.assertTrue((package / "manager.py").is_file())

    def test_deleted_legacy_native_project_is_not_required(self):
        self.assertFalse((ROOT / "backend/mobile/android").exists())


if __name__ == "__main__":
    unittest.main()
