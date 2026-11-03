"""Dedicated API routes for ai_automation; taxonomy only, not live job listings."""
from fastapi import APIRouter, HTTPException, Query
from .services import get_specialization_resource, get_status
from .catalog import get_work_type, search_work_types
from .validators import validate_work_types
from . import SPECIALIZATION_ID, SPECIALIZATION_NAME

router = APIRouter(prefix=f"/freelance/specializations/{SPECIALIZATION_ID}", tags=[f"Freelance — {SPECIALIZATION_NAME}"])

@router.get("")
def read_specialization():
    return {"success": True, "specialization": get_specialization_resource()}

@router.get("/status")
def read_status():
    return get_status()

@router.get("/work-types")
def read_work_types(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = search_work_types(q) if q else get_specialization_resource()["work_types"]
    return {"success": True, "specialization_id": SPECIALIZATION_ID, "count": len(items), "work_types": items}

@router.get("/work-types/{work_type_id}")
def read_work_type(work_type_id: str):
    item = get_work_type(work_type_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "WORK_TYPE_NOT_FOUND", "work_type_id": work_type_id})
    return {"success": True, "work_type": {"id": item.id, "name": item.name, "description": item.description, "specialization_id": item.specialization_id, "taxonomy_status": item.taxonomy_status}}

@router.get("/integrity")
def read_integrity():
    return validate_work_types()
