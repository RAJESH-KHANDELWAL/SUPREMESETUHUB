"""Home-Based Work, Homemakers & Care Economy domain package; classification only, not verified live listings."""
DOMAIN_ID = "home_homemaker_care_economy"
DOMAIN_NAME = "Home-Based Work, Homemakers & Care Economy"
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
SUBCATEGORY_IDS: tuple[str, ...] = (
    "home_based_enterprise",
    "home_food_business",
    "tailoring_handicrafts",
    "home_tuition",
    "online_freelancing",
    "remote_employment",
    "reselling",
    "crafts_and_artisan_work",
    "childcare_services",
    "eldercare_services",
    "caregiving_support",
    "domestic_services",
    "home_management_services",
    "community_support",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
