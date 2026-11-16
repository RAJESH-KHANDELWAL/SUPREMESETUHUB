"""Backward-compatible import facade for the canonical Bada Business catalog."""
from backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    OFFICIAL_PUBLIC_API_VERIFIED,
    LIVE_CONNECTION_VERIFIED,
    PLATFORM_PROFILE,
    PLATFORM_LINKS,
    PROGRAMS,
    STATUS,
    PROVIDER,
    get_catalog,
    get_program,
    list_programs,
)

__all__ = [
    "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "OFFICIAL_PUBLIC_API_VERIFIED",
    "LIVE_CONNECTION_VERIFIED", "PLATFORM_PROFILE", "PLATFORM_LINKS",
    "PROGRAMS", "STATUS", "PROVIDER", "get_catalog", "get_program",
    "list_programs",
]
