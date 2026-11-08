"""HTTP endpoints for Permanent Staffing Services."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/staffing/permanent_staffing_services", tags=["Work & Careers", "staffing", "permanent_staffing_services"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
