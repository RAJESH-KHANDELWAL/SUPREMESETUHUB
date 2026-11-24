"""Company data-provider metadata endpoints."""
from fastapi import APIRouter,HTTPException
from .service import get_provider,get_provider_status,list_providers
router=APIRouter(prefix="/global/company-directory/providers",tags=["COMPANY DATA PROVIDERS"])
@router.get("")
def providers():
 items=list_providers(); return {"success":True,"count":len(items),"items":items}
@router.get("/status")
def status(): return {"success":True,**get_provider_status()}
@router.get("/{provider_id}")
def provider(provider_id:str):
 item=get_provider(provider_id)
 if item is None: raise HTTPException(status_code=404,detail="PROVIDER_NOT_FOUND")
 return {"success":True,"item":item}
