"""HTTP endpoints for Night Shift Occupations."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/shift_work/night_shift_occupations", tags=["Work & Careers", "shift_work", "night_shift_occupations"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
