"""Executive Jobs API routes."""
from fastapi import APIRouter,HTTPException,Query
from .categories import list_tracks,get_track,search_tracks
from .services import get_status
router=APIRouter(prefix="/executive-jobs",tags=["Work & Careers — Executive Jobs"])
@router.get("/status")
def status(): return get_status()
@router.get("/specializations")
@router.get("/tracks", include_in_schema=False)
def tracks():
 items=list_tracks(); return {"success":True,"count":len(items),"taxonomy_only":True,"specializations":items,"tracks":items}
@router.get("/specializations/{track_id}")
@router.get("/tracks/{track_id}", include_in_schema=False)
def track_detail(track_id:str):
 item=get_track(track_id)
 if item is None: raise HTTPException(status_code=404,detail={"error":"TRACK_NOT_FOUND","category_id":"executive_jobs","track_id":track_id})
 return {"success":True,"specialization":item,"track":item}
@router.get("/search")
def search(q:str=Query(min_length=1,max_length=100)):
 items=search_tracks(q); return {"success":True,"count":len(items),"specializations":items,"tracks":items}
