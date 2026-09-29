from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.engines.ai.manager import AIEngine


router = APIRouter(
    prefix="/api/v1/ai",
    tags=["Central AI"],
)

# One shared AI Engine instance
ai_engine = AIEngine()


class AIGenerateRequest(BaseModel):
    capability: str
    provider: str
    payload: dict[str, Any] = Field(default_factory=dict)


@router.get("/status")
def ai_status():
    return {
        "success": True,
        "ai": ai_engine.status(),
    }


@router.get("/capabilities")
def ai_capabilities():
    return {
        "success": True,
        "capabilities": sorted(ai_engine.CAPABILITIES),
    }


@router.get("/providers")
def ai_providers():
    return {
        "success": True,
        "providers": ai_engine.list_providers(),
    }


@router.get("/providers/{capability}")
def ai_providers_by_capability(capability: str):
    try:
        providers = ai_engine.providers_for(capability)
        return {
            "success": True,
            "capability": capability,
            "providers": providers,
        }
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.post("/generate")
def ai_generate(request: AIGenerateRequest):
    try:
        result = ai_engine.generate(
            capability=request.capability,
            provider=request.provider,
            **request.payload,
        )

        return {
            "success": True,
            "provider": request.provider,
            "capability": request.capability,
            "result": result,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="AI_PROVIDER_REQUEST_FAILED",
        ) from exc
