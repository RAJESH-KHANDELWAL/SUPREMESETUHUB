"""Legacy namespace retained only to avoid breaking old imports.

New code must import from backend.bada_business_ecosystem.
"""
from backend.bada_business_ecosystem import (
    ECOSYSTEM,
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog,
    get_program,
    list_programs,
)

__all__ = [
    "ECOSYSTEM", "ECOSYSTEM_ID", "ECOSYSTEM_NAME",
    "get_catalog", "get_program", "list_programs",
]