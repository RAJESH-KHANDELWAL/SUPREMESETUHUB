from fastapi import APIRouter,HTTPException,Query
from .schemas import PersonalWellnessListResponse,PersonalWellnessDetailResponse
from .service import PersonalWellnessService
router=APIRouter(prefix="/personal-lifestyle-wellness",tags=["GLOBAL BADA BUSINESS - PERSONAL, FAMILY, RELATIONSHIPS & WELLNESS"])
service=PersonalWellnessService()
@router.get("/status")
def status(): return service.get_status()
@router.get("/categories",response_model=PersonalWellnessListResponse)
def categories(q:str|None=Query(default=None,min_length=1,max_length=100),include_adult:bool=Query(default=False,description="Include separately classified 18+ categories; this flag is not age verification.")):
 items=service.list_categories(q,include_adult=include_adult)
 return {"success":True,"count":len(items),"categories":items}
@router.get("/categories/{category_id}",response_model=PersonalWellnessDetailResponse)
def category(category_id:str,include_adult:bool=Query(default=False,description="Include separately classified 18+ categories; this flag is not age verification.")):
 item=service.get_category(category_id,include_adult=include_adult)
 if item is None: raise HTTPException(status_code=404,detail={"error":"CATEGORY_NOT_FOUND_OR_RESTRICTED","category_id":category_id})
 return {"success":True,"category":item}
