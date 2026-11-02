"""FastAPI routes for Education, Learning & Training."""
from fastapi import APIRouter, HTTPException, Query

from .schemas import EducationCategoryDetailResponse, EducationCategoryListResponse
from .service import EducationLearningService

router = APIRouter(
    prefix="/education-learning-training",
    tags=["GLOBAL BADA BUSINESS - EDUCATION & LEARNING"],
)
service = EducationLearningService()

@router.get("/status")
def get_status():
    return service.get_status()

@router.get("/categories", response_model=EducationCategoryListResponse)
def list_categories(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_categories(query=q)
    return {"success": True, "count": len(items), "categories": items}

@router.get("/categories/{category_id}", response_model=EducationCategoryDetailResponse)
def get_category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "EDUCATION_CATEGORY_NOT_FOUND", "category_id": category_id},
        )
    return {"success": True, "category": item}
