"""FastAPI routes for Finance, Banking & Insurance."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import FinanceCategoryDetailResponse, FinanceCategoryListResponse
from .service import FinanceService

router = APIRouter(prefix="/finance-banking-insurance", tags=["GLOBAL BADA BUSINESS - FINANCE & BANKING"])
service = FinanceService()

@router.get("/status")
def get_status():
    return service.get_status()

@router.get("/categories", response_model=FinanceCategoryListResponse)
def list_domain_categories(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_categories(query=q)
    return {"success": True, "count": len(items), "categories": items}

@router.get("/categories/{category_id}", response_model=FinanceCategoryDetailResponse)
def get_domain_category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "category": item}
