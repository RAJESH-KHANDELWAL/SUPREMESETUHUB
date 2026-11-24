"""HTTP endpoints for Independent Professional Contracts."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/contract_jobs/independent_professional_contracts", tags=["Work & Careers", "contract_jobs", "independent_professional_contracts"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
