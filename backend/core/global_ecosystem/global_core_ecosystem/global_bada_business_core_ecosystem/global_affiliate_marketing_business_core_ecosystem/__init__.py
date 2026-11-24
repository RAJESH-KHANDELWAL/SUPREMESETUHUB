"""Global affiliate marketing business CORE package."""

from .catalog import (
    AFFILIATE_NETWORK_CATALOG,
    PLATFORM_CATALOG,
    get_platform,
    list_platforms,
)
from .manager import GlobalAffiliateMarketingCoreManager, get_manager
from .module_service import AffiliatePlatformModuleService
from .orchestrator import AffiliateMarketingCoreOrchestrator
from .policies import (
    validate_affiliate_disclosure,
    validate_http_url,
    validate_program_activation,
)
from .service import AffiliateMarketingCoreService, PLATFORM_IDS

LAYER = "CORE"
ECOSYSTEM_ID = "GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM"

__all__ = [
    "LAYER", "ECOSYSTEM_ID", "PLATFORM_IDS",
    "AFFILIATE_NETWORK_CATALOG", "PLATFORM_CATALOG",
    "get_platform", "list_platforms",
    "GlobalAffiliateMarketingCoreManager", "get_manager",
    "AffiliatePlatformModuleService", "AffiliateMarketingCoreOrchestrator",
    "AffiliateMarketingCoreService", "validate_affiliate_disclosure",
    "validate_http_url", "validate_program_activation",
]
