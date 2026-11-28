"""Stable Python manager for Global VPN Core."""
from typing import Any
from .orchestrator import VPNCoreOrchestrator
from .service import VPNCoreService
from .domain_runtime import VPNCoreDomainManager
class VPNCoreManager:
 NAME="GLOBAL VPN CORE ECOSYSTEM";ECOSYSTEM_ID="GLOBAL-VPN-CORE-ECOSYSTEM"
 def __init__(self)->None:self._orchestrator=VPNCoreOrchestrator();self._service=VPNCoreService()
 def status(self)->dict[str,Any]:return self._service.status()
 def health(self)->dict[str,Any]:return self._orchestrator.health()
 def list_providers(self)->dict[str,Any]:return self._orchestrator.list_providers()
 def get_provider(self,provider_id:str)->dict[str,Any]|None:return self._orchestrator.get_provider(provider_id)
 def list_domains(self)->dict[str,Any]:return self._orchestrator.domains()
 def list_domain_inventory(self)->list[dict[str,str]]:return self._orchestrator.domain_inventory()
 def dependency_map(self)->dict[str,Any]:return self._orchestrator.dependency_map()
 def get_domain_manager(self,domain_id:str)->VPNCoreDomainManager:return VPNCoreDomainManager(domain_id)
def get_manager()->VPNCoreManager:return VPNCoreManager()
__all__=["VPNCoreManager","get_manager"]
