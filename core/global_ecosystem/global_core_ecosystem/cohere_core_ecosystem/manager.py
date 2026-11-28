"""Canonical Cohere Core manager, aligned with the Google Core facade."""
from __future__ import annotations

from typing import Any

from .contracts import CapabilityRequest, CoreResult, TenantContext
from .domain_runtime import CohereCoreDomainManager
from .orchestrator import CohereCoreOrchestrator
from .service import CohereCoreService


class CohereCoreManager:
    """Stable provider entry point for read-only inventory and validation."""

    NAME = "COHERE CORE ECOSYSTEM"
    ECOSYSTEM_ID = "COHERE-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self.service = CohereCoreService()
        self._orchestrator = CohereCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        return self.service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_modules(enabled_only=enabled_only)

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_module(ecosystem_id)

    def list_capabilities(self) -> dict[str, Any]:
        return self._orchestrator.capabilities()

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def list_offerings(self) -> dict[str, Any]:
        return self._orchestrator.capabilities()

    def get_offering(self, capability: str) -> dict[str, Any] | None:
        return self._orchestrator.get_module(capability)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def get_domain_manager(self, domain_id: str) -> CohereCoreDomainManager:
        return CohereCoreDomainManager(domain_id)

    def validate(self, request: CapabilityRequest) -> CoreResult:
        return self.service.validate(request)

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        return self.service.authorize_capability(capability, context)

    def authorize_operation(self, operation: str, *, explicitly_authorized: bool = False) -> None:
        self.service.authorize_operation(operation, explicitly_authorized=explicitly_authorized)


def get_manager() -> CohereCoreManager:
    """Return the canonical Cohere Core manager."""
    return CohereCoreManager()


__all__ = ["CohereCoreManager", "get_manager"]
