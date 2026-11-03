from fastapi import APIRouter, HTTPException, Query
from .service import BusinessComplianceService

router = APIRouter(prefix="/compliance", tags=["GLOBAL BADA BUSINESS - BUSINESS COMPLIANCE"])
service = BusinessComplianceService()

@router.get("/status")
def status():
    return service.get_status()

@router.get("/jurisdictions")
def jurisdictions():
    items = service.list_jurisdictions()
    return {"success": True, "count": len(items), "jurisdictions": items}

@router.get("/jurisdictions/{country_code}")
def jurisdiction_detail(country_code: str):
    item = service.get_jurisdiction(country_code)
    if item is None:
        raise HTTPException(status_code=404, detail={"error":"JURISDICTION_NOT_FOUND","country_code":country_code.upper()})
    return {"success": True, "jurisdiction": item}

@router.get("/jurisdictions/{country_code}/subdivisions")
def country_subdivisions(country_code: str):
    item = service.get_jurisdiction(country_code)
    if item is None:
        raise HTTPException(status_code=404, detail={"error":"JURISDICTION_NOT_FOUND","country_code":country_code.upper()})
    if country_code.upper() != "IN":
        raise HTTPException(status_code=501, detail={"error":"SUBNATIONAL_DATASET_NOT_CURATED","country_code":country_code.upper()})
    items = service.list_india_subdivisions()
    return {"success": True, "country_code": "IN", "count": len(items), "subdivisions": items, "status": "jurisdiction_index_only"}

@router.get("/jurisdictions/india/subdivisions")
def india_subdivisions(subdivision_type: str | None = Query(default=None, pattern="^(state|union_territory)$")):
    items = service.list_india_subdivisions(subdivision_type)
    return {"success": True, "country_code": "IN", "count": len(items), "subdivisions": items, "status": "jurisdiction_index_only"}

@router.get("/jurisdictions/india/subdivisions/{subdivision_code}")
def india_subdivision(subdivision_code: str):
    item = service.get_india_subdivision(subdivision_code)
    if item is None:
        raise HTTPException(status_code=404, detail={"error":"INDIA_SUBDIVISION_NOT_FOUND","subdivision_code":subdivision_code.upper()})
    return {"success": True, "subdivision": item}

@router.get("/jurisdictions/india/subdivisions/{subdivision_code}/requirements")
def india_subdivision_requirements(subdivision_code: str):
    item = service.get_india_subdivision(subdivision_code)
    if item is None:
        raise HTTPException(status_code=404, detail={"error":"INDIA_SUBDIVISION_NOT_FOUND","subdivision_code":subdivision_code.upper()})
    raise HTTPException(status_code=501, detail={"error":"STATE_SPECIFIC_RULES_NOT_CURATED","subdivision_code":subdivision_code.upper(),"message":"The subdivision is indexed, but state-specific legal requirements have not yet been verified and curated from official sources."})

@router.get("/requirements")
def requirements(
    country_code: str = Query(default="IN", min_length=2, max_length=8),
    q: str | None = Query(default=None, min_length=1, max_length=100),
    area: str | None = Query(default=None, min_length=1, max_length=60),
    subdivision_code: str | None = Query(default=None, min_length=2, max_length=2),
):
    items = service.list_requirements(country_code, q, area, subdivision_code)
    if items is None:
        raise HTTPException(status_code=501, detail={"error":"JURISDICTION_DATASET_NOT_AVAILABLE","country_code":country_code.upper(),"message":"This jurisdiction is framework-only. Country-specific requirements have not yet been curated."})
    return {"success": True, "country_code": country_code.upper(), "count": len(items), "requirements": items, "status": "starter_reference_not_legal_advice"}

@router.get("/requirements/{requirement_id}")
def requirement(requirement_id: str, country_code: str = Query(default="IN", min_length=2, max_length=8)):
    item = service.get_requirement(requirement_id, country_code)
    if item is None:
        raise HTTPException(status_code=404, detail={"error":"COMPLIANCE_TOPIC_NOT_FOUND_OR_NOT_CURATED","requirement_id":requirement_id,"country_code":country_code.upper()})
    return {"success": True, "requirement": item, "status": "starter_reference_not_legal_advice"}
