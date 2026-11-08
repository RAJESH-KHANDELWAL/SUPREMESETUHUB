"""Compatibility exports; canonical resources live in global_bada_business_ecosystem."""
from backend.bada_business_ecosystem.global_bada_business_ecosystem.platform_resources import (
    ECOSYSTEM_ID, ECOSYSTEM_NAME, PROVIDER, STATUS,
    OFFICIAL_PUBLIC_API_VERIFIED, LIVE_CONNECTION_VERIFIED,
    PLATFORM_LINKS, PLATFORM_PROFILE, PROGRAMS,
    get_catalog, get_program, list_programs,
)
__all__ = [
    "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "PROVIDER", "STATUS",
    "OFFICIAL_PUBLIC_API_VERIFIED", "LIVE_CONNECTION_VERIFIED",
    "PLATFORM_LINKS", "PLATFORM_PROFILE", "PROGRAMS",
    "get_catalog", "get_program", "list_programs",
]
