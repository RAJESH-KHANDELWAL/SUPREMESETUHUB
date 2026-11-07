"""Global AI ecosystem bridge to the central AI engine and AI API provider catalog."""
from __future__ import annotations

from fastapi import APIRouter

from backend.api.ai import ai_engine
from backend.api.global_api_ecosystem_catalog import list_ai_api_provider_ecosystems
from backend.supreme.personal_ai.research import status as personal_ai_status
from backend.supreme.supreme_ecosystem.supreme_ai_ecosystem import status as supreme_ai_status

router = APIRouter(
    prefix="/api/v1/global-ai-ecosystem",
    tags=["GLOBAL AI ECOSYSTEM"],
)


@router.get("/status")
def global_ai_ecosystem_status():
    return {
        "success": True,
        "system": "GLOBAL AI ECOSYSTEM",
        "parent": "GLOBAL AI API ECOSYSTEM",
        "root": "GLOBAL API ECOSYSTEM",
        "central_ai": ai_engine.status(),
        "personal_ai_research": personal_ai_status(),
        "supreme_ai_ecosystem": supreme_ai_status(),
        "source_package": "backend.api.global_ecosystem.global_api_ecosystem.global_ai_api_ecosystem",
        "api_provider_ecosystem_count": len(list_ai_api_provider_ecosystems()),
        "privacy": "PRIVATE_BY_DEFAULT",
    }


@router.get("/capabilities")
def global_ai_capabilities():
    return {
        "success": True,
        "system": "GLOBAL AI ECOSYSTEM",
        "capabilities": sorted(ai_engine.CAPABILITIES),
    }


@router.get("/providers")
def global_ai_providers():
    return {
        "success": True,
        "system": "GLOBAL AI ECOSYSTEM",
        "registered_runtime_providers": ai_engine.list_providers(),
        "api_provider_ecosystems": list_ai_api_provider_ecosystems(),
        "note": (
            "registered_runtime_providers are the providers currently registered in "
            "the central AI engine; api_provider_ecosystems is the wider catalog. "
            "Catalog presence does not mean credentials or live API access are configured."
        ),
    }


@router.get("/api-ecosystems")
def global_ai_api_ecosystems():
    providers = list_ai_api_provider_ecosystems()
    return {
        "success": True,
        "system": "GLOBAL AI API ECOSYSTEM",
        "parent": "GLOBAL API ECOSYSTEM",
        "count": len(providers),
        "providers": providers,
        "runtime_registry": ai_engine.list_providers(),
    }
