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

@router.get("/requirements")
def requirements(
    country_code: str = Query(default="IN", min_length=2, max_length=8),
    q: str | None = Query(default=None, min_length=1, max_length=100),
    area: str | None = Query(default=None, min_length=1, max_length=60),
):
    items = service.list_requirements(country_code, q, area)
    if items is None:
        raise HTTPException(status_code=501, detail={"error":"JURISDICTION_DATASET_NOT_AVAILABLE","country_code":country_code.upper(),"message":"This jurisdiction is framework-only. Country-specific requirements have not yet been curated."})
    return {"success": True, "country_code": country_code.upper(), "count": len(items), "requirements": items, "status": "starter_reference_not_legal_advice"}

@router.get("/requirements/{requirement_id}")
def requirement(requirement_id: str, country_code: str = Query(default="IN", min_length=2, max_length=8)):
    item = service.get_requirement(requirement_id, country_code)
    if item is None:
        raise HTTPException(status_code=404, detail={"error":"COMPLIANCE_TOPIC_NOT_FOUND_OR_NOT_CURATED","requirement_id":requirement_id,"country_code":country_code.upper()})
    return {"success": True, "requirement": item, "status": "starter_reference_not_legal_advice"}
