from fastapi import APIRouter, HTTPException

from .schemas import BusinessEcosystemStatus
from .service import BusinessEcosystemService


router = APIRouter(
    prefix="/api/v1/global-ecosystem/business",
    tags=["GLOBAL BUSINESS API ECOSYSTEM"],
)

service = BusinessEcosystemService()


@router.get("/status", response_model=BusinessEcosystemStatus)
def get_status():
    return service.get_status()


@router.get("/modules")
def list_modules():
    return service.list_modules()


@router.get("/modules/{module_id}")
def get_module(module_id: str):
    module = service.get_module(module_id)

    if module is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "BUSINESS_MODULE_NOT_FOUND",
                "module_id": module_id,
            },
        )

    return {
        "success": True,
        "ecosystem_id": "global-business",
        "module": module,
    }
