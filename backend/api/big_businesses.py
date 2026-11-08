"""Enterprise API namespace sharing the canonical persistent Business domain."""
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException

from backend.businesses.intelligence_service import BigBusinessIntelligenceService

from backend.api import businesses as business_api
from backend.security.dependencies import get_current_user
from backend.schemas.business import BusinessCreateRequest

router = APIRouter(prefix="/big-businesses", tags=["Big Businesses"])

BIG_BUSINESS_TYPES = {"LARGE_BUSINESS", "ENTERPRISE"}
intelligence_service = BigBusinessIntelligenceService()


def _big_business_records(current_user: dict[str, Any]) -> list[dict[str, Any]]:
    result = business_api.get_businesses(current_user=current_user)
    return [
        item for item in result["data"]
        if str(item.get("business_type", "")).strip().upper() in BIG_BUSINESS_TYPES
    ]


@router.get("/overview")
def overview(current_user: dict[str, Any] = Depends(get_current_user)):
    records = _big_business_records(current_user)
    return {
        "name": "BIG BUSINESSES",
        "message": "Enterprise business portfolio retrieved successfully",
        "count": len(records),
        "enterprise_count": sum(
            1 for item in records
            if str(item.get("business_type", "")).strip().upper() == "ENTERPRISE"
        ),
        "capabilities": [
            "company and legal-name profiles",
            "industry and operating-region classification",
            "employee and revenue-band metadata",
            "parent-company references",
            "department and tag organization",
            "compliance status tracking",
            "owner-scoped access using existing business authorization",
        ],
        "data": records,
        "storage_note": (
            "Business records are stored through the central SQLite DatabaseService. "
            "Durability in hosted environments depends on SUPREME_DB_PATH being "
            "configured to a persistent mounted volume."
        ),
    }


@router.get("/")
def list_big_businesses(current_user: dict[str, Any] = Depends(get_current_user)):
    return overview(current_user=current_user)


@router.post("/")
def create_big_business(
    request: BusinessCreateRequest,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    requested_type = str(request.business_type or "").strip().upper()
    if requested_type not in BIG_BUSINESS_TYPES:
        raise HTTPException(
            status_code=422,
            detail="BIG_BUSINESS_TYPE_REQUIRED",
        )
    return business_api.create_business(request=request, current_user=current_user)


@router.get("/{business_id}")
def get_big_business(
    business_id: str,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    result = business_api.get_business(business_id=business_id, current_user=current_user)
    data = result["data"]
    if str(data.get("business_type", "")).strip().upper() not in BIG_BUSINESS_TYPES:
        # Do not disclose whether a non-enterprise business belongs to another user.
        raise HTTPException(status_code=404, detail="BIG_BUSINESS_NOT_FOUND")
    return {"message": "Big Business retrieved successfully", "data": data}


@router.get("/intelligence/health")
def intelligence_health(current_user: dict[str, Any] = Depends(get_current_user)):
    """Return non-sensitive readiness information for the intelligence service."""
    return intelligence_service.health()


@router.post("/compare")
def compare_big_businesses(
    payload: dict[str, Any] = Body(...),
    current_user: dict[str, Any] = Depends(get_current_user),
):
    """Compare documentation readiness for businesses visible to this user."""
    business_ids = payload.get("business_ids")
    if (
        not isinstance(business_ids, list)
        or not business_ids
        or len(business_ids) > 50
        or any(not isinstance(item, str) or not item.strip() for item in business_ids)
    ):
        raise HTTPException(
            status_code=422,
            detail="business_ids must be a non-empty list of up to 50 business IDs",
        )

    # Resolve access through the established owner-scoped Business API first.
    visible_ids = {
        str(item.get("business_id", ""))
        for item in _big_business_records(current_user)
    }
    if any(item not in visible_ids for item in business_ids):
        raise HTTPException(status_code=404, detail="BIG_BUSINESS_NOT_FOUND")

    try:
        results = intelligence_service.compare(business_ids)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except LookupError as exc:
        raise HTTPException(status_code=404, detail="BIG_BUSINESS_NOT_FOUND") from exc

    return {
        "message": "Big Business intelligence comparison completed",
        "count": len(results),
        "data": results,
        "note": "This compares profile documentation readiness, not market position or financial performance.",
    }


@router.get("/{business_id}/intelligence")
def get_big_business_intelligence(
    business_id: str,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    """Return explainable profile completeness, readiness and risk signals."""
    # Existing API performs owner/admin authorization and hides inaccessible IDs.
    get_big_business(business_id=business_id, current_user=current_user)
    try:
        assessment = intelligence_service.assess(business_id)
    except LookupError as exc:
        raise HTTPException(status_code=404, detail="BIG_BUSINESS_NOT_FOUND") from exc
    return {
        "message": "Big Business intelligence assessment completed",
        "data": assessment.to_dict(),
    }


@router.get("/{business_id}/action-plan")
def get_big_business_action_plan(
    business_id: str,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    """Return prioritized follow-up tasks derived from the assessment."""
    get_big_business(business_id=business_id, current_user=current_user)
    try:
        plan = intelligence_service.action_plan(business_id)
    except LookupError as exc:
        raise HTTPException(status_code=404, detail="BIG_BUSINESS_NOT_FOUND") from exc
    return {
        "message": "Big Business action plan generated",
        "data": plan,
    }
