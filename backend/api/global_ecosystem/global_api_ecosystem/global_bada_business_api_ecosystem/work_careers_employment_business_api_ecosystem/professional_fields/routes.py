"""Shared Professional Fields API Ecosystem registry and field routers."""
from dataclasses import asdict
from fastapi import APIRouter, HTTPException, Query
from .services import search_professional_fields, get_professional_fields_status
from .catalog import list_professional_fields, get_professional_field, get_professional_subcategory

router = APIRouter(prefix="/professional-fields", tags=["Work & Careers — Professional Fields"])

@router.get("")
def list_fields(q: str | None = Query(default=None, min_length=1, max_length=100)):
    fields = list_professional_fields()
    if q:
        matches = search_professional_fields(q)
        ids = {item["field"]["id"] for item in matches}
        fields = [item for item in fields if item.id in ids]
    records = [{"api_ecosystem_id": f"{item.id.upper()}_PROFESSIONAL_FIELD_API_ECOSYSTEM", "id": item.id, "name": item.name, "description": item.description, "subcategory_count": len(item.subcategories), "taxonomy_status": "taxonomy_only"} for item in fields]
    return {"success": True, "count": len(records), "professional_fields": records}

@router.get("/integrity")
def integrity():
    result = get_professional_fields_status()
    if not result["structurally_valid"]:
        raise HTTPException(status_code=500, detail=result)
    return result

@router.get("/{field_id}")
def field_detail(field_id: str):
    field = get_professional_field(field_id)
    if field is None:
        raise HTTPException(status_code=404, detail={"error": "PROFESSIONAL_FIELD_NOT_FOUND", "field_id": field_id})
    return {"success": True, "api_ecosystem": {"api_ecosystem_id": f"{field.id.upper()}_PROFESSIONAL_FIELD_API_ECOSYSTEM", "parent_api_ecosystem_id": "WORK_CAREERS_EMPLOYMENT_API_ECOSYSTEM", "taxonomy_status": "taxonomy_only"}, "field": {"id": field.id, "name": field.name, "description": field.description, "subcategories": [asdict(item) for item in field.subcategories]}}

@router.get("/{field_id}/subcategories")
def subcategories(field_id: str, q: str | None = Query(default=None, min_length=1, max_length=100)):
    field = get_professional_field(field_id)
    if field is None:
        raise HTTPException(status_code=404, detail={"error": "PROFESSIONAL_FIELD_NOT_FOUND", "field_id": field_id})
    items = list(field.subcategories)
    if q:
        needle = q.casefold().strip()
        items = [item for item in items if needle in item.id.casefold() or needle in item.name.casefold() or needle in item.description.casefold()]
    return {"success": True, "parent_api_ecosystem_id": f"{field.id.upper()}_PROFESSIONAL_FIELD_API_ECOSYSTEM", "count": len(items), "subcategories": [{"api_ecosystem_id": f"{field.id.upper()}_{item.id.upper()}_PROFESSIONAL_SUBCATEGORY_API_ECOSYSTEM", **asdict(item), "taxonomy_status": "taxonomy_only"} for item in items]}

@router.get("/{field_id}/subcategories/{subcategory_id}")
def subcategory_detail(field_id: str, subcategory_id: str):
    field = get_professional_field(field_id)
    item = get_professional_subcategory(field_id, subcategory_id)
    if field is None or item is None:
        raise HTTPException(status_code=404, detail={"error": "PROFESSIONAL_SUBCATEGORY_NOT_FOUND", "field_id": field_id, "subcategory_id": subcategory_id})
    return {"success": True, "api_ecosystem": {"api_ecosystem_id": f"{field.id.upper()}_{item.id.upper()}_PROFESSIONAL_SUBCATEGORY_API_ECOSYSTEM", "parent_api_ecosystem_id": f"{field.id.upper()}_PROFESSIONAL_FIELD_API_ECOSYSTEM", "taxonomy_status": "taxonomy_only"}, "subcategory": asdict(item)}

# Field-owned API Ecosystems: status, occupation listing, occupation detail and search.
from .it_technology.routes import router as it_technology_router
from .banking_finance.routes import router as banking_finance_router
from .healthcare_medical.routes import router as healthcare_medical_router
from .education_training.routes import router as education_training_router
from .engineering_construction.routes import router as engineering_construction_router
from .sales_marketing.routes import router as sales_marketing_router
from .legal_compliance.routes import router as legal_compliance_router
from .agriculture_food.routes import router as agriculture_food_router
from .manufacturing_operations.routes import router as manufacturing_operations_router
from .real_estate_facilities.routes import router as real_estate_facilities_router
from .hospitality_tourism.routes import router as hospitality_tourism_router
from .transport_logistics.routes import router as transport_logistics_router

router.include_router(it_technology_router)
router.include_router(banking_finance_router)
router.include_router(healthcare_medical_router)
router.include_router(education_training_router)
router.include_router(engineering_construction_router)
router.include_router(sales_marketing_router)
router.include_router(legal_compliance_router)
router.include_router(agriculture_food_router)
router.include_router(manufacturing_operations_router)
router.include_router(real_estate_facilities_router)
router.include_router(hospitality_tourism_router)
router.include_router(transport_logistics_router)
