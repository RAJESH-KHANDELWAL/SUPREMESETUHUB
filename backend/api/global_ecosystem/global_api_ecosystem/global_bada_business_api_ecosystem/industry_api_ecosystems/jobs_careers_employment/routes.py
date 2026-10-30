"""FastAPI routes for Jobs, Careers & Employment."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import JobsCareersCategoryDetailResponse, JobsCareersCategoryListResponse
from .service import JobsCareersService

router = APIRouter(prefix="/jobs-careers-employment", tags=["GLOBAL BADA BUSINESS - JOBS & CAREERS"])
service = JobsCareersService()

@router.get("/status")
def get_status():
    return service.get_status()

@router.get("/categories", response_model=JobsCareersCategoryListResponse)
def list_domain_categories(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_categories(query=q)
    return {"success": True, "count": len(items), "categories": items}

@router.get("/categories/{category_id}", response_model=JobsCareersCategoryDetailResponse)
def get_domain_category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "category": item}
