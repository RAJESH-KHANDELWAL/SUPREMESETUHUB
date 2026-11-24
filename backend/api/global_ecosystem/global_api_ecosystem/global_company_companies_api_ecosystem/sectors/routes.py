"""Company sector HTTP endpoints."""
from fastapi import APIRouter,HTTPException,Query
from .service import SectorService
router=APIRouter(prefix="/global/company-directory/sectors",tags=["COMPANY SECTORS"])
service=SectorService()
@router.get("")
def sectors(q:str|None=Query(default=None)):
 items=service.list_sectors(q); return {"success":True,"count":len(items),"items":items}
@router.get("/status")
def status(): return {"success":True,**service.get_status()}
@router.get("/{sector_id}")
def sector(sector_id:str):
 item=service.get_sector(sector_id)
 if item is None: raise HTTPException(status_code=404,detail="SECTOR_NOT_FOUND")
 return {"success":True,"item":item}
