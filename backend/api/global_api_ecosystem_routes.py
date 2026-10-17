"""GLOBAL API ECOSYSTEM catalog routes."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from backend.api.global_api_ecosystem_catalog import (
    get_provider_ecosystem,
    list_ai_api_provider_ecosystems,
    list_ecosystems,
    list_provider_ecosystems,
)

router = APIRouter(
    prefix="/api/v1/global-api-ecosystem",
    tags=["GLOBAL API ECOSYSTEM"],
)


@router.get("/status")
def global_api_ecosystem_status():
    ecosystems = list_ecosystems()
    providers = list_provider_ecosystems()
    return {
        "success": True,
        "system": "GLOBAL API ECOSYSTEM",
        "parent": "GLOBAL ECOSYSTEM",
        "ecosystem_count": len(ecosystems),
        "provider_ecosystem_count": len(providers),
        "ai_api_provider_count": len(list_ai_api_provider_ecosystems()),
        "live_connections_verified": sum(1 for provider in providers if provider["live_connection_verified"]),
        "catalog_only_is_not_connected": True,
    }


@router.get("/ecosystems")
def global_api_ecosystems():
    items = list_ecosystems()
    return {"success": True, "system": "GLOBAL API ECOSYSTEM", "count": len(items), "ecosystems": items}


@router.get("/providers")
def global_api_providers(family: str | None = Query(default=None, description="Optional family such as AI, CLOUD, STORAGE, PAYMENT")):
    providers = list_provider_ecosystems(family)
    return {
        "success": True,
        "system": "GLOBAL API ECOSYSTEM",
        "family": family.upper() if family else None,
        "count": len(providers),
        "providers": providers,
        "note": "Catalog membership is not a live provider connection. See implementation_status for the current code boundary.",
    }


@router.get("/providers/{provider_id}")
def global_api_provider(provider_id: str):
    provider = get_provider_ecosystem(provider_id)
    if provider is None:
        raise HTTPException(status_code=404, detail="API_PROVIDER_ECOSYSTEM_NOT_FOUND")
    return {"success": True, "system": "GLOBAL API ECOSYSTEM", "provider": provider}


@router.get("/ai-providers")
def global_api_ai_providers():
    providers = list_ai_api_provider_ecosystems()
    return {"success": True, "system": "GLOBAL API ECOSYSTEM", "family": "AI", "count": len(providers), "providers": providers}
