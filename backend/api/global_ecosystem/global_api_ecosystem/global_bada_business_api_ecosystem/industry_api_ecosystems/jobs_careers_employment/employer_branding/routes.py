"""Category-specific API routes for Employer Branding & Talent Marketing."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/employer-branding", tags=["JOBS & CAREERS - EMPLOYER BRANDING & TALENT MARKETING"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
