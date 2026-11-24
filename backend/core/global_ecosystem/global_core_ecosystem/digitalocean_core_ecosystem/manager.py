"""Canonical manager for the DigitalOcean Core Ecosystem."""
from __future__ import annotations

from typing import Any

from .catalog import get_catalog, list_capabilities
from .orchestrator import DigitalOceanCoreOrchestrator
from .policy import DigitalOceanCorePolicy


class DigitalOceanCoreManager:
    """Stable read-only entry point for DigitalOcean Core metadata."""

    NAME = "DIGITALOCEAN CORE ECOSYSTEM"
    ECOSYSTEM_ID = "DIGITALOCEAN-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = DigitalOceanCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = get_catalog()
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "name": self.NAME,
            "provider": "digitalocean",
            "status": catalog["status"],
            "capability_count": len(catalog["capabilities"]),
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "health": self.health(),
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
        metadata = self.get_capability(capability)
        if metadata is None:
            raise ValueError("unknown DigitalOcean Core capability")
        DigitalOceanCorePolicy.validate_capability(capability, enabled=True)
        return self._orchestrator.validate(capability, payload)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()


def get_manager() -> DigitalOceanCoreManager:
    """Return the canonical DigitalOcean Core manager."""
    return DigitalOceanCoreManager()


__all__ = ["DigitalOceanCoreManager", "get_manager"]
