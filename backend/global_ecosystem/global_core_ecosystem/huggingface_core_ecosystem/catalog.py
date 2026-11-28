"""Canonical Hugging Face CORE catalog and cross-layer references."""
from copy import deepcopy
from .constants import *
from .product_catalog import list_products, product_summary
from .domain_catalog import list_domains, domain_summary

def get_catalog() -> dict:
    products = list_products()
    domains = list_domains()
    return {
        "ecosystem_id": ECOSYSTEM_ID, "name": ECOSYSTEM_NAME, "provider_id": PROVIDER_ID,
        "provider": "Hugging Face", "layer": LAYER, "parent_id": PARENT_ECOSYSTEM_ID,
        "status": "CORE_CATALOG_ONLY", "enabled": True,
        "capabilities": ["PROVIDER_IDENTITY","PRODUCT_DISCOVERY","DOMAIN_TAXONOMY","LIFECYCLE_METADATA",
                         "TENANT_CONTEXT","SECRET_REFERENCE_BOUNDARY","POLICY_GUARDRAILS","READINESS",
                         "DEPENDENCY_DISCOVERY","QUOTA_AND_HEALTH_METADATA"],
        "products": products, **product_summary(), "domains": domains, **domain_summary(),
        "master_catalog": {"path": MASTER_CATALOG_PATH, "access_mode": "READ_ONLY",
                           "canonical_entry_ids": list(CANONICAL_MASTER_ENTRY_IDS),
                           "catalogue_entries_added": 0},
        "api_catalog_ref": API_CATALOG_PATH, "engine_ref": ENGINE_PATH, "runtime_ref": RUNTIME_PATH,
        "live_connection_verified": False, "connected": False, "api_calls_performed": 0,
        "remote_operations_enabled": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    }
def get_huggingface_core_catalog() -> dict:
    return deepcopy(get_catalog())
