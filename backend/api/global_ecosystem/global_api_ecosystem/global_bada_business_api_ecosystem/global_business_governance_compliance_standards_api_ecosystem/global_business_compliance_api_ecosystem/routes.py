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
    items = service.list_compliance_rules("IN", subdivision_code=subdivision_code)
    state_items = [x for x in items if x["subdivision_code"] == subdivision_code.upper()]
    if not state_items:
        raise HTTPException(status_code=501, detail={"error":"STATE_SPECIFIC_RULES_NOT_CURATED","subdivision_code":subdivision_code.upper()})
    return {"success": True, "country_code": "IN", "subdivision_code": subdivision_code.upper(), "count": len(state_items), "requirements": state_items, "status": "discovery_records_not_legal_advice"}

@router.get("/rules")
def compliance_rules(
    country_code: str = Query(default="IN", min_length=2, max_length=8),
    area: str | None = Query(default=None, min_length=1, max_length=60),
    applicability_status: str | None = Query(default=None, min_length=1, max_length=80),
    source_verification_status: str | None = Query(default=None, min_length=1, max_length=100),
    subdivision_code: str | None = Query(default=None, min_length=2, max_length=2),
):
    items = service.list_compliance_rules(country_code, area, applicability_status, source_verification_status, subdivision_code)
    if items is None:
        raise HTTPException(status_code=501, detail={"error":"COMPLIANCE_RULE_DATASET_NOT_CURATED","country_code":country_code.upper(),"message":"A country profile may exist, but its rule records are not yet curated."})
    return {"success": True, "country_code": country_code.upper(), "subdivision_code": subdivision_code.upper() if subdivision_code else None, "count": len(items), "rules": items, "status": "discovery_records_not_legal_advice"}

@router.get("/rules/{rule_id}")
def compliance_rule(rule_id: str, country_code: str = Query(default="IN", min_length=2, max_length=8), subdivision_code: str | None = Query(default=None, min_length=2, max_length=2)):
    item = service.get_compliance_rule(rule_id, country_code, subdivision_code)
    if item is None:
        raise HTTPException(status_code=404, detail={"error":"COMPLIANCE_RULE_NOT_FOUND_OR_NOT_CURATED","rule_id":rule_id,"country_code":country_code.upper()})
    return {"success": True, "rule": item, "status": "discovery_record_not_legal_advice"}

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
