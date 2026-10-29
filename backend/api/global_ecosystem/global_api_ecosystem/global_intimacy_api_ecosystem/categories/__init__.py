"""Visible category index for the global relationship and intimacy ecosystem.

Category-specific package directories live beside this module. These packages
currently define catalog metadata/contracts only and do not claim live providers.
"""
from __future__ import annotations

from pathlib import Path

CATEGORY_PACKAGE_IDS: tuple[str, ...] = (
    "adult_advertising_affiliates",
    "adult_communities",
    "adult_content_hosting",
    "adult_content_publishing",
    "adult_creator_economy",
    "adult_ecommerce",
    "adult_industry_business",
    "adult_live_streaming",
    "adult_payments_payouts",
    "adult_performer_talent",
    "adult_photography",
    "adult_studios_production",
    "age_assurance",
    "consent_and_boundaries",
    "consent_and_safety",
    "content_moderation",
    "couples_services",
    "copyright_takedown",
    "dating_matchmaking",
    "erotic_audio",
    "erotic_literature",
    "global_provider_directory",
    "intimacy_wellness",
    "marriage_family",
    "pornography_video_platforms",
    "privacy_identity",
    "relationship_therapy_directory",
    "relationships",
    "reproductive_health",
    "sex_education",
    "sex_toys_wellness_retail",
    "sexual_health",
    "adult_compliance_records",
)

def list_category_packages() -> list[dict[str, str]]:
    """Return category ids and expected visible package paths."""
    root = Path(__file__).parent
    return [
        {
            "category_id": package_id.upper(),
            "package": package_id,
            "path": str(root / package_id),
        }
        for package_id in CATEGORY_PACKAGE_IDS
    ]
