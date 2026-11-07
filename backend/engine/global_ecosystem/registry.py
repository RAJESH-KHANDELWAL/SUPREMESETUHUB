"""Backward-compatible ENGINE registry facade over canonical CORE storage."""
from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.registry import (
    GlobalEcosystemRegistry as CoreGlobalEcosystemRegistry,
)
from backend.core.global_ecosystem.global_core_ecosystem.models import GlobalEcosystemIdentity


class GlobalEcosystemRegistry:
    """Compatibility adapter delegating all state to the CORE registry."""

    def __init__(self, core_registry: CoreGlobalEcosystemRegistry | None = None) -> None:
        self._core_registry = core_registry or CoreGlobalEcosystemRegistry()

    def register(self, identity: GlobalEcosystemIdentity | dict[str, Any]) -> dict[str, Any]:
        if isinstance(identity, dict):
            identity = GlobalEcosystemIdentity(
                ecosystem_id=str(identity.get("ecosystem_id", "")).strip(),
                name=str(identity.get("name", "")).strip(),
                ecosystem_type=str(identity.get("ecosystem_type", "GENERAL")).strip(),
                repository_ref=identity.get("repository_ref"),
                status=str(identity.get("status", "REGISTERED")),
                enabled=bool(identity.get("enabled", True)),
                capabilities=list(identity.get("capabilities", [])),
                metadata=dict(identity.get("metadata", {})),
                message=identity.get("message"),
                parent_id=identity.get("parent_id"),
            )
        return self._core_registry.register(identity)

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._core_registry.get(ecosystem_id)

    def list(self) -> list[dict[str, Any]]:
        return self._core_registry.list()

    def names(self) -> list[str]:
        return self._core_registry.names()

    def exists(self, ecosystem_id: str) -> bool:
        return self._core_registry.exists(ecosystem_id)

    def count(self) -> int:
        return self._core_registry.count()

    def clear(self) -> None:
        self._core_registry.clear()


EcosystemRegistry = GlobalEcosystemRegistry
