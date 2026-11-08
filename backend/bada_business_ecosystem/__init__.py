"""Canonical BADA BUSINESS ECOSYSTEM root package."""
from .global_bada_business_ecosystem import (
    ECOSYSTEM as GLOBAL_BADA_BUSINESS_ECOSYSTEM,
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog,
    get_program,
    list_programs,
)
from .api_ecosystem import router as api_router

ECOSYSTEM = {
    "id": "BADA_BUSINESS_ECOSYSTEM",
    "name": "BADA BUSINESS ECOSYSTEM",
    "parent": "GLOBAL ECOSYSTEM",
    "child_ecosystems": ["GLOBAL_BADA_BUSINESS_ECOSYSTEM"],
    "api_ecosystem": "GLOBAL_BADA_BUSINESS_API_ECOSYSTEM",
}

__all__ = [
    "ECOSYSTEM", "GLOBAL_BADA_BUSINESS_ECOSYSTEM",
    "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "get_catalog", "get_program",
    "list_programs", "api_router",
]
