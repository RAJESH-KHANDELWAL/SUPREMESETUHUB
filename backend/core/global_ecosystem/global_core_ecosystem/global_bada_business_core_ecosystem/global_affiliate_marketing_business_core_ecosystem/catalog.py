"""Canonical affiliate platform identity inventory; no live-status inference."""
from __future__ import annotations

from typing import Any

# Candidate identities carried forward from the former Global/India folder taxonomy.
# These are discovery records only, not assertions of program availability or terms.
_GLOBAL_NETWORKS = (
    "adobe_affiliate", "agoda_affiliate", "aliexpress_portals",
    "amazon_associates_global", "awin", "booking_com_affiliate",
    "canva_affiliate", "cj_affiliate", "clickbank", "coursera_affiliate",
    "digistore24", "ebay_partner_network", "envato_affiliate",
    "etsy_affiliate", "fiverr_affiliate", "flexoffers", "hubspot_affiliate",
    "impact_com", "partnerize", "partnerstack", "rakuten_advertising",
    "semrush_affiliate", "shareasale", "shopify_affiliate", "skimlinks",
    "sovrn_commerce", "travelpayouts", "udemy_affiliate",
)
_INDIA_NETWORKS = (
    "admitad_india", "amazon_associates_india", "bigrock_affiliate",
    "cashkaro", "cuelinks", "earnkaro", "flipkart_affiliate", "gopaisa",
    "hostinger_affiliate_india", "optimise_media_india", "vcommission",
    "youtag_wellness_referral",
)

def _display_name(slug: str) -> str:
    return slug.replace("_", " ").replace("com", "com").title()

AFFILIATE_NETWORK_CATALOG: tuple[dict[str, Any], ...] = tuple(
    {
        "platform_id": slug.upper().replace("_", "-"),
        "slug": slug,
        "name": _display_name(slug),
        "region_scope": region,
        "record_type": "NETWORK_CANDIDATE",
        "catalog_status": "DISCOVERY_ONLY",
        "verification_status": "UNVERIFIED",
        "program_status": "NOT_ASSESSED",
        "terms_url": None,
        "commission_terms": None,
        "live_connection_verified": False,
    }
    for region, slugs in (("GLOBAL", _GLOBAL_NETWORKS), ("INDIA", _INDIA_NETWORKS))
    for slug in slugs
)

# These program identities were explicitly separated in the original CORE catalog.
# Their terms remain unverified until evidence is recorded for each platform.
PLATFORM_CATALOG: tuple[dict[str, Any], ...] = (
    {
        "platform_id": "I-DIGITALPRENEUR",
        "slug": "i_digitalpreneur",
        "name": "iDigitalPreneur",
        "region_scope": "UNSPECIFIED",
        "record_type": "PROGRAM_PLATFORM",
        "catalog_status": "REGISTERED_IDENTITY",
        "verification_status": "UNVERIFIED",
        "program_status": "PENDING_VERIFICATION",
        "terms_url": None,
        "commission_terms": None,
        "live_connection_verified": False,
    },
    {
        "platform_id": "LEADSGURU",
        "slug": "leadsguru",
        "name": "LeadsGuru",
        "region_scope": "UNSPECIFIED",
        "record_type": "PROGRAM_PLATFORM",
        "catalog_status": "REGISTERED_IDENTITY",
        "verification_status": "UNVERIFIED",
        "program_status": "PENDING_VERIFICATION",
        "terms_url": None,
        "commission_terms": None,
        "live_connection_verified": False,
    },
    {
        "platform_id": "MILLIONAIRE-TRACK",
        "slug": "millionaire_track",
        "name": "Millionaire Track",
        "region_scope": "UNSPECIFIED",
        "record_type": "PROGRAM_PLATFORM",
        "catalog_status": "REGISTERED_IDENTITY",
        "verification_status": "UNVERIFIED",
        "program_status": "PENDING_VERIFICATION",
        "terms_url": None,
        "commission_terms": None,
        "live_connection_verified": False,
    },
)

_ALL_BY_ID = {
    item["platform_id"]: item
    for item in (*PLATFORM_CATALOG, *AFFILIATE_NETWORK_CATALOG)
}
if len(_ALL_BY_ID) != len(PLATFORM_CATALOG) + len(AFFILIATE_NETWORK_CATALOG):
    raise RuntimeError("DUPLICATE_AFFILIATE_PLATFORM_ID")

def list_platforms(*, region: str | None = None, include_candidates: bool = True) -> list[dict[str, Any]]:
    """Return copied platform metadata; candidates are discovery-only by default."""
    records = list(PLATFORM_CATALOG)
    if include_candidates:
        records.extend(AFFILIATE_NETWORK_CATALOG)
    normalized_region = region.strip().upper() if region else None
    if normalized_region:
        records = [item for item in records if item["region_scope"] == normalized_region]
    return [dict(item) for item in records]

def get_platform(platform_id: str) -> dict[str, Any] | None:
    """Resolve an exact canonical platform ID without implying program approval."""
    if not isinstance(platform_id, str) or not platform_id.strip():
        return None
    record = _ALL_BY_ID.get(platform_id.strip().upper())
    return dict(record) if record else None

__all__ = [
    "AFFILIATE_NETWORK_CATALOG", "PLATFORM_CATALOG",
    "get_platform", "list_platforms",
]
