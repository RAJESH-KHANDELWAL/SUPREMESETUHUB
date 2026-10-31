"""Public Sector, Nonprofits & Social Impact domain package; classification only, not verified live listings."""
DOMAIN_ID = "public_nonprofit_social_impact"
DOMAIN_NAME = "Public Sector, Nonprofits & Social Impact"
ADULT_RESTRICTED = false
DEFAULT_DISCOVERY_ENABLED = true
SUBCATEGORY_IDS: tuple[str, ...] = (
    "government_departments",
    "public_services",
    "municipal_services",
    "public_procurement",
    "nonprofit_organizations",
    "charities",
    "foundations",
    "community_development",
    "rural_development",
    "social_enterprise",
    "volunteering",
    "skill_development_programs",
    "environmental_initiatives",
    "public_information_services",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
