"""HTTP endpoints for Small Business Jobs."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/private_sector_jobs/small_business_jobs", tags=["Work & Careers", "private_sector_jobs", "small_business_jobs"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
