"""Entrepreneurship, Startups & Innovation domain package; classification only, not verified live listings."""
DOMAIN_ID = "entrepreneurship_startups"
DOMAIN_NAME = "Entrepreneurship, Startups & Innovation"
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
SUBCATEGORY_IDS: tuple[str, ...] = (
    "business_ideas",
    "business_planning",
    "startup_formation",
    "validation_research",
    "incubators",
    "accelerators",
    "mentorship",
    "cofounder_matching",
    "fundraising",
    "angel_investment",
    "venture_capital",
    "bootstrapping",
    "crowdfunding",
    "intellectual_property",
    "product_development",
    "market_entry",
    "scaling_operations",
    "export_readiness",
    "social_enterprise",
    "rural_entrepreneurship",
    "women_entrepreneurship",
    "student_entrepreneurship",
    "franchise_entrepreneurship",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
