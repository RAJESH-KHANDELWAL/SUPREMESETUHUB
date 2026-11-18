"""Read-only access to the canonical global server CORE domain registry."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

_REGISTRY_PATH = Path(__file__).with_name("domain_registry.json")

def load_domain_registry() -> dict[str, Any]:
    data = json.loads(_REGISTRY_PATH.read_text(encoding="utf-8"))
    domains = data.get("domains", [])
    if data.get("domain_count") != len(domains):
        raise ValueError("domain_count does not match registered domains")
    ids = [row.get("domain_id") for row in domains]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate domain_id in registry")
    for row in domains:
        name = row.get("directory", "")
        if not name.startswith("server_") or not name.endswith("_core_ecosystem"):
            raise ValueError(f"invalid CORE domain directory: {name}")
    return data

def get_domain(domain_id: str) -> dict[str, Any] | None:
    key = str(domain_id).strip().upper()
    return next((row for row in load_domain_registry()["domains"] if row["domain_id"] == key), None)
