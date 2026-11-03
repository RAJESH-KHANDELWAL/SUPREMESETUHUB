"""Domain services for central ministries and departments."""
from .categories import get_department_taxonomy
from .validators import validate_department

def get_directory_contract() -> dict:
    return {**get_department_taxonomy(), "source_policy": "official_ministry_or_department_sources", "live_vacancies_available": False}

def assess_department(record: dict) -> dict:
    return validate_department(record)
