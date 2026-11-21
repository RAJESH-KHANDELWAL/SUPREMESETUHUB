"""Read-only mapping to the canonical 2468-target master catalogue."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

MASTER_CATALOG_PATH = Path(__file__).resolve().parents[3] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
RELEVANT_ENTRY_IDS = ("S07_adult_photography", "S07_copyright_and_licensing", "S07_consent_verification", "S07_age_verification", "S07_non_consensual_content_prevention",)

def master_catalog_status() -> dict[str, Any]:
    if not MASTER_CATALOG_PATH.is_file():
        return {"available": False, "source": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json", "access_mode": "READ_ONLY", "error": "MASTER_CATALOG_NOT_FOUND"}
    try:
        data = json.loads(MASTER_CATALOG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"available": False, "access_mode": "READ_ONLY", "error": type(exc).__name__}
    entries = {entry.get("entry_id"): entry for section in data.get("sections", []) for entry in section.get("entries", [])}
    refs = [entries[key] for key in RELEVANT_ENTRY_IDS if key in entries]
    expansion = data.get("expansion", {})
    return {"available": True, "catalogue_id": data.get("catalogue_id"), "target_unique_entries": expansion.get("target_unique_entries"), "current_unique_entries": expansion.get("current_unique_entries"), "remaining_unique_entries": expansion.get("remaining_unique_entries"), "referenced_entry_count": len(refs), "references": refs, "source": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json", "access_mode": "READ_ONLY"}
