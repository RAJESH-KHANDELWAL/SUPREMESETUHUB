"""Python integration tests for Backend Global Android Ecosystem."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = (
    ROOT / "backend" / "android" / "global_ecosystem"
    / "global_android_ecosystem"
)
MANAGER_FILE = PACKAGE / "manager.py"
FOUNDATION_MANAGER_FILE = (
    ROOT / "backend" / "foundation" / "global_ecosystem"
    / "global_foundation_ecosystem" / "android" / "manager.py"
)


def load_module(path, module_name):
    spec = spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GlobalAndroidEcosystemTests(unittest.TestCase):
    def test_package_files_exist(self):
        self.assertTrue((PACKAGE / "README.md").is_file())
        self.assertTrue((PACKAGE / "__init__.py").is_file())
        self.assertTrue(MANAGER_FILE.is_file())
        self.assertTrue(FOUNDATION_MANAGER_FILE.is_file())

    def test_manager_resolves_android_component(self):
        module = load_module(MANAGER_FILE, "global_android_ecosystem_manager")
        manager = module.get_manager()

        self.assertIsInstance(manager, module.GlobalAndroidEcosystemManager)
        self.assertEqual(
            manager.get_component().__class__.__name__,
            "AndroidFoundationManager",
        )

    def test_ecosystem_status_and_contract(self):
        module = load_module(MANAGER_FILE, "global_android_ecosystem_status_manager")
        manager = module.get_manager()
        status = manager.status()
        contract = manager.project_contract()

        self.assertEqual(status["status"], "INTEGRATED")
        self.assertEqual(status["ecosystem"], "GLOBAL_ANDROID_ECOSYSTEM")
        self.assertEqual(status["project_path"], "backend/mobile/android")
        self.assertFalse(status["build_verified"])
        self.assertEqual(contract["application_id"], "com.mainbasefoundation.android")


if __name__ == "__main__":
    unittest.main()
