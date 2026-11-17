"""Canonical provider-neutral SERVER CORE catalog."""
from __future__ import annotations
from copy import deepcopy
from .constants import ECOSYSTEM_ID,ECOSYSTEM_NAME,CAPABILITIES
from .provider_catalog import get_provider_catalog,provider_summary
def get_catalog():
    return {"ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"layer":"CORE","status":"CORE_CATALOG_ONLY","capabilities":list(CAPABILITIES),"providers":get_provider_catalog(),**provider_summary(),"service_tiers":[{"tier_id":x,"rank":i+1} for i,x in enumerate(("NORMAL","BASIC","STANDARD","PREMIUM","PROFESSIONAL","ENTERPRISE","SUPREME"))],"remote_operations_enabled":False,"api_calls_performed":0,"registry_persistence":"PROCESS_LOCAL_ONLY"}
def get_server_core_catalog(): return deepcopy(get_catalog())
