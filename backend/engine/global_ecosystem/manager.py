"""GLOBAL ECOSYSTEM ENGINE MANAGER.

The engine is a runtime facade over the canonical Core ecosystem registry.
Core owns the canonical hierarchy; Engine preserves the public runtime API.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class GlobalEcosystemManager:
    """Runtime facade over the canonical GLOBAL Core Ecosystem manager."""

    def __init__(self) -> None:
        from backend.core.global_ecosystem.global_core_ecosystem.manager import (
            GlobalEcosystemManager as CoreGlobalEcosystemManager,
        )

        self.name = "GLOBAL ECOSYSTEM"
        self.version = "1.0.0"
        self._core_manager = CoreGlobalEcosystemManager()
        self.registry = self._core_manager.registry

    def register(self, ecosystem: dict[str, Any]) -> dict[str, Any]:
        """Register an ecosystem through the canonical Core registry."""
        from backend.core.global_ecosystem.global_core_ecosystem.models import (
            GlobalEcosystemIdentity,
        )

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
        """Return engine status with the canonical registry count."""
        core_status = self._core_manager.status()
        return {
            **core_status,
            "name": self.name,
            "version": self.version,
            "status": "OPERATIONAL" if core_status.get("success") else "NOT_INITIALIZED",
            "enabled": True,
            "ecosystem_count": self.registry.count(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def health(self) -> dict[str, Any]:
        """Return runtime health without claiming an external provider connection."""
        core_health = self._core_manager.health()
        return {
            "success": bool(core_health.get("success")),
            "service": self.name,
            "status": "HEALTHY" if core_health.get("success") else "DEGRADED",
            "registry_available": self.registry is not None,
            "ecosystem_count": self.registry.count(),
            "core_health": core_health,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def list(self) -> dict[str, Any]:
        """List the canonical ecosystem registrations."""
        return self._core_manager.list()

    def names(self) -> dict[str, Any]:
        """List registered ecosystem names."""
        return self._core_manager.names()

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        """Get an ecosystem by ID or exact name."""
        return self._core_manager.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        """Check whether an ecosystem is registered."""
        return self._core_manager.exists(ecosystem_id)

    def tree(self) -> dict[str, Any]:
        """Return the nested canonical hierarchy."""
        return self._core_manager.tree()

    def connection_map(self) -> dict[str, Any]:
        """Return parent-child links for the canonical hierarchy."""
        return self._core_manager.connection_map()


EcosystemManager = GlobalEcosystemManager
