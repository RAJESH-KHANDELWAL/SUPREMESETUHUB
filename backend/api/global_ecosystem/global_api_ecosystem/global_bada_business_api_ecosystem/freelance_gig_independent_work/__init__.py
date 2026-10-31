"""Freelancing, Gig & Independent Work domain package; classification only, not verified live listings."""
DOMAIN_ID = "freelance_gig_independent_work"
DOMAIN_NAME = "Freelancing, Gig & Independent Work"
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
SUBCATEGORY_IDS: tuple[str, ...] = (
    "writing_editing",
    "translation_localization",
    "graphic_design",
    "web_development",
    "app_development",
    "software_engineering",
    "data_analysis",
    "ai_automation",
    "digital_marketing",
    "seo",
    "social_media_management",
    "video_audio_production",
    "photography",
    "virtual_assistance",
    "bookkeeping_accounting",
    "legal_consulting",
    "business_consulting",
    "tutoring",
    "coaching_training",
    "delivery_gig_work",
    "driving_transport_gigs",
    "home_service_gigs",
    "creative_commissions",
    "professional_contracting",
    "microtasks",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
