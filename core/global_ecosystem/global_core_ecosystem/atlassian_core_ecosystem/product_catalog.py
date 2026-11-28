"""Atlassian family-level offering inventory; not an API availability assertion."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .catalog import get_atlassian_core_catalog

def list_atlassian_offerings() -> list[dict[str, Any]]:
    rows = []
    for module in get_atlassian_core_catalog()["children"]:
        rows.append({"id": module["ecosystem_id"], "name": module["name"], "family": module["ecosystem_id"].removeprefix("ATLASSIAN-").removesuffix("-CORE-ECOSYSTEM"), "core_module": module["core_module"], "api_catalog_ref": module["api_catalog_ref"], "capabilities": list(module["capabilities"]), "domains": list(module["domains"]), "api_available": None, "live_connection_verified": False})
    return rows

def atlassian_offerings_summary() -> dict[str, Any]:
    items = list_atlassian_offerings()
    return {"success": True, "provider": "atlassian", "count": len(items), "api_available_count": 0, "live_connections_verified": 0, "offerings": items}
