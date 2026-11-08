"""Canonical Bada Business product ecosystem package.

All platform-specific information is owned under backend.bada_business_ecosystem.
"""
from .platform_resources import get_catalog, get_program, list_programs
from .api_ecosystem import router as api_router

ECOSYSTEM = {
    "id": "BADA_BUSINESS_ECOSYSTEM",
    "name": "BADA BUSINESS ECOSYSTEM",
    "parent": "GLOBAL ECOSYSTEM",
    "components": [
        "platform", "links", "programs", "courses", "products",
        "events", "registration", "referrals", "platform_resources",
        "api_ecosystem",
    ],
}

__all__ = ["ECOSYSTEM", "get_catalog", "get_program", "list_programs", "api_router"]
