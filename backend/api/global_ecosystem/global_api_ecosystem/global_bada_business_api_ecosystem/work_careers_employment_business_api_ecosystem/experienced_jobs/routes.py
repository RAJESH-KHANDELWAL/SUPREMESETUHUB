"""Experienced Professional Jobs API routes."""
from fastapi import APIRouter,HTTPException,Query
from .categories import list_tracks,get_track,search_work_jobs
from .services import get_status
router=APIRouter(prefix="/experienced-jobs",tags=["Work & Careers — Experienced Professional Jobs"])
@router.get("/status")
def status(): return get_status()
@router.get("/work-jobs")
def work_jobs():
 items=list_tracks(); return {"success":True,"count":len(items),"taxonomy_only":True,"work_jobs":items}
@router.get("/work-jobs/{specialization_id}")
def track_detail(specialization_id:str):
 item=get_track(specialization_id)
 if item is None: raise HTTPException(status_code=404,detail={"error":"TRACK_NOT_FOUND","category_id":"experienced_jobs","specialization_id":specialization_id})
 return {"success":True,"track":item}
@router.get("/search")
def search(q:str=Query(min_length=1,max_length=100)):
 items=search_work_jobs(q); return {"success":True,"count":len(items),"work_jobs":items}
