"""Canonical, read-only database provider catalog; mirrors the API catalog contract."""
from __future__ import annotations
from copy import deepcopy
from pathlib import Path

ECOSYSTEM_ID = "GLOBAL-DATABASE-CORE-ECOSYSTEM"
API_CATALOG_REF = "backend/api/global_ecosystem/global_api_ecosystem/global_database_api_ecosystem/service.py"
CATEGORY_IDS = (
    "relational", "document", "key_value", "graph", "time_series", "vector",
    "search_analytics", "embedded_edge", "warehouse_lakehouse", "cloud_database_platform",
)
PROVIDERS = (
    {"provider_id": "aws", "provider_name": "AWS", "package": "aws_database_core_ecosystem", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "apple", "provider_name": "Apple", "package": "apple_database_core_ecosystem", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "google", "provider_name": "Google", "package": "google_database_core_ecosystem", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "ibm", "provider_name": "IBM", "package": "ibm_database_core_ecosystem", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "microsoft", "provider_name": "Microsoft", "package": "microsoft_database_core_ecosystem", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "oracle", "provider_name": "Oracle", "package": "oracle_database_core_ecosystem", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "salesforce", "provider_name": "Salesforce", "package": "salesforce_database_core_ecosystem", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
)

def list_providers():
    return deepcopy(list(PROVIDERS))

def get_provider(provider_id: str):
    return next((deepcopy(p) for p in PROVIDERS if p["provider_id"] == provider_id.strip().casefold()), None)

def list_categories():
    return list(CATEGORY_IDS)

def validate_catalog():
    ids = [p["provider_id"] for p in PROVIDERS]
    packages = [p["package"] for p in PROVIDERS]
    base = Path(__file__).parent
    return {
        "valid": len(ids) == 7 and len(set(ids)) == 7 and len(set(packages)) == 7,
        "provider_count": len(ids),
        "category_count": len(CATEGORY_IDS),
        "missing_manifests": [p["package"] for p in PROVIDERS if not (base / p["package"] / "ecosystem_manifest.json").is_file()],
    }
