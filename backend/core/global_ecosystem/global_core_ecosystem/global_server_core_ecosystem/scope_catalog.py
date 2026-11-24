"""Read-only loaders for Bharat-to-global server scope metadata."""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent


def _load(name: str) -> dict[str, Any]:
    path = _ROOT / name
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{name} must contain a JSON object")
    return value


def get_geographic_scope_catalog() -> dict[str, Any]:
    return deepcopy(_load("geographic_scope_catalog.json"))


def get_workload_domain_catalog() -> dict[str, Any]:
    return deepcopy(_load("workload_domain_catalog.json"))


def get_service_tier_catalog() -> dict[str, Any]:
    return deepcopy(_load("service_tier_catalog.json"))


def get_scope_catalog() -> dict[str, Any]:
    return {
        "geographic_scope": get_geographic_scope_catalog(),
        "workload_domains": get_workload_domain_catalog(),
        "service_tiers": get_service_tier_catalog(),
    }


def find_workload_domain(domain_id: str) -> dict[str, Any] | None:
    needle = str(domain_id).strip().upper()
    for item in get_workload_domain_catalog().get("domains", []):
        if item.get("domain_id") == needle:
            return deepcopy(item)
    return None
