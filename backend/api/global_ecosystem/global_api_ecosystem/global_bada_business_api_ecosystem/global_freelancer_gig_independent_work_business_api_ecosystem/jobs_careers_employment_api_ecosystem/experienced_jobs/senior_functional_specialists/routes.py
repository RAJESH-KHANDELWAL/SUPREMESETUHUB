"""HTTP endpoints for Senior Functional Specialists."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/experienced_jobs/senior_functional_specialists", tags=["Work & Careers", "experienced_jobs", "senior_functional_specialists"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
