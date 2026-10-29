"""Integration catalog; no provider credentials or live adapter is implemented here."""
from copy import deepcopy
from typing import Any

_ENTRIES: tuple[dict[str, Any], ...] = (
    {"integration_id":"relationship_education_platforms","name":"Relationship Education Platforms","category_ids":["RELATIONSHIPS","COUPLES_SERVICES"],"description":"Provider-neutral integration boundary for relationship education, coaching directories, booking, and learning resources.","implementation_status":"CATALOG_ONLY","official_api_required":True,"live_connection_verified":False,"compliance_review_required":True},
    {"integration_id":"dating_matchmaking_platforms","name":"Adult Dating and Matchmaking Platforms","category_ids":["DATING_MATCHMAKING","CONSENT_AND_SAFETY"],"description":"Provider-neutral boundary for adult profiles, consent-first messaging, reporting, moderation, and account controls.","implementation_status":"CATALOG_ONLY","official_api_required":True,"live_connection_verified":False,"compliance_review_required":True},
    {"integration_id":"sexual_health_information","name":"Sexual Health Information Services","category_ids":["SEXUAL_HEALTH","INTIMACY_WELLNESS"],"description":"Information and referral integration boundary; not a diagnostic or prescription service.","implementation_status":"CATALOG_ONLY","official_api_required":True,"live_connection_verified":False,"compliance_review_required":True},
    {"integration_id":"adult_industry_business_platforms","name":"Lawful Adult-Industry Business Platforms","category_ids":["ADULT_INDUSTRY_BUSINESS","ADULT_CONTENT_PUBLISHING"],"description":"Business operations, creator administration, rights management, compliance, and reporting where officially supported.","implementation_status":"CATALOG_ONLY","official_api_required":True,"live_connection_verified":False,"compliance_review_required":True},
    {"integration_id":"adult_content_hosting_delivery","name":"Adult-Content Hosting and Delivery","category_ids":["ADULT_CONTENT_HOSTING","ADULT_CONTENT_PUBLISHING"],"description":"Hosting, storage, CDN, moderation, and publishing adapters only for providers that explicitly permit the intended lawful content.","implementation_status":"CATALOG_ONLY","official_api_required":True,"live_connection_verified":False,"compliance_review_required":True},
    {"integration_id":"privacy_age_assurance_consent","name":"Privacy, Age Assurance, and Consent Services","category_ids":["CONSENT_AND_SAFETY","DATING_MATCHMAKING","ADULT_INDUSTRY_BUSINESS"],"description":"Provider-neutral boundary for privacy controls, age assurance, consent records, reporting, and abuse prevention.","implementation_status":"CATALOG_ONLY","official_api_required":True,"live_connection_verified":False,"compliance_review_required":True},
)

def list_entries(category_id: str | None = None) -> list[dict[str, Any]]:
    """Return integration metadata, optionally filtered by category ID."""
    entries = list(_ENTRIES)
    if category_id:
        key = category_id.strip().upper()
        entries = [entry for entry in entries if key in entry["category_ids"]]
    return deepcopy(entries)
