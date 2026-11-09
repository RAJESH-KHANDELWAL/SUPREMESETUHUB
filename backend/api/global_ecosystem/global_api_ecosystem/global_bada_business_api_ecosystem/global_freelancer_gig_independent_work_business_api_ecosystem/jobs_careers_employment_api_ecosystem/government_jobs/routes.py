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

@router.get("/specializations")
@router.get("/tracks", include_in_schema=False)
def get_tracks():
    tracks = list_government_job_tracks()
    return {"success": True, "count": len(tracks), "taxonomy_only": True, "specializations": tracks, "tracks": tracks}

@router.get("/specializations/{track_id}")
@router.get("/tracks/{track_id}", include_in_schema=False)
def get_track_detail(track_id: str):
    track = get_government_job_track(track_id)
    if track is None:
        raise HTTPException(status_code=404, detail={"error": "GOVERNMENT_JOB_TRACK_NOT_FOUND", "track_id": track_id})
    return {"success": True, "track": track}

@router.get("/search")
def search_tracks(q: str = Query(min_length=1, max_length=100)):
    tracks = search_government_job_tracks(q)
    return {"success": True, "count": len(tracks), "specializations": tracks, "tracks": tracks}

@router.get("/integrity")
def get_integrity():
    result = get_government_jobs_status()
    if not result["structurally_valid"]:
        raise HTTPException(status_code=500, detail=result)
    return result
