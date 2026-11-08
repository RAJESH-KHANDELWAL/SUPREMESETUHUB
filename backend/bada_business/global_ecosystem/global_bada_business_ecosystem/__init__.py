"""Legacy import facade for the canonical top-level Bada Business Ecosystem."""
from backend.bada_business_ecosystem import (
    ECOSYSTEM,
    get_catalog as get_platform_resource_catalog,
    get_program,
    list_programs,
)
from backend.bada_business_ecosystem.platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
)

__all__ = [
    "ECOSYSTEM",
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "get_platform_resource_catalog",
    "get_program",
    "list_programs",
]
