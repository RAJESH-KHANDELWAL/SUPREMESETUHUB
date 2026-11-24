"""REST routes for the global cultural knowledge ecosystem."""
from __future__ import annotations
from fastapi import APIRouter, HTTPException, Query
from .schemas import CulturalSearchRequest, CulturalRecordWriteRequest
from .service import GlobalCulturalAPIService
from backend.database.global_ecosystem.global_database_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_database_ecosystem.repository import GlobalCulturalRepository

router = APIRouter(prefix="/api/v1/global-vasudhaiva-kutumbakam",
                   tags=["GLOBAL VASUDHAIVA KUTUMBAKAM / CULTURE"])
service = GlobalCulturalAPIService()
repository = GlobalCulturalRepository()

@router.get("/status")
def status():
    return {"success": True, **service.status()}

@router.get("/domains")
def domains():
    return {"success": True, "domains": service.domains()}

@router.get("/knowledge")
def knowledge():
    return {"success": True, "knowledge": service.knowledge()}

@router.get("/search")
def search(q: str = Query(min_length=1, max_length=300),
           domain: str | None = Query(default=None, max_length=100)):
    try:
        return {"success": True, **service.search(q, domain)}
    except (ValueError, KeyError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.post("/ai-context")
def ai_context(request: CulturalSearchRequest):
    try:
        return {"success": True, "context": service.ai_context(request.query, request.domain)}
    except (ValueError, KeyError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.get("/records/{record_id}")
def get_record(record_id: str):
    try:
        record = repository.get(record_id)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="CULTURAL_DATABASE_UNAVAILABLE") from exc
    if record is None:
        raise HTTPException(status_code=404, detail="CULTURAL_RECORD_NOT_FOUND")
    return {"success": True, "record": record}

@router.get("/records")
def search_records(q: str = Query(min_length=1, max_length=300),
                   domain: str | None = Query(default=None, max_length=100),
                   limit: int = Query(default=30, ge=1, le=100)):
    try:
        return {"success": True, "records": repository.search(q, domain, limit)}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="CULTURAL_DATABASE_UNAVAILABLE") from exc

@router.post("/records")
def save_record(request: CulturalRecordWriteRequest):
    try:
        repository.save(request.model_dump())
    except (ValueError, KeyError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=503, detail="CULTURAL_DATABASE_UNAVAILABLE") from exc
    return {"success": True, "record_id": request.record_id, "publication_status": request.publication_status}
