"""Backward-compatible import facade for the modular company ecosystem."""
from pathlib import Path
from fastapi import APIRouter

# Legacy tests and consumers import schemas/service from this module path.
__path__ = [str(Path(__file__).with_name("global_company_companies_api_ecosystem"))]

from .global_company_companies_api_ecosystem import router as _modular_router

# Preserve the historical flat router view for callers that inspect .routes.
# The canonical package router (mounted by the application) includes all class routers.
router = APIRouter(tags=["GLOBAL COMPANY API COMPATIBILITY"])
router.routes.extend(route for route in _modular_router.routes if hasattr(route, "path"))

ECOSYSTEM_NAME = "global_company_companies_api_ecosystem"

def get_ecosystem_info() -> dict[str, str]:
    return {"name": ECOSYSTEM_NAME, "status": "catalog_available"}

__all__ = ["router", "get_ecosystem_info", "ECOSYSTEM_NAME"]
