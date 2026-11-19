"""Canonical Global People Life CORE registry and compatibility facade."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .constants import ECOSYSTEM_ID,ECOSYSTEM_NAME,PARENT_ECOSYSTEM_ID,STATUS
from .domain_catalog import DOMAIN_DEFINITIONS,list_people_life_domains,people_life_domain_summary

SERVICE_TIERS=(
 {"tier_id":"NORMAL","name":"Normal","rank":1},
 {"tier_id":"BASIC","name":"Basic","rank":2},
 {"tier_id":"STANDARD","name":"Standard","rank":3},
 {"tier_id":"PREMIUM","name":"Premium","rank":4},
 {"tier_id":"PROFESSIONAL","name":"Professional","rank":5},
 {"tier_id":"ENTERPRISE","name":"Enterprise","rank":6},
 {"tier_id":"SUPREME","name":"Supreme","rank":7},
)
PEOPLE_LIFE_CORE_ECOSYSTEM: dict[str,Any]={
 "ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"provider":"global_people_life",
 "ecosystem_type":"GLOBAL_CORE_SERVICE","parent_id":PARENT_ECOSYSTEM_ID,"status":STATUS,"enabled":True,
 "capabilities":["PEOPLE_LIFE_DOMAIN_REGISTRY","LIFE_STAGE_AND_SERVICE_DISCOVERY","PRIVACY_AND_SAFETY_POLICY_METADATA","AGE_AND_CONSENT_POLICY_BOUNDARY","WORK_FAMILY_AND_WELLBEING_TAXONOMY"],
 "children":[{"ecosystem_id":f"PEOPLE-LIFE-DOMAIN-{x['id']}","name":x["name"],"domain_id":x["id"],"core_module":f"backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/{x['folder']}","status":STATUS,"enabled":True,"age_restricted":bool(x.get("age_restricted")),"capabilities":["DOMAIN_METADATA_READ","SERVICE_DISCOVERY_READ"]} for x in list_people_life_domains()]
}

def get_people_life_core_catalog() -> dict[str,Any]: return deepcopy(PEOPLE_LIFE_CORE_ECOSYSTEM)
def list_people_life_core_modules(include_disabled: bool=False) -> list[dict[str,Any]]:
    items=deepcopy(PEOPLE_LIFE_CORE_ECOSYSTEM["children"])
    return items if include_disabled else [x for x in items if x.get("enabled",True)]
def get_catalog() -> dict[str,Any]:
    domains=list_people_life_domains(); summary=people_life_domain_summary()
    return {"ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"parent_id":PARENT_ECOSYSTEM_ID,"status":STATUS,
      "division_count":1,"divisions":[{"division_id":"PEOPLE-LIFE","name":"PEOPLE LIFE","folder":"global_people_life_core_ecosystem"}],
      "domain_count":len(domains),"domains":domains,"service_tiers":deepcopy(list(SERVICE_TIERS)),
      **summary,"adult_content_policy_metadata":True,"live_service_connections_verified":False,"api_calls_performed":0}
