"""FastAPI routes for Agriculture, Food & Natural Resources."""
from fastapi import APIRouter, HTTPException, Query

from .schemas import AgricultureCategoryDetailResponse, AgricultureCategoryListResponse
from .service import AgricultureFoodService

router = APIRouter(
    prefix="/agriculture-food-natural-resources",
    tags=["GLOBAL BADA BUSINESS - AGRICULTURE & FOOD"],
)
service = AgricultureFoodService()

@router.get("/status")
def get_status():
    return service.get_status()

@router.get("/categories", response_model=AgricultureCategoryListResponse)
def list_categories(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_categories(query=q)
    return {"success": True, "count": len(items), "categories": items}

@router.get("/categories/{category_id}", response_model=AgricultureCategoryDetailResponse)
def get_category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "AGRICULTURE_CATEGORY_NOT_FOUND", "category_id": category_id},
        )
    return {"success": True, "category": item}
