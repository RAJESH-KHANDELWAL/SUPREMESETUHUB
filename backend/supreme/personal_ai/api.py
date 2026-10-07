from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from .core import SupremePersonalAI


router = APIRouter(
    prefix="/api/v1/supreme/personal-ai",
    tags=["SUPREME PERSONAL AI"],
)

supreme = SupremePersonalAI()


class PlanRequest(BaseModel):
    request: str = Field(min_length=1)
    actor_role: str = "OWNER"


class MemoryRequest(BaseModel):
    content: str = Field(min_length=1)
    category: str = "general"
    actor_role: str = "OWNER"


@router.get("/status")
def status():
    return supreme.status()


@router.get("/capabilities")
def capabilities():
    return {
        "success": True,
        "capabilities": supreme.capabilities(),
    }


@router.post("/plan")
def plan(payload: PlanRequest):
    try:
        return supreme.plan(
            request=payload.request,
            actor_role=payload.actor_role,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.get("/memory")
def memory():
    return {
        "success": True,
        "count": supreme.memory.count(),
        "records": supreme.memory.list(),
    }


@router.post("/memory")
def remember(payload: MemoryRequest):
    try:
        memory = supreme.remember(
            content=payload.content,
            category=payload.category,
            actor_role=payload.actor_role,
        )

        return {
            "success": True,
            "memory": memory,
        }

    except PermissionError as exc:
        raise HTTPException(
            status_code=403,
            detail=str(exc),
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
