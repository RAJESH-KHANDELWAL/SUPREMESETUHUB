"""GLOBAL CORE ECOSYSTEM entry point for the MAIN BASE FOUNDATION CORE layer.

Mirrors the API layer's entry-file-plus-package layout:
backend/core/global_ecosystem/global_core_ecosystem.py
backend/core/global_ecosystem/global_core_ecosystem/
The package owns implementation modules; this file is the public layer entry point.
"""

from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.manager import (
    GlobalEcosystemManager,
)

ECOSYSTEM_ID = "GLOBAL_CORE_ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL CORE ECOSYSTEM"
ECOSYSTEM_VERSION = "1.0.0"


def status() -> dict[str, Any]:
    """Return the registered GLOBAL CORE ECOSYSTEM foundation status."""
    manager = GlobalEcosystemManager()
    result = manager.status()
    return {
        "success": bool(result.get("success")),
        "ecosystem_id": ECOSYSTEM_ID,
        "ecosystem": ECOSYSTEM_NAME,
        "version": ECOSYSTEM_VERSION,
        "status": result.get("status", "NOT_INITIALIZED"),
        "module_count": result.get("count", 0),
    }


def list_modules() -> dict[str, Any]:
    """List modules registered in the GLOBAL CORE ECOSYSTEM catalog."""
    result = GlobalEcosystemManager().list()
    return {
        "success": bool(result.get("success")),
        "count": result.get("count", 0),
        "items": result.get("ecosystems", []),
    }


def get_module(module_id: str) -> dict[str, Any]:
    """Retrieve one module by its ecosystem ID or exact name."""
    record = GlobalEcosystemManager().get(module_id)
    if record is None:
        return {
            "success": False,
            "error": "MODULE_NOT_FOUND",
            "module_id": module_id,
        }
    return {"success": True, "item": record}


def tree() -> dict[str, Any]:
    """Return the nested GLOBAL CORE ECOSYSTEM module hierarchy."""
    result = GlobalEcosystemManager().tree()
    return {
        "success": bool(result.get("success")),
        "name": ECOSYSTEM_NAME,
        "id": ECOSYSTEM_ID,
        "children": [result.get("tree")] if result.get("tree") else [],
    }


__all__ = [
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "ECOSYSTEM_VERSION",
    "status",
    "list_modules",
    "get_module",
    "tree",
]
