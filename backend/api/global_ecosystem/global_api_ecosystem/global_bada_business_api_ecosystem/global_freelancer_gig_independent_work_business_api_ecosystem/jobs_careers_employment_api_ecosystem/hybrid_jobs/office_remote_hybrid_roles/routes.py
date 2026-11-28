"""HTTP endpoints for Office and Remote Hybrid Roles."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/hybrid_jobs/office_remote_hybrid_roles", tags=["Work & Careers", "hybrid_jobs", "office_remote_hybrid_roles"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
