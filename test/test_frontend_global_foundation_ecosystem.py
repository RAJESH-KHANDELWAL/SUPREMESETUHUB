"""Frontend-side tests for Foundation and Infrastructure ecosystem connectors."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[2]
FOUNDATION = ROOT / "frontend" / "foundation"
GLOBAL_ECOSYSTEM = FOUNDATION / "global_ecosystem"
PACKAGE = GLOBAL_ECOSYSTEM / "global_foundation_ecosystem"


def load_module(path, name):
    spec = spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FrontendGlobalFoundationEcosystemTests(unittest.TestCase):
    def test_frontend_parent_manager_health(self):
        report = load_module(GLOBAL_ECOSYSTEM / "manager.py", "frontend_global_ecosystem_manager").get_manager().health()
        self.assertTrue(report["healthy"], report)

    def test_frontend_foundation_manager_health(self):
        report = load_module(PACKAGE / "manager.py", "frontend_global_foundation_manager").get_manager().health()
        self.assertTrue(report["healthy"], report)

    def test_frontend_to_backend_foundation_connector(self):
        result = load_module(
            PACKAGE / "frontend_global_foundation_ecosystem_backend_global_foundation_ecosystem_connect.py",
            "frontend_global_foundation_connector",
        ).connect_foundations()
        self.assertTrue(result["connected"], result)

    def test_frontend_foundation_to_backend_infrastructure_connector(self):
        result = load_module(
            PACKAGE / "frontend_global_foundation_ecosystem_backend_global_infrastructure_ecosystem_connect.py",
            "frontend_foundation_backend_infrastructure_ecosystem_connector",
        ).connect_ecosystems()
        self.assertTrue(result["connected"], result)

    def test_frontend_foundation_to_backend_infrastructure_root_connector(self):
        result = load_module(
            FOUNDATION / "frontend_foundation_backend_infrastructure_connect.py",
            "frontend_foundation_backend_infrastructure_connector",
        ).connect_frontend_foundation_backend_infrastructure()
        self.assertTrue(result["connected"], result)

    def test_frontend_global_infrastructure_to_backend_global_foundation_connector(self):
        connector = (
            ROOT / "frontend" / "infrastructure" / "global_ecosystem"
            / "global_infrastructure_ecosystem"
            / "frontend_global_infrastructure_ecosystem_backend_global_foundation_ecosystem_connect.py"
        )
        result = load_module(connector, "frontend_global_infrastructure_backend_foundation").connect_ecosystems()
        self.assertTrue(result["connected"], result)

    @unittest.skipUnless(shutil.which("php"), "PHP CLI is not installed")
    def test_frontend_php_files_pass_syntax_check(self):
        files = (
            FOUNDATION / "manager.php",
            FOUNDATION / "frontend_foundation_backend_infrastructure_connect.php",
            GLOBAL_ECOSYSTEM / "manager.php",
            PACKAGE / "manager.php",
            PACKAGE / "frontend_global_foundation_ecosystem_backend_global_foundation_ecosystem_connect.php",
            PACKAGE / "frontend_global_foundation_ecosystem_backend_global_infrastructure_ecosystem_connect.php",
            ROOT / "frontend/infrastructure/global_ecosystem/global_infrastructure_ecosystem/frontend_global_infrastructure_ecosystem_backend_global_foundation_ecosystem_connect.php",
        )
        for path in files:
            result = subprocess.run(["php", "-l", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, f"{path}: {result.stdout}{result.stderr}")


if __name__ == "__main__":
    unittest.main()
