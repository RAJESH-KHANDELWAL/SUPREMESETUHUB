"""Dedicated API Ecosystem descriptor for the private_companies track."""
from .categories import CATEGORY_ID, TRACK_ID
from .services import get_track_api_resource, get_track_status
from .validators import validate_track_definition

def get_api_ecosystem() -> dict:
    resource = get_track_api_resource()
    return {
        "api_ecosystem_id": f"{CATEGORY_ID.upper()}_{TRACK_ID.upper()}_API_ECOSYSTEM",
        "api_ecosystem_name": f"{resource['name']} API Ecosystem",
        "parent_api_ecosystem_id": f"{CATEGORY_ID.upper()}_API_ECOSYSTEM",
        "category_id": CATEGORY_ID,
        "track_id": TRACK_ID,
        "resource": resource,
        "status": get_track_status(),
        "integrity": validate_track_definition(),
        "taxonomy_status": "taxonomy_only",
        "live_vacancies_verified": False,
    }
