"""Compatibility facade for the canonical Finance, Banking & Insurance ecosystem."""
from ..global_finance_banking_insurance_api_ecosystem import (
    INDUSTRY_ID as DOMAIN_ID, INDUSTRY_NAME as DOMAIN_NAME, SUBCATEGORY_IDS,
    COVERAGE, CHANNELS, STATUS,
)
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True

def list_subcategories():
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]

__all__ = ["DOMAIN_ID", "DOMAIN_NAME", "ADULT_RESTRICTED", "DEFAULT_DISCOVERY_ENABLED", "SUBCATEGORY_IDS", "COVERAGE", "CHANNELS", "STATUS", "list_subcategories"]
