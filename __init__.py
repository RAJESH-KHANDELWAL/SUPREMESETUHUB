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
    """Return the CORE subtree, not the enclosing GLOBAL ECOSYSTEM root."""
    result = _get_manager().tree()
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
        "id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "children": core_node.get("children", []) if core_node else [],
        "tree": core_node,
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
