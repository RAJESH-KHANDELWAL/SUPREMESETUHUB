"""Taxonomy loader for GLOBAL AI Storage Ecosystem."""
from __future__ import annotations
import json
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
TAXONOMY_PATH = PACKAGE_ROOT / "taxonomy" / "global_ai_storage_taxonomy.json"

def load_taxonomy() -> dict:
    with TAXONOMY_PATH.open("r", encoding="utf-8") as stream:
        return json.load(stream)

def list_categories() -> list[dict]:
    return list(load_taxonomy().get("categories", []))

def find_category(category_id: str) -> dict | None:
    wanted = str(category_id).strip().upper()
    return next((item for item in list_categories()
                 if item.get("category_id", "").upper() == wanted), None)
