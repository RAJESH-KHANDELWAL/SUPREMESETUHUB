"""Jurisdiction source metadata endpoints."""
from fastapi import APIRouter,HTTPException,Query
from .service import CountrySourceService
router=APIRouter(prefix="/global/company-directory/countries",tags=["COMPANY COUNTRIES"])
service=CountrySourceService()
@router.get("")
def countries(): return {"success":True,**service.list_countries()}
@router.get("/sources")
def sources(country:str|None=Query(default=None,min_length=2,max_length=2)): return {"success":True,**service.list_sources(country)}
@router.get("/sources/{source_id}")
def source(source_id:str):
 item=service.get_source(source_id)
 if item is None: raise HTTPException(status_code=404,detail="COUNTRY_SOURCE_NOT_FOUND")
 return {"success":True,"registry_status":"source_directory_only","item":item}
