"""Global Bada Business API ecosystem package entry point.

Expose the business API router and the master industry registry from their
canonical modules while preserving the existing package import contract.
"""

from .industry_api_ecosystems.registry import (
    INDUSTRY_ECOSYSTEMS,
    get_industry_ecosystem,
    list_industry_ecosystems,
)
from .industry_api_ecosystems.service import IndustryEcosystemService
from .routes import router

__all__ = [
    "router",
    "INDUSTRY_ECOSYSTEMS",
    "get_industry_ecosystem",
    "list_industry_ecosystems",
    "IndustryEcosystemService",
]
