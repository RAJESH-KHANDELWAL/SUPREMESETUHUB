"""Canonical manager for NSFWinfra Core Ecosystem metadata."""
from __future__ import annotations
from typing import Any
from .orchestrator import NSFWinfraCoreOrchestrator
from .domain_runtime import NSFWinfraCoreDomainManager
from .service import NSFWinfraCoreEcosystemService
class NSFWinfraCoreManager:
 NAME="NSFW INFRA CORE ECOSYSTEM"
 ECOSYSTEM_ID="NSFWINFRA-CORE-ECOSYSTEM"
 def __init__(self):
  self._orchestrator=NSFWinfraCoreOrchestrator();self._service=NSFWinfraCoreEcosystemService()
 def status(self)->dict[str,Any]:return self._service.status()
 def health(self)->dict[str,Any]:return self._orchestrator.health()
 def list_products(self,*,enabled_only:bool=False)->dict[str,Any]:return self._orchestrator.products(enabled_only)
 def get_product(self,ecosystem_id:str)->dict[str,Any]|None:return self._orchestrator.product(ecosystem_id)
 def list_domains(self)->dict[str,Any]:return self._orchestrator.domains()
 def list_domain_inventory(self)->list[dict]:return self._orchestrator.domain_inventory()
 def list_offerings(self)->dict[str,Any]:return self._orchestrator.offerings()
 def dependency_map(self)->dict[str,Any]:return self._orchestrator.dependency_map()
 def master_catalog(self)->dict[str,Any]:return master_catalog_reference()
 def get_domain_manager(self,domain_id:str)->NSFWinfraCoreDomainManager:return NSFWinfraCoreDomainManager(domain_id)
def get_manager()->NSFWinfraCoreManager:return NSFWinfraCoreManager()
__all__=["NSFWinfraCoreManager","get_manager"]
