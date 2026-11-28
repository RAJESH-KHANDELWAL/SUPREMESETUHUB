"""Compatibility facade; canonical implementation lives in industry_api_ecosystems.government_public_services_social_impact."""
from ..government_public_services_social_impact import (
    INDUSTRY_ID as DOMAIN_ID,
    INDUSTRY_NAME as DOMAIN_NAME,
)
from ..government_public_services_social_impact.catalog import (
    CATEGORIES,
    LEGACY_CATEGORY_CROSSWALK,
)
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
SUBCATEGORY_IDS = tuple(LEGACY_CATEGORY_CROSSWALK)

def list_subcategories() -> list[dict[str, str]]:
    return [
        {"id": legacy_id, "name": legacy_id.replace("_", " ").title(),
         "domain_id": DOMAIN_ID,
         "canonical_category_id": canonical_id}
        for legacy_id, canonical_id in LEGACY_CATEGORY_CROSSWALK.items()
    ]
