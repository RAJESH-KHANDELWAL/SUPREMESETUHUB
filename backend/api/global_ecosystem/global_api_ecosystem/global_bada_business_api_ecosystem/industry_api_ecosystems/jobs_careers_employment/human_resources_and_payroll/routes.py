"""Category-specific API routes for Human Resources & Payroll."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/human-resources-and-payroll", tags=["JOBS & CAREERS - HUMAN RESOURCES & PAYROLL"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
