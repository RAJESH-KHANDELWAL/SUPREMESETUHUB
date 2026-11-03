"""Category-specific API routes for Career Guidance & Counselling."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/career-guidance-and-counselling", tags=["JOBS & CAREERS - CAREER GUIDANCE & COUNSELLING"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
