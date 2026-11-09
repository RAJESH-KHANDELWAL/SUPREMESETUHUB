"""HTTP endpoints for Career Re-entry Professional Roles."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/return_to_work/career_reentry_professional_roles", tags=["Work & Careers", "return_to_work", "career_reentry_professional_roles"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
