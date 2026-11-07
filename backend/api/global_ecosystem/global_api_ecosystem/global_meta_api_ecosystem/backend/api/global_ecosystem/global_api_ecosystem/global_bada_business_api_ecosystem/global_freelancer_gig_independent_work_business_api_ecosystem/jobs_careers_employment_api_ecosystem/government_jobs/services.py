"""Service layer for Government Jobs taxonomy; no live vacancy data is provided."""
from .categories import CATEGORY_ID, CATEGORY_NAME, list_tracks, get_track, validate_tracks

def list_government_job_tracks() -> list[dict]:
    return list_tracks()

def get_government_job_track(track_id: str) -> dict | None:
    return get_track(track_id)

def search_government_job_tracks(query: str) -> list[dict]:
    needle = query.strip().casefold()
    if not needle:
        return []
    return [
        track for track in list_tracks()
        if needle in track["id"].casefold()
        or needle in track["name"].casefold()
        or needle in track["description"].casefold()
        or any(needle in role.casefold() for role in track["role_families"])
    ]

def get_government_jobs_status() -> dict:
    return {
        "success": True,
        "category_id": CATEGORY_ID,
        "category_name": CATEGORY_NAME,
        "taxonomy_status": "taxonomy_only",
        "live_vacancies_available": False,
        **validate_tracks(),
    }
