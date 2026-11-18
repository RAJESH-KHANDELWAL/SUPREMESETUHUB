"""Canonical provider inventory for Global Storage Core."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

GLOBAL_STORAGE_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "GLOBAL-STORAGE-CORE-ECOSYSTEM",
    "name": "GLOBAL STORAGE CORE ECOSYSTEM",
    "provider": "global",
    "ecosystem_type": "GLOBAL_STORAGE_CONTROL_PLANE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": True,
    "providers": [
        {"provider_id":"apple","name":"APPLE STORAGE CORE ECOSYSTEM","ecosystem_id":"APPLE-STORAGE-CORE-ECOSYSTEM","package":"apple_storage_core_ecosystem","status":"STORAGE_CORE_CATALOG_ONLY","enabled":True,"capabilities":["OBJECT_STORAGE_METADATA","FILE_STORAGE_METADATA","SYNC_POLICY_METADATA"],"adapter_ref":None},
        {"provider_id":"aws","name":"AWS STORAGE CORE ECOSYSTEM","ecosystem_id":"AWS-STORAGE-CORE-ECOSYSTEM","package":"aws_storage_core_ecosystem","status":"STORAGE_CORE_CATALOG_ONLY","enabled":True,"capabilities":["OBJECT_STORAGE_METADATA","BUCKET_POLICY_METADATA","RETENTION_POLICY_METADATA"],"adapter_ref":None},
        {"provider_id":"digitalocean","name":"DIGITALOCEAN STORAGE CORE ECOSYSTEM","ecosystem_id":"DIGITALOCEAN-STORAGE-CORE-ECOSYSTEM","package":"digitalocean_storage_core_ecosystem","status":"STORAGE_CORE_CATALOG_ONLY","enabled":True,"capabilities":["OBJECT_STORAGE_METADATA","SPACE_POLICY_METADATA","RETENTION_POLICY_METADATA"],"adapter_ref":None},
        {"provider_id":"google","name":"GOOGLE STORAGE CORE ECOSYSTEM","ecosystem_id":"GOOGLE-STORAGE-CORE-ECOSYSTEM","package":"google_storage_core_ecosystem","status":"STORAGE_CORE_CATALOG_ONLY","enabled":True,"capabilities":["OBJECT_STORAGE_METADATA","BUCKET_POLICY_METADATA","RETENTION_POLICY_METADATA","TENANT_ISOLATION_METADATA"],"adapter_ref":None},
        {"provider_id":"microsoft","name":"MICROSOFT STORAGE CORE ECOSYSTEM","ecosystem_id":"MICROSOFT-STORAGE-CORE-ECOSYSTEM","package":"microsoft_storage_core_ecosystem","status":"STORAGE_CORE_CATALOG_ONLY","enabled":True,"capabilities":["OBJECT_STORAGE_METADATA","FILE_STORAGE_METADATA","RETENTION_POLICY_METADATA"],"adapter_ref":None},
    ],
    "shared_components": {"integrations":"Provider adapter registration metadata only; no API clients.","services":"Core orchestration and read-only metadata services.","tools":"Validation and diagnostics; no destructive storage operations."},
    "security": {"tenant_context_required":True,"secrets_in_catalog":False,"live_connections_verified":False,"destructive_operations_enabled":False},
}

def get_storage_core_catalog() -> dict[str, Any]:
    return deepcopy(GLOBAL_STORAGE_CORE_ECOSYSTEM)

def list_storage_providers(*, enabled_only: bool = False) -> list[dict[str, Any]]:
    providers = get_storage_core_catalog()["providers"]
    return [item for item in providers if item.get("enabled", True)] if enabled_only else providers

def get_storage_provider(provider_id: str) -> dict[str, Any] | None:
    needle = provider_id.strip().casefold()
    if not needle: return None
    return next((item for item in list_storage_providers() if item["provider_id"].casefold() == needle or item["ecosystem_id"].casefold() == needle), None)
