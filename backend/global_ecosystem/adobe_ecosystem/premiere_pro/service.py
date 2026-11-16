"""Catalog descriptor for premiere pro."""

PRODUCT_KEY = "premiere_pro"
DESCRIPTION = "Video editing, timelines, media and export workflows"
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
