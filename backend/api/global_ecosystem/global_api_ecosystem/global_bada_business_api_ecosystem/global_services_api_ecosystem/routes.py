"""FastAPI routes for GLOBAL SERVICES API ECOSYSTEM."""
from fastapi import APIRouter, HTTPException, Query
from .service import GlobalServicesAPIService

router = APIRouter(prefix="/services", tags=["GLOBAL SERVICES API ECOSYSTEM"])
service = GlobalServicesAPIService()

@router.get("/status")
def ecosystem_status():
    return service.status()

@router.get("/categories")
def list_service_categories():
    return service.categories()

@router.get("/categories/search")
def search_service_categories(q: str = Query(min_length=1, max_length=120)):
    results = service.search(q)
    return {"success": True, "count": len(results), "categories": results}

@router.get("/categories/{category_id}")
def get_service_category(category_id: str):
    item = service.category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "SERVICE_CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "category": item}
