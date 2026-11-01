"""Backward-compatible package alias for the modular company ecosystem."""
from pathlib import Path

# Preserve legacy imports of global_companies_api_ecosystem.schemas and .service.
__path__ = [str(Path(__file__).with_name("global_company_companies_api_ecosystem"))]

from .global_company_companies_api_ecosystem import router

ECOSYSTEM_NAME = "global_company_companies_api_ecosystem"

def get_ecosystem_info() -> dict[str, str]:
    return {"name": ECOSYSTEM_NAME, "status": "catalog_available"}

__all__ = ["router", "get_ecosystem_info", "ECOSYSTEM_NAME"]
