"""Read-only bridge to the repository's 2468-target master ecosystem catalog.

Only explicitly mapped human-language records are surfaced. The master file
remains the single source of truth; this module never copies or mutates it.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

MASTER_CATALOG_RELATIVE_PATH = Path("backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json")
REPOSITORY_ROOT = Path(__file__).resolve().parents[4]
MASTER_CATALOG_PATH = REPOSITORY_ROOT / MASTER_CATALOG_RELATIVE_PATH

# Exact source IDs from the master catalog. Adjacent topics are contextual,
# not reclassified as language domains.
LANGUAGE_SOURCE_ENTRY_IDS = frozenset({"S02_language"})
ADJACENT_SOURCE_ENTRY_IDS = frozenset({"S02_education", "S02_culture", "S04_communication"})


def load_master_catalog() -> dict[str, Any]:
    if not MASTER_CATALOG_PATH.is_file():
        raise FileNotFoundError(f"MASTER_ECOSYSTEM_CATALOG_NOT_FOUND: {MASTER_CATALOG_PATH}")
    return json.loads(MASTER_CATALOG_PATH.read_text(encoding="utf-8"))


def _indexed_entries(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for section in catalog.get("sections", []):
        for entry in section.get("entries", []):
            entry_id = entry.get("entry_id")
            if entry_id:
                result[entry_id] = {
                    **entry,
                    "source_section_id": section.get("section_id"),
                    "source_section_title": section.get("title"),
                }
    return result


def get_language_master_entries() -> list[dict[str, Any]]:
    entries = _indexed_entries(load_master_catalog())
    return [dict(entries[key]) for key in sorted(LANGUAGE_SOURCE_ENTRY_IDS) if key in entries]


def get_adjacent_master_entries() -> list[dict[str, Any]]:
    entries = _indexed_entries(load_master_catalog())
    return [dict(entries[key]) for key in sorted(ADJACENT_SOURCE_ENTRY_IDS) if key in entries]


def master_catalog_mapping_summary() -> dict[str, Any]:
    catalog = load_master_catalog()
    expansion = catalog.get("expansion", {})
    return {
        "source_file": MASTER_CATALOG_RELATIVE_PATH.as_posix(),
        "target_unique_entries": expansion.get("target_unique_entries"),
        "current_unique_entries": expansion.get("current_unique_entries"),
        "remaining_unique_entries": expansion.get("remaining_unique_entries"),
        "source_catalog_status": expansion.get("status"),
        "language_source_entry_count": len(get_language_master_entries()),
        "adjacent_context_entry_count": len(get_adjacent_master_entries()),
        "mapping_is_exhaustive": False,
        "source_is_read_only": True,
    }
