"""Corporate-group taxonomy endpoints."""
from fastapi import APIRouter,HTTPException,Query
from .service import DomainService
router=APIRouter(prefix="/global/company-directory/corporate-groups",tags=["GLOBAL CORPORATE GROUPS"])
service=DomainService()
@router.get("/catalog")
def catalog(q:str|None=Query(default=None)):
 items=service.list_categories(q)
 return {"success":True,"count":len(items),"items":[{"id":x.id,"name":x.name,"domain_id":x.domain_id} for x in items]}
@router.get("/catalog/{category_id}")
def category(category_id:str):
 item=service.get_category(category_id)
 if item is None: raise HTTPException(status_code=404,detail="CORPORATE_GROUP_CATEGORY_NOT_FOUND")
 return {"success":True,"item":{"id":item.id,"name":item.name,"domain_id":item.domain_id}}
@router.get("/status")
def status(): return service.get_status()
