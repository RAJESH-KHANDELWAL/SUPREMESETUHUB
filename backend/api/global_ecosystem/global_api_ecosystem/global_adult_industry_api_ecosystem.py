"""Compatibility metadata for the adult-industry API catalog under Bada Business.

The API provider modules are maintained in adult_business_api_ecosystem/.
"""

ECOSYSTEM_NAME = "adult_business_api_ecosystem"
LEGACY_ECOSYSTEM_NAME = "global_adult_industry_api_ecosystem"
LEGACY_PACKAGE_NAME = "adult_business_ecosystem"
PACKAGE_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/adult_business_api_ecosystem"
ECOSYSTEM_FAMILY = "BADA_BUSINESS"
AGE_RESTRICTION = "18+"
STATUS = "catalog_only"


def get_ecosystem_info() -> dict[str, str]:
    return {
        "name": ECOSYSTEM_NAME,
        "legacy_name": LEGACY_ECOSYSTEM_NAME,
        "legacy_package_name": LEGACY_PACKAGE_NAME,
        "family": ECOSYSTEM_FAMILY,
        "package_path": PACKAGE_PATH,
        "age_restriction": AGE_RESTRICTION,
        "status": STATUS,
        "integration_state": "not_live_connected",
    }
