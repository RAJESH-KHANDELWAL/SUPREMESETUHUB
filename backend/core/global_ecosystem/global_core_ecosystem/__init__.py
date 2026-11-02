"""Public GLOBAL CORE ECOSYSTEM package and entry point.

The package directory takes precedence over the sibling
global_core_ecosystem.py module during Python imports. Keep the public API
here so dotted imports resolve to the same identity and operations.
"""

from __future__ import annotations

from typing import Any

from .catalog import get_catalog, get_category_catalog, get_registration_catalog
from .manager import EcosystemManager, GlobalEcosystemManager
from .models import EcosystemIdentity, GlobalEcosystemIdentity
from .registry import EcosystemRegistry, GlobalEcosystemRegistry
from .referral_service import SupremeReferralService

ECOSYSTEM_ID = "GLOBAL-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL CORE ECOSYSTEM"
ECOSYSTEM_VERSION = "1.0.0"


def status() -> dict[str, Any]:
    """Return the registered GLOBAL CORE ECOSYSTEM foundation status."""
    result = GlobalEcosystemManager().status()
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
    """Retrieve one module by its ecosystem ID."""
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
    "get_catalog",
    "get_category_catalog",
    "get_registration_catalog",
    "EcosystemManager",
    "GlobalEcosystemManager",
    "EcosystemIdentity",
    "GlobalEcosystemIdentity",
    "EcosystemRegistry",
    "GlobalEcosystemRegistry",
    "SupremeReferralService",
]
