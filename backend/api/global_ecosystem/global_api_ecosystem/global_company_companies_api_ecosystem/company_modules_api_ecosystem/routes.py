"""HTTP endpoints for discovering company-specific code modules."""
from fastapi import APIRouter, HTTPException, Query

from .service import CompanyModulesService

router = APIRouter(
    prefix="/global/company-directory/company-modules",
    tags=["GLOBAL COMPANY MODULE DIRECTORY"],
)
service = CompanyModulesService()


@router.get("/status")
def company_modules_status():
    return service.get_status()


@router.get("")
def list_company_modules():
    return service.list_modules()


@router.get("/search")
def search_company_modules(q: str = Query(min_length=1, max_length=100)):
    return service.search_modules(q)


@router.get("/{company_id}")
def get_company_module(company_id: str):
    item = service.get_module(company_id)
    if item is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "COMPANY_MODULE_NOT_FOUND", "company_id": company_id},
        )
    return {"success": True, "module": item}
