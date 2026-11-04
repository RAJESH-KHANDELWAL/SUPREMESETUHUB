"""FastAPI routes for Energy, Utilities & Environment."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import (
    EnergyEnvironmentListResponse, EnergyEnvironmentDetailResponse,
    EnergyBusinessDomainListResponse, EnergyBusinessDomainDetailResponse,
)
from .service import EnergyEnvironmentService

router = APIRouter(prefix="/energy-utilities-environment", tags=["GLOBAL BADA BUSINESS - ENERGY, UTILITIES & ENVIRONMENT"])
service = EnergyEnvironmentService()

@router.get("/status")
def status():
    return service.get_status()

@router.get("/categories", response_model=EnergyEnvironmentListResponse)
def categories(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_categories(q)
    return {"success": True, "count": len(items), "categories": items}

@router.get("/categories/{category_id}", response_model=EnergyEnvironmentDetailResponse)
def category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "category": item}

@router.get("/domains", response_model=EnergyBusinessDomainListResponse)
def business_domains(
    q: str | None = Query(default=None, min_length=1, max_length=100),
    category_id: str | None = Query(default=None, min_length=1, max_length=100),
):
    items = service.list_business_domains(q, category_id)
    return {"success": True, "count": len(items), "business_domains": items}

@router.get("/domains/{domain_id}", response_model=EnergyBusinessDomainDetailResponse)
def business_domain(domain_id: str):
    item = service.get_business_domain(domain_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "BUSINESS_DOMAIN_NOT_FOUND", "domain_id": domain_id})
    return {"success": True, "business_domain": item}
