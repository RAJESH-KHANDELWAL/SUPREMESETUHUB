"""HTTP endpoints for Campus Recruitment Placements."""
from fastapi import APIRouter
from .services import get_job_family

router = APIRouter(prefix="/work-careers/placements/campus_recruitment_placements", tags=["Work & Careers", "placements", "campus_recruitment_placements"])

@router.get("")
def read_job_family():
    return {"success": True, "job_family": get_job_family()}

@router.get("/roles")
def read_role_examples():
    family = get_job_family()
    return {"success": True, "count": len(family["role_examples"]), "roles": family["role_examples"]}
