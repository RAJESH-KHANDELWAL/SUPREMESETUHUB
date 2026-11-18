"""FastAPI routes for the universal work/business taxonomy."""
from fastapi import APIRouter, HTTPException, Query
from .service import UniversalWorkBusinessTaxonomyService

router = APIRouter(prefix="/work-business-taxonomy", tags=["GLOBAL BADA BUSINESS - UNIVERSAL WORK BUSINESS TAXONOMY"])
service = UniversalWorkBusinessTaxonomyService()

@router.get("/status")
def get_status():
    return service.get_status()

@router.get("/sectors")
def list_sectors(include_adult: bool = Query(default=False, description="Taxonomy visibility only; not age verification or legal authorization.")):
    return service.list_sectors(include_adult)

@router.get("/sectors/search")
def search_sectors(q: str = Query(min_length=1, max_length=100), include_adult: bool = Query(default=False)):
    results = service.search(q, include_adult)
    return {"success": True, "count": len(results), "results": results}

@router.get("/sectors/{sector_id}")
def get_sector(sector_id: str, include_adult: bool = Query(default=False)):
    item = service.get_sector(sector_id, include_adult)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "WORK_BUSINESS_SECTOR_NOT_FOUND", "sector_id": sector_id})
    return {"success": True, "sector": item}

@router.get("/facets")
def get_facets():
    return {"success": True, "facets": service.get_facets()}

@router.get("/integrity")
def get_integrity():
    result = service.integrity()
    if not result["valid"]:
        raise HTTPException(status_code=500, detail=result)
    return {"success": True, **result}
