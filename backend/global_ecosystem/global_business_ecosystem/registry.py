"""Lookup and search for registered global business ecosystem namespaces."""
from __future__ import annotations
from copy import deepcopy
from .catalog import BUSINESS_ECOSYSTEMS

def list_business_ecosystems(*, category: str | None = None) -> tuple[dict, ...]:
    items = BUSINESS_ECOSYSTEMS
    if category:
        normalized = category.strip().lower()
        items = tuple(item for item in items if item["category"] == normalized)
    return tuple(deepcopy(item) for item in items)

def get_business_ecosystem(ecosystem_id: str) -> dict | None:
    if not isinstance(ecosystem_id, str):
        return None
    key = ecosystem_id.strip().lower()
    for item in BUSINESS_ECOSYSTEMS:
        if item["id"] == key:
            return deepcopy(item)
    return None

def search_business_ecosystems(query: str) -> tuple[dict, ...]:
    term = (query or "").strip().casefold()
    if not term:
        return ()
    found = []
    for item in BUSINESS_ECOSYSTEMS:
        haystack = " ".join((item["id"], item["name"], item["category"], item.get("relationship", ""))).casefold()
        if term in haystack:
            found.append(deepcopy(item))
    return tuple(found)

def validate_registry() -> tuple[str, ...]:
    errors = []
    ids = [item.get("id") for item in BUSINESS_ECOSYSTEMS]
    if len(ids) != len(set(ids)):
        errors.append("duplicate business ecosystem IDs")
    for item in BUSINESS_ECOSYSTEMS:
        if not item.get("package_path"):
            errors.append(f"{item.get('id')}: missing package_path")
    return tuple(errors)

__all__ = ["list_business_ecosystems", "get_business_ecosystem", "search_business_ecosystems", "validate_registry"]
