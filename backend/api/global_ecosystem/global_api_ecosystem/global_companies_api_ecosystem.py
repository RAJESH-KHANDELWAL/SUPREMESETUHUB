"""Name-matching module for the global_company_companies_api_ecosystem package."""

ECOSYSTEM_NAME = "global_company_companies_api_ecosystem"


def get_ecosystem_info() -> dict[str, str]:
    """Return basic metadata for this ecosystem package."""
    return {"name": ECOSYSTEM_NAME, "status": "scaffold"}
