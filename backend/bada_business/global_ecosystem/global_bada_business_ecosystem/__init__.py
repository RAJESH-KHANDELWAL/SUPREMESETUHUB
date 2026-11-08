"""Legacy compatibility facade for the canonical Bada Business global ecosystem."""
from backend.bada_business_ecosystem.global_ecosystem import (
    ECOSYSTEM,
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog,
    get_platform_resource_catalog,
    get_program,
    list_programs,
)

__all__ = [
    "ECOSYSTEM",
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "get_catalog",
    "get_platform_resource_catalog",
    "get_program",
    "list_programs",
]
