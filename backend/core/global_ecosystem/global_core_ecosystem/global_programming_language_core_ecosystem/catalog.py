"""Canonical Global Programming Language CORE registry and compatibility facade."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, PARENT_ECOSYSTEM_ID, STATUS
from .domain_catalog import list_programming_language_domains, programming_language_domain_summary
from .language_catalog import LANGUAGE_RECORDS, language_catalog_summary, list_language_records
SERVICE_TIERS = (
 {"tier_id":"NORMAL","name":"Normal","rank":1},{"tier_id":"BASIC","name":"Basic","rank":2},
 {"tier_id":"STANDARD","name":"Standard","rank":3},{"tier_id":"PREMIUM","name":"Premium","rank":4},
 {"tier_id":"PROFESSIONAL","name":"Professional","rank":5},{"tier_id":"ENTERPRISE","name":"Enterprise","rank":6},
 {"tier_id":"SUPREME","name":"Supreme","rank":7},
)
PROGRAMMING_LANGUAGE_CORE_ECOSYSTEM: dict[str, Any] = {
 "ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"provider":"global_programming_languages",
 "ecosystem_type":"GLOBAL_CORE_SERVICE","parent_id":PARENT_ECOSYSTEM_ID,"status":STATUS,"enabled":True,
 "coverage":{"domains":26,"language_metadata_records":len(LANGUAGE_RECORDS),"coverage_exhaustive":False},
 "capabilities":["PROGRAMMING_LANGUAGE_DOMAIN_REGISTRY","LANGUAGE_TYPE_CLASSIFICATION","LANGUAGE_FAMILY_AND_DIALECT_METADATA","ALIAS_AND_PARADIGM_METADATA","VERSION_AND_SPECIFICATION_METADATA","RUNTIME_COMPILER_DISCOVERY_METADATA","TOOLCHAIN_BUILD_AND_PACKAGE_METADATA","QUERY_MARKUP_SERIALIZATION_CLASSIFICATION","HARDWARE_SHADER_AND_GPU_LANGUAGE_CLASSIFICATION","SMART_CONTRACT_AND_PROOF_LANGUAGE_CLASSIFICATION","TESTING_QUALITY_SECURITY_LIFECYCLE_METADATA","SERVICE_TIER_METADATA"],
 "children":[{"ecosystem_id":f"PROGRAMMING-LANGUAGE-DOMAIN-{x['id']}","name":x["name"],"domain_id":x["id"],"core_module":f"backend/core/global_ecosystem/global_core_ecosystem/global_programming_language_core_ecosystem/{x['folder']}","status":STATUS,"enabled":True,"capabilities":["DOMAIN_METADATA_READ","LANGUAGE_CLASSIFICATION_READ"]} for x in list_programming_language_domains()],
}
def get_programming_language_core_catalog() -> dict[str, Any]: return deepcopy(PROGRAMMING_LANGUAGE_CORE_ECOSYSTEM)
def list_programming_language_core_modules(include_disabled: bool = False) -> list[dict[str, Any]]:
 items=deepcopy(PROGRAMMING_LANGUAGE_CORE_ECOSYSTEM["children"])
 return items if include_disabled else [x for x in items if x.get("enabled",True)]
def get_catalog() -> dict[str, Any]:
 domains=list_programming_language_domains()
 return {"ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"parent_id":PARENT_ECOSYSTEM_ID,"status":STATUS,"division_count":1,"divisions":[{"division_id":"PROGRAMMING","name":"PROGRAMMING LANGUAGES","folder":"global_programming_language_core_ecosystem"}],"domain_count":len(domains),"domains":domains,"language_record_count":language_catalog_summary()["record_count"],"languages":list_language_records(),"service_tiers":deepcopy(list(SERVICE_TIERS)),"domain_coverage_exhaustive":False,"language_coverage_exhaustive":False,"runtime_execution_verified":False,"api_calls_performed":0}
