"""HTTP endpoints for International Remote Employment."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/international_jobs/international_remote_employment", tags=["Work & Careers", "international_jobs", "international_remote_employment"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
