"""Google storage taxonomy loader."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

TAXONOMY_PATH = Path(__file__).with_name("taxonomy") / "google_storage_taxonomy.json"

def load_taxonomy() -> dict[str, Any]:
    """Load the checked-in taxonomy file."""
    with TAXONOMY_PATH.open("r", encoding="utf-8") as stream:
        data = json.load(stream)
    if data.get("ecosystem_id") != "GOOGLE_STORAGE_ECOSYSTEM":
        raise ValueError("Unexpected taxonomy ecosystem_id")
    return data

def list_ecosystems(*, include_catalog_only: bool = True) -> list[dict[str, Any]]:
    rows = [item for group in load_taxonomy()["categories"] for item in group["items"]]
    return rows if include_catalog_only else [row for row in rows if row.get("status") != "CATALOG_ONLY"]

def find_ecosystem(name: str) -> dict[str, Any] | None:
    normalized = name.strip().upper()
    return next((row for row in list_ecosystems() if row["name"] == normalized or row["id"] == normalized), None)
