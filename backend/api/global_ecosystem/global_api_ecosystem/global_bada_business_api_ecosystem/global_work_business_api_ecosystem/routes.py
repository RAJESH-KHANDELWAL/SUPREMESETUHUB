"""REST routes for aggregate Work & Business discovery."""
from fastapi import APIRouter, HTTPException, Query
from .service import GlobalWorkBusinessAPIService

router = APIRouter(prefix="/work-business-directory",
                   tags=["GLOBAL BADA BUSINESS - WORK & BUSINESS API"])
service = GlobalWorkBusinessAPIService()

@router.get("/status")
def status():
    return service.status()

@router.get("/sectors")
def sectors(include_adult: bool = Query(default=False)):
    return service.list_sectors(include_adult)

@router.get("/sectors/search")
def search_sectors(q: str = Query(min_length=1, max_length=120),
                   include_adult: bool = Query(default=False)):
    results = service.search_sectors(q, include_adult)
    return {"success": True, "count": len(results), "sectors": results}

@router.get("/sectors/{sector_id}")
def get_sector(sector_id: str, include_adult: bool = Query(default=False)):
    item = service.get_sector(sector_id, include_adult)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "WORK_BUSINESS_SECTOR_NOT_FOUND", "sector_id": sector_id})
    return {"success": True, "sector": item}

@router.get("/facets")
def facets():
    return {"success": True, "facets": service.facets()}

@router.get("/freelance-specializations")
def freelance_specializations():
    return {"success": True, **service.freelance_specializations()}

@router.get("/jobs-careers/status")
def jobs_careers_status():
    return service.jobs_careers_status()
