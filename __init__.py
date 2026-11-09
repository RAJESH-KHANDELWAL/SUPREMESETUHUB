"""Canonical GLOBAL BADA BUSINESS ECOSYSTEM package.

This package owns Bada Business ecosystem resource metadata and catalogues.
API, CORE, ENGINE, DATABASE and runtime integrations remain independently
owned by their respective architecture layers.
"""

from .platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog,
    get_program,
    list_programs,
)

ECOSYSTEM = {
    "id": "GLOBAL_BADA_BUSINESS_ECOSYSTEM",
    "name": "GLOBAL BADA BUSINESS ECOSYSTEM",
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
