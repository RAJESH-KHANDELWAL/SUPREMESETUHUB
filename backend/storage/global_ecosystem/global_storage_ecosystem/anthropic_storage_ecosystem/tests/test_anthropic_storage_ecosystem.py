import json
import unittest
from pathlib import Path

from ..anthropic_storage_ecosystem import (
    ANTHROPIC_STORAGE_ECOSYSTEM,
    list_anthropic_storage_ecosystems,
)


ROOT = Path(__file__).resolve().parents[1]


class AnthropicStorageEcosystemTests(unittest.TestCase):
    def test_child_ids_and_folders_are_unique(self):
        children = list_anthropic_storage_ecosystems()
        self.assertEqual(len(children), 2)
        self.assertEqual(len({item["id"] for item in children}), len(children))
        self.assertEqual(len({item["folder"] for item in children}), len(children))

    def test_child_readmes_exist(self):
        for item in list_anthropic_storage_ecosystems():
            self.assertTrue((ROOT / item["folder"] / "README.md").is_file())

    def test_manifest_matches_catalog_children(self):
        manifest = json.loads((ROOT / "ecosystem_manifest.json").read_text(encoding="utf-8"))
        catalog_ids = {item["id"] for item in ANTHROPIC_STORAGE_ECOSYSTEM["children"]}
        manifest_ids = {item["id"] for item in manifest["children"]}
        self.assertEqual(catalog_ids, manifest_ids)

    def test_no_live_connection_is_claimed(self):
        self.assertEqual(ANTHROPIC_STORAGE_ECOSYSTEM["connection_state"], "NOT_CONFIGURED")
        self.assertFalse(ANTHROPIC_STORAGE_ECOSYSTEM["external_connections_verified"])

    def test_not_misrepresented_as_general_cloud_storage(self):
        self.assertFalse(ANTHROPIC_STORAGE_ECOSYSTEM["is_general_purpose_cloud_storage"])


if __name__ == "__main__":
    unittest.main()
