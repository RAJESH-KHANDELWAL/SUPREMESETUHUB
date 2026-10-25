"""Enterprise API namespace sharing the canonical business domain."""
from typing import Any
from fastapi import APIRouter, Depends
from backend.api import businesses as business_api
from backend.security.dependencies import get_current_user
from backend.schemas.business import BusinessCreateRequest

router = APIRouter(prefix="/big-businesses", tags=["Big Businesses"])

@router.get("/overview")
def overview(current_user: dict[str, Any] = Depends(get_current_user)):
    result = business_api.get_businesses(current_user=current_user)
    records = result["data"]
    return {
        "name": "BIG BUSINESSES",
        "message": "Enterprise business portfolio retrieved successfully",
        "count": len(records),
        "enterprise_count": sum(1 for item in records if str(item.get("business_type", "")).upper() in {"LARGE_BUSINESS", "ENTERPRISE"}),
        "capabilities": [
            "company and legal-name profiles", "industry and operating-region classification",
            "employee and revenue-band metadata", "parent-company references",
            "department and tag organization", "compliance status tracking",
            "owner-scoped access using existing business authorization",
        ],
        "data": records,
        "storage_note": "BusinessService currently uses in-memory records; durable multi-instance enterprise persistence is not enabled.",
    }

@router.get("/")
def list_big_businesses(current_user: dict[str, Any] = Depends(get_current_user)):
    return overview(current_user=current_user)

@router.post("/")
def create_big_business(request: BusinessCreateRequest, current_user: dict[str, Any] = Depends(get_current_user)):
    return business_api.create_business(request=request, current_user=current_user)

@router.get("/{business_id}")
def get_big_business(business_id: str, current_user: dict[str, Any] = Depends(get_current_user)):
    result = business_api.get_business(business_id=business_id, current_user=current_user)
    return {"message": "Big Business retrieved successfully", "data": result["data"]}
