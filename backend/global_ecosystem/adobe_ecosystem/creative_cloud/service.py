"""Catalog descriptor for creative cloud."""

PRODUCT_KEY = "creative_cloud"
DESCRIPTION = "Creative Cloud apps, account, sync and storage"
MATURITY_LEVELS = ("basic", "standard", "professional", "enterprise", "supreme")
REGIONS = ("India", "Global")

def get_capabilities() -> dict:
    """Return metadata only; this function does not call Adobe services."""
    return {
        "product": PRODUCT_KEY,
        "description": DESCRIPTION,
        "maturity_levels": MATURITY_LEVELS,
        "regions": REGIONS,
        "integration_status": "catalog_only",
    }
