"""Read-only API routes for the Bada Business provider integration registry."""
from fastapi import APIRouter, HTTPException

from .schemas import IntegrationDetailResponse, IntegrationListResponse, IntegrationStatusResponse
from .service import get_entry, get_status, list_entries

router = APIRouter(prefix="/integrations", tags=["GLOBAL BADA BUSINESS - API INTEGRATIONS"])

@router.get("/status", response_model=IntegrationStatusResponse)
def integration_status():
    return get_status()

@router.get("", response_model=IntegrationListResponse)
def integrations_list():
    items = list_entries()
    return {"success": True, "count": len(items), "registry_status": "catalog_reference_only", "items": items}

@router.get("/{integration_id}", response_model=IntegrationDetailResponse)
def integration_detail(integration_id: str):
    item = get_entry(integration_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "BUSINESS_INTEGRATION_NOT_FOUND", "integration_id": integration_id})
    return {"success": True, "integration": item}
