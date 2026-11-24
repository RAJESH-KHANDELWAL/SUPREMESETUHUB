"""REST endpoints for the Culture Service Work Business API ecosystem."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from .schemas import (
    CultureServiceWorkBusinessAIRequest,
    CultureServiceWorkBusinessRecordRequest,
)
from .service import GlobalCultureServiceWorkBusinessAPIService

router = APIRouter(
    prefix="/culture-service-work-business",
    tags=["GLOBAL BADA BUSINESS - CULTURE SERVICE WORK BUSINESS API"],
)
service = GlobalCultureServiceWorkBusinessAPIService()


@router.get("/status")
def status():
    return {"success": True, **service.status()}


@router.get("/catalogue")
def catalogue(domain: str | None = Query(default=None)):
    try:
        capabilities = service.catalogue(domain)
        return {"success": True, "count": len(capabilities), "capabilities": capabilities}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.get("/search")
def search(
    q: str = Query(min_length=1, max_length=300),
    domain: str | None = Query(default=None),
):
    try:
        return {"success": True, **service.search(q, domain)}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.post("/ai-context")
def ai_context(request: CultureServiceWorkBusinessAIRequest):
    try:
        return {
            "success": True,
            "context": service.ai_context(request.question, request.domain),
        }
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.get("/records")
def records(
    q: str = Query(default="", max_length=300),
    capability_id: str | None = Query(default=None, max_length=100),
    limit: int = Query(default=50, ge=1, le=100),
):
    """List APPROVED records only; repository enforces the publication filter."""
    try:
        rows = service.search_records(q, capability_id, limit)
        return {
            "success": True,
            "count": len(rows),
            "records": rows,
            "visibility": "APPROVED_ONLY",
        }
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="CULTURE_SERVICE_WORK_BUSINESS_DATABASE_UNAVAILABLE",
        ) from exc


@router.get("/records/{record_id}")
def get_record(record_id: str):
    """Expose approved records only; draft/review records are not public."""
    try:
        record = service.get_record(record_id)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="CULTURE_SERVICE_WORK_BUSINESS_DATABASE_UNAVAILABLE",
        ) from exc
    if record is None or str(record.get("status", "")).upper() != "APPROVED":
        # Do not reveal whether an unpublished record ID exists.
        raise HTTPException(status_code=404, detail="RECORD_NOT_FOUND")
    return {"success": True, "record": record}


@router.post("/records")
def save_record(request: CultureServiceWorkBusinessRecordRequest):
    try:
        result = service.save_record(request.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="CULTURE_SERVICE_WORK_BUSINESS_DATABASE_UNAVAILABLE",
        ) from exc
    return {"success": True, **result}


@router.get("/capabilities/{capability_id}")
def get_capability(capability_id: str):
    """Return one canonical CORE capability definition."""
    capability = service.core.capability(capability_id)
    if capability is None:
        raise HTTPException(status_code=404, detail="CAPABILITY_NOT_FOUND")
    return {"success": True, "capability": capability}


@router.post("/records/validate")
def validate_record(request: CultureServiceWorkBusinessRecordRequest):
    """Validate a proposed record without persisting it."""
    record = request.model_dump()
    errors = service.validate_record(record)
    return {
        "success": not errors,
        "valid": not errors,
        "errors": errors,
        "publication_allowed": service.can_publish_record(record),
    }
