"""Adobe Core Ecosystem read-only control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_adobe_core_catalog
from .orchestrator import AdobeCoreOrchestrator
class AdobeCoreEcosystemService:
    NAME="ADOBE CORE ECOSYSTEM"
    def __init__(self) -> None: self.orchestrator=AdobeCoreOrchestrator()
    def status(self) -> dict[str,Any]:
        catalog=get_adobe_core_catalog(); items=catalog["children"]
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],"name":self.NAME,
            "provider":"adobe","status":catalog["status"],"module_count":len(items),
            "connected_modules":0,"live_connection_verified":False,"api_calls_performed":0,
            "health":self.orchestrator.health(),"api_catalog_ref":catalog["api_catalog_ref"]}
    def list_modules(self) -> dict[str,Any]: return self.orchestrator.list_products()
    def get_module(self, ecosystem_id: str) -> dict[str,Any] | None: return self.orchestrator.get_product(ecosystem_id)
    def health(self) -> dict[str,Any]: return self.orchestrator.health()
    def dependency_map(self) -> dict[str,Any]: return self.orchestrator.dependency_map()
