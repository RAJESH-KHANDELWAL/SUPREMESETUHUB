"""SUPREME ECOSYSTEM entry module under MAIN SUPREME.

The sibling supreme_ecosystem/ directory contains the ecosystem's domain modules.
The root backend/supreme.py remains the MAIN SUPREME entry point.
"""
from __future__ import annotations

from typing import Any

from backend.supreme.supreme_ecosystem.supreme_ecosystem import supreme_ecosystem

SYSTEM_NAME = "SUPREME ECOSYSTEM"
PARENT_SYSTEM = "SUPREME"
ACCESS_POLICY = "PRIVATE_BY_DEFAULT"
MODULE_PACKAGE = "backend.supreme.supreme_ecosystem"
LAYER_PACKAGES = {
    "core": "backend.supreme.core",
    "engines": "backend.supreme.engines",
    "database": "backend.supreme.database",
    "storage": "backend.supreme.storage",
}


def status() -> dict[str, Any]:
    """Return ecosystem hierarchy and layer map without opening the database."""
    return {
        "success": True,
        "system": SYSTEM_NAME,
        "parent": PARENT_SYSTEM,
        "privacy": ACCESS_POLICY,
        "module_package": MODULE_PACKAGE,
        "layers": dict(LAYER_PACKAGES),
        "ecosystem": supreme_ecosystem.status(),
    }


__all__ = ["SYSTEM_NAME", "PARENT_SYSTEM", "ACCESS_POLICY", "MODULE_PACKAGE", "LAYER_PACKAGES", "status"]
