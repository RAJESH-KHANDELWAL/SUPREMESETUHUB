"""CORE namespace and orchestration for affiliate marketing domains."""

from .service import AffiliateMarketingCoreService, PLATFORM_IDS
from .policies import (
    validate_affiliate_disclosure,
    validate_http_url,
    validate_program_activation,
)

LAYER = "CORE"
ECOSYSTEM_ID = "GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM"

__all__ = [
    "LAYER", "ECOSYSTEM_ID", "PLATFORM_IDS",
    "AffiliateMarketingCoreService",
    "validate_affiliate_disclosure", "validate_http_url",
    "validate_program_activation",
]
