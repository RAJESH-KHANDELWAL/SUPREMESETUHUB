"""Public IBM Core status and parent registry integration."""
from __future__ import annotations
from typing import Any
from .catalog import get_catalog
from .orchestrator import IBMCoreOrchestrator
class IBMCoreEcosystemService:
    def __init__(self) -> None: self._orchestrator=IBMCoreOrchestrator()
    def status(self) -> dict[str,Any]:
        c=get_catalog(); h=self._orchestrator.health()
        return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":c["name"],"provider":"ibm","status":c["status"],"parent_id":c["parent_id"],"product_count":c["product_count"],"domain_count":c["domain_count"],"live_connection_verified":False,"api_calls_performed":0,"health":h,"master_catalog_alignment":c["master_catalog_alignment"]}
