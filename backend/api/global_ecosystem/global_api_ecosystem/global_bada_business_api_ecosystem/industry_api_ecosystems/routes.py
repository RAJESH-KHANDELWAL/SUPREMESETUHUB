"""FastAPI routes for Industry API Ecosystems."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import IndustryEcosystemDetailResponse, IndustryEcosystemListResponse
from .service import IndustryEcosystemService

router = APIRouter(prefix="/industries", tags=["GLOBAL BADA BUSINESS - INDUSTRY API ECOSYSTEMS"])
service = IndustryEcosystemService()

@router.get("/status")
def get_status():
    return service.get_status()

@router.get("", response_model=IndustryEcosystemListResponse)
def list_industries(
    channel: str | None = Query(default=None, pattern="^(online|offline|hybrid)$"),
    coverage: str | None = Query(default=None, pattern="^(india|global)$"),
    q: str | None = Query(default=None, min_length=1, max_length=100),
    include_adult: bool = Query(default=False, description="Show separately classified 18+ taxonomy; this flag is not age verification."),
):
    items = service.list_industries(channel=channel, coverage=coverage, query=q, include_adult=include_adult)
    return {"success": True, "count": len(items), "industries": items}

@router.get("/{industry_id}", response_model=IndustryEcosystemDetailResponse)
def get_industry(
    industry_id: str,
    include_adult: bool = Query(default=False, description="Show separately classified 18+ taxonomy; this flag is not age verification."),
):
    item = service.get_industry(industry_id, include_adult=include_adult)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "INDUSTRY_ECOSYSTEM_NOT_FOUND", "industry_id": industry_id})
    return {"success": True, "industry": item}


# Domain-specific industry APIs
from .agriculture_food_natural_resources.routes import router as agriculture_food_router

router.include_router(agriculture_food_router)
