"""DATABASE namespace and repository for affiliate marketing domains."""

from .repository import AffiliateMarketingRepository
from .schema import (
    EVENTS_TABLE,
    PROGRAMS_TABLE,
    REFERRALS_TABLE,
    SCHEMA_VERSION,
    schema_statements,
)

LAYER = "DATABASE"
ECOSYSTEM_ID = "GLOBAL-AFFILIATE-MARKETING-BUSINESS-DATABASE-ECOSYSTEM"
PLATFORM_IDS = ("I-DIGITALPRENEUR", "LEADSGURU", "MILLIONAIRE-TRACK")

__all__ = [
    "LAYER", "ECOSYSTEM_ID", "PLATFORM_IDS",
    "AffiliateMarketingRepository", "SCHEMA_VERSION",
    "PROGRAMS_TABLE", "REFERRALS_TABLE", "EVENTS_TABLE",
    "schema_statements",
]
