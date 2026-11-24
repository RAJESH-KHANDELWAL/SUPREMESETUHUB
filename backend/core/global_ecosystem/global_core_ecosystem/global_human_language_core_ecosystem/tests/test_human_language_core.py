from __future__ import annotations

import json
import unittest
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.global_human_language_core_ecosystem import manager
from backend.core.global_ecosystem.global_core_ecosystem.global_human_language_core_ecosystem.master_catalog import (
    get_adjacent_master_entries,
    get_language_master_entries,
    master_catalog_mapping_summary,
)


class HumanLanguageCoreTests(unittest.TestCase):
    def test_manager_contract(self):
        self.assertEqual(manager.describe()["ecosystem_id"], "GLOBAL-HUMAN-LANGUAGE-CORE-ECOSYSTEM")
        self.assertEqual(manager.status()["api_calls_performed"], 0)
        self.assertFalse(manager.health()["live_connections_verified"])

    def test_domain_and_provider_registries_are_unique(self):
        data = manager.catalog()
        self.assertEqual(data["domain_count"], len({x["id"] for x in data["domains"]}))
        self.assertEqual(data["provider_count"], len({x["provider_id"] for x in data["providers"]}))

    def test_master_catalog_is_read_only_and_mapped_by_source_id(self):
        entries = get_language_master_entries()
        self.assertTrue(entries)
        self.assertEqual({x["entry_id"] for x in entries}, {"S02_language"})
        summary = master_catalog_mapping_summary()
        self.assertTrue(summary["source_is_read_only"])
        self.assertFalse(summary["mapping_is_exhaustive"])
        self.assertEqual(summary["source_file"], "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json")

    def test_adjacent_context_is_not_reclassified_as_language(self):
        adjacent = get_adjacent_master_entries()
        self.assertEqual(
            {x["entry_id"] for x in adjacent},
            {"S02_education", "S02_culture", "S04_communication"},
        )
        self.assertNotIn("S02_education", {x["entry_id"] for x in get_language_master_entries()})

    def test_master_catalog_target_is_not_claimed_as_current_coverage(self):
        summary = master_catalog_mapping_summary()
        self.assertGreater(summary["target_unique_entries"], summary["current_unique_entries"])


if __name__ == "__main__":
    unittest.main()
