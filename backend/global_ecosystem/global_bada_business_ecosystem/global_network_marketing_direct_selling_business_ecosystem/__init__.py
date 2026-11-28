"""Network-marketing, direct-selling and affiliate ecosystem registry."""
from .catalog import (
    ECOSYSTEMS,
    find_platform,
    get_business_ecosystem,
    list_business_ecosystems,
    validate_business_ecosystems,
)

ECOSYSTEM_ID = "GLOBAL-NETWORK-MARKETING-DIRECT-SELLING-BUSINESS-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL NETWORK MARKETING & DIRECT SELLING BUSINESS ECOSYSTEM"
CHILD_ECOSYSTEMS = tuple(item["id"] for item in ECOSYSTEMS)

__all__ = [
    "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "CHILD_ECOSYSTEMS", "ECOSYSTEMS",
    "list_business_ecosystems", "get_business_ecosystem", "find_platform",
    "validate_business_ecosystems",
]
