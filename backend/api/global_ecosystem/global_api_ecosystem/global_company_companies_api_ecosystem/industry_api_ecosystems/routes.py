"""Company industry taxonomy endpoints."""
from fastapi import APIRouter,HTTPException,Query
from .service import IndustryService
router=APIRouter(prefix="/global/company-directory/industries",tags=["COMPANY INDUSTRIES"])
service=IndustryService()
@router.get("")
def industries(q:str|None=Query(default=None)):
 items=service.list_industries(q); return {"success":True,"count":len(items),"items":items,"registry_status":"curated_taxonomy"}
@router.get("/status")
def status(): return {"success":True,**service.get_status()}
@router.get("/{industry_id}")
def industry(industry_id:str):
 item=service.get_industry(industry_id)
 if item is None: raise HTTPException(status_code=404,detail="INDUSTRY_NOT_FOUND")
 return {"success":True,"item":item}
