"""Stable product inventory facade for Microsoft Core."""
from __future__ import annotations
from typing import Any
from .catalog import get_microsoft_core_catalog

def list_microsoft_products(*, enabled_only: bool = False) -> list[dict[str, Any]]:
    items = get_microsoft_core_catalog()["children"]
    return [item for item in items if not enabled_only or item.get("enabled", True)]

def microsoft_offerings_summary() -> dict[str, Any]:
    items = list_microsoft_products()
    return {"success": True, "count": len(items), "offerings": items, "live_connections_verified": 0}
