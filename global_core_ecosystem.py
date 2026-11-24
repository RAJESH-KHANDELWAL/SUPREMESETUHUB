"""Public Python entry point for GLOBAL CORE ECOSYSTEM.

This module delegates hierarchy ownership to the shared GLOBAL ECOSYSTEM
manager and exposes only the GLOBAL CORE ECOSYSTEM subtree.
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
    records = result.get("ecosystems", [])
    core_records = [
        item for item in records
        if item.get("ecosystem_id") == ECOSYSTEM_ID
        or item.get("parent_id") == ECOSYSTEM_ID
    ]
    return {
        "success": bool(result.get("success")),
        "count": len(core_records),
        "items": core_records,
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
    master_root = result.get("tree") if isinstance(result, dict) else None
    core_node = None
    if isinstance(master_root, dict):
        core_node = next(
            (
                child
                for child in master_root.get("children", [])
                if child.get("ecosystem_id") == ECOSYSTEM_ID
            ),
            None,
        )
    return {
        "success": bool(result.get("success")) and core_node is not None
        if isinstance(result, dict)
        else False,
        "name": ECOSYSTEM_NAME,
        "id": ECOSYSTEM_ID,
        "children": core_node.get("children", []) if core_node else [],
        "tree": core_node,
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
