"""Legacy import facade. The canonical implementation is now in backend.bada_business_ecosystem."""
from backend.bada_business_ecosystem.platform_resources import (
    ECOSYSTEM_ID, ECOSYSTEM_NAME, get_catalog, get_program, list_programs,
    OFFICIAL_PUBLIC_API_VERIFIED, LIVE_CONNECTION_VERIFIED,
    PLATFORM_LINKS, PLATFORM_PROFILE, PROGRAMS, STATUS,
)
__all__ = [
    "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "get_catalog", "get_program",
    "list_programs", "OFFICIAL_PUBLIC_API_VERIFIED",
    "LIVE_CONNECTION_VERIFIED", "PLATFORM_LINKS", "PLATFORM_PROFILE",
    "PROGRAMS", "STATUS",
]
