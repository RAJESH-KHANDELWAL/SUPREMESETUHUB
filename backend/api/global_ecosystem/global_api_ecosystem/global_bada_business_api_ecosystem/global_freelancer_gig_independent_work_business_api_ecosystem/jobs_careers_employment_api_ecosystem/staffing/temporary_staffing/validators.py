"""Structural validators for the temporary_staffing track package."""
from .categories import TRACK_ID, CATEGORY_ID, get_track_definition

def validate_track_definition() -> dict:
    try:
        item = get_track_definition()
    except LookupError as exc:
        return {"valid": False, "category_id": CATEGORY_ID, "track_id": TRACK_ID, "errors": [str(exc)], "taxonomy_only": True}
    required = ("id", "name", "description")
    missing = [key for key in required if not isinstance(item.get(key), str) or not item[key].strip()]
    return {"valid": not missing, "category_id": CATEGORY_ID, "track_id": TRACK_ID, "missing_fields": missing, "taxonomy_only": True, "live_vacancies_verified": False}
