"""Catalog for the Bada Business platform resources supplied by the repository owner.

This is a content/resource catalog, not a claim of official API access.
"""
from __future__ import annotations

from typing import Any

from .programs.lfp_digital import LFP_DIGITAL
from .programs.bb_impact import BB_IMPACT
from .programs.idea_to_ipo import IDEA_TO_IPO


ECOSYSTEM_ID = "BADA_BUSINESS"
ECOSYSTEM_NAME = "BADA BUSINESS API ECOSYSTEM"
PROVIDER = "Bada Business"
STATUS = "RESOURCE_CATALOG_ONLY"
OFFICIAL_PUBLIC_API_VERIFIED = False
LIVE_CONNECTION_VERIFIED = False

PLATFORM_PROFILE: dict[str, Any] = {
    "provider": PROVIDER,
    "ecosystem_id": ECOSYSTEM_ID,
    "ecosystem_name": ECOSYSTEM_NAME,
    "website_content_source": "USER_PROVIDED_PAGE_CAPTURE",
    "source_url": None,
    "contact": {
        "phone_display": "7611967229",
        "phone_country_code": "+91",
        "verification": "user_supplied_page_capture_not_independently_verified",
    },
    "navigation": [
        "Home", "Event", "Products", "7 Star", "Dr Vivek Bindra",
        "Business Blog", "LFP",
    ],
    "status": STATUS,
    "official_public_api_verified": OFFICIAL_PUBLIC_API_VERIFIED,
    "live_connection_verified": LIVE_CONNECTION_VERIFIED,
}

PROGRAMS = {
    "lfp_digital": LFP_DIGITAL,
    "bb_impact": BB_IMPACT,
    "idea_to_ipo": IDEA_TO_IPO,
}

def get_catalog() -> dict[str, Any]:
    return {
        "success": True,
        "ecosystem_id": ECOSYSTEM_ID,
        "ecosystem_name": ECOSYSTEM_NAME,
        "status": STATUS,
        "platform": PLATFORM_PROFILE,
        "programs": PROGRAMS,
        "program_count": len(PROGRAMS),
        "official_public_api_verified": OFFICIAL_PUBLIC_API_VERIFIED,
        "live_connection_verified": LIVE_CONNECTION_VERIFIED,
    }

def get_program(program_id: str) -> dict[str, Any] | None:
    return PROGRAMS.get(program_id.strip().lower())

def list_programs() -> list[dict[str, Any]]:
    return [dict(value) for value in PROGRAMS.values()]
