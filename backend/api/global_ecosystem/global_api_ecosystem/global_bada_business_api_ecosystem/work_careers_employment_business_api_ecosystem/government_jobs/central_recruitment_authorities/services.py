"""Service functions for recruitment authority taxonomy."""
from .categories import get_authority_taxonomy
from .validators import validate_authority

def get_authority_directory_contract() -> dict:
    return {**get_authority_taxonomy(), "source_policy": "official_authority_sources_only", "live_vacancies_available": False}

def assess_authority_record(record: dict) -> dict:
    return validate_authority(record)
