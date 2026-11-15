"""Read-only discovery routes for GLOBAL APP API."""
from fastapi import APIRouter,HTTPException,Query
from .schemas import EcosystemStatus
from .service import EcosystemService
router=APIRouter(prefix="/app",tags=["GLOBAL APP API ECOSYSTEM"])
service=EcosystemService()
@router.get("/status",response_model=EcosystemStatus)
def get_status(): return service.get_status()
@router.get("/providers")
def list_providers(origin:str|None=None,category:str|None=None): return service.list_providers(origin=origin,category=category)
@router.get("/providers/{provider_id}")
def get_provider(provider_id:str):
 provider=service.get_provider(provider_id)
 if provider is None: raise HTTPException(status_code=404,detail={"error":"PROVIDER_NOT_FOUND","provider_id":provider_id})
 return {"success":True,"provider":provider}
@router.get("/search")
def search_providers(q:str=Query(min_length=1,max_length=100)):
 rows=service.search_providers(q);return {"success":True,"count":len(rows),"providers":rows}
@router.get("/types")
def list_app_types(): return service.list_app_types()
@router.get("/capabilities")
def list_capabilities(): return service.list_capabilities()
@router.get("/domains")
def list_domains(): return service.list_domains()
