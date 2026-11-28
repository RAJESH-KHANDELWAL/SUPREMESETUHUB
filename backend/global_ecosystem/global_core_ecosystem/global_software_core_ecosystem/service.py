"""Public Global Software Core status service."""
from __future__ import annotations
from typing import Any
from .catalog import get_software_core_catalog
from .orchestrator import GlobalSoftwareCoreOrchestrator
class GlobalSoftwareCoreService:
    def __init__(self): self.orchestrator=GlobalSoftwareCoreOrchestrator()
    def status(self) -> dict[str, Any]:
        c=get_software_core_catalog(); h=self.orchestrator.health()
        return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":c["name"],"status":c["status"],"provider_count":h["provider_count"],"domain_count":h["domain_count"],"live_connection_verified":False,"api_calls_performed":0,"health":h}
    def list_providers(self): return self.orchestrator.list_providers()
    def list_domains(self): return self.orchestrator.domains()
