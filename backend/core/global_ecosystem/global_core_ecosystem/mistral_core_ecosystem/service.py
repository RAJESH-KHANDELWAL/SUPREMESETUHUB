"""Public Mistral Core Ecosystem read-only control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_mistral_core_catalog
from .orchestrator import MistralCoreOrchestrator

class MistralCoreEcosystemService:
 NAME="MISTRAL CORE ECOSYSTEM"
 def __init__(self)->None: self.orchestrator=MistralCoreOrchestrator()
 def status(self)->dict[str,Any]:
  cat=get_mistral_core_catalog();health=self.orchestrator.health()
  return {"success":True,"ecosystem_id":cat["ecosystem_id"],"name":self.NAME,
   "provider":"mistral","vendor":"Mistral AI","status":cat["status"],
   "module_count":len(cat["children"]),"domain_count":health["domain_count"],
   "connected_modules":0,"live_connection_verified":False,"api_calls_performed":0,
   "api_transport_in_core":False,"execution_in_core":False,
   "master_catalog":self.orchestrator.master_catalog(),"health":health}
 def list_modules(self)->dict[str,Any]: return self.orchestrator.list_products()
 def list_domains(self)->dict[str,Any]: return self.orchestrator.domains()
 def list_offerings(self)->dict[str,Any]: return self.orchestrator.offerings()
 def get_module(self,ecosystem_id:str)->dict[str,Any]|None: return self.orchestrator.get_product(ecosystem_id)

__all__=["MistralCoreEcosystemService"]
