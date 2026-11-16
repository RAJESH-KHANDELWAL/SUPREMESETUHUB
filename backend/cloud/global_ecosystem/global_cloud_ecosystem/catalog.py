"""Canonical metadata catalog for GLOBAL CLOUD ECOSYSTEM."""
from __future__ import annotations
from typing import Any

CLOUD_ECOSYSTEM_PROFILE = {
    "ecosystem_id": "GLOBAL_CLOUD_ECOSYSTEM",
    "name": "GLOBAL CLOUD ECOSYSTEM",
    "layer": "CLOUD",
    "status": "FOUNDATION_READY",
    "runtime_status": "NO_LIVE_CONNECTIONS_CONFIGURED",
    "description": "Provider-neutral registry and integration contracts for cloud infrastructure services.",
}

CLOUD_PROVIDERS = (
    {"provider_id": "google_cloud", "name": "Google Cloud", "category": "public_cloud", "capabilities": ("compute", "storage", "database", "networking", "ai_ml"), "adapter_module": "google_cloud.service", "status": "not_configured"},
    {"provider_id": "aws_cloud", "name": "Amazon Web Services", "category": "public_cloud", "capabilities": ("compute", "storage", "database", "networking", "ai_ml"), "adapter_module": "aws_cloud.service", "status": "not_configured"},
    {"provider_id": "microsoft_azure", "name": "Microsoft Azure", "category": "public_cloud", "capabilities": ("compute", "storage", "database", "networking", "ai_ml"), "adapter_module": None, "status": "not_configured"},
    {"provider_id": "cloudflare_cloud", "name": "Cloudflare", "category": "edge_cloud", "capabilities": ("dns", "cdn", "edge_compute", "security", "object_storage"), "adapter_module": "cloudflare_cloud.service", "status": "not_configured"},
)

def get_cloud_catalog() -> dict[str, Any]:
    return {
        "ecosystem": dict(CLOUD_ECOSYSTEM_PROFILE),
        "providers": [
            {**item, "capabilities": list(item["capabilities"])}
            for item in CLOUD_PROVIDERS
        ],
        "provider_count": len(CLOUD_PROVIDERS),
        "live_connections_enabled": False,
    }
