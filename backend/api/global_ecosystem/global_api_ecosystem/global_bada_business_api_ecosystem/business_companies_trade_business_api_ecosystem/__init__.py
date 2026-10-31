"""Businesses, Companies & Trade domain package; classification only, not verified live listings."""
DOMAIN_ID = "business_companies_trade"
DOMAIN_NAME = "Businesses, Companies & Trade"
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
SUBCATEGORY_IDS: tuple[str, ...] = (
    "sole_proprietorship",
    "partnership",
    "limited_liability_partnership",
    "private_limited_company",
    "public_company",
    "cooperative",
    "micro_business",
    "small_business",
    "medium_business",
    "large_enterprise",
    "multinational",
    "family_business",
    "home_based_business",
    "local_business",
    "franchise",
    "dealership",
    "distributorship",
    "wholesale",
    "retail",
    "manufacturing",
    "import_export",
    "trading",
    "ecommerce",
    "marketplace_seller",
    "subscription_business",
    "business_services",
    "business_transfer_acquisition",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
