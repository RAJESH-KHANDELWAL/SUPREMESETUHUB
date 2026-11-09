"""HTTP endpoints for Career Assessment Services."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/career_guidance/career_assessment_services", tags=["Work & Careers", "career_guidance", "career_assessment_services"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
