from fastapi import APIRouter, HTTPException, Query
from .schemas import HomeServicesDetailResponse, HomeServicesListResponse
from .service import HomeServicesFacilityService

router=APIRouter(prefix="/home-services-facility-management",tags=["GLOBAL BADA BUSINESS - HOME SERVICES & FACILITY MANAGEMENT"])
service=HomeServicesFacilityService()

@router.get("/status")
def status(): return service.get_status()

@router.get("/categories",response_model=HomeServicesListResponse)
def categories(q: str | None = Query(default=None,min_length=1,max_length=100),channel: str | None = Query(default=None,pattern="^(online|offline|hybrid)$")):
 items=service.list_categories(query=q,channel=channel)
 return {"success":True,"count":len(items),"categories":items}

@router.get("/categories/{category_id}",response_model=HomeServicesDetailResponse)
def category(category_id: str):
 item=service.get_category(category_id)
 if item is None: raise HTTPException(status_code=404,detail={"error":"CATEGORY_NOT_FOUND","category_id":category_id})
 return {"success":True,"category":item}

@router.get("/cross-ecosystem-links")
def cross_ecosystem_links(): return {"success":True,"links":service.get_cross_ecosystem_links()}
