"""API identity for ministry and department recruitment directory."""
from .categories import get_department_taxonomy

def get_api_ecosystem() -> dict:
    return {"api_ecosystem_id": "CENTRAL_GOVERNMENT_MINISTRIES_AND_DEPARTMENTS_API_ECOSYSTEM", **get_department_taxonomy(), "live_vacancies_available": False}
