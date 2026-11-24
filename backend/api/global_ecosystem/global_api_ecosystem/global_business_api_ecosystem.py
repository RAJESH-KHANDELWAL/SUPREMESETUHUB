"""Legacy name-matching entry point for the renamed Bada Business ecosystem."""

ECOSYSTEM_NAME = "global_bada_business_api_ecosystem"
LEGACY_ECOSYSTEM_NAME = "global_business_api_ecosystem"
PACKAGE_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem"
STATUS = "catalog_available"


def get_ecosystem_info() -> dict[str, str]:
    return {
        "name": ECOSYSTEM_NAME,
        "legacy_name": LEGACY_ECOSYSTEM_NAME,
        "package_path": PACKAGE_PATH,
        "status": STATUS,
    }
