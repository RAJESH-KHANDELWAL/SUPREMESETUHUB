"""API identity for the central recruitment authorities domain."""
from .categories import get_authority_taxonomy

def get_api_ecosystem() -> dict:
    taxonomy = get_authority_taxonomy()
    return {"api_ecosystem_id": "GOVERNMENT_JOBS_CENTRAL_RECRUITMENT_AUTHORITIES_API_ECOSYSTEM", **taxonomy, "live_vacancies_available": False}
