"""Canonical Atlassian Core Ecosystem manager, modeled on Google Core manager APIs."""
from __future__
from typing import Any
from .orchestrator import AtlassianCoreOrchestrator
from .domain_runtime import AtlassianCoreDomainManager
from .service import AtlassianCoreEcosystemService
class AtlassianCoreManager:
 NAME="ATLASSIAN CORE ECOSYSTEM"; ECOSYSTEM_ID="ATLASSIAN-CORE-ECOSYSTEM"
 def __init__(self)->None: self._orchestrator=AtlassianCoreOrchestrator(); self._service=AtlassianCoreEcosystemService()
 def status(self)->dict[str,Any]: return self._service.status()
 def health(self)->dict[str,Any]: return self._orchestrator.health()
 def list_products(self,*,enabled_only:bool=False)->dict[str,Any]: return self._orchestrator.list_products(enabled_only=enabled_only)
 def get_product(self,ecosystem_id:str)->dict[str,Any]|None: return self._orchestrator.get_product(ecosystem_id)
 def list_domains(self)->dict[str,Any]: return self._orchestrator.domains()
 def list_domain_inventory(self)->list[dict[str,Any]]: return self._orchestrator.domain_inventory()
 def list_offerings(self)->dict[str,Any]: return self._orchestrator.offerings()
 def get_offering(self,product_id:str)->dict[str,Any]|None: return self._orchestrator.get_offering(product_id)
 def dependency_map(self)->dict[str,Any]: return self._orchestrator.dependency_map()
 def get_domain_manager(self,domain_id:str)->AtlassianCoreDomainManager: return AtlassianCoreDomainManager(domain_id)
def get_manager()->AtlassianCoreManager: return AtlassianCoreManager()
__all__=["AtlassianCoreManager","get_manager"]
