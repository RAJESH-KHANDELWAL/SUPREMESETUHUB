"""Canonical manager for Global Storage Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .orchestrator import GlobalStorageCoreOrchestrator
from .domain_runtime import StorageCoreDomainManager
from .service import GlobalStorageCoreEcosystemService
class GlobalStorageCoreManager:
 NAME="GLOBAL STORAGE CORE ECOSYSTEM"
 ECOSYSTEM_ID="GLOBAL-STORAGE-CORE-ECOSYSTEM"
 def __init__(self): self._orchestrator=GlobalStorageCoreOrchestrator(); self._service=GlobalStorageCoreEcosystemService()
 def status(self): return self._service.status()
 def health(self): return self._orchestrator.health()
 def list_providers(self,*,enabled_only:bool=False): return self._orchestrator.list_providers(enabled_only=enabled_only)
 def get_provider(self,provider_id:str): return self._orchestrator.get_provider(provider_id)
 def list_products(self,*,provider_id:str|None=None,domain_id:str|None=None,enabled_only:bool=False): return self._orchestrator.list_products(provider_id=provider_id,domain_id=domain_id,enabled_only=enabled_only)
 def get_product(self,product_id:str): return self._orchestrator.get_product(product_id)
 def list_domains(self): return self._orchestrator.domains()
 def list_domain_inventory(self): return self._orchestrator.domain_inventory()
 def dependency_map(self): return self._orchestrator.dependency_map()
 def get_domain_manager(self,domain_id:str): return StorageCoreDomainManager(domain_id)
def get_manager()->GlobalStorageCoreManager: return GlobalStorageCoreManager()
__all__=["GlobalStorageCoreManager","get_manager"]
