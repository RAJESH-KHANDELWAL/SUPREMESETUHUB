"""Catalog of relationship, intimacy, health-information and adult-industry services."""
from copy import deepcopy
from typing import Any

_ENTRIES: tuple[dict[str, Any], ...] = (
    {
        "service_id": "relationship_education",
        "name": "Relationship Education and Communication",
        "category_ids": ["RELATIONSHIPS"],
        "description": "Communication skills, conflict resolution, relationship literacy, and educational resources.",
        "audience": "general; age rating depends on provider content",
        "implementation_status": "CATALOG_ONLY",
        "requires_compliance_review": True,
    },
    {
        "service_id": "intimacy_wellness_education",
        "name": "Intimacy and Sexual Wellness Education",
        "category_ids": ["INTIMACY_WELLNESS", "SEXUAL_HEALTH"],
        "description": "Consent-led adult intimacy education and general wellbeing information; no diagnosis or prescription.",
        "audience": "age-appropriate audiences; adults for explicit or age-restricted content",
        "implementation_status": "CATALOG_ONLY",
        "requires_compliance_review": True,
    },
    {
        "service_id": "dating_matchmaking",
        "name": "Dating and Matchmaking",
        "category_ids": ["DATING_MATCHMAKING", "CONSENT_AND_SAFETY"],
        "description": "Adult dating discovery, profiles, reporting, blocking, safety controls, and moderation.",
        "audience": "adults where the platform is age-restricted",
        "implementation_status": "CATALOG_ONLY",
        "requires_compliance_review": True,
    },
    {
        "service_id": "couples_support",
        "name": "Couples Support and Coaching Directory",
        "category_ids": ["COUPLES_SERVICES", "RELATIONSHIPS"],
        "description": "Directory and scheduling boundaries for qualified relationship-support professionals; verify credentials and local rules.",
        "audience": "general; provider-specific limits apply",
        "implementation_status": "CATALOG_ONLY",
        "requires_compliance_review": True,
    },
    {
        "service_id": "lawful_adult_business",
        "name": "Adult-Industry Business Services",
        "category_ids": ["ADULT_INDUSTRY_BUSINESS"],
        "description": "Business administration, content-rights workflows, creator operations, compliance and reporting for lawful adult businesses.",
        "audience": "verified adult businesses and authorized operators",
        "implementation_status": "CATALOG_ONLY",
        "requires_compliance_review": True,
    },
    {
        "service_id": "adult_content_hosting_publishing",
        "name": "Adult-Content Hosting and Publishing Services",
        "category_ids": ["ADULT_CONTENT_HOSTING", "ADULT_CONTENT_PUBLISHING"],
        "description": "Provider discovery for hosting or publishing services whose current rules expressly allow the intended lawful content.",
        "audience": "adults and authorized businesses; age and consent controls required",
        "implementation_status": "CATALOG_ONLY",
        "requires_compliance_review": True,
    },
)

def list_entries(category_id: str | None = None) -> list[dict[str, Any]]:
    """Return service catalog entries, optionally filtered by category."""
    entries = list(_ENTRIES)
    if category_id:
        key = category_id.strip().upper()
        entries = [entry for entry in entries if key in entry["category_ids"]]
    return deepcopy(entries)
