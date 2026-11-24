"""Independent API Ecosystem contract for recruitment."""
from .categories import CATEGORY_ID, CATEGORY_NAME, PARENT_DOMAIN_ID, TAXONOMY_STATUS, list_tracks, get_track, validate_tracks

def get_api_ecosystem() -> dict:
    integrity = validate_tracks()
    return {"api_ecosystem_id": f"{CATEGORY_ID.upper()}_API_ECOSYSTEM", "api_ecosystem_name": f"{CATEGORY_NAME} API Ecosystem", "parent_api_ecosystem_id": "WORK_CAREERS_EMPLOYMENT_API_ECOSYSTEM", "parent_domain_id": PARENT_DOMAIN_ID, "category_id": CATEGORY_ID, "category_name": CATEGORY_NAME, "taxonomy_status": TAXONOMY_STATUS, "capabilities": ["status", "track_list", "track_detail", "track_search", "integrity"], "track_count": integrity.get("track_count", 0), "structurally_valid": integrity.get("structurally_valid", False), "live_vacancies_verified": False, "employers_verified": False}

def list_track_api_ecosystems() -> list[dict]:
    return [{"api_ecosystem_id": f"{CATEGORY_ID.upper()}_{track['id'].upper()}_API_ECOSYSTEM", "api_ecosystem_name": f"{track['name']} API Ecosystem", "parent_api_ecosystem_id": f"{CATEGORY_ID.upper()}_API_ECOSYSTEM", "category_id": CATEGORY_ID, "track_id": track["id"], "track_name": track["name"], "taxonomy_status": TAXONOMY_STATUS, "live_vacancies_verified": False} for track in list_tracks()]

def get_track_api_ecosystem(track_id: str) -> dict | None:
    track = get_track(track_id)
    if track is None:
        return None
    return {"api_ecosystem_id": f"{CATEGORY_ID.upper()}_{track_id.upper()}_API_ECOSYSTEM", "api_ecosystem_name": f"{track['name']} API Ecosystem", "parent_api_ecosystem_id": f"{CATEGORY_ID.upper()}_API_ECOSYSTEM", "category_id": CATEGORY_ID, "track": track, "taxonomy_status": TAXONOMY_STATUS, "live_vacancies_verified": False}
