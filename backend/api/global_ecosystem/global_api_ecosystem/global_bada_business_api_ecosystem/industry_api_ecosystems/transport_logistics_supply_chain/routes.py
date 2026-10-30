from fastapi import APIRouter, HTTPException, Query
from .schemas import TransportListResponse, TransportDetailResponse
from .service import TransportService
router=APIRouter(prefix="/transport-logistics-supply-chain",tags=["GLOBAL BADA BUSINESS - TRANSPORT & LOGISTICS"])
service=TransportService()
@router.get("/status")
def status(): return service.get_status()
@router.get("/categories",response_model=TransportListResponse)
def categories(q: str | None=Query(default=None,min_length=1,max_length=100)):
    items=service.list_categories(q)
    return {"success":True,"count":len(items),"categories":items}
@router.get("/categories/{category_id}",response_model=TransportDetailResponse)
def category(category_id: str):
    item=service.get_category(category_id)
    if item is None: raise HTTPException(status_code=404,detail={"error":"CATEGORY_NOT_FOUND","category_id":category_id})
    return {"success":True,"category":item}
