"""Adobe storage taxonomy loader and lookup helpers."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
TAXONOMY_PATH = Path(__file__).with_name("taxonomy") / "adobe_storage_taxonomy.json"
def load_taxonomy() -> dict[str, Any]:
    with TAXONOMY_PATH.open("r", encoding="utf-8") as stream:
        data = json.load(stream)
    if data.get("ecosystem_id") != "ADOBE_STORAGE_ECOSYSTEM":
        raise ValueError("Unexpected taxonomy ecosystem_id")
    return data
def list_ecosystems() -> list[dict[str, str]]:
    rows = []
    for group in load_taxonomy()["groups"]:
        for category in group["categories"]:
            rows.append({"group":group["group"],"category":category,
                "name":f"ADOBE_{category.upper()}_STORAGE_ECOSYSTEM",
                "status":"CATALOG_ONLY","external_connection_state":"NOT_CONFIGURED"})
    return rows
def find_ecosystem(name: str) -> dict[str, str] | None:
    needle = name.strip().upper()
    return next((row for row in list_ecosystems()
        if row["name"] == needle or row["category"].upper() == needle), None)
