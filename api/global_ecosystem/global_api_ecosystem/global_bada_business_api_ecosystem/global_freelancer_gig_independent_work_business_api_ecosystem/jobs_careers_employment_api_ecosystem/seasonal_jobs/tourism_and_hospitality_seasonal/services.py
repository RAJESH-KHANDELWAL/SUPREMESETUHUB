"""Service layer for the tourism_and_hospitality_seasonal API resource; no live vacancies are asserted."""
from .categories import CATEGORY_ID, TRACK_ID, get_track_definition

def get_track_api_resource() -> dict:
    definition = get_track_definition()
    return {
        "id": TRACK_ID,
        "category_id": CATEGORY_ID,
        "name": definition["name"],
        "description": definition["description"],
        "role_families": list(definition.get("role_families", ())),
        "taxonomy_status": "taxonomy_only",
        "live_vacancies_available": False,
    }

def get_track_status() -> dict:
    resource = get_track_api_resource()
    return {
        "success": True,
        "category_id": CATEGORY_ID,
        "track_id": TRACK_ID,
        "taxonomy_status": "taxonomy_only",
        "live_vacancies_available": False,
        "structurally_valid": bool(resource["name"] and resource["description"]),
    }
