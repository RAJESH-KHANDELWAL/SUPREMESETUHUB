"""Read-only endpoints for approved Bada Business ecosystem requirements."""
from fastapi import APIRouter

from .registry import list_approved_requirements, list_scope_constraints, validate_approved_requirements

router = APIRouter(prefix="/governance", tags=["GLOBAL BADA BUSINESS - GOVERNANCE"])

@router.get("/approved-requirements")
def get_approved_requirements():
    requirements = list_approved_requirements()
    return {
        "success": True,
        "ecosystem_id": "global-bada-business",
        "count": len(requirements),
        "requirements": requirements,
        "note": "Approved scope decisions; implementation status is stated per requirement.",
    }

@router.get("/requirements/integrity")
def get_approved_requirements_integrity():
    result = validate_approved_requirements()
    return {"success": result["valid"], **result}


@router.get("/scope-constraints")
def get_scope_constraints():
    constraints = list_scope_constraints()
    return {"success": True, "count": len(constraints), "constraints": constraints}
