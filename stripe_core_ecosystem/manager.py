"""Canonical manager for the Stripe Core Ecosystem."""
from __future__ import annotations

from typing import Any

from .module_service import StripeModuleCoreService
from .orchestrator import StripeCoreOrchestrator
from .service import StripeCoreEcosystemService


class StripeCoreManager:
    """Stable application entry point for Stripe Core metadata."""

    NAME = "STRIPE CORE ECOSYSTEM"
    ECOSYSTEM_ID = "STRIPE-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = StripeCoreOrchestrator()
        self._service = StripeCoreEcosystemService()

    def status(self) -> dict[str, Any]:
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

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def master_catalog_reference(self) -> dict[str, Any]:
        return self._orchestrator.master_catalog_reference()

    def module_manager(self, ecosystem_id: str) -> StripeModuleCoreService:
        return StripeModuleCoreService(ecosystem_id)


def get_manager() -> StripeCoreManager:
    """Return the canonical Stripe Core manager."""
    return StripeCoreManager()


__all__ = ["StripeCoreManager", "get_manager"]
