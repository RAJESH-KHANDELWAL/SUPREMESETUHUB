"""Read-only, on-demand reference to the canonical Global Supreme master catalog."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
CATALOG_ID = "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
TARGET_UNIQUE_ENTRIES = 2468
CATALOG_RELATIVE_PATH = "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
def catalog_path() -> Path:
    return Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
def reference(*, load_summary: bool = False) -> dict[str, Any]:
    result: dict[str, Any] = {"catalog_id": CATALOG_ID, "target_unique_entries": TARGET_UNIQUE_ENTRIES, "path": CATALOG_RELATIVE_PATH, "access_mode": "READ_ONLY_ON_DEMAND", "loaded": False}
    if not load_summary:
        return result
    path = catalog_path()
    if not path.is_file():
        result.update({"loaded": False, "status": "NOT_FOUND"})
        return result
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        result.update({"loaded": False, "status": "INVALID_OR_UNREADABLE", "error_type": type(exc).__name__})
        return result
    expansion = data.get("expansion", {})
    result.update({"loaded": True, "status": "AVAILABLE", "catalog_id_verified": data.get("catalogue_id") == CATALOG_ID, "target_unique_entries": expansion.get("target_unique_entries"), "current_unique_entries": expansion.get("current_unique_entries"), "remaining_unique_entries": expansion.get("remaining_unique_entries"), "catalog_status": expansion.get("status")})
    return result
