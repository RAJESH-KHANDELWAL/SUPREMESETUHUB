"""Public entry point for GLOBAL CORE ECOSYSTEM.

The package is nested under GLOBAL ECOSYSTEM; keep the master root identity
and the CORE child identity separate in all public responses.
"""
from .manager import GlobalEcosystemManager

LAYER = "CORE"
ECOSYSTEM_ID = "GLOBAL-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL CORE ECOSYSTEM"
ROOT_ID = ECOSYSTEM_ID

_manager: GlobalEcosystemManager | None = None


def _get_manager() -> GlobalEcosystemManager:
    global _manager
    if _manager is None:
        _manager = GlobalEcosystemManager()
    return _manager


def status():
    manager = _get_manager()
    result = manager.status()
    result["ecosystem_id"] = ECOSYSTEM_ID
    result["ecosystem"] = ECOSYSTEM_NAME
    result["name"] = ECOSYSTEM_NAME
    return result


def tree():
    """Return the GLOBAL ECOSYSTEM root with CORE as a child."""
    result = _get_manager().tree()
    root = result.get("tree") if isinstance(result, dict) else None
    return {
        "success": bool(result.get("success")) if isinstance(result, dict) else False,
        "id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "children": [root] if root else [],
        "tree": root,
    }


def list_modules():
    records = _get_manager().list()["ecosystems"]
    core_records = [
        item for item in records
        if item.get("ecosystem_id") == ECOSYSTEM_ID
        or item.get("parent_id") == ECOSYSTEM_ID
    ]
    return {"success": True, "count": len(core_records), "items": core_records}


def get_module(module_id: str):
    item = _get_manager().get(module_id)
    if item is None:
        return {"success": False, "error": "MODULE_NOT_FOUND", "item": None}
    return {"success": True, "item": item}


__all__ = [
    "LAYER", "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "ROOT_ID",
    "GlobalEcosystemManager", "status", "tree", "list_modules", "get_module",
]
