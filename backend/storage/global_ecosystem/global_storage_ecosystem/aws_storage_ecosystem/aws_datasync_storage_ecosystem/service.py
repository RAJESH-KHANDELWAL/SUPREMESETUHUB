"""Public category facade; deliberately read-only until integration is verified."""
from .ecosystem_service import get_status

def describe() -> dict:
    return get_status()
