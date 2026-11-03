"""Category-specific API routes for Internships & Apprenticeships."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/internships-and-apprenticeships", tags=["JOBS & CAREERS - INTERNSHIPS & APPRENTICESHIPS"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
