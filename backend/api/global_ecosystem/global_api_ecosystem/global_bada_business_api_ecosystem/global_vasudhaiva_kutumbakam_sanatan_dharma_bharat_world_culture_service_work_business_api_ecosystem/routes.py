"""REST endpoints for the Culture Service Work Business API ecosystem."""
from __future__ import annotations
from fastapi import APIRouter,HTTPException,Query
from .schemas import CultureServiceWorkBusinessRecordRequest,CultureServiceWorkBusinessAIRequest
from .service import GlobalCultureServiceWorkBusinessAPIService
router=APIRouter(prefix="/culture-service-work-business",tags=["GLOBAL BADA BUSINESS - CULTURE SERVICE WORK BUSINESS API"])
service=GlobalCultureServiceWorkBusinessAPIService()
@router.get("/status")
def status():return {"success":True,**service.status()}
@router.get("/catalogue")
def catalogue(domain:str|None=Query(default=None)):
    try:return {"success":True,"count":len(service.catalogue(domain)),"capabilities":service.catalogue(domain)}
    except ValueError as exc:raise HTTPException(status_code=422,detail=str(exc)) from exc
@router.get("/search")
def search(q:str=Query(min_length=1,max_length=300),domain:str|None=Query(default=None)):
    try:return {"success":True,**service.search(q,domain)}
    except ValueError as exc:raise HTTPException(status_code=422,detail=str(exc)) from exc
@router.post("/ai-context")
def ai_context(request:CultureServiceWorkBusinessAIRequest):
    try:return {"success":True,"context":service.ai_context(request.question,request.domain)}
    except ValueError as exc:raise HTTPException(status_code=422,detail=str(exc)) from exc
@router.get("/records")
def records(q:str=Query(default="",max_length=300),capability_id:str|None=Query(default=None,max_length=100),limit:int=Query(default=50,ge=1,le=100)):
    try:
        rows=service.search_records(q,capability_id,limit)
        return {"success":True,"count":len(rows),"records":rows}
    except Exception as exc:raise HTTPException(status_code=503,detail="CULTURE_SERVICE_WORK_BUSINESS_DATABASE_UNAVAILABLE") from exc
@router.get("/records/{record_id}")
def get_record(record_id:str):
    try:record=service.get_record(record_id)
    except Exception as exc:raise HTTPException(status_code=503,detail="CULTURE_SERVICE_WORK_BUSINESS_DATABASE_UNAVAILABLE") from exc
    if record is None:raise HTTPException(status_code=404,detail="RECORD_NOT_FOUND")
    return {"success":True,"record":record}
@router.post("/records")
def save_record(request:CultureServiceWorkBusinessRecordRequest):
    try:service.save_record(request.model_dump())
    except ValueError as exc:raise HTTPException(status_code=422,detail=str(exc)) from exc
    except Exception as exc:raise HTTPException(status_code=503,detail="CULTURE_SERVICE_WORK_BUSINESS_DATABASE_UNAVAILABLE") from exc
    return {"success":True,"record_id":request.record_id,"status":request.status}
