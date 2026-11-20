"""Central manager for the Google Core Ecosystem.

This manager coordinates catalog, domain and product metadata only. It does
not perform OAuth, Google API requests, persistence or background execution.
Those responsibilities belong to their dedicated ecosystem layers.
"""
from __future__ import annotations

from typing import Any

from .orchestrator import GoogleCoreOrchestrator
from .domain_runtime import GoogleCoreDomainManager
from .service import GoogleCoreEcosystemService


class GoogleCoreManager:
    """Stable entry point for applications consuming Google Core metadata."""

    NAME = "GOOGLE CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GOOGLE-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = GoogleCoreOrchestrator()
        self._service = GoogleCoreEcosystemService()

    def status(self) -> dict[str, Any]:
        """Return ecosystem status without implying live provider connectivity."""
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(enabled_only=enabled_only)

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(ecosystem_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def list_offerings(self) -> dict[str, Any]:
        return self._orchestrator.offerings()

    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_offering(product_id)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def get_domain_manager(self, domain_id: str) -> GoogleCoreDomainManager:
        \"\"\"Return a read-only manager for a registered domain ID.\"\"\"
        return GoogleCoreDomainManager(domain_id)


def get_manager() -> GoogleCoreManager:
    """Return the canonical Google Core manager instance."""
    return GoogleCoreManager()


__all__ = ["GoogleCoreManager", "get_manager"]
