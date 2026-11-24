"""FastAPI routes for manufacturing, industrial and factory services."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import (
    ManufacturingCategoryListResponse, ManufacturingCategoryDetailResponse,
    ManufacturingBusinessDomainListResponse, ManufacturingBusinessDomainDetailResponse,
)
from .service import ManufacturingService

router = APIRouter(
    prefix="/manufacturing-industrial-services",
    tags=["GLOBAL BADA BUSINESS - MANUFACTURING & FACTORY SERVICES"],
)
service = ManufacturingService()

@router.get("/status")
def status():
    return service.get_status()

@router.get("/integrity")
def integrity():
    report = service.get_integrity()
    if not report["structurally_valid"]:
        raise HTTPException(status_code=500, detail=report)
    return {"success": True, **report}

@router.get("/categories", response_model=ManufacturingCategoryListResponse)
def categories(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_categories(q)
    return {"success": True, "count": len(items), "categories": items}

@router.get("/categories/{category_id}", response_model=ManufacturingCategoryDetailResponse)
def category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "category": item}

@router.get("/domains", response_model=ManufacturingBusinessDomainListResponse)
def business_domains(
    q: str | None = Query(default=None, min_length=1, max_length=100),
    category_id: str | None = Query(default=None, min_length=1, max_length=100),
):
    items = service.list_business_domains(q, category_id)
    return {"success": True, "count": len(items), "business_domains": items}

@router.get("/domains/{domain_id}", response_model=ManufacturingBusinessDomainDetailResponse)
def business_domain(domain_id: str):
    item = service.get_business_domain(domain_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "BUSINESS_DOMAIN_NOT_FOUND", "domain_id": domain_id})
    return {"business_domain": item}
