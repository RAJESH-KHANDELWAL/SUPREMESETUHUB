"""Field-specific API Ecosystem routes for sales_marketing."""
from fastapi import APIRouter, HTTPException, Query
from .categories import FIELD_ID, FIELD_NAME, FIELD_DESCRIPTION
from .services import list_subcategories, get_subcategory
from .validators import validate_field_taxonomy

router = APIRouter(prefix=f"/{FIELD_ID}", tags=[f"Work & Careers — {FIELD_NAME}"])

@router.get("/status")
def field_status():
    return {"success": True, "api_ecosystem_id": f"{FIELD_ID.upper()}_PROFESSIONAL_FIELD_API_ECOSYSTEM", "field_id": FIELD_ID, "field_name": FIELD_NAME, "description": FIELD_DESCRIPTION, **validate_field_taxonomy()}

@router.get("/occupations")
def occupations():
    items = list_subcategories()
    return {"success": True, "count": len(items), "taxonomy_only": True, "occupations": [{"api_ecosystem_id": f"{FIELD_ID.upper()}_{item['id'].upper()}_PROFESSIONAL_SUBCATEGORY_API_ECOSYSTEM", "parent_field_id": FIELD_ID, **item} for item in items]}

@router.get("/occupations/{occupation_id}")
def occupation_detail(occupation_id: str):
    item = get_subcategory(occupation_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "PROFESSIONAL_SUBCATEGORY_NOT_FOUND", "field_id": FIELD_ID, "subcategory_id": occupation_id})
    return {"success": True, "api_ecosystem_id": f"{FIELD_ID.upper()}_{occupation_id.upper()}_PROFESSIONAL_SUBCATEGORY_API_ECOSYSTEM", "parent_field_id": FIELD_ID, "taxonomy_only": True, "occupation": item}

@router.get("/search")
def search_occupations(q: str = Query(min_length=1, max_length=100)):
    needle = q.strip().casefold()
    items = [item for item in list_subcategories() if any(needle in str(item[key]).casefold() for key in ("id", "name", "description"))]
    return {"success": True, "count": len(items), "taxonomy_only": True, "occupations": items}
