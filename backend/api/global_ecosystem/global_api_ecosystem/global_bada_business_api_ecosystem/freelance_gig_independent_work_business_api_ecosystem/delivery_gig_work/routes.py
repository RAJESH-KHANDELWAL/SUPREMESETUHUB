"""Dedicated specialization and independent work-type API routes."""
from importlib import import_module
from pkgutil import iter_modules

from fastapi import APIRouter, HTTPException, Query

from . import SPECIALIZATION_ID, SPECIALIZATION_NAME
from . import __path__ as _specialization_package_path
from .catalog import get_work_type, search_work_types
from .services import get_specialization_resource, get_status
from .validators import validate_work_types

router = APIRouter(
    prefix=f"/freelance/specializations/{SPECIALIZATION_ID}",
    tags=[f"Freelance — {SPECIALIZATION_NAME}"],
)


@router.get("")
def read_specialization():
    return {"success": True, "specialization": get_specialization_resource()}


@router.get("/status")
def read_status():
    return get_status()


@router.get("/work-types")
def read_work_types(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = search_work_types(q) if q else get_specialization_resource()["work_types"]
    return {
        "success": True,
        "specialization_id": SPECIALIZATION_ID,
        "count": len(items),
        "work_types": items,
    }


@router.get("/work-types/{work_type_id}")
def read_work_type(work_type_id: str):
    item = get_work_type(work_type_id)
    if item is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "WORK_TYPE_NOT_FOUND", "work_type_id": work_type_id},
        )
    return {
        "success": True,
        "work_type": {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "specialization_id": item.specialization_id,
            "taxonomy_status": item.taxonomy_status,
        },
    }


@router.get("/integrity")
def read_integrity():
    return validate_work_types()


# Every work type is an independent child API package. Mount each child router
# below its own /work-types/{work_type_id} route prefix.
for _child_package in iter_modules(_specialization_package_path):
    if not _child_package.ispkg or _child_package.name in {"tests", "__pycache__"}:
        continue
    _child_router = import_module(
        f"{__package__}.{_child_package.name}.routes"
    ).router
    router.include_router(_child_router)
