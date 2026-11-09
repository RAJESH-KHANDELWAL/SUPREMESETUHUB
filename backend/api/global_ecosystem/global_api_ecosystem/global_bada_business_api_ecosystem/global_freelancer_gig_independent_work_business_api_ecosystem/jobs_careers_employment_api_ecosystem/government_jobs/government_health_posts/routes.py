"""HTTP endpoints for Government Health Posts."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/government_jobs/government_health_posts", tags=["Work & Careers", "government_jobs", "government_health_posts"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
