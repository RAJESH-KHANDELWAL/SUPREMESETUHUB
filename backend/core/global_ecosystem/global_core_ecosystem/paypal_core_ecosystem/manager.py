"""Canonical Python entry point for PayPal Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .orchestrator import PayPalCoreOrchestrator
from .service import PayPalCoreEcosystemService
class PayPalCoreManager:
    NAME = "PAYPAL CORE ECOSYSTEM"
    ECOSYSTEM_ID = "PAYPAL-CORE-ECOSYSTEM"
    def __init__(self) -> None:
        self._orchestrator = PayPalCoreOrchestrator()
        self._service = PayPalCoreEcosystemService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def health(self) -> dict[str, Any]: return self._orchestrator.health()
    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]: return self._orchestrator.list_products(enabled_only=enabled_only)
    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None: return self._orchestrator.get_product(ecosystem_id)
    def list_domains(self) -> dict[str, Any]: return self._orchestrator.domains()
    def list_domain_inventory(self) -> list[dict[str, Any]]: return self._orchestrator.domain_inventory()
    def dependency_map(self) -> dict[str, Any]: return self._orchestrator.dependency_map()
    def product_manager(self, ecosystem_id: str):
        from .module_service import PayPalProductCoreService
        return PayPalProductCoreService(ecosystem_id)
def get_manager() -> PayPalCoreManager: return PayPalCoreManager()
__all__ = ["PayPalCoreManager", "get_manager"]
