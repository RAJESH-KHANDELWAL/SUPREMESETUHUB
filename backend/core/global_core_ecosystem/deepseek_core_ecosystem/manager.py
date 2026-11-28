"""Canonical manager for the DeepSeek Core Ecosystem."""
from __future__ import annotations

from typing import Any

from .catalog import get_catalog, list_capabilities
from .orchestrator import DeepSeekCoreOrchestrator
from .policy import public_provider_metadata


class DeepSeekCoreManager:
    """Stable read-only entry point for DeepSeek Core metadata."""

    NAME = "DEEPSEEK CORE ECOSYSTEM"
    ECOSYSTEM_ID = "DEEPSEEK-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = DeepSeekCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = public_provider_metadata(get_catalog())
        health = self._orchestrator.health()
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "name": self.NAME,
            "provider": "deepseek",
            "status": catalog["status"],
            "capability_count": len(catalog["capabilities"]),
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "health": health,
        }

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_capabilities(self) -> dict[str, Any]:
        return self._orchestrator.capabilities()

    def get_capability(self, capability: str) -> dict[str, Any] | None:
        if not isinstance(capability, str):
            return None
        return list_capabilities().get(capability.strip().casefold())

    def validate(self, capability: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self._orchestrator.validate(capability, payload)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()


def get_manager() -> DeepSeekCoreManager:
    """Return the canonical DeepSeek Core manager."""
    return DeepSeekCoreManager()


__all__ = ["DeepSeekCoreManager", "get_manager"]
