"""Category-specific API routes for Executive Search & Leadership Hiring."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/executive-search", tags=["JOBS & CAREERS - EXECUTIVE SEARCH & LEADERSHIP HIRING"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
