"""Programming-language CORE discovery and taxonomy orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import get_programming_language_core_catalog
from .domain_catalog import get_programming_language_domain, list_programming_language_domains, programming_language_domain_summary
from .language_catalog import get_language_record, language_catalog_summary, list_language_records
from .policy import safe_module_summary

class ProgrammingLanguageCoreOrchestrator:
    def catalog(self) -> dict[str, Any]:
        return get_programming_language_core_catalog()
    def list_domains(self, *, enabled_only: bool = False) -> dict[str, Any]:
        items=self.catalog()["children"]
        if enabled_only: items=[x for x in items if x.get("enabled",True)]
        return {"success":True,"count":len(items),"domains":[safe_module_summary(x) for x in items]}
    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return get_programming_language_domain(domain_id)
    def domains(self) -> dict[str, Any]:
        return {"success":True,**programming_language_domain_summary(),"domains":list_programming_language_domains()}
    def languages(self, language_type: str | None = None, *, search: str | None = None) -> dict[str, Any]:
        items=list_language_records(language_type, search=search)
        return {"success":True,"count":len(items),"languages":items,"coverage_exhaustive":False,"metadata_only":True}
    def get_language(self, language_id_or_name: str) -> dict[str, Any] | None:
        return get_language_record(language_id_or_name)
    def health(self) -> dict[str, Any]:
        catalog=self.catalog(); domains=programming_language_domain_summary(); languages=language_catalog_summary()
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","domain_count":domains["domain_count"],"language_record_count":languages["record_count"],"enabled_domain_count":sum(bool(x.get("enabled",True)) for x in catalog["children"]),"runtime_execution_verified":False,"compiler_execution_verified":False,"api_calls_performed":0,"warning":"Catalog records do not prove an installed compiler, runtime, package, license entitlement or secure execution environment."}
