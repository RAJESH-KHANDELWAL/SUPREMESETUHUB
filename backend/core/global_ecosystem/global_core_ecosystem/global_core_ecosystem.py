"""Public Python entry point for GLOBAL CORE ECOSYSTEM.

This module lives inside the canonical package and delegates domain behavior
to the package manager. It does not own a second registry or catalog.
"""
from __future__ import annotations

from typing import Any

from .manager import GlobalEcosystemManager, get_manager

ECOSYSTEM_ID = "GLOBAL-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL CORE ECOSYSTEM"
ECOSYSTEM_VERSION = "1.0.0"


def status() -> dict[str, Any]:
    result = get_manager().status()
    return {
        "success": bool(result.get("success")),
        "ecosystem_id": ECOSYSTEM_ID,
        "ecosystem": ECOSYSTEM_NAME,
        "version": ECOSYSTEM_VERSION,
        "status": result.get("status", "NOT_INITIALIZED"),
        "module_count": result.get("count", 0),
    }


def list_modules() -> dict[str, Any]:
    result = get_manager().list()
    return {
        "success": bool(result.get("success")),
        "count": result.get("count", 0),
        "items": result.get("ecosystems", []),
    }


def get_module(module_id: str) -> dict[str, Any]:
    record = get_manager().get(module_id)
    if record is None:
        return {
            "success": False,
            "error": "MODULE_NOT_FOUND",
            "module_id": module_id,
        }
    return {"success": True, "item": record}


def tree() -> dict[str, Any]:
    result = get_manager().tree()
    return {
        "success": bool(result.get("success")),
        "name": ECOSYSTEM_NAME,
        "id": ECOSYSTEM_ID,
        "children": [result.get("tree")] if result.get("tree") else [],
    }


__all__ = [
    "GlobalEcosystemManager",
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "ECOSYSTEM_VERSION",
    "status",
    "list_modules",
    "get_module",
    "tree",
]
