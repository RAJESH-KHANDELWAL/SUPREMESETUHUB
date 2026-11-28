"""Framework-neutral status and health handlers for GLOBAL_INDIVIDUAL_CONSENT_AND_AUTHORIZATION_REFERENCES_STORAGE_ECOSYSTEM."""
from ..ecosystem_service import CategoryEcosystemService


def get_ecosystem_status() -> dict:
    return CategoryEcosystemService().describe()


def get_health() -> dict:
    return CategoryEcosystemService().health()
