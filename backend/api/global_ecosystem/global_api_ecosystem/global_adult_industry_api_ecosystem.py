"""Name-matching entry point for the GLOBAL ADULT INDUSTRY API ECOSYSTEM package.

The provider catalog lives in the sibling global_adult_industry_api_ecosystem/ directory.
This module is catalog metadata only; it does not claim that any provider has a public API
or a live authenticated integration.
"""

ECOSYSTEM_NAME = "global_adult_industry_api_ecosystem"
PACKAGE_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_adult_industry_api_ecosystem"
ECOSYSTEM_FAMILY = "ADULT_INDUSTRY"
STATUS = "catalog_only"


def get_ecosystem_info() -> dict[str, str]:
    """Return metadata for discovery by the global API ecosystem index."""
    return {
        "name": ECOSYSTEM_NAME,
        "family": ECOSYSTEM_FAMILY,
        "package_path": PACKAGE_PATH,
        "status": STATUS,
        "integration_state": "not_live_connected",
    }
