"""HTTP endpoints for Apprentice Trade Roles."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/entry_level_jobs/apprentice_trade_roles", tags=["Work & Careers", "entry_level_jobs", "apprentice_trade_roles"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
