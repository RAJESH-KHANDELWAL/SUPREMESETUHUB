from fastapi import APIRouter, HTTPException, Query

from .schemas import BusinessEcosystemStatus
from .service import BusinessEcosystemService


router = APIRouter(
    prefix="/api/v1/global-ecosystem/business",
    tags=["GLOBAL BADA BUSINESS API ECOSYSTEM"],
)

service = BusinessEcosystemService()


@router.get("/status", response_model=BusinessEcosystemStatus)
def get_status():
    return service.get_status()


@router.get("/modules")
def list_modules():
    return service.list_modules()


@router.get("/modules/{module_id}")
def get_module(module_id: str):
    module = service.get_module(module_id)
    if module is None:
        raise HTTPException(status_code=404, detail={"error": "BUSINESS_MODULE_NOT_FOUND", "module_id": module_id})
    return {"success": True, "ecosystem_id": service.ECOSYSTEM_ID, "module": module}


@router.get("/dimensions")
def list_business_dimensions():
    return service.list_dimensions()


@router.get("/dimensions/{dimension_id}")
def get_business_dimension(dimension_id: str):
    dimension = service.get_dimension(dimension_id)
    if dimension is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "BUSINESS_DIMENSION_NOT_FOUND", "dimension_id": dimension_id},
        )
    return {"success": True, "ecosystem_id": service.ECOSYSTEM_ID, "dimension": dimension}


@router.get("/catalog")
def list_business_categories(
    channel: str | None = Query(default=None, pattern="^(online|offline|hybrid)$"),
    include_adult: bool = Query(default=False, description="Include 18+ adult-industry categories"),
):
    return service.list_categories(channel=channel, include_adult=include_adult)


@router.get("/catalog/search")
def search_business_categories(
    q: str = Query(min_length=1, max_length=100),
    include_adult: bool = Query(default=False),
):
    results = service.search_categories(q, include_adult=include_adult)
    return {"success": True, "count": len(results), "categories": results}


@router.get("/catalog/{category_id}")
def get_business_category(
    category_id: str,
    include_adult: bool = Query(default=False),
):
    category = service.get_category(category_id, include_adult=include_adult)
    if category is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "BUSINESS_CATEGORY_NOT_FOUND", "category_id": category_id},
        )
    return {"success": True, "category": category}
