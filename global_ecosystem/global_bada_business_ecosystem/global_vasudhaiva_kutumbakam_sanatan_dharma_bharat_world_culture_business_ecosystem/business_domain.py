"""Business-domain models for the cultural-world-culture business ecosystem.

These models describe proposed offerings. They do not represent live sellers,
inventory, payments, bookings, legal approvals or verified partnerships.
"""
from dataclasses import dataclass
from typing import Optional, Tuple

BUSINESS_DOMAINS = {
    "heritage_tourism": {"name": "Heritage and Responsible Tourism", "activities": ("guided_interpretation", "heritage_trails", "community_tours")},
    "arts_crafts_handloom": {"name": "Arts, Crafts and Handloom", "activities": ("artisan_goods", "commissions", "exhibitions", "workshops")},
    "cultural_education_language": {"name": "Cultural Education and Language", "activities": ("courses", "language_learning", "workshops", "translation")},
    "research_archives_knowledge": {"name": "Research, Archives and Knowledge", "activities": ("documentation", "oral_history_projects", "archival_services")},
    "events_festivals_exhibitions": {"name": "Events, Festivals and Exhibitions", "activities": ("festivals", "conferences", "exhibitions", "performances")},
    "publishing_media_content": {"name": "Publishing, Media and Content", "activities": ("books", "documentaries", "podcasts", "digital_publications")},
    "ethical_products_responsible_commerce": {"name": "Ethical Products and Responsible Commerce", "activities": ("verified_products", "responsible_sourcing", "creator_commerce")},
    "community_enterprise_social_impact": {"name": "Community Enterprise and Social Impact", "activities": ("cooperatives", "skills_programs", "community_enterprises")},
    "hospitality_food_heritage_experience": {"name": "Hospitality, Food Heritage and Experiences", "activities": ("responsible_stays", "culinary_heritage", "local_experiences")},
    "global_cultural_exchange_partnerships": {"name": "Global Cultural Exchange and Partnerships", "activities": ("institutional_exchange", "artist_residencies", "joint_programs")},
}

@dataclass(frozen=True)
class ProviderProfile:
    provider_id: str
    display_name: str
    provider_type: str
    region: Optional[str] = None
    languages: Tuple[str, ...] = ()
    verification_status: str = "unverified"

    def __post_init__(self):
        if not self.provider_id.strip() or not self.display_name.strip():
            raise ValueError("provider_id and display_name are required")
        if self.provider_type not in {"individual", "business", "community_group", "institution", "nonprofit"}:
            raise ValueError("unsupported provider_type")
        if self.verification_status not in {"unverified", "pending", "verified", "suspended"}:
            raise ValueError("unsupported verification_status")

@dataclass(frozen=True)
class BusinessOffering:
    offering_id: str
    title: str
    domain: str
    offering_type: str
    provider: ProviderProfile
    description: str
    cultural_origin: Optional[str] = None
    provenance_reference: Optional[str] = None
    rights_status: str = "unknown"
    consent_status: str = "pending"
    fair_compensation_defined: bool = False
    safety_reviewed: bool = False
    legal_reviewed: bool = False
    status: str = "draft"

    def __post_init__(self):
        if not self.offering_id.strip() or not self.title.strip():
            raise ValueError("offering_id and title are required")
        if self.domain not in BUSINESS_DOMAINS:
            raise ValueError("domain must be one of BUSINESS_DOMAINS")
        if self.offering_type not in {"product", "service", "course", "event", "experience", "partnership"}:
            raise ValueError("unsupported offering_type")
        if self.rights_status not in {"public_domain", "licensed", "permission_required", "restricted", "unknown"}:
            raise ValueError("unsupported rights_status")
        if self.consent_status not in {"granted", "pending", "denied", "not_required"}:
            raise ValueError("unsupported consent_status")
        if self.status not in {"draft", "under_review", "approved", "published", "paused", "rejected"}:
            raise ValueError("unsupported status")
