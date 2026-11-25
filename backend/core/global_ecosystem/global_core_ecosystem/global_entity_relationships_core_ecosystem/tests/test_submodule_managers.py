"""Tests ensuring all 36 category subfolders contain and expose usable contracts."""
from pathlib import Path
import importlib.util
import unittest

ROOT = Path(__file__).resolve().parents[1]
# Select real category modules by their contract files; this excludes data/tests,
# generated __pycache__, and any unrelated directory automatically.
MODULE_DIRS = sorted(
    folder for folder in ROOT.iterdir()
    if folder.is_dir()
    and (folder / "manager.py").is_file()
    and (folder / "manager.php").is_file()
    and (folder / "__init__.py").is_file()
    and (folder / "README.md").is_file()
    and folder.name not in {"data", "tests"}
)


class SubmoduleContractTests(unittest.TestCase):
    def test_all_category_folders_have_manager_php_init_readme(self):
        self.assertEqual(len(MODULE_DIRS), 36)
        for folder in MODULE_DIRS:
            with self.subTest(folder=folder.name):
                for name in ("manager.py", "manager.php", "__init__.py", "README.md"):
                    self.assertTrue((folder / name).is_file(), f"missing {name} in {folder.name}")
                    self.assertGreater((folder / name).stat().st_size, 0, f"empty {name} in {folder.name}")

    def test_all_managers_follow_global_naming_and_metadata_only_boundary(self):
        ids = []
        for folder in MODULE_DIRS:
            with self.subTest(folder=folder.name):
                spec = importlib.util.spec_from_file_location(f"manager_{folder.name}", folder / "manager.py")
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                manager = module.get_manager()
                status = manager.status()
                self.assertTrue(status["name"].startswith("GLOBAL "))
                self.assertTrue(status["name"].endswith(" CORE ECOSYSTEM"))
                self.assertTrue(status["ecosystem_id"].startswith("GLOBAL-"))
                self.assertTrue(status["ecosystem_id"].endswith("-CORE-ECOSYSTEM"))
                self.assertFalse(status["live_connection_verified"])
                self.assertFalse(status["persistence_enabled"])
                ids.append(status["ecosystem_id"])
        self.assertEqual(len(ids), len(set(ids)))

    def test_category_contracts_reject_missing_fields_and_accept_complete_unverified_records(self):
        for folder in MODULE_DIRS:
            spec = importlib.util.spec_from_file_location(f"contract_{folder.name}", folder / "manager.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            manager = module.get_manager()
            required = manager.get_required_fields()
            with self.subTest(folder=folder.name):
                with self.assertRaises(module.ValidationError):
                    manager.validate({})
                complete = {field: "sample-value" for field in required}
                complete.update({
                    "relationship_id": "test-rel",
                    "source_entity_id": "entity-a",
                    "target_entity_id": "entity-b",
                    "relationship_type": "affiliated_with",
                    "verification_status": "UNVERIFIED",
                })
                self.assertTrue(manager.validate(complete)["valid"])

    def test_verified_relationship_requires_evidence(self):
        folder = ROOT / "global_entity_relationships_core_ecosystem"
        spec = importlib.util.spec_from_file_location("verification_manager", folder / "manager.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        manager = module.get_manager()
        record = {
            "relationship_id": "r",
            "source_entity_id": "a",
            "target_entity_id": "b",
            "relationship_type": "affiliated_with",
            "verification_status": "VERIFIED",
            "source_urls": [],
        }
        with self.assertRaises(module.ValidationError):
            manager.validate(record)
        record["source_urls"] = ["https://example.org/evidence"]
        self.assertTrue(manager.validate(record)["valid"])


if __name__ == "__main__":
    unittest.main()
