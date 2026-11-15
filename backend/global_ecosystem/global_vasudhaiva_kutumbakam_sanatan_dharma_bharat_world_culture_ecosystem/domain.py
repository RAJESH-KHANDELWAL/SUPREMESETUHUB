"""Canonical cultural domain vocabulary and resource models.

This module models cultural knowledge and heritage, not commercial listings.
It intentionally keeps source provenance, community context and access status
attached to each resource.
"""
from dataclasses import dataclass, field
from typing import Optional, Tuple

CULTURAL_PILLARS = {
    "vasudhaiva_kutumbakam": {
        "name": "Vasudhaiva Kutumbakam",
        "meaning": "Shared humanity, mutual respect and the world as one family",
        "focus": ("intercultural_dialogue", "shared_human_values", "global_cooperation"),
    },
    "sanatan_dharma": {
        "name": "Sanatan Dharma",
        "meaning": "Plural philosophical, spiritual, ethical, textual and living traditions",
        "focus": ("philosophy", "texts", "knowledge_systems", "living_traditions"),
    },
    "bharat_sanskriti": {
        "name": "Bharat Sanskriti",
        "meaning": "India's plural civilizational, regional, linguistic and creative heritage",
        "focus": ("languages", "literature", "arts", "crafts", "festivals", "heritage"),
    },
    "world_culture": {
        "name": "World Culture",
        "meaning": "The distinct cultures, languages, histories and living communities of the world",
        "focus": ("world_languages", "global_heritage", "creative_traditions", "cultural_exchange"),
    },
}

CULTURAL_AREAS = (
    "philosophy_and_knowledge", "history_and_heritage", "languages_and_literature",
    "arts_and_crafts", "festivals_and_living_traditions", "places_and_cultural_landscapes",
    "education_and_research", "communities_and_institutions", "global_cultural_exchange",
)

@dataclass(frozen=True)
class CulturalResource:
    """A discoverable cultural knowledge or heritage resource."""

    resource_id: str
    title: str
    pillar: str
    area: str
    description: str
    region: Optional[str] = None
    language: Optional[str] = None
    community_context: Optional[str] = None
    source_reference: Optional[str] = None
    source_kind: str = "unspecified"  # documented, oral_history, traditional_account, interpretation
    rights_status: str = "unknown"  # public_domain, licensed, permission_required, restricted, unknown
    consent_status: str = "not_required"  # granted, pending, denied, not_required
    access_level: str = "public"  # public, community, restricted
    tags: Tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self):
        if not self.resource_id.strip() or not self.title.strip():
            raise ValueError("resource_id and title are required")
        if self.pillar not in CULTURAL_PILLARS:
            raise ValueError("pillar must be one of the canonical cultural pillars")
        if self.area not in CULTURAL_AREAS:
            raise ValueError("area must be a canonical cultural area")
        if self.source_kind not in {"documented", "oral_history", "traditional_account", "interpretation", "unspecified"}:
            raise ValueError("unsupported source_kind")
        if self.rights_status not in {"public_domain", "licensed", "permission_required", "restricted", "unknown"}:
            raise ValueError("unsupported rights_status")
        if self.consent_status not in {"granted", "pending", "denied", "not_required"}:
            raise ValueError("unsupported consent_status")
        if self.access_level not in {"public", "community", "restricted"}:
            raise ValueError("unsupported access_level")
