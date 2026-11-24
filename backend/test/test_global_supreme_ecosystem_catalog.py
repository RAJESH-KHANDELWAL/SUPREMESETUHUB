"""Regression tests for the GLOBAL TO SUPREME master catalog."""
from __future__ import annotations

from copy import deepcopy
import unittest

from backend.engine.global_ecosystem.global_engine_ecosystem.manager import (
    MASTER_CATALOG_TARGET_UNIQUE_ENTRIES,
    _summarize_master_catalog,
    get_master_catalog,
)


class GlobalSupremeEcosystemCatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.catalog = get_master_catalog()

    def test_current_catalog_metadata_matches_actual_entries(self) -> None:
        summary = _summarize_master_catalog(self.catalog)
        self.assertEqual(summary["target_unique_entry_count"], MASTER_CATALOG_TARGET_UNIQUE_ENTRIES)
        self.assertEqual(summary["unique_entry_count"], 246)
        self.assertEqual(summary["remaining_unique_entries"], 2222)
        self.assertFalse(summary["target_reached"])

    def test_rejects_stale_current_entry_metadata(self) -> None:
        catalog = deepcopy(self.catalog)
        catalog["expansion"]["current_unique_entries"] += 1
        with self.assertRaisesRegex(ValueError, "current_unique_entries mismatch"):
            _summarize_master_catalog(catalog)

    def test_rejects_stale_remaining_entry_metadata(self) -> None:
        catalog = deepcopy(self.catalog)
        catalog["expansion"]["remaining_unique_entries"] -= 1
        with self.assertRaisesRegex(ValueError, "remaining_unique_entries mismatch"):
            _summarize_master_catalog(catalog)

    def test_rejects_duplicate_entry_ids(self) -> None:
        catalog = deepcopy(self.catalog)
        catalog["sections"][1]["entries"][0]["entry_id"] = (
            catalog["sections"][0]["entries"][0]["entry_id"]
        )
        with self.assertRaisesRegex(ValueError, "duplicate master catalog entry_id"):
            _summarize_master_catalog(catalog)

    def test_rejects_duplicate_unique_names(self) -> None:
        catalog = deepcopy(self.catalog)
        catalog["sections"][1]["entries"][0]["name"] = (
            catalog["sections"][0]["entries"][0]["name"]
        )
        with self.assertRaisesRegex(ValueError, "Duplicate unique catalog entry name"):
            _summarize_master_catalog(catalog)

    def test_rejects_invalid_cross_reference(self) -> None:
        catalog = deepcopy(self.catalog)
        cross_reference = next(
            entry
            for section in catalog["sections"]
            for entry in section["entries"]
            if entry.get("entry_kind") == "cross_reference"
        )
        cross_reference["canonical_entry_id"] = "MISSING_CANONICAL_ENTRY"
        with self.assertRaisesRegex(ValueError, "missing/non-canonical entry"):
            _summarize_master_catalog(catalog)


if __name__ == "__main__":
    unittest.main()
