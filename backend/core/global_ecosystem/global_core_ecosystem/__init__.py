"""Public entry point for GLOBAL CORE ECOSYSTEM."""

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
    result.setdefault("ecosystem_id", ECOSYSTEM_ID)
    result.setdefault("ecosystem", ECOSYSTEM_NAME)
    return result


def tree():
    return _get_manager().tree()


def list_modules():
    manager = _get_manager()
    records = manager.list()
    return {"success": True, "count": len(records), "items": records}


def get_module(module_id: str):
    item = _get_manager().get(module_id)
    if item is None:
        return {"success": False, "error": "MODULE_NOT_FOUND", "item": None}
    return {"success": True, "item": item}


__all__ = [
    "LAYER",
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "ROOT_ID",
    "GlobalEcosystemManager",
    "status",
    "tree",
    "list_modules",
    "get_module",
]
