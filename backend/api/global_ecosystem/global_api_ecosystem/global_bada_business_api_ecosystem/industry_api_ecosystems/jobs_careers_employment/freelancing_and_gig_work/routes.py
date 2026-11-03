"""Category-specific API routes for Freelancing & Gig Work."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/freelancing-and-gig-work", tags=["JOBS & CAREERS - FREELANCING & GIG WORK"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
