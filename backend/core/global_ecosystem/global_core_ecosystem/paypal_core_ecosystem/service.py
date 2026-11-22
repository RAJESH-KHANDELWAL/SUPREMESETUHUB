"""Public PayPal Core read-only service and registry status."""
from __future__ import annotations
from typing import Any
from .catalog import get_paypal_core_catalog
from .master_catalog import get_master_catalog_status
from .orchestrator import PayPalCoreOrchestrator
class PayPalCoreEcosystemService:
    NAME = "PAYPAL CORE ECOSYSTEM"
    def __init__(self) -> None: self.orchestrator = PayPalCoreOrchestrator()
    def status(self) -> dict[str, Any]:
        catalog = get_paypal_core_catalog()
        health = self.orchestrator.health()
        master = get_master_catalog_status()
        return {"success": True, "ecosystem_id": catalog["ecosystem_id"], "name": self.NAME, "provider": "paypal", "status": catalog["status"], "product_count": len(catalog["children"]), "domain_count": health["domain_count"], "connected_products": 0, "live_connection_verified": False, "api_calls_performed": 0, "api_transport_in_core": False, "master_catalog": master}
    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]: return self.orchestrator.list_products(enabled_only=enabled_only)
    def list_domains(self) -> dict[str, Any]: return self.orchestrator.domains()
    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None: return self.orchestrator.get_product(ecosystem_id)
    def health(self) -> dict[str, Any]: return self.orchestrator.health()
    def dependency_map(self) -> dict[str, Any]: return self.orchestrator.dependency_map()
