"""Stable Python manager for Global VPS Core."""
from typing import Any
from .orchestrator import VPSCoreOrchestrator
from .service import VPSCoreService
from .domain_runtime import VPSCoreDomainManager
class VPSCoreManager:
 NAME="GLOBAL VPS CORE ECOSYSTEM";ECOSYSTEM_ID="GLOBAL-VPS-CORE-ECOSYSTEM"
 def __init__(self)->None:self._orchestrator=VPSCoreOrchestrator();self._service=VPSCoreService()
 def status(self)->dict[str,Any]:return self._service.status()
 def health(self)->dict[str,Any]:return self._orchestrator.health()
 def list_providers(self,*,enabled_only:bool=False)->dict[str,Any]:return self._orchestrator.list_providers(enabled_only=enabled_only)
 def get_provider(self,provider_id:str)->dict[str,Any]|None:return self._orchestrator.get_provider(provider_id)
 def list_domains(self)->dict[str,Any]:return self._orchestrator.domains()
 def list_domain_inventory(self)->list[dict[str,str]]:return self._orchestrator.domain_inventory()
 def dependency_map(self)->dict[str,Any]:return self._orchestrator.dependency_map()
 def get_domain_manager(self,domain_id:str)->VPSCoreDomainManager:return VPSCoreDomainManager(domain_id)
def get_manager()->VPSCoreManager:return VPSCoreManager()
__all__=["VPSCoreManager","get_manager"]
