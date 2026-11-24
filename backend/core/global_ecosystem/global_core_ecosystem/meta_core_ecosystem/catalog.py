"""Canonical Meta provider Core catalog, sourced from Meta API family registry."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .constants import ECOSYSTEM_ID,ECOSYSTEM_NAME,API_ROOT,ENGINE_ROOT,CANONICAL_MASTER_ENTRY_IDS
from .product_catalog import list_meta_products
from .domain_catalog import list_meta_domain_inventory
from backend.api.global_ecosystem.global_api_ecosystem.meta_api_ecosystem.meta_api_ecosystem import META_API_ECOSYSTEM
META_CORE_ECOSYSTEM:dict[str,Any]={
 "ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"provider":"meta","provider_id":"meta",
 "ecosystem_type":"PROVIDER_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM",
 "status":"CORE_CATALOG_ONLY","enabled":True,
 "api_catalog_ref":API_ROOT,"engine_catalog_ref":ENGINE_ROOT,
 "source_api_catalog":"backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_api_ecosystem.py",
 "master_catalog_path":"backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
 "canonical_master_entry_ids":list(CANONICAL_MASTER_ENTRY_IDS),
 "master_catalog_alignment":"EXISTING_RELATED_TOPICS_ONLY_NO_META_SPECIFIC_ENTRY",
 "live_connection_verified":False,"oauth_exchange_in_core":False,
 "api_transport_in_core":False,"engine_execution_in_core":False,
 "remote_operations_enabled":False,"credential_storage":"TENANT_SCOPED_EXTERNAL_SECRET_STORE_ONLY",
}
def get_meta_core_catalog()->dict[str,Any]:
    products=list_meta_products()
    domains=list_meta_domain_inventory()
    return {**deepcopy(META_CORE_ECOSYSTEM),"children":products,"product_count":len(products),"domains":domains,"domain_count":len(domains),"api_calls_performed":0}
