"""Global AI ecosystem bridge to the central AI engine and AI API provider catalog."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.engine.global_ecosystem.global_engine_ecosystem.global_ai_engine_ecosystem.manager import EcosystemEngineManager
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.service import GlobalAICoreService

from backend.api.ai import ai_engine
from backend.api.global_api_ecosystem_catalog import list_ai_api_provider_ecosystems
from backend.supreme.personal_ai.research import status as personal_ai_status
from backend.supreme.supreme_ecosystem.supreme_ai_ecosystem import status as supreme_ai_status

router = APIRouter(
    prefix="/api/v1/global-ai-ecosystem",
    tags=["GLOBAL AI ECOSYSTEM"],
)

# Application composition: API exposes CORE; CORE receives the ENGINE executor.
_global_ai_engine = EcosystemEngineManager()
_global_ai_core = GlobalAICoreService(executor=_global_ai_engine.generate)


class GlobalAIGenerateRequest(BaseModel):
    task: str = Field(min_length=1, max_length=12000)
    context: dict = Field(default_factory=dict)
    provider_id: str = Field(default="openai", min_length=1, max_length=80)
    capability: str = Field(default="text", min_length=1, max_length=80)


@router.post("/generate")
def global_ai_generate(request: GlobalAIGenerateRequest):
    try:
        return _global_ai_core.generate(
            task=request.task,
            context=request.context,
            provider_id=request.provider_id,
            capability=request.capability,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail="GLOBAL_AI_PROVIDER_REQUEST_FAILED") from exc


@router.get("/engine-status")
def global_ai_engine_status():
    return {"success": True, "system": "GLOBAL AI ENGINE ECOSYSTEM", "engine": _global_ai_engine.status()}


@router.get("/status")
def global_ai_ecosystem_status():
    return {
        "success": True,
        "system": "GLOBAL AI ECOSYSTEM",
        "parent": "GLOBAL AI API ECOSYSTEM",
        "root": "GLOBAL API ECOSYSTEM",
        "central_ai": ai_engine.status(),
        "global_ai_engine": _global_ai_engine.status(),
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
        "capabilities": _global_ai_engine.status()["capabilities"],
    }


@router.get("/providers")
def global_ai_providers():
    return {
        "success": True,
        "system": "GLOBAL AI ECOSYSTEM",
        "registered_runtime_providers": _global_ai_engine.provider_status(),
        "central_ai_engine_providers": ai_engine.list_providers(),
        "api_provider_ecosystems": list_ai_api_provider_ecosystems(),
        "note": (
            "registered_runtime_providers are the providers currently registered in "
            "the Global AI Engine; central_ai_engine_providers lists shared platform providers; "
            "api_provider_ecosystems is the wider catalog. "
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
        "runtime_registry": _global_ai_engine.provider_status(),
    }
