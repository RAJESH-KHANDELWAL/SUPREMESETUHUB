"""Category packages owned by GLOBAL RELATIONSHIP AND INTIMACY ECOSYSTEM.

These taxonomy packages are intentionally scoped to this ecosystem and are not
part of the shared Global API category namespace.
"""

from __future__ import annotations

CATEGORY_PACKAGE_IDS: tuple[str, ...] = (
    "adult_advertising_affiliates",
    "adult_communities",
    "adult_compliance_records",
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
    "copyright_takedown",
    "couples_services",
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
)


def list_category_packages() -> list[dict[str, str]]:
    """Return category IDs and canonical package paths."""
    return [
        {
            "category_id": package_id.upper(),
            "package": package_id,
            "path": "categories/" + package_id,
        }
        for package_id in CATEGORY_PACKAGE_IDS
    ]
