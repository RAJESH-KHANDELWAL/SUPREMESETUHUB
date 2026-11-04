"""Integration taxonomy for the global relationship, intimacy, and adult-industry ecosystem.

All records are discovery metadata until an official and permitted integration is
implemented, authorized, and tested. Third-party unofficial account APIs are not
mislabelled as official.
"""
from copy import deepcopy
from typing import Any

_ROWS: tuple[tuple[str, str, list[str], str], ...] = (
    ("relationship_education","Relationship education and coaching directories",["RELATIONSHIPS","COUPLES_SERVICES"],"Directories, education catalogs, scheduling, and learning content."),
    ("dating_platforms","Adult dating and matchmaking",["DATING_MATCHMAKING"],"Approved profile, account, safety, and discovery APIs where provided by the platform."),
    ("couples_therapy","Qualified couples therapy directories",["RELATIONSHIP_THERAPY_DIRECTORY","COUPLES_SERVICES"],"Credential-aware professional directories and scheduling; not a clinical engine."),
    ("sexual_health","Sexual and reproductive health information",["SEXUAL_HEALTH","REPRODUCTIVE_HEALTH"],"Public education and verified service-referral integrations."),
    ("intimacy_wellness","Adult intimacy and sexual wellness education",["INTIMACY_WELLNESS","SEX_EDUCATION"],"Consent-centred adult wellness information and product discovery."),
    ("age_assurance","Age-assurance and age-gating services",["AGE_ASSURANCE","CONSENT_AND_SAFETY"],"Age-gating workflows selected for legality, proportionality, privacy, and data minimization."),
    ("identity_privacy","Identity, privacy, and account protection",["PRIVACY_IDENTITY","CONSENT_AND_SAFETY"],"Authorized identity/account controls, privacy preferences, access, and deletion workflows."),
    ("creator_platforms","Adult creator subscriptions and monetization",["ADULT_CREATOR_ECONOMY","ADULT_INDUSTRY_BUSINESS"],"Creator-account administration and monetization only through documented, permitted interfaces."),
    ("adult_video_publishing","Adult video/pornography publishing platforms",["PORNOGRAPHY_VIDEO_PLATFORMS","ADULT_CONTENT_PUBLISHING"],"Adult-content catalog and publishing interfaces where officially documented and permitted."),
    ("adult_live_streaming","Adult live-streaming and cam platforms",["ADULT_LIVE_STREAMING"],"Authorized broadcaster operations, moderation, and account-management services."),
    ("studio_production","Adult studio and production operations",["ADULT_STUDIOS_PRODUCTION","ADULT_PERFORMER_TALENT"],"Production schedules, release records, rights administration, and talent operations."),
    ("erotic_audio","Erotic audio and adult podcasts",["EROTIC_AUDIO"],"Publishing, subscriptions, audio distribution, and media metadata."),
    ("erotic_literature","Erotic literature and adult publishing",["EROTIC_LITERATURE"],"Adult publishing catalogs, book metadata, subscriptions, and rights records."),
    ("adult_communities","Adult community and membership platforms",["ADULT_COMMUNITIES"],"Adult-gated memberships, moderation, reporting, and community administration."),
    ("adult_photography","Authorized adult photography portfolios",["ADULT_PHOTOGRAPHY"],"Media portfolio metadata and rights records for consensual adult imagery only."),
    ("adult_wellness_ecommerce","Adult wellness and intimate products commerce",["ADULT_ECOMMERCE","SEX_TOYS_WELLNESS_RETAIL"],"Product catalogs, inventory, checkout, shipping, and customer support where permitted."),
    ("adult_payments","Adult-industry payments and payouts",["ADULT_PAYMENTS_PAYOUTS"],"Merchant onboarding and payouts only after payment-provider underwriting and permission."),
    ("adult_affiliates","Adult advertising and affiliate programs",["ADULT_ADVERTISING_AFFILIATES"],"Approved campaigns, attribution, and affiliate reporting under network policies."),
    ("compliance_records","Adult-industry compliance and records",["ADULT_COMPLIANCE_RECORDS","ADULT_STUDIOS_PRODUCTION"],"Consent/release records, age/identity records, retention, and audit support."),
    ("moderation_takedowns","Moderation, reporting, and rights takedowns",["CONTENT_MODERATION","COPYRIGHT_TAKEDOWN"],"Safety reporting, escalation, copyright complaints, and removal/appeal workflows."),
    ("hosting_cdn_storage","Adult-content hosting and delivery",["ADULT_CONTENT_HOSTING","ADULT_CONTENT_PUBLISHING"],"Cloud/hosting/storage/CDN adapters only where current provider terms explicitly permit the use."),
)

_ENTRIES: tuple[dict[str, Any], ...] = tuple(
    {
        "integration_id": integration_id,
        "name": name,
        "category_ids": category_ids,
        "description": description,
        "implementation_status": "CATALOG_ONLY",
        "official_api_required": True,
        "live_connection_verified": False,
        "compliance_review_required": True,
    }
    for integration_id, name, category_ids, description in _ROWS
)

def list_entries(category_id: str | None = None) -> list[dict[str, Any]]:
    """Return integration entries, optionally filtered by category ID."""
    rows = list(_ENTRIES)
    if category_id:
        key = category_id.strip().upper()
        rows = [row for row in rows if key in row["category_ids"]]
    return deepcopy(rows)
