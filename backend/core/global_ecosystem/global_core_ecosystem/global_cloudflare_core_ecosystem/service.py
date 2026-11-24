"""Read-only Cloudflare Core control-plane service."""
from __future__ import annotations
from typing import Any
from .orchestrator import CloudflareCoreOrchestrator

class CloudflareCoreEcosystemService:
    NAME = "GLOBAL CLOUDFLARE CORE ECOSYSTEM"
    def __init__(self) -> None:
        self.orchestrator = CloudflareCoreOrchestrator()
    def status(self) -> dict[str, Any]:
        health = self.orchestrator.health()
        return {"success": True, "ecosystem_id": "GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM",
                "name": self.NAME, "provider": "cloudflare",
                "status": health["status"], "module_count": health["product_count"],
                "domain_count": health["domain_count"],
                "implemented_product_count": 0, "live_connection_verified": False,
                "api_calls_performed": 0, "health": health}
    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()
    def list_products(self) -> dict[str, Any]:
        return self.orchestrator.list_products()
    def list_domains(self) -> dict[str, Any]:
        return self.orchestrator.domains()
    def get_product(self, product_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_product(product_id)
    def directory_audit(self) -> list[dict[str, Any]]:
        return self.orchestrator.directory_audit()
    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()
