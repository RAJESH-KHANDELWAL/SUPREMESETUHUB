"""FastAPI endpoints for the adult-only wellness taxonomy."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import AdultWellnessListResponse, AdultWellnessDetailResponse
from .service import AdultWellnessEcosystemService

router = APIRouter(prefix="/adult-wellness", tags=["ADULT SEXUAL WELLNESS API ECOSYSTEM (18+)"])
service = AdultWellnessEcosystemService()

@router.get("/status")
def status():
    return service.get_status()

@router.get("", response_model=AdultWellnessListResponse)
def list_categories(coverage: str | None = Query(default=None, pattern="^(india|global)$"), q: str | None = Query(default=None, min_length=1, max_length=120)):
    items = service.list_categories(coverage=coverage, query=q)
    return {"success": True, "count": len(items), "categories": items}

@router.get("/{category_id}", response_model=AdultWellnessDetailResponse)
def get_category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "ADULT_WELLNESS_CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "category": item}
