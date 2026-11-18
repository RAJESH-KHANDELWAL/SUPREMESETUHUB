"""Backward-compatible imports for the GLOBAL CORE ECOSYSTEM catalog."""
from backend.core.global_ecosystem.global_core_ecosystem.manager import (
    CATEGORIES, COMPANY_REGISTRATIONS, PERSONAL_REGISTRATIONS, ROOT, ROOT_ID,
    get_catalog, get_category_catalog, get_registration_catalog,
)

__all__ = [
    "CATEGORIES", "COMPANY_REGISTRATIONS", "PERSONAL_REGISTRATIONS", "ROOT",
    "ROOT_ID", "get_catalog", "get_category_catalog", "get_registration_catalog",
]
