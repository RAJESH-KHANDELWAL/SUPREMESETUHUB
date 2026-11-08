"""Legacy compatibility facade for backend.bada_business_ecosystem.global_bada_business_ecosystem."""
from backend.bada_business_ecosystem.global_bada_business_ecosystem import (
    ECOSYSTEM,
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog as get_platform_resource_catalog,
    get_program,
    list_programs,
)
__all__ = [
    "ECOSYSTEM", "ECOSYSTEM_ID", "ECOSYSTEM_NAME",
    "get_platform_resource_catalog", "get_program", "list_programs",
]
