"""Compatibility facade for the source-aware Global Companies adapter package."""
from pathlib import Path

from fastapi import APIRouter

# This module shares its name with the canonical package directory.
__path__ = [str(Path(__file__).with_name("global_companies_ecosystem"))]

from .global_companies_ecosystem import (
    get_company_adapter_status,
    get_company_ecosystem_status,
    get_ecosystem_info,
    get_company_profile,
    get_company_sources,
    list_companies,
    router as _modular_router,
)

router = APIRouter(tags=["GLOBAL COMPANIES ECOSYSTEM COMPATIBILITY"])
router.routes.extend(route for route in _modular_router.routes if hasattr(route, "path"))

__all__ = [
    "router",
    "list_companies",
    "get_company_profile",
    "get_company_sources",
    "get_company_adapter_status",
    "get_company_ecosystem_status",
    "get_ecosystem_info",
]
