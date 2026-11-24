"""Central manager for programming-language CORE metadata (Google Core pattern)."""
from __future__ import annotations
from typing import Any
from .orchestrator import ProgrammingLanguageCoreOrchestrator
from .service import ProgrammingLanguageCoreEcosystemService
from .module_service import ProgrammingLanguageDomainCoreService
class GlobalProgrammingLanguageCoreManager:
 NAME="GLOBAL PROGRAMMING LANGUAGE CORE ECOSYSTEM"
 ECOSYSTEM_ID="GLOBAL-PROGRAMMING-LANGUAGE-CORE-ECOSYSTEM"
 def __init__(self)->None:
  self._orchestrator=ProgrammingLanguageCoreOrchestrator();self._service=ProgrammingLanguageCoreEcosystemService()
 def status(self)->dict[str,Any]: return self._service.status()
 def health(self)->dict[str,Any]: return self._orchestrator.health()
 def catalog(self)->dict[str,Any]: return self._orchestrator.catalog()
 def list_domains(self)->dict[str,Any]: return self._orchestrator.domains()
 def list_domain_inventory(self)->list[dict[str,Any]]: return self._orchestrator.catalog().get("children",[])
 def list_languages(self,language_type:str|None=None,*,search:str|None=None)->dict[str,Any]: return self._orchestrator.languages(language_type,search=search)
 def get_language(self,language_id_or_name:str)->dict[str,Any]|None: return self._orchestrator.get_language(language_id_or_name)
 def get_domain(self,domain_id:str)->dict[str,Any]|None: return self._orchestrator.get_domain(domain_id)
 def get_domain_manager(self,domain_id:str)->ProgrammingLanguageDomainCoreService: return ProgrammingLanguageDomainCoreService(domain_id)
 def list_tiers(self)->dict[str,Any]:
  from .catalog import SERVICE_TIERS
  return {"success":True,"count":len(SERVICE_TIERS),"tiers":list(SERVICE_TIERS)}
ProgrammingLanguageCoreManager=GlobalProgrammingLanguageCoreManager
def get_manager()->GlobalProgrammingLanguageCoreManager: return GlobalProgrammingLanguageCoreManager()
__all__=["GlobalProgrammingLanguageCoreManager","ProgrammingLanguageCoreManager","get_manager"]
