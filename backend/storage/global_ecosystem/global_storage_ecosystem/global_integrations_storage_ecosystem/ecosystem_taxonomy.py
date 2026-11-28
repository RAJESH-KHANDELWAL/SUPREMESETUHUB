"""API-aligned taxonomy loader for GLOBAL INTEGRATIONS storage namespaces."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

TAXONOMY_PATH = Path(__file__).with_name("taxonomy") / "global_integrations_storage_taxonomy.json"

def load_taxonomy() -> dict[str, Any]:
    data = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    if data.get("ecosystem_id") != "GLOBAL_INTEGRATIONS_STORAGE_ECOSYSTEM":
        raise ValueError("Unexpected GLOBAL INTEGRATIONS storage taxonomy identity")
    return data

def list_ecosystems() -> list[dict[str, str]]:
    return [dict(row) for group in load_taxonomy()["groups"] for row in group["categories"]]

def find_ecosystem(name: str) -> dict[str, str] | None:
    needle = name.strip().upper()
    return next((row for row in list_ecosystems() if row["category"] == needle or row["storage_folder"].upper() == needle), None)
