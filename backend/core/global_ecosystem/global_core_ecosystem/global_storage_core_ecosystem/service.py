"""Read-only service facade for Global Storage CORE."""
from __future__ import annotations

from typing import Any

from .capability_catalog import CAPABILITIES
from .contracts import CoreResult
from .policy import redact_metadata
from .provider_catalog import get_provider, list_providers


def describe() -> dict[str, Any]:
    return {
        "ecosystem_id": "GLOBAL-STORAGE-CORE-ECOSYSTEM",
        "layer": "CORE",
        "category": "STORAGE",
        "mode": "CORE_CATALOG_ONLY",
        "provider_count": len(list_providers(include_disabled=True)),
        "capability_count": len(CAPABILITIES),
        "providers": [p.provider_id for p in list_providers(include_disabled=True)],
        "capabilities": sorted(CAPABILITIES),
    }


def readiness() -> dict[str, Any]:
    """CORE catalog readiness only; this is not a live provider health check."""
    return {
        "status": "CORE_METADATA_AVAILABLE",
        "provider_connections_verified": False,
        "provider_api_calls_performed": 0,
        "operational_storage_available": None,
    }


def list_provider_metadata() -> CoreResult:
    records = []
    for provider in list_providers():
        records.append({
            "provider_id": provider.provider_id,
            "display_name": provider.display_name,
            "category": provider.category,
            "capabilities": list(provider.capabilities),
            "regions": list(provider.regions),
            "readiness": provider.readiness.value,
            "api_available": provider.api_available,
            "connection_verified": provider.connection_verified,
            "credential_reference_required": provider.credential_reference_required,
        })
    return CoreResult(True, status="CORE_METADATA_AVAILABLE",
                      data=redact_metadata({"providers": records, "capabilities": CAPABILITIES}))


def get_provider_metadata(provider_id: str) -> CoreResult:
    provider = get_provider(provider_id)
    if provider is None:
        return CoreResult(False, status="NOT_FOUND", errors=["PROVIDER_NOT_FOUND"])
    return CoreResult(True, status=provider.readiness.value, data={
        "provider_id": provider.provider_id,
        "display_name": provider.display_name,
        "category": provider.category,
        "capabilities": list(provider.capabilities),
        "regions": list(provider.regions),
        "api_available": provider.api_available,
        "connection_verified": provider.connection_verified,
    })


__all__ = ["describe", "readiness", "list_provider_metadata", "get_provider_metadata"]
