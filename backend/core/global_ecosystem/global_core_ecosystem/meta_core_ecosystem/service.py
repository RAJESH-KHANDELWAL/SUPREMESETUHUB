"""Public Meta Core status and Global Core registry integration."""
from __future__ import annotations
from typing import Any
from .catalog import get_meta_core_catalog
from .orchestrator import MetaCoreOrchestrator
class MetaCoreEcosystemService:
    NAME="META CORE ECOSYSTEM"
    def __init__(self)->None: self.orchestrator=MetaCoreOrchestrator()
    def manager_status(self)->dict[str,Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            record=GlobalEcosystemManager().get("META-CORE-ECOSYSTEM")
        except Exception as exc: return {"success":False,"registered":False,"ecosystem":None,"error":type(exc).__name__}
        return {"success":record is not None,"registered":record is not None,"ecosystem":record,"live_connection_verified":False}
    def status(self)->dict[str,Any]:
        catalog=get_meta_core_catalog(); health=self.orchestrator.health(); registry=self.manager_status()
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],"name":self.NAME,"provider":"meta","status":catalog["status"],"registry_status":registry["registered"],"parent_id":catalog["parent_id"],"product_count":catalog["product_count"],"domain_count":catalog["domain_count"],"connected_products":0,"live_connection_verified":False,"api_calls_performed":0,"health":health,"api_catalog_ref":catalog["api_catalog_ref"],"engine_catalog_ref":catalog["engine_catalog_ref"]}
    def list_products(self)->dict[str,Any]: return self.orchestrator.list_products()
    def list_domains(self)->dict[str,Any]: return self.orchestrator.domains()
    def health(self)->dict[str,Any]: return self.orchestrator.health()
    def dependency_map(self)->dict[str,Any]: return self.orchestrator.dependency_map()
