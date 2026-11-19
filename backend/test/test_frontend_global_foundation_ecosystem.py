"""Tests for the frontend Global Foundation Ecosystem."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[2]
FRONTEND = ROOT / "frontend" / "foundation" / "global_ecosystem"
PACKAGE = FRONTEND / "global_foundation_ecosystem"


def load_module(path, name):
    spec = spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FrontendGlobalFoundationEcosystemTests(unittest.TestCase):
    def test_frontend_parent_manager_health(self):
        manager = load_module(FRONTEND / "manager.py", "frontend_global_ecosystem_manager").get_manager()
        report = manager.health()
        self.assertTrue(report["healthy"], report)

    def test_frontend_foundation_manager_health(self):
        manager = load_module(PACKAGE / "manager.py", "frontend_global_foundation_manager").get_manager()
        report = manager.health()
        self.assertTrue(report["healthy"], report)

    def test_frontend_connector_detects_both_sides(self):
        connector = load_module(
            PACKAGE / "frontend_global_foundation_ecosystem_backend_global_foundation_ecosystem_connect.py",
            "frontend_global_foundation_connector",
        ).connect_foundations()
        self.assertTrue(connector["connected"], connector)

    @unittest.skipUnless(shutil.which("php"), "PHP CLI is not installed")
    def test_frontend_php_files_pass_syntax_check(self):
        files = (
            FRONTEND / "manager.php",
            PACKAGE / "manager.php",
            PACKAGE / "frontend_global_foundation_ecosystem_backend_global_foundation_ecosystem_connect.php",
        )
        for path in files:
            result = subprocess.run(["php", "-l", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
