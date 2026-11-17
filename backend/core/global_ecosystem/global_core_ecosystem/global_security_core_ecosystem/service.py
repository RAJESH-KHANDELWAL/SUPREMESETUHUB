"""Global Security CORE read-only control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_catalog,get_security_core_catalog
from .orchestrator import SecurityCoreOrchestrator
class SecurityCoreEcosystemService:
    NAME="GLOBAL SECURITY CORE ECOSYSTEM"
    def __init__(self): self.orchestrator=SecurityCoreOrchestrator()
    def status(self)->dict[str,Any]:
        catalog=get_catalog(); health=self.orchestrator.health(); manager=self.manager_status()
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],"name":self.NAME,"status":catalog["status"],"registry_status":manager["registered"],"domain_count":health["domain_count"],"provider_count":health["provider_count"],"live_service_connections_verified":False,"health":health,"manager_registration":manager}
    def catalog(self): return get_catalog()
    def list_modules(self,enabled_only=False): return self.orchestrator.list_modules(enabled_only)
    def list_domains(self): return self.orchestrator.list_domains()
    def list_providers(self): return self.orchestrator.list_providers()
    def health(self): return self.orchestrator.health()
    def dependency_map(self): return self.orchestrator.dependency_map()
    def manager_status(self):
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            record=GlobalEcosystemManager().get("GLOBAL-SECURITY-CORE-ECOSYSTEM")
        except Exception as exc: return {"success":False,"registered":False,"ecosystem":None,"error":type(exc).__name__}
        return {"success":record is not None,"registered":record is not None,"ecosystem":record,"live_service_connections_verified":False}
