"""Canonical Bada Business product ecosystem package."""
from .platform_resources import get_catalog, get_program, list_programs
from .api_ecosystem import router as api_router

ECOSYSTEM = {
    "id": "BADA_BUSINESS_ECOSYSTEM",
    "name": "BADA BUSINESS ECOSYSTEM",
    "parent": "GLOBAL ECOSYSTEM",
    "platform_root": "backend/bada_business_ecosystem",
    "components": [
        "platform", "links", "programs", "courses", "products",
        "events", "registration", "referrals", "platform_resources",
        "api_ecosystem",
    ],
}

__all__ = ["ECOSYSTEM", "get_catalog", "get_program", "list_programs", "api_router"]
