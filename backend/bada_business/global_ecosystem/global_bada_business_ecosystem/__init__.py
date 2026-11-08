"""Legacy compatibility facade for Bada Business resources."""
from backend.bada_business_ecosystem import (
    ECOSYSTEM, ECOSYSTEM_ID, ECOSYSTEM_NAME,
    get_catalog, get_program, list_programs,
)
__all__ = ["ECOSYSTEM", "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "get_catalog", "get_program", "list_programs"]
