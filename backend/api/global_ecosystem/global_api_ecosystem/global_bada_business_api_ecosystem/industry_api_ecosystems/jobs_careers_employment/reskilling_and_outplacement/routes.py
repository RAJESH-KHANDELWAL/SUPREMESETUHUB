"""Category-specific API routes for Reskilling & Outplacement."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/reskilling-and-outplacement", tags=["JOBS & CAREERS - RESKILLING & OUTPLACEMENT"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
