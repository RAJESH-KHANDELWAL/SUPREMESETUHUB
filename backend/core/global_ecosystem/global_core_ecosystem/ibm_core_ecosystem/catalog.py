"""Canonical IBM provider-level Core catalog; read-only metadata, not API transport."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, API_ROOT, ENGINE_ROOT, CANONICAL_MASTER_ENTRY_IDS
from .product_catalog import list_products
from .domain_catalog import list_domains

IBM_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": ECOSYSTEM_ID,
    "name": ECOSYSTEM_NAME,
    "provider_id": "ibm",
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "CORE_CATALOG_ONLY",
    "api_catalog_ref": API_ROOT,
    "engine_catalog_ref": ENGINE_ROOT,
    "canonical_master_entry_ids": list(CANONICAL_MASTER_ENTRY_IDS),
    "master_catalog_alignment": "RELATED_CANONICAL_TECHNOLOGY_TOPICS_NO_IBM_SPECIFIC_ENTRY",
    "live_connection_verified": False,
    "api_transport_in_core": False,
    "engine_execution_in_core": False,
    "remote_operations_enabled": False,
    "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
}
def get_catalog() -> dict[str, Any]:
    products=list_products()
    return {**deepcopy(IBM_CORE_ECOSYSTEM),"children":products,"product_count":len(products),"domains":list_domains(),"domain_count":len(list_domains()),"api_calls_performed":0}
