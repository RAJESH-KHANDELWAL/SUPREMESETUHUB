"""Global business umbrella ecosystem.

Aggregates business-domain namespaces and connects canonical provider/business
vertical packages without copying their provider records or runtime logic.
"""
from .catalog import get_catalog, list_business_ecosystems
from .registry import get_business_ecosystem, search_business_ecosystems
from .service import GlobalBusinessEcosystemService
from .adapters.bada_business import get_bada_business_connection

ECOSYSTEM_ID = "GLOBAL_BUSINESS_ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL BUSINESS ECOSYSTEM"
LAYER = "GLOBAL_ECOSYSTEM"

__all__ = [
    "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "LAYER", "get_catalog",
    "list_business_ecosystems", "get_business_ecosystem",
    "search_business_ecosystems", "GlobalBusinessEcosystemService",
    "get_bada_business_connection",
]
