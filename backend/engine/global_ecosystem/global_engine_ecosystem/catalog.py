"""ENGINE-owned catalog of executable ecosystem modules.

This module discovers ENGINE packages from this layer's own filesystem. It does
not import or duplicate API, CORE, DATABASE, STORAGE, or SERVER implementations.
"""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT_ID = "GLOBAL-ENGINE-ECOSYSTEM"
ROOT: dict[str, Any] = {
    "ecosystem_id": ROOT_ID,
    "name": "GLOBAL ENGINE ECOSYSTEM",
    "ecosystem_type": "ENGINE_LAYER",
    "status": "REGISTERED",
    "enabled": True,
    "capabilities": ["EXECUTION", "PROCESSING", "ORCHESTRATION"],
    "parent_id": None,
    "metadata": {"owner_layer": "ENGINE"},
}

_PACKAGE_ROOT = Path(__file__).resolve().parent


def _discover() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Discover provider groups and executable engine modules owned by ENGINE."""
    categories: list[dict[str, Any]] = []
    providers: list[dict[str, Any]] = []
    for directory in sorted(_PACKAGE_ROOT.iterdir(), key=lambda item: item.name):
        if not directory.is_dir() or directory.name.startswith("_"):
            continue
        if not directory.name.endswith("_engine_ecosystem"):
            continue
        category_id = directory.name.removesuffix("_engine_ecosystem").upper().replace("_", "-")
        modules = sorted(directory.rglob("engine.py"))
        categories.append({
            "ecosystem_id": f"{category_id}-ENGINE-ECOSYSTEM",
            "name": directory.name.replace("_", " ").upper(),
            "ecosystem_type": "ENGINE_CATEGORY",
            "parent_id": ROOT_ID,
            "module_count": len(modules),
            "status": "DISCOVERED" if modules else "CATALOG_ONLY",
            "capabilities": ["ENGINE_MODULE_DISCOVERY"],
        })
        for module in modules:
            relative = module.parent.relative_to(_PACKAGE_ROOT).as_posix()
            module_id = relative.upper().replace("/", "-").replace("_", "-")
            providers.append({
                "ecosystem_id": module_id,
                "name": relative.replace("/", " ").replace("_", " ").upper(),
                "ecosystem_type": "ENGINE_MODULE",
                "parent_id": f"{category_id}-ENGINE-ECOSYSTEM",
                "module": f"{__package__}." + relative.replace("/", "."),
                "entrypoint": "engine.py",
                "status": "DISCOVERED",
                "capabilities": ["ENGINE_EXECUTION_MODULE"],
            })
    return categories, providers


def get_catalog() -> list[dict[str, Any]]:
    """Return independent copies of the ENGINE root and discovered modules."""
    categories, providers = _discover()
    return [deepcopy(ROOT), *deepcopy(categories), *deepcopy(providers)]


def get_category_catalog() -> list[dict[str, Any]]:
    """Return the discovered ENGINE category catalog."""
    categories, _ = _discover()
    return deepcopy(categories)


def get_provider_catalog() -> list[dict[str, Any]]:
    """Return discovered executable ENGINE modules (not external providers)."""
    _, providers = _discover()
    return deepcopy(providers)


CATEGORIES, PROVIDER_ECOSYSTEMS = _discover()
