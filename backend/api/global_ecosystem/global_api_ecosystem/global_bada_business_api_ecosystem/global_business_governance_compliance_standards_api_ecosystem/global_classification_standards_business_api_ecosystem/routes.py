from fastapi import APIRouter, HTTPException
from .registry import list_classifications, get_classification, list_country_systems, validate_classification_registry

router = APIRouter(tags=["BUSINESS CLASSIFICATION STANDARDS"])

@router.get("/classifications")
def classifications_list():
    items = list_classifications()
    return {"success": True, "count": len(items), "items": items, "note": "Registry metadata only; inspect each status before treating a source dataset as available."}

@router.get("/classifications/countries")
def classification_countries():
    items = list_country_systems()
    return {"success": True, "count": len(items), "items": items}

@router.get("/classifications/integrity")
def classification_integrity():
    result = validate_classification_registry()
    if not result["structurally_valid"]:
        raise HTTPException(status_code=500, detail=result)
    return {"success": True, **result}

@router.get("/classifications/{classification_id}")
def classification_detail(classification_id: str):
    item = get_classification(classification_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "CLASSIFICATION_NOT_FOUND", "classification_id": classification_id})
    return {"success": True, "classification": item}
