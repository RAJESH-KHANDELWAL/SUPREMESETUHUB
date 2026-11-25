"""Backend-side tests for Foundation and Infrastructure ecosystem connectors."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[2]
FOUNDATION = ROOT / "backend" / "foundation"
GLOBAL_ECOSYSTEM = FOUNDATION / "global_ecosystem"
PACKAGE = GLOBAL_ECOSYSTEM / "global_foundation_ecosystem"
# "sync" is a canonical domain, not a legacy consolidated folder.
CONSOLIDATED_FOLDERS = (
    "audit", "core", "dependencies", "file_manager",
    "identity", "registry", "security",
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
        report = load_module(GLOBAL_ECOSYSTEM / "manager.py", "backend_global_ecosystem_manager").get_manager().health()
        self.assertTrue(report["healthy"], report)

    def test_backend_foundation_manager_health(self):
        report = load_module(PACKAGE / "manager.py", "backend_global_foundation_manager").get_manager().health()
        self.assertTrue(report["healthy"], report)

    def test_removed_domain_folders_stay_consolidated(self):
        present = [name for name in CONSOLIDATED_FOLDERS if (PACKAGE / name).exists()]
        self.assertEqual(present, [], f"Unwanted domain folders/files remain: {present}")
        misplaced = [name for name in CONSOLIDATED_FOLDERS if (FOUNDATION / name).exists()]
        self.assertEqual(misplaced, [], f"Unwanted folders remain at foundation root: {misplaced}")

    def test_sync_remains_a_canonical_foundation_domain(self):
        sync_package = PACKAGE / "sync" / "global_ecosystem" / "global_sync_ecosystem"
        self.assertTrue(sync_package.is_dir(), f"Missing canonical sync domain: {sync_package}")
        self.assertTrue((sync_package / "README.md").is_file())

    def test_backend_to_frontend_foundation_connector(self):
        result = load_module(
            PACKAGE / "backend_global_foundation_ecosystem_frontend_global_foundation_ecosystem_connect.py",
            "backend_global_foundation_connector",
        ).connect_foundations()
        self.assertTrue(result["connected"], result)

    def test_backend_foundation_to_frontend_infrastructure_connector(self):
        result = load_module(
            PACKAGE / "backend_global_foundation_ecosystem_frontend_global_infrastructure_ecosystem_connect.py",
            "backend_foundation_frontend_infrastructure_ecosystem_connector",
        ).connect_ecosystems()
        self.assertTrue(result["connected"], result)

    def test_backend_foundation_to_frontend_infrastructure_root_connector(self):
        result = load_module(
            FOUNDATION / "backend_foundation_frontend_infrastructure_connect.py",
            "backend_foundation_frontend_infrastructure_connector",
        ).connect_backend_foundation_frontend_infrastructure()
        self.assertTrue(result["connected"], result)

    def test_backend_global_infrastructure_to_frontend_global_foundation_connector(self):
        connector = (
            ROOT / "backend" / "infrastructure" / "global_ecosystem"
            / "global_infrastructure_ecosystem"
            / "backend_global_infrastructure_ecosystem_frontend_global_foundation_ecosystem_connect.py"
        )
        result = load_module(connector, "backend_global_infrastructure_frontend_foundation").connect_ecosystems()
        self.assertTrue(result["connected"], result)

    @unittest.skipUnless(shutil.which("php"), "PHP CLI is not installed")
    def test_backend_php_files_pass_syntax_check(self):
        files = (
            FOUNDATION / "manager.php",
            FOUNDATION / "backend_foundation_frontend_infrastructure_connect.php",
            GLOBAL_ECOSYSTEM / "manager.php",
            PACKAGE / "manager.php",
            PACKAGE / "backend_global_foundation_ecosystem_frontend_global_foundation_ecosystem_connect.php",
            PACKAGE / "backend_global_foundation_ecosystem_frontend_global_infrastructure_ecosystem_connect.php",
            ROOT / "backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem/backend_global_infrastructure_ecosystem_frontend_global_foundation_ecosystem_connect.php",
        )
        for path in files:
            result = subprocess.run(["php", "-l", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, f"{path}: {result.stdout}{result.stderr}")


if __name__ == "__main__":
    unittest.main()
