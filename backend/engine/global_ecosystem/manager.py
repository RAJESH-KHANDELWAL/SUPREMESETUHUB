"""GLOBAL ECOSYSTEM engine facade over the canonical CORE hierarchy."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.manager import (
    GlobalEcosystemManager as CoreGlobalEcosystemManager,
)
from backend.core.global_ecosystem.global_core_ecosystem.models import GlobalEcosystemIdentity


class GlobalEcosystemManager:
    """Preserve ENGINE's dictionary API while using one canonical CORE registry."""

    def __init__(self) -> None:
        self.name = "GLOBAL ECOSYSTEM"
        self.version = "1.0.0"
        self._core_manager = CoreGlobalEcosystemManager()
        self.registry = self._core_manager.registry

    def register(self, ecosystem: dict[str, Any]) -> dict[str, Any]:
        identity = GlobalEcosystemIdentity(
            ecosystem_id=str(ecosystem.get("ecosystem_id", "")).strip(),
            name=str(ecosystem.get("name", "")).strip(),
            ecosystem_type=str(ecosystem.get("ecosystem_type", "GENERAL")).strip(),
            repository_ref=ecosystem.get("repository_ref"),
            status=str(ecosystem.get("status", "REGISTERED")),
            enabled=bool(ecosystem.get("enabled", True)),
            capabilities=list(ecosystem.get("capabilities", [])),
            metadata=dict(ecosystem.get("metadata", {})),
            message=ecosystem.get("message"),
            parent_id=ecosystem.get("parent_id") or self._core_manager.ROOT_ID,
        )
        return self._core_manager.register(identity)

    def status(self) -> dict[str, Any]:
        core = self._core_manager.status()
        return {
            **core,
            "name": self.name,
            "version": self.version,
            "status": "OPERATIONAL" if core.get("success") else "NOT_INITIALIZED",
            "enabled": True,
            "ecosystem_count": self.registry.count(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def health(self) -> dict[str, Any]:
        core = self._core_manager.health()
        return {
            "success": bool(core.get("success")),
            "service": self.name,
            "status": "HEALTHY" if core.get("success") else "DEGRADED",
            "registry_available": True,
            "ecosystem_count": self.registry.count(),
            "core_health": core,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def list(self) -> dict[str, Any]:
        return self._core_manager.list()

    def names(self) -> dict[str, Any]:
        return self._core_manager.names()

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._core_manager.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        return self._core_manager.exists(ecosystem_id)

    def tree(self) -> dict[str, Any]:
        return self._core_manager.tree()

    def connection_map(self) -> dict[str, Any]:
        return self._core_manager.connection_map()


EcosystemManager = GlobalEcosystemManager
