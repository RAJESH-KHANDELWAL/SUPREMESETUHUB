"""Canonical manager for the Mistral Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .domain_runtime import MistralCoreDomainManager
from .orchestrator import MistralCoreOrchestrator
from .service import MistralCoreEcosystemService

class MistralCoreManager:
 NAME="MISTRAL CORE ECOSYSTEM"
 ECOSYSTEM_ID="MISTRAL-CORE-ECOSYSTEM"
 def __init__(self)->None:
  self._orchestrator=MistralCoreOrchestrator()
  self._service=MistralCoreEcosystemService()
 def status(self)->dict[str,Any]: return self._service.status()
 def health(self)->dict[str,Any]: return self._orchestrator.health()
 def catalog(self)->dict[str,Any]: return self._orchestrator.catalog()
 def list_products(self,*,enabled_only:bool=False)->dict[str,Any]: return self._orchestrator.list_products(enabled_only=enabled_only)
 def get_product(self,identifier:str)->dict[str,Any]|None: return self._orchestrator.get_product(identifier)
 def list_domains(self)->dict[str,Any]: return self._orchestrator.domains()
 def list_domain_inventory(self)->list[dict[str,Any]]: return self._orchestrator.domain_inventory()
 def list_offerings(self)->dict[str,Any]: return self._orchestrator.offerings()
 def get_offering(self,offering_id:str)->dict[str,Any]|None: return self._orchestrator.get_offering(offering_id)
 def master_catalog(self)->dict[str,Any]: return self._orchestrator.master_catalog()
 def dependency_map(self)->dict[str,Any]: return self._orchestrator.dependency_map()
 def get_domain_manager(self,domain_id:str)->MistralCoreDomainManager: return MistralCoreDomainManager(domain_id)

def get_manager()->MistralCoreManager:
 """Return the canonical Mistral Core manager."""
 return MistralCoreManager()

__all__=["MistralCoreManager","get_manager"]
