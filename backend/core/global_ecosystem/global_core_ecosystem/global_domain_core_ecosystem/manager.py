"""Canonical manager for GLOBAL DOMAIN CORE ECOSYSTEM."""
from __future__ import annotations
from typing import Any
from .orchestrator import DomainCoreOrchestrator
from .module_service import DomainModuleService
from .service import GlobalDomainCoreService
class GlobalDomainCoreManager:
    NAME="GLOBAL DOMAIN CORE ECOSYSTEM"
    ECOSYSTEM_ID="GLOBAL-DOMAIN-CORE-ECOSYSTEM"
    def __init__(self):
        self.orchestrator=DomainCoreOrchestrator()
        self.service=GlobalDomainCoreService()
    def status(self): return self.service.status()
    def health(self): return self.orchestrator.health()
    def list_providers(self): return self.orchestrator.providers()
    def list_domains(self): return self.orchestrator.domains()
    def get_domain_manager(self, domain_id:str): return DomainModuleService(domain_id)
def get_manager() -> GlobalDomainCoreManager:
    return GlobalDomainCoreManager()
__all__=["GlobalDomainCoreManager","get_manager"]
