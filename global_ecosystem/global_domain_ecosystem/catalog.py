"""Master Bharat-to-global domain taxonomy."""
from __future__ import annotations

GEOGRAPHIC_SCOPES = (
    "bharat_india", "indian_states_and_union_territories", "south_asia",
    "central_asia", "east_asia", "southeast_asia", "middle_east",
    "africa", "europe", "north_america", "latin_america_caribbean",
    "oceania", "global_cross_border",
)
MATURITY_LEVELS = (
    "basic_normal", "standard", "professional", "advanced", "expert",
    "enterprise_industrial", "research_frontier", "supreme_long_horizon",
)
DOMAIN_GROUPS = {
    "society_and_public": (
        "government", "public_services", "civic_technology", "law_and_justice",
        "public_safety", "international_relations", "community_development",
    ),
    "business_and_economy": (
        "business", "entrepreneurship", "commerce", "retail", "finance",
        "banking", "insurance", "accounting", "taxation", "fintech",
        "trade", "investment_information", "network_marketing", "direct_selling",
    ),
    "technology_and_digital": (
        "software", "websites", "mobile_apps", "developer_platforms", "ai",
        "machine_learning", "data", "cloud", "devops", "cybersecurity",
        "telecommunications", "internet", "blockchain", "robotics",
        "quantum_computing", "semiconductors", "digital_identity",
    ),
    "knowledge_and_people": (
        "education", "research", "science", "careers", "human_resources",
        "skills", "culture", "languages", "accessibility",
    ),
    "health_and_life": (
        "healthcare", "public_health", "medical_technology", "wellness",
        "mental_wellbeing", "relationships", "family", "sexual_health",
        "reproductive_health",
    ),
    "adult_only_media_and_services": (
        "adult_content_platforms", "adult_entertainment", "adult_creator_economy",
        "adult_subscriptions", "adult_content_distribution", "adult_content_moderation",
        "age_assurance", "consent_and_release_management", "adult_privacy",
        "adult_payments_and_payouts", "copyright_and_takedowns",
    ),
    "media_and_entertainment": (
        "media", "publishing", "film", "television", "music", "gaming",
        "esports", "creator_economy", "events", "sports",
    ),
    "industry_and_infrastructure": (
        "agriculture", "food", "manufacturing", "construction", "real_estate",
        "energy", "water", "transport", "logistics", "supply_chain",
        "aerospace", "space", "defence_resilience", "environment", "climate",
    ),
    "places_and_services": (
        "tourism", "travel", "hospitality", "property_services",
        "professional_services", "local_services", "nonprofits",
        "humanitarian_services",
    ),
}
PROHIBITED_USE_CASES = (
    "sexual_content_involving_minors",
    "non_consensual_intimate_imagery",
    "coercion_exploitation_or_trafficking",
    "sexual_extortion_or_hidden_camera_content",
    "fraud_identity_theft_or_unauthorised_access",
)

def get_domain_catalog() -> dict:
    """Return a detached catalog with consistent scope and maturity definitions."""
    return {
        "geographic_scopes": list(GEOGRAPHIC_SCOPES),
        "maturity_levels": list(MATURITY_LEVELS),
        "domain_groups": {name: list(items) for name, items in DOMAIN_GROUPS.items()},
        "prohibited_use_cases": list(PROHIBITED_USE_CASES),
        "status": "CATALOG_DEFINED",
    }

__all__ = [
    "GEOGRAPHIC_SCOPES", "MATURITY_LEVELS", "DOMAIN_GROUPS",
    "PROHIBITED_USE_CASES", "get_domain_catalog",
]
