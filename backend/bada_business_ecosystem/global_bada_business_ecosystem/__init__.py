"""Canonical GLOBAL BADA BUSINESS ECOSYSTEM package."""
from .platform_resources import (
    ECOSYSTEM_ID, ECOSYSTEM_NAME, get_catalog, get_program, list_programs,
)
ECOSYSTEM = {
    "id": ECOSYSTEM_ID,
    "name": ECOSYSTEM_NAME,
    "parent": "BADA BUSINESS ECOSYSTEM",
}

def get_platform_resource_catalog():
    """Backward-compatible explicit catalog accessor."""
    return get_catalog()

__all__ = [
    "ECOSYSTEM", "ECOSYSTEM_ID", "ECOSYSTEM_NAME",
    "get_catalog", "get_platform_resource_catalog", "get_program",
    "list_programs",
]
