"""Python contract tests for the canonical Backend Android Foundation."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
ANDROID_FOUNDATION_MANAGER = (
    ROOT / "backend" / "foundation" / "global_ecosystem"
    / "global_foundation_ecosystem" / "android" / "manager.py"
)
ANDROID_BUILD_FILE = ROOT / "backend" / "mobile" / "android" / "app" / "build.gradle"


def load_manager(path, module_name):
    spec = spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load manager: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BackendAndroidFoundationTests(unittest.TestCase):
    def test_canonical_android_project_files_exist(self):
        self.assertTrue(ANDROID_FOUNDATION_MANAGER.is_file())
        self.assertTrue(ANDROID_BUILD_FILE.is_file())

    def test_android_foundation_contract(self):
        manager_class = load_manager(
            ANDROID_FOUNDATION_MANAGER, "backend_android_foundation_manager"
        ).AndroidFoundationManager
        contract = manager_class().project_contract()

        self.assertEqual(contract["project_path"], "backend/mobile/android")
        self.assertEqual(contract["app_module_path"], "backend/mobile/android/app")
        self.assertEqual(contract["application_id"], "com.mainbasefoundation.android")
        self.assertEqual(contract["namespace"], "com.mainbasefoundation.android")
        self.assertEqual(contract["compile_sdk"], 36)
        self.assertEqual(contract["min_sdk"], 26)
        self.assertEqual(contract["target_sdk"], 36)
        self.assertEqual(contract["java_version"], 17)
        self.assertEqual(contract["release_task"], ":app:bundleRelease")

    def test_android_foundation_status_does_not_claim_build_verification(self):
        manager_class = load_manager(
            ANDROID_FOUNDATION_MANAGER, "backend_android_foundation_status_manager"
        ).AndroidFoundationManager
        status = manager_class().status()

        self.assertEqual(status["status"], "CONFIGURED")
        self.assertFalse(status["build_verified"])


if __name__ == "__main__":
    unittest.main()
