import json
import unittest
from pathlib import Path

from ..ecosystem_service import EcosystemService
from ..ecosystem_taxonomy import load_taxonomy
from ..ecosystem_models import CloudStorageRecord

ROOT = Path(__file__).resolve().parents[1]


class CloudStorageFoundationTests(unittest.TestCase):
    def test_safe_readiness(self):
        state = EcosystemService().describe()
        self.assertEqual(state["connection_state"], "NOT_CONFIGURED")
        self.assertFalse(state["external_connections_verified"])
        self.assertFalse(state["storage_operations_enabled"])

    def test_taxonomy_has_unique_groups(self):
        taxonomy = load_taxonomy()
        ids = [item["group_id"] for item in taxonomy["groups"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_category_index_matches_manifest_count(self):
        index = json.loads((ROOT / "category_index.json").read_text(encoding="utf-8"))
        manifest = json.loads((ROOT / "ecosystem_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(len(index["folders"]), manifest["category_folder_count"])
        for category in index["folders"]:
            package = ROOT / category["folder"]
            self.assertTrue((package / "README.md").is_file())
            self.assertTrue((package / "ecosystem_manifest.json").is_file())
            self.assertTrue((package / "api" / "routes.py").is_file())
            self.assertTrue((package / "models" / "record.py").is_file())
            self.assertTrue((package / "schemas" / "manifest.schema.json").is_file())
            self.assertTrue((package / "tests" / "test_foundation.py").is_file())
            self.assertTrue((package / "php" / f'{category["folder"]}.php').is_file())

    def test_provider_index_is_metadata_only_and_unconfigured(self):
        index = json.loads((ROOT / "provider_index.json").read_text(encoding="utf-8"))
        self.assertTrue(index["providers"])
        self.assertFalse((ROOT / "providers").exists())
        for provider in index["providers"]:
            self.assertEqual(provider["connection_state"], "NOT_CONFIGURED")
            self.assertNotIn("namespace", provider)

    def test_removed_legacy_group_folders(self):
        self.assertFalse((ROOT / "categories").exists())
        self.assertFalse((ROOT / "providers").exists())

    def test_record_defaults_to_unconfigured(self):
        record = CloudStorageRecord("r1", "AWS", "OBJECT_STORAGE", "Example")
        self.assertEqual(record.connection_state, "NOT_CONFIGURED")

    def test_connection_cannot_be_asserted_by_metadata_record(self):
        with self.assertRaises(ValueError):
            CloudStorageRecord("r2", "AWS", "OBJECT_STORAGE", "Example", connection_state="CONNECTED")


if __name__ == "__main__":
    unittest.main()
