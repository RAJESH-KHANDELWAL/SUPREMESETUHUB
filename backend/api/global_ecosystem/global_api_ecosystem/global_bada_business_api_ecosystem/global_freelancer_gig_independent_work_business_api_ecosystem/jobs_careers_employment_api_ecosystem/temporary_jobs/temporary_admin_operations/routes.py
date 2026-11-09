"""HTTP endpoints for Temporary Admin and Operations Roles."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/temporary_jobs/temporary_admin_operations", tags=["Work & Careers", "temporary_jobs", "temporary_admin_operations"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
