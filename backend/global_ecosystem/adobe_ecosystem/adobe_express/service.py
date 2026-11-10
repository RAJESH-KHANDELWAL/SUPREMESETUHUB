"""Catalog descriptor for adobe express."""

PRODUCT_KEY = "adobe_express"
DESCRIPTION = "Templates, social content and quick design workflows"
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
