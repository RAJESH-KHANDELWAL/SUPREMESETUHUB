"""Framework-neutral status and health handlers for GLOBAL_INDIVIDUAL_PERSONAL_PHOTO_AND_VIDEO_STORAGE_STORAGE_ECOSYSTEM."""
from ..ecosystem_service import CategoryEcosystemService


def get_ecosystem_status() -> dict:
    return CategoryEcosystemService().describe()


def get_health() -> dict:
    return CategoryEcosystemService().health()
