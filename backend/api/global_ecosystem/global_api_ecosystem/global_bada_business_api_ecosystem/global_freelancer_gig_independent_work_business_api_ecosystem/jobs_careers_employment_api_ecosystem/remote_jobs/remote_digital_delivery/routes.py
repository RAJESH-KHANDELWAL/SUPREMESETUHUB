"""HTTP endpoints for Remote Digital Delivery."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/remote_jobs/remote_digital_delivery", tags=["Work & Careers", "remote_jobs", "remote_digital_delivery"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
