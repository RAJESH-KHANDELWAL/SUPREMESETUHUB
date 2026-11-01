"""Global company profile adapters and aggregate directory service."""
from .routes import router
from .service import (
    get_company_adapter_status,
    get_company_ecosystem_status,
    get_company_profile,
    get_company_sources,
    list_companies,
)

def get_ecosystem_info():
    return get_company_ecosystem_status()


__all__ = [
    "router",
    "list_companies",
    "get_company_profile",
    "get_company_sources",
    "get_company_adapter_status",
    "get_company_ecosystem_status",
    "get_ecosystem_info",
]
