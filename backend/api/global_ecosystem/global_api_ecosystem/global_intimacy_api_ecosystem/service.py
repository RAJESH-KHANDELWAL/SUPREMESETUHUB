"""Catalog and discovery service for relationship and intimacy domains.

Records are metadata only. Do not infer endorsement, legal eligibility, or live
API connectivity from catalog presence. Provider policy and API support must be
verified before any adapter is implemented.
"""

from copy import deepcopy
from typing import Any

CATEGORIES: tuple[dict[str, Any], ...] = (
    {
        "category_id": "RELATIONSHIPS",
        "name": "Relationship Education and Support",
        "description": "Relationship skills, communication, conflict resolution, dating safety, and educational resources.",
        "scope": "Adults and general educational services; no claim of clinical treatment.",
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": False,
        "requires_compliance_review": True,
    },
    {
        "category_id": "INTIMACY_WELLNESS",
        "name": "Intimacy and Sexual Wellness",
        "description": "Evidence-informed adult intimacy education, consent, sexual wellbeing, and non-diagnostic wellness resources.",
        "scope": "Educational and wellness information for consenting adults; avoid diagnosis or unsupported medical claims.",
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": True,
        "requires_compliance_review": True,
    },
    {
        "category_id": "DATING_MATCHMAKING",
        "name": "Dating and Matchmaking",
        "description": "Adult dating, matchmaking, profile safety, moderation, and consent-first communication services.",
        "scope": "Adults only where age-restricted; identity, privacy, safety, and moderation requirements must be reviewed.",
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": True,
        "requires_compliance_review": True,
    },
    {
        "category_id": "COUPLES_SERVICES",
        "name": "Couples and Relationship Services",
        "description": "Couples education, coaching directories, appointment discovery, and relationship-support services.",
        "scope": "Provider credentials, jurisdictional limits, privacy, and health-professional boundaries require validation.",
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": False,
        "requires_compliance_review": True,
    },
    {
        "category_id": "SEXUAL_HEALTH",
        "name": "Sexual Health Information",
        "description": "General sexual-health education, consent, contraception awareness, and links to qualified services.",
        "scope": "Informational routing only; not a diagnosis, prescription, or emergency-care service.",
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": False,
        "requires_compliance_review": True,
    },
    {
        "category_id": "ADULT_INDUSTRY_BUSINESS",
        "name": "Adult-Industry Business Platforms",
        "description": "Business software and platform APIs serving lawful adult-industry businesses, such as account tools, creator operations, compliance, and payments.",
        "scope": "Catalog business services only; require provider-policy, payment, jurisdiction, consent, and age-verification reviews.",
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": True,
        "requires_compliance_review": True,
    },
    {
        "category_id": "ADULT_CONTENT_HOSTING",
        "name": "Adult-Content Hosting and Delivery",
        "description": "Hosting, content delivery, storage, moderation, and access-control services where the provider explicitly permits lawful adult content.",
        "scope": "Provider terms must explicitly allow the intended content; require age/consent safeguards, reporting, and legal review.",
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": True,
        "requires_compliance_review": True,
    },
    {
        "category_id": "ADULT_CONTENT_PUBLISHING",
        "name": "Adult Content Publishing Platforms",
        "description": "Platform and publishing APIs for lawful adult content, including rights management, moderation, and creator account operations.",
        "scope": "No non-consensual intimate imagery, exploitation, or content involving minors; verify each provider's rules and API availability.",
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": True,
        "requires_compliance_review": True,
    },
    {
        "category_id": "CONSENT_AND_SAFETY",
        "name": "Consent, Privacy, and Safety",
        "description": "Consent workflows, age assurance, privacy controls, reporting, moderation, and abuse-prevention tooling.",
        "scope": "Use data-minimization and access controls; age-assurance requirements depend on jurisdiction and product design.",
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": False,
        "requires_compliance_review": True,
    },
)

# Initial ecosystem-level provider directory is intentionally conservative.
# These are category leads, not claims that their APIs support each use case.
PROVIDERS: tuple[dict[str, Any], ...] = (
    {
        "provider_id": "planned_relationship_services",
        "name": "Relationship Services Provider Directory",
        "category_ids": ["RELATIONSHIPS", "COUPLES_SERVICES", "INTIMACY_WELLNESS"],
        "official_url": None,
        "official_api_docs_url": None,
        "implementation_status": "CATALOG_ONLY",
        "live_connection_verified": False,
        "notes": "Directory placeholder; replace with individually researched providers and verified official policies.",
    },
    {
        "provider_id": "planned_dating_platforms",
        "name": "Adult Dating Platform Directory",
        "category_ids": ["DATING_MATCHMAKING", "CONSENT_AND_SAFETY"],
        "official_url": None,
        "official_api_docs_url": None,
        "implementation_status": "CATALOG_ONLY",
        "live_connection_verified": False,
        "notes": "Directory placeholder; API access and permitted integrations must be verified provider by provider.",
    },
    {
        "provider_id": "planned_adult_industry_business",
        "name": "Lawful Adult-Industry Business Services Directory",
        "category_ids": ["ADULT_INDUSTRY_BUSINESS", "ADULT_CONTENT_PUBLISHING", "ADULT_CONTENT_HOSTING"],
        "official_url": None,
        "official_api_docs_url": None,
        "implementation_status": "CATALOG_ONLY",
        "live_connection_verified": False,
        "notes": "Directory placeholder; do not infer adult-content permission, API availability, or production integration.",
    },
)

SAFETY_SCOPE = [
    "Adults only for age-restricted services",
    "Consent and rights verification",
    "No sexual content involving minors",
    "No non-consensual intimate imagery or exploitation",
    "Privacy, security, moderation, and reporting controls",
    "Verify local law and each provider's current terms",
    "Catalog records do not imply a live API connection",
]


def list_categories() -> list[dict[str, Any]]:
    """Return a copy of all ecosystem categories."""
    return deepcopy(list(CATEGORIES))


def list_providers(category_id: str | None = None) -> list[dict[str, Any]]:
    """Return provider directory records, optionally filtered by category."""
    providers = list(PROVIDERS)
    if category_id:
        key = category_id.strip().upper()
        providers = [p for p in providers if key in p["category_ids"]]
    return deepcopy(providers)


def get_ecosystem_status() -> dict[str, Any]:
    """Return honest readiness status for the catalog layer."""
    return {
        "success": True,
        "system": "GLOBAL RELATIONSHIP AND INTIMACY API ECOSYSTEM",
        "catalog_only": True,
        "live_connections_verified": False,
        "category_count": len(CATEGORIES),
        "provider_count": len(PROVIDERS),
        "safety_scope": list(SAFETY_SCOPE),
    }
