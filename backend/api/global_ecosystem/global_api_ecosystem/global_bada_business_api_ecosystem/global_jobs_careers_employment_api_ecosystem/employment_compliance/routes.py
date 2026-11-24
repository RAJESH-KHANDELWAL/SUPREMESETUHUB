"""Dedicated category API routes and mounted subcategory routers."""
from importlib import import_module
from pkgutil import iter_modules
from fastapi import APIRouter, HTTPException
from . import __path__ as _category_package_path
from .categories import CATEGORY_ID
from .services import get_category_resource, get_category_status, list_subcategory_resources

router = APIRouter(prefix=f"/categories/{CATEGORY_ID}/package", tags=[f"Jobs & Careers category — {CATEGORY_ID}"])


@router.get("")
def read_category():
    try:
        return get_category_resource()
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/status")
def read_status():
    return get_category_status()


@router.get("/subcategories")
def list_subcategories():
    items = list_subcategory_resources()
    return {"success": True, "category_id": CATEGORY_ID, "count": len(items), "subcategories": items}


@router.get("/integrity")
def read_integrity():
    result = get_category_status()
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result)
    return result


for _child in iter_modules(_category_package_path):
    if _child.ispkg and _child.name not in {"tests", "__pycache__"}:
        router.include_router(import_module(f"{__package__}.{_child.name}.routes").router)
