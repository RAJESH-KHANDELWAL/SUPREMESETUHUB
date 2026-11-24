"""Canonical Enterprise directory routes; /business remains a legacy alias."""
from fastapi import APIRouter,HTTPException,Query
from .service import get_catalog,get_profile,list_profiles,search_profiles
router=APIRouter(prefix="/global/company-directory/enterprises",tags=["GLOBAL ENTERPRISE DIRECTORY"])
@router.get("/catalog")
def catalog(): return {"success":True,"record_type":"enterprise","category":get_catalog()}
@router.get("/profiles")
def profiles(q:str|None=Query(default=None),country:str|None=Query(default=None,min_length=2,max_length=2),industry:str|None=Query(default=None),limit:int=Query(default=50,ge=1,le=200),offset:int=Query(default=0,ge=0)):
 return list_profiles(q=q,country=country,industry=industry,limit=limit,offset=offset)
@router.get("/search")
def search(q:str=Query(min_length=1,max_length=100),country:str|None=Query(default=None,min_length=2,max_length=2),industry:str|None=Query(default=None),limit:int=Query(default=50,ge=1,le=200),offset:int=Query(default=0,ge=0)):
 return search_profiles(q=q,country=country,industry=industry,limit=limit,offset=offset)
@router.get("/profiles/{profile_id}")
def profile(profile_id:str):
 item=get_profile(profile_id)
 if item is None: raise HTTPException(status_code=404,detail={"error":"ENTERPRISE_PROFILE_NOT_FOUND","profile_id":profile_id})
 return item
