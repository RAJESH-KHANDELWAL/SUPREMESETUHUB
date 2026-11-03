"""Category-specific API routes for Outsourcing & Business Process Services."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/outsourcing-and-bpo", tags=["JOBS & CAREERS - OUTSOURCING & BUSINESS PROCESS SERVICES"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
