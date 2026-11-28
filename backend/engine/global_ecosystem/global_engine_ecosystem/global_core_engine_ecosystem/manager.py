"""GLOBAL CORE ENGINE ECOSYSTEM identity and manager.

This package lives under backend/engine/global_ecosystem/global_engine_ecosystem.
It defines the CORE ENGINE foundation for the GLOBAL ENGINE ECOSYSTEM.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from ..manager import EcosystemIdentity
from ..registry import GlobalEcosystemRegistry

ROOT_ID = "GLOBAL-CORE-ENGINE-ECOSYSTEM"
ROOT: dict[str, Any] = {
    "ecosystem_id": ROOT_ID,
    "name": "GLOBAL CORE ENGINE ECOSYSTEM",
    "ecosystem_type": "CORE_ENGINE_LAYER",
    "status": "REGISTERED",
    "enabled": True,
    "capabilities": [
        "ENGINE_FOUNDATION",
        "ENGINE_CONTRACTS",
        "ENGINE_LIFECYCLE",
        "ENGINE_REGISTRY_COORDINATION",
        "ENGINE_HEALTH_AND_DIAGNOSTICS",
    ],
    "parent_id": None,
    "metadata": {
        "owner_layer": "ENGINE",
        "foundation_layer": "CORE_ENGINE",
        "implementation_path": "backend/engine/global_ecosystem/global_engine_ecosystem/global_core_engine_ecosystem",
        "engine_runtime_owner": "GLOBAL-ENGINE-ECOSYSTEM",
        "note": "Foundation metadata and registry only; does not duplicate engine execution modules.",
    },
}


def get_catalog() -> list[dict[str, Any]]:
    """Return a defensive copy of the CORE ENGINE root catalog."""
    return [deepcopy(ROOT)]


class GlobalCoreEngineEcosystemManager:
    """Manage CORE ENGINE foundation identities without owning engine execution."""

    ROOT_ID = ROOT_ID
    ROOT_NAME = "GLOBAL CORE ENGINE ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        self.registry = GlobalEcosystemRegistry()
        for record in get_catalog():
            self.registry.register(EcosystemIdentity(**record))

    def status(self) -> dict[str, Any]:
        root = self.registry.get(self.ROOT_ID)
        return {
            "success": root is not None,
            "ecosystem_id": self.ROOT_ID,
            "name": self.ROOT_NAME,
            "version": self.VERSION,
            "status": "FOUNDATION_READY" if root else "NOT_INITIALIZED",
            "registry_count": self.registry.count(),
        }

    def health(self) -> dict[str, Any]:
        ready = self.registry.exists(self.ROOT_ID)
        return {
            "success": ready,
            "service": self.ROOT_NAME,
            "status": "HEALTHY" if ready else "DEGRADED",
            "registry_available": self.registry is not None,
            "registry_count": self.registry.count(),
        }

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self.registry.get(ecosystem_id)

    def list(self) -> dict[str, Any]:
        records = self.registry.list()
        return {"success": True, "count": len(records), "ecosystems": records}


EcosystemManager = GlobalCoreEngineEcosystemManager

__all__ = [
    "ROOT_ID", "ROOT", "get_catalog",
    "GlobalCoreEngineEcosystemManager", "EcosystemManager",
]
