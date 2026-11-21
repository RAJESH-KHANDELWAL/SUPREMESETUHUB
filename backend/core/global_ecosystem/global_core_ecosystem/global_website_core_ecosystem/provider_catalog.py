"""Curated website provider/platform identity metadata; never asserts live integration."""
from __future__ import annotations

_PROVIDERS = (
    {"provider_id": "aws", "name": "Amazon Web Services", "package": "aws_website_core_ecosystem", "provider_type": "CLOUD_HOSTING_AND_WEB_INFRASTRUCTURE"},
    {"provider_id": "google", "name": "Google", "package": "google_website_core_ecosystem", "provider_type": "WEBSITE_PLATFORM_AND_CLOUD"},
    {"provider_id": "microsoft", "name": "Microsoft", "package": "microsoft_website_core_ecosystem", "provider_type": "CLOUD_HOSTING_AND_WEBSITE_PLATFORM"},
    {"provider_id": "vicetemple", "name": "ViceTemple", "package": "vicetemple_website_core_ecosystem", "provider_type": "WEBSITE_HOSTING_PROVIDER"},
)

def list_providers() -> list[dict]:
    return [
        {**item, "status": "CATALOG_ONLY", "live_connection_verified": False,
         "remote_operations_enabled": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"}
        for item in _PROVIDERS
    ]

def get_provider(provider_id: str) -> dict | None:
    key = str(provider_id).strip().lower()
    return next((item for item in list_providers() if item["provider_id"] == key), None)

def provider_summary() -> dict:
    items = list_providers()
    return {"provider_count": len(items), "provider_ids": [item["provider_id"] for item in items]}
