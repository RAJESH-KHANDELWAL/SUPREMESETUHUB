"""GLOBAL ECOSYSTEM package within BADA BUSINESS ECOSYSTEM."""
from .platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog,
    get_program,
    list_programs,
)

ECOSYSTEM = {
    "id": "GLOBAL_ECOSYSTEM",
    "name": "GLOBAL ECOSYSTEM",
    "parent": "BADA_BUSINESS_ECOSYSTEM",
}

def get_platform_resource_catalog():
    """Return the canonical global platform resource catalog."""
    return get_catalog()

__all__ = [
    "ECOSYSTEM",
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "get_catalog",
    "get_platform_resource_catalog",
    "get_program",
    "list_programs",
]
