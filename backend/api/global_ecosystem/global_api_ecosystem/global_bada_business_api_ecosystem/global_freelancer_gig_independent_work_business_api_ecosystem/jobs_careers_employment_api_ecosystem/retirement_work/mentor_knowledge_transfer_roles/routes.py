"""HTTP endpoints for Mentor and Knowledge Transfer Roles."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/retirement_work/mentor_knowledge_transfer_roles", tags=["Work & Careers", "retirement_work", "mentor_knowledge_transfer_roles"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
