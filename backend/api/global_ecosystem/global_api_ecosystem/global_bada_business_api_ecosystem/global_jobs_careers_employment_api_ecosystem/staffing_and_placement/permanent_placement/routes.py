"""Dedicated endpoints for one Jobs & Careers industry subcategory."""
from fastapi import APIRouter, HTTPException
from .categories import SUBCATEGORY_ID
from .services import get_subcategory_resource, get_subcategory_status

router = APIRouter(prefix=f"/subcategories/{SUBCATEGORY_ID}", tags=[f"Jobs & Careers subcategory — {SUBCATEGORY_ID}"])


@router.get("")
def read_subcategory():
    try:
        return get_subcategory_resource()
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/status")
def read_status():
    return get_subcategory_status()


@router.get("/integrity")
def read_integrity():
    result = get_subcategory_status()
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result)
    return result
