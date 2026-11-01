"""Compatibility facade for the source-aware Company profile adapter ecosystem."""
from .global_companies_ecosystem import (
    get_company_adapter_status,
    get_company_ecosystem_status,
    get_company_profile,
    get_company_sources,
    list_companies,
    router,
)

__all__ = [
    "router",
    "list_companies",
    "get_company_profile",
    "get_company_sources",
    "get_company_adapter_status",
    "get_company_ecosystem_status",
]
