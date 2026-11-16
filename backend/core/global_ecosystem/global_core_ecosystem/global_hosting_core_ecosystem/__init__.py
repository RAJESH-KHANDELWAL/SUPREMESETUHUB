"""GLOBAL HOSTING CORE ECOSYSTEM public package exports."""
from .catalog import get_hosting_core_catalog, list_hosting_capability_domains
from .contracts import HostingCoreResult, HostingReadiness, HostingTenantContext
from .orchestrator import GlobalHostingCoreOrchestrator
from .policy import HostingCorePolicy, HostingCorePolicyError
from .provider_catalog import (get_hosting_provider, hosting_provider_summary,
                               list_hosting_capability_packages, list_hosting_providers)
from .service import GlobalHostingCoreEcosystemService

LAYER = "CORE"
CATEGORY = "HOSTING"
ECOSYSTEM_NAME = "GLOBAL HOSTING CORE ECOSYSTEM"
ECOSYSTEM_ID = "GLOBAL-HOSTING-CORE-ECOSYSTEM"

__all__ = [
    "LAYER", "CATEGORY", "ECOSYSTEM_NAME", "ECOSYSTEM_ID",
    "HostingCoreResult", "HostingReadiness", "HostingTenantContext",
    "HostingCorePolicy", "HostingCorePolicyError",
    "GlobalHostingCoreOrchestrator", "GlobalHostingCoreEcosystemService",
    "get_hosting_core_catalog", "list_hosting_capability_domains",
    "get_hosting_provider", "hosting_provider_summary",
    "list_hosting_capability_packages", "list_hosting_providers",
]
