"""Read-only public service for Global Storage Core."""
from __future__ import annotations
from typing import Any
from .catalog import get_storage_core_catalog
from .orchestrator import GlobalStorageCoreOrchestrator
class GlobalStorageCoreEcosystemService:
 NAME="GLOBAL STORAGE CORE ECOSYSTEM"
 def __init__(self): self.orchestrator=GlobalStorageCoreOrchestrator()
 def status(self)->dict[str,Any]:
  c=get_storage_core_catalog(); h=self.orchestrator.health()
  return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":self.NAME,"status":c["status"],"provider_count":h["provider_count"],"product_count":h["product_count"],"domain_count":h["domain_count"],"live_connection_verified":False,"storage_operations_performed":0,"health":h}
 def list_providers(self): return self.orchestrator.list_providers()
 def list_products(self,**filters): return self.orchestrator.list_products(**filters)
 def list_domains(self): return self.orchestrator.domains()
 def health(self): return self.orchestrator.health()
 def dependency_map(self): return self.orchestrator.dependency_map()
