"""Canonical Bada Business ecosystem package."""
from .platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog as get_platform_resource_catalog,
    get_program,
    list_programs,
)

ECOSYSTEM = {
    "id": "BADA_BUSINESS_ECOSYSTEM",
    "name": "BADA BUSINESS ECOSYSTEM",
    "parent": "GLOBAL ECOSYSTEM",
    "api_ecosystem": "GLOBAL BADA BUSINESS API ECOSYSTEM",
    "platform_resources": "platform_resources",
}

__all__ = [
    "ECOSYSTEM", "ECOSYSTEM_ID", "ECOSYSTEM_NAME",
    "get_platform_resource_catalog", "get_program", "list_programs",
]
