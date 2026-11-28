"""Public IBM Core status and parent registry integration."""
from __future__ import annotations
from typing import Any
from .catalog import get_catalog
from .orchestrator import IBMCoreOrchestrator

class IBMCoreEcosystemService:
    def __init__(self) -> None:
        self._orchestrator=IBMCoreOrchestrator()

    def manager_status(self) -> dict[str,Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            record=GlobalEcosystemManager().get("IBM-CORE-ECOSYSTEM")
        except Exception as exc:
            return {"success":False,"registered":False,"ecosystem":None,"error":type(exc).__name__}
        return {"success":record is not None,"registered":record is not None,"ecosystem":record,"live_connection_verified":False}

    def status(self) -> dict[str,Any]:
        catalog=get_catalog()
        health=self._orchestrator.health()
        registry=self.manager_status()
        return {
            "success":True,
            "ecosystem_id":catalog["ecosystem_id"],
            "name":catalog["name"],
            "provider":"ibm",
            "status":catalog["status"],
            "registry_status":registry["registered"],
            "parent_id":catalog["parent_id"],
            "product_count":catalog["product_count"],
            "domain_count":catalog["domain_count"],
            "connected_products":0,
            "live_connection_verified":False,
            "api_calls_performed":0,
            "health":health,
            "master_catalog_alignment":catalog["master_catalog_alignment"],
        }

    def list_products(self) -> dict[str,Any]:
        products=self._orchestrator.products()
        return {"success":True,"count":len(products),"products":products}

    def list_domains(self) -> dict[str,Any]:
        domains=self._orchestrator.domains()
        return {"success":True,"count":len(domains),"domains":domains}

    def health(self) -> dict[str,Any]: return self._orchestrator.health()
    def dependency_map(self) -> dict[str,Any]: return self._orchestrator.dependency_map()
