"""Tests for the backend Global Foundation Ecosystem and consolidated layout."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "backend" / "foundation" / "global_ecosystem"
PACKAGE = BACKEND / "global_foundation_ecosystem"
CONSOLIDATED_FOLDERS = (
    "android", "audit", "core", "dependencies", "file_manager",
    "identity", "registry", "security", "sync",
)

def load_module(path, name):
    spec = spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class BackendGlobalFoundationEcosystemTests(unittest.TestCase):
    def test_backend_parent_manager_health(self):
        manager = load_module(BACKEND / "manager.py", "backend_global_ecosystem_manager").get_manager()
        report = manager.health()
        self.assertTrue(report["healthy"], report)

    def test_backend_foundation_manager_health(self):
        manager = load_module(PACKAGE / "manager.py", "backend_global_foundation_manager").get_manager()
        report = manager.health()
        self.assertTrue(report["healthy"], report)

    def test_remaining_foundation_folders_are_consolidated(self):
        missing = [name for name in CONSOLIDATED_FOLDERS if not (PACKAGE / name).is_dir()]
        self.assertEqual(missing, [], f"Missing consolidated folders: {missing}")
        misplaced = [name for name in CONSOLIDATED_FOLDERS if (ROOT / "backend" / "foundation" / name).exists()]
        self.assertEqual(misplaced, [], f"Folders remain outside ecosystem: {misplaced}")

    def test_backend_connector_detects_both_sides(self):
        connector = load_module(
            PACKAGE / "backend_global_foundation_ecosystem_frontend_global_foundation_ecosystem_connect.py",
            "backend_global_foundation_connector",
        ).connect_foundations()
        self.assertTrue(connector["connected"], connector)

    @unittest.skipUnless(shutil.which("php"), "PHP CLI is not installed")
    def test_backend_php_files_pass_syntax_check(self):
        files = (
            BACKEND / "manager.php",
            PACKAGE / "manager.php",
            PACKAGE / "backend_global_foundation_ecosystem_frontend_global_foundation_ecosystem_connect.php",
        )
        for path in files:
            result = subprocess.run(["php", "-l", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

if __name__ == "__main__":
    unittest.main()
