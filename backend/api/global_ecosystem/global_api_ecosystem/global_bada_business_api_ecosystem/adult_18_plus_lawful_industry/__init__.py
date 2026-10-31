"""Adult 18+ & Sexual Wellness Industry domain package; classification only, not verified live listings."""
DOMAIN_ID = "adult_18_plus_lawful_industry"
DOMAIN_NAME = "Adult 18+ & Sexual Wellness Industry"
ADULT_RESTRICTED = true
DEFAULT_DISCOVERY_ENABLED = false
SUBCATEGORY_IDS: tuple[str, ...] = (
    "sexual_wellness_education",
    "adult_health_information",
    "couples_intimacy_education",
    "lawful_adult_entertainment",
    "adult_content_creation",
    "adult_creator_platforms",
    "adult_studio_businesses",
    "adult_subscription_services",
    "adult_payment_compliance",
    "age_verification_services",
    "consent_and_safeguarding",
    "privacy_and_content_protection",
    "lawful_adult_retail",
    "adult_industry_professional_services",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
