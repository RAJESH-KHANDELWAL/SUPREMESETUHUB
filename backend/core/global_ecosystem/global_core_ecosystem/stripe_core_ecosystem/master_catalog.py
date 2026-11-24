"""Read-only bridge to the canonical 2468-target master ecosystem catalog."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

MASTER_CATALOG_PATH = "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_CATALOG_TARGET = 2468
PAYMENT_TERMS = (
    "payment gateway", "payment processing", "merchant acquiring",
    "billing", "settlement", "payout", "refund", "subscription",
    "stripe", "financial payment",
)


def _walk_entries(value: Any):
    if isinstance(value, dict):
        entry_id = value.get("entry_id")
        if isinstance(entry_id, str):
            haystack = " ".join(str(part) for part in value.values()).casefold()
            if any(term in haystack for term in PAYMENT_TERMS):
                yield entry_id
        for child in value.values():
            yield from _walk_entries(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_entries(child)


def get_master_catalog_status() -> dict[str, Any]:
    """Read counts and relevant existing entry IDs; never write or expand the source."""
    path = Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    if not path.is_file():
        return {
            "available": False, "path": MASTER_CATALOG_PATH,
            "access_mode": "READ_ONLY_ON_DEMAND",
            "target_unique_entries": MASTER_CATALOG_TARGET,
            "source_modified": False,
        }
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        expansion = data.get("expansion", {})
        ids = sorted(set(_walk_entries(data)))
        return {
            "available": True,
            "path": MASTER_CATALOG_PATH,
            "catalogue_id": data.get("catalogue_id"),
            "access_mode": "READ_ONLY_ON_DEMAND",
            "target_unique_entries": expansion.get("target_unique_entries", MASTER_CATALOG_TARGET),
            "current_unique_entries": expansion.get("current_unique_entries"),
            "remaining_unique_entries": expansion.get("remaining_unique_entries"),
            "related_existing_entry_ids": ids,
            "related_entry_count": len(ids),
            "taxonomy_entries_added": 0,
            "source_modified": False,
        }
    except (OSError, json.JSONDecodeError, AttributeError, TypeError):
        return {
            "available": False, "path": MASTER_CATALOG_PATH,
            "access_mode": "READ_ONLY_ON_DEMAND",
            "target_unique_entries": MASTER_CATALOG_TARGET,
            "error": "MASTER_CATALOG_READ_FAILED",
            "source_modified": False,
        }


__all__ = ["MASTER_CATALOG_PATH", "MASTER_CATALOG_TARGET", "get_master_catalog_status"]
