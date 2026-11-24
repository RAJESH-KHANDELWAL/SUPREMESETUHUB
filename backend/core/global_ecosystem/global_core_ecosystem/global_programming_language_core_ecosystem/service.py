"""Global Programming Language CORE Ecosystem read-only control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_programming_language_core_catalog
from .orchestrator import ProgrammingLanguageCoreOrchestrator

class ProgrammingLanguageCoreEcosystemService:
    NAME="GLOBAL PROGRAMMING LANGUAGE CORE ECOSYSTEM"
    def __init__(self) -> None:
        self.orchestrator=ProgrammingLanguageCoreOrchestrator()
    def status(self) -> dict[str, Any]:
        catalog=get_programming_language_core_catalog(); health=self.orchestrator.health()
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],"name":self.NAME,"status":catalog["status"],"module_count":len(catalog["children"]),"domain_count":health["domain_count"],"language_record_count":health["language_record_count"],"runtime_execution_verified":False,"compiler_execution_verified":False,"api_calls_performed":0,"health":health}
    def list_modules(self) -> dict[str, Any]: return self.orchestrator.list_domains()
    def list_domains(self) -> dict[str, Any]: return self.orchestrator.domains()
    def list_languages(self, language_type: str | None = None, *, search: str | None = None) -> dict[str, Any]: return self.orchestrator.languages(language_type, search=search)
    def get_language(self, language_id_or_name: str) -> dict[str, Any] | None: return self.orchestrator.get_language(language_id_or_name)
    def get_module(self, domain_id: str) -> dict[str, Any] | None: return self.orchestrator.get_domain(domain_id)
    def health(self) -> dict[str, Any]: return self.orchestrator.health()
