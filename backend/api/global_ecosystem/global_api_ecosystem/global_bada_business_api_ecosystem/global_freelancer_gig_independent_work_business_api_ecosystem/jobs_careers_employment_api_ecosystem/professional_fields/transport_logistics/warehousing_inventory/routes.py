"""FastAPI router for this professional subcategory API Ecosystem."""
from dataclasses import asdict
from fastapi import APIRouter
from . import SUBCATEGORY_ID
from .services import get_status, get_subcategory
router = APIRouter(prefix=f"/subcategories/{SUBCATEGORY_ID}", tags=["Professional Subcategory API Ecosystem"])
@router.get("/status")
def status():
    return get_status()
@router.get("")
def detail():
    return {"success": True, "subcategory": asdict(get_subcategory()), "taxonomy_only": True}
