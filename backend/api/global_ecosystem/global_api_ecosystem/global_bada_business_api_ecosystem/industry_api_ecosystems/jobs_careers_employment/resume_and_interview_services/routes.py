"""Category-specific API routes for Resume, Interview & Job Readiness."""
from fastapi import APIRouter
from .service import CategoryService

service = CategoryService()
router = APIRouter(prefix="/category-modules/resume-and-interview-services", tags=["JOBS & CAREERS - RESUME, INTERVIEW & JOB READINESS"])

@router.get("")
def get_category_module():
    return {"success": True, "category": service.get_category()}

@router.get("/status")
def get_category_module_status():
    return service.get_status()
