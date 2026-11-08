"""Canonical Bada Business platform links and program resources.

This stable import path currently delegates to the backwards-compatible
resource implementation while migration is completed.
"""
from backend.bada_business.global_ecosystem.global_bada_business_ecosystem.platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog,
    get_program,
    list_programs,
)
from backend.bada_business.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog import (
    OFFICIAL_PUBLIC_API_VERIFIED,
    LIVE_CONNECTION_VERIFIED,
    PLATFORM_LINKS,
    PLATFORM_PROFILE,
    PROGRAMS,
    STATUS,
)

__all__ = [
    "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "get_catalog", "get_program",
    "list_programs", "OFFICIAL_PUBLIC_API_VERIFIED",
    "LIVE_CONNECTION_VERIFIED", "PLATFORM_LINKS", "PLATFORM_PROFILE",
    "PROGRAMS", "STATUS",
]
