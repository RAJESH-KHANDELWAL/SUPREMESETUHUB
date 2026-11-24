"""GitHub storage taxonomy loader and lookup helpers."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

TAXONOMY_PATH = Path(__file__).with_name("taxonomy") / "github_storage_taxonomy.json"

def load_taxonomy() -> dict[str, Any]:
    with TAXONOMY_PATH.open("r", encoding="utf-8") as stream:
        data = json.load(stream)
    if data.get("ecosystem_id") != "GITHUB_STORAGE_ECOSYSTEM":
        raise ValueError("Unexpected taxonomy ecosystem_id")
    return data

def list_ecosystems() -> list[dict[str, str]]:
    rows = []
    for group in load_taxonomy()["groups"]:
        for category in group["categories"]:
            rows.append({"group": group["group"], "category": category, "name": f"GITHUB_{category}_STORAGE_ECOSYSTEM", "status": "CATALOG_ONLY", "provider_product_verified": "false"})
    return rows

def find_ecosystem(name: str) -> dict[str, str] | None:
    needle = name.strip().upper()
    return next((row for row in list_ecosystems() if row["name"] == needle or row["category"] == needle), None)
