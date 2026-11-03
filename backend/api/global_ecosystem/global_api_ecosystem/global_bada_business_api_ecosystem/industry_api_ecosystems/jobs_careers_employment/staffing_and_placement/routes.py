"""Category-specific API routes for Staffing & Placement."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/staffing-and-placement", tags=["JOBS & CAREERS - STAFFING & PLACEMENT"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
