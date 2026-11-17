"""Canonical Server Core inventory and scope catalog."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .constants import CAPABILITIES, ECOSYSTEM_ID, ECOSYSTEM_NAME
from .domain_catalog import server_core_domain_summary
from .provider_catalog import get_provider_catalog, provider_summary
from .scope_catalog import get_scope_catalog

def get_catalog() -> dict[str, Any]:
    scope=get_scope_catalog()
    domains=server_core_domain_summary()
    return {"ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,
            "provider":"provider-neutral","ecosystem_type":"GLOBAL_INFRASTRUCTURE_CORE",
            "parent_id":"GLOBAL-CORE-ECOSYSTEM","layer":"CORE",
            "status":"CORE_CATALOG_AVAILABLE","enabled":True,
            "capabilities":list(CAPABILITIES),"providers":get_provider_catalog(),
            **provider_summary(),"core_domains":domains["domains"],
            "core_domain_count":domains["domain_count"],
            "workload_domains":scope["workload_domains"]["domains"],
            "workload_domain_count":len(scope["workload_domains"]["domains"]),
            "geographic_scope":scope["geographic_scope"],
            "service_tiers":scope["service_tiers"]["tiers"],
            "adult_workload_policy":scope["workload_domains"]["adult_workload_policy"],
            "remote_operations_enabled":False,"live_provider_connections_verified":0,
            "api_calls_performed":0,"registry_persistence":"PROCESS_LOCAL_ONLY"}

def get_server_core_catalog() -> dict[str, Any]:
    return deepcopy(get_catalog())
