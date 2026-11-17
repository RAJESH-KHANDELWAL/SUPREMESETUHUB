"""Anthropic storage taxonomy loader and lookup helpers."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
TAXONOMY_PATH = Path(__file__).with_name("taxonomy") / "anthropic_storage_taxonomy.json"
def load_taxonomy() -> dict[str, Any]:
    data = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    if data.get("ecosystem_id") != "ANTHROPIC_STORAGE_ECOSYSTEM":
        raise ValueError("Unexpected taxonomy ecosystem_id")
    return data
def list_ecosystems() -> list[str]:
    return list(load_taxonomy()["child_ecosystems"])
