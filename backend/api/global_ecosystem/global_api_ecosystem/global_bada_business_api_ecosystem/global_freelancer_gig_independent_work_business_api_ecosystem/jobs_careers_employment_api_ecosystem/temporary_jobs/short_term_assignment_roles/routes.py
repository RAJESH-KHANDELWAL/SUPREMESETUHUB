"""HTTP endpoints for Short-Term Assignment Roles."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/temporary_jobs/short_term_assignment_roles", tags=["Work & Careers", "temporary_jobs", "short_term_assignment_roles"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
