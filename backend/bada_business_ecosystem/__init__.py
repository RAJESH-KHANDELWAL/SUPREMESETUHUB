"""Canonical BADA BUSINESS ECOSYSTEM package.

Product/resource metadata lives directly under this package. HTTP API
implementation remains independently owned by backend.api.
"""
from .platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog,
    get_program,
    list_programs,
)

ECOSYSTEM = {
    "id": "BADA_BUSINESS_ECOSYSTEM",
    "name": "BADA BUSINESS ECOSYSTEM",
    "provider": "Bada Business",
}

__all__ = [
    "ECOSYSTEM",
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "get_catalog",
    "get_program",
    "list_programs",
]
