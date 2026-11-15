"""Grouped taxonomy loader and read-only catalog helpers."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
TAXONOMY_PATH=Path(__file__).resolve().parent/"taxonomy"/"global_ai_storage_taxonomy.json"
def load_taxonomy()->dict[str,Any]:
    with TAXONOMY_PATH.open("r",encoding="utf-8") as stream: return json.load(stream)
def list_ecosystems()->list[dict[str,str]]:
    data=load_taxonomy(); rows=[]
    for group in data.get("groups",[]):
        for category in group.get("categories",[]): rows.append({"group":group["group"],"category":category,"name":f"GLOBAL_AI_{category}_STORAGE_ECOSYSTEM","status":"CATALOG_ONLY","provider_product_verified":"false"})
    return rows
def find_ecosystem(name_or_category:str)->dict[str,str]|None:
    needle=str(name_or_category).strip().upper()
    return next((row for row in list_ecosystems() if needle in (row["name"],row["category"])),None)
