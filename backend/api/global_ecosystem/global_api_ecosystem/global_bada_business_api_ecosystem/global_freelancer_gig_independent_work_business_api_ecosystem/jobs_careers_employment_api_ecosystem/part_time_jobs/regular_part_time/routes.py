"""Dedicated API Ecosystem endpoints for the regular_part_time track."""
from fastapi import APIRouter, HTTPException
from .categories import CATEGORY_ID, TRACK_ID
from .services import get_track_api_resource, get_track_status

router = APIRouter(
    prefix=f"/tracks/{TRACK_ID}/api-ecosystem",
    tags=[f"Work & Careers — {CATEGORY_ID} — {TRACK_ID}"],
)

@router.get("")
def read_track_api_ecosystem():
    try:
        return {"success": True, "resource": get_track_api_resource()}
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

@router.get("/status")
def read_track_status():
    try:
        return get_track_status()
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

@router.get("/role-families")
def read_role_families():
    try:
        resource = get_track_api_resource()
        return {"success": True, "count": len(resource["role_families"]), "role_families": resource["role_families"]}
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
