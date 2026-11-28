from fastapi import APIRouter, HTTPException, Query

from .schemas import (
    BeautyCategoryListResponse,
    BeautyCategoryDetailResponse,
    BeautyBusinessDomainListResponse,
    BeautyBusinessDomainDetailResponse,
)
from .service import BeautyFashionLifestyleService

router = APIRouter(
    prefix="/beauty-fashion-lifestyle",
    tags=["GLOBAL BADA BUSINESS - BEAUTY & LIFESTYLE"],
)
service = BeautyFashionLifestyleService()


@router.get("/status")
def status():
    return service.get_status()


@router.get("/categories", response_model=BeautyCategoryListResponse)
def categories(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_categories(q)
    return {"success": True, "count": len(items), "categories": items}


@router.get("/categories/{category_id}", response_model=BeautyCategoryDetailResponse)
def category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "category": item}


@router.get("/domains", response_model=BeautyBusinessDomainListResponse)
def business_domains(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_business_domains(q)
    return {"success": True, "count": len(items), "domains": items}


@router.get("/domains/{domain_id}", response_model=BeautyBusinessDomainDetailResponse)
def business_domain(domain_id: str):
    item = service.get_business_domain(domain_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "BUSINESS_DOMAIN_NOT_FOUND", "domain_id": domain_id})
    return {"success": True, "domain": item}
