"""Government Jobs taxonomy API routes."""
from fastapi import APIRouter, HTTPException, Query

from .services import (
    get_government_job_track,
    get_government_jobs_status,
    list_government_job_tracks,
    search_government_job_tracks,
)

router = APIRouter(prefix="/government-jobs", tags=["Work & Careers — Government Jobs"])

@router.get("/status")
def get_status():
    return get_government_jobs_status()

@router.get("/work-jobs")
def get_work_jobs():
    work_jobs = list_government_job_tracks()
    return {"success": True, "count": len(work_jobs), "taxonomy_only": True, "work_jobs": work_jobs}

@router.get("/work-jobs/{specialization_id}")
def get_work_job_detail(specialization_id: str):
    track = get_government_job_track(specialization_id)
    if track is None:
        raise HTTPException(status_code=404, detail={"error": "GOVERNMENT_JOB_TRACK_NOT_FOUND", "specialization_id": specialization_id})
    return {"success": True, "track": track}

@router.get("/search")
def search_work_jobs(q: str = Query(min_length=1, max_length=100)):
    work_jobs = search_government_job_tracks(q)
    return {"success": True, "count": len(work_jobs), "work_jobs": work_jobs}

@router.get("/integrity")
def get_integrity():
    result = get_government_jobs_status()
    if not result["structurally_valid"]:
        raise HTTPException(status_code=500, detail=result)
    return result
