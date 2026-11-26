"""Curated provider identity metadata; registration is not a live integration."""
from __future__ import annotations
from copy import deepcopy

_PROVIDERS = (
    {"provider_id": "aws", "name": "Amazon Web Services", "package": "aws_web_core_ecosystem", "provider_type": "CLOUD_AND_WEB_INFRASTRUCTURE"},
    {"provider_id": "cloudflare", "name": "Cloudflare", "package": "cloudflare_web_core_ecosystem", "provider_type": "DNS_CDN_AND_EDGE"},
    {"provider_id": "google", "name": "Google", "package": "google_web_core_ecosystem", "provider_type": "WEB_AND_CLOUD_PLATFORM"},
    {"provider_id": "microsoft", "name": "Microsoft", "package": "microsoft_web_core_ecosystem", "provider_type": "WEB_AND_CLOUD_PLATFORM"},
)
def list_providers() -> list[dict]:
    return [dict(item, status="CATALOG_ONLY", live_connection_verified=False,
                 remote_operations_enabled=False, credential_storage="EXTERNAL_SECRET_STORE_ONLY")
            for item in _PROVIDERS]

def get_provider(provider_id: str) -> dict | None:
    key = str(provider_id).strip().lower()
    return next((item for item in list_providers() if item["provider_id"] == key), None)

def provider_summary() -> dict:
    items = list_providers()
    return {"provider_count": len(items), "provider_ids": [item["provider_id"] for item in items]}
