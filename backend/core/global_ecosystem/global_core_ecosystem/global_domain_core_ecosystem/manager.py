"""Canonical manager for GLOBAL DOMAIN CORE ECOSYSTEM."""
from __future__ import annotations
from .orchestrator import DomainCoreOrchestrator
from .module_service import DomainModuleService
from .service import GlobalDomainCoreService
from .catalog import ECOSYSTEM_ID, ECOSYSTEM_NAME, list_sector_ecosystems
class GlobalDomainCoreManager:
    NAME=ECOSYSTEM_NAME
    ECOSYSTEM_ID=ECOSYSTEM_ID
    def __init__(self):
        self.orchestrator=DomainCoreOrchestrator()
        self.service=GlobalDomainCoreService()
    def status(self):
        result=self.service.status()
        result["ecosystem_name"]=self.NAME
        result["sector_ecosystem_count"]=len(list_sector_ecosystems())
        result["naming_standard"]="GLOBAL + SUBJECT + CORE ECOSYSTEM"
        return result
    def health(self): return self.orchestrator.health()
    def list_providers(self): return self.orchestrator.providers()
    def list_domains(self): return self.orchestrator.domains()
    def list_sector_ecosystems(self): return list_sector_ecosystems()
    def get_sector_ecosystem(self,ecosystem_id:str):
        return next((row for row in list_sector_ecosystems() if row["ecosystem_id"]==ecosystem_id),None)
    def get_domain_manager(self, domain_id:str): return DomainModuleService(domain_id)
def get_manager() -> GlobalDomainCoreManager:
    return GlobalDomainCoreManager()
__all__=["GlobalDomainCoreManager","get_manager"]
