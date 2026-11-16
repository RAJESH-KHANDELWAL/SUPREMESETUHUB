"""Dedicated endpoints for one freelance/gig work type."""
from fastapi import APIRouter, HTTPException
from .categories import SPECIALIZATION_ID, WORK_TYPE_ID
from .services import get_work_type_resource, get_work_type_status

# This router is mounted inside the owning specialization router, so the
# prefix is intentionally relative to avoid duplicating the specialization path.
router = APIRouter(
    prefix=f"/work-types/{WORK_TYPE_ID}",
    tags=[f"Freelance work type — {WORK_TYPE_ID}"],
)


@router.get("")
def read_work_type():
    try:
        return get_work_type_resource()
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/status")
def read_status():
    return get_work_type_status()


@router.get("/integrity")
def read_integrity():
    result = get_work_type_status()
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result)
    return result
