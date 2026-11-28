"""Authenticated-by-platform cultural knowledge API."""
from __future__ import annotations
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem.service import CulturalKnowledgeDomainService
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem import CULTURAL_DOMAINS
from backend.engine.global_ecosystem.global_engine_ecosystem.cultural_knowledge_engine_ecosystem.manager import CulturalKnowledgeEngineManager
from backend.ai.cultural_knowledge_assistant import CulturalKnowledgeAssistant
from backend.database.cultural_knowledge_repository import CulturalKnowledgeRepository

router = APIRouter(prefix="/api/v1/global-cultural-knowledge", tags=["GLOBAL CULTURAL KNOWLEDGE"])
domain_service = CulturalKnowledgeDomainService()
engine = CulturalKnowledgeEngineManager(core=domain_service, domains=CULTURAL_DOMAINS)
assistant = CulturalKnowledgeAssistant(engine=engine)
repository = CulturalKnowledgeRepository()

class CulturalSearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=300)
    domain: str | None = Field(default=None, max_length=80)

@router.get("/status")
def cultural_knowledge_status():
    return {"success": True, "ecosystem": domain_service.describe(),
            "engine": engine.status(),
            "database": "AVAILABLE_ON_INITIALIZATION",
            "ai_context_builder": "READY_NO_PROVIDER_CALL",
            "cloud_sync": "ADAPTER_REQUIRED"}

@router.get("/knowledge")
def cultural_knowledge():
    return {"success": True, "knowledge": domain_service.knowledge()}

@router.get("/search")
def cultural_knowledge_search(q: str = Query(min_length=1, max_length=300),
                              domain: str | None = Query(default=None, max_length=80)):
    try:
        return {"success": True, "results": engine.search(q, domain=domain)}
    except (ValueError, KeyError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.post("/ai-context")
def cultural_ai_context(request: CulturalSearchRequest):
    try:
        return {"success": True, "context": assistant.build_context(request.query, request.domain)}
    except (ValueError, KeyError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.get("/records/{record_id}")
def cultural_record(record_id: str):
    try:
        record = repository.get(record_id)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="CULTURAL_DATABASE_UNAVAILABLE") from exc
    if record is None:
        raise HTTPException(status_code=404, detail="CULTURAL_RECORD_NOT_FOUND")
    return {"success": True, "record": record}
