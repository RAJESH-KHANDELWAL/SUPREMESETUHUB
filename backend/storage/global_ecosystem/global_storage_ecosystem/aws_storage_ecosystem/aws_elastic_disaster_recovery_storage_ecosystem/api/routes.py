"""Framework-neutral read-only API handler for category status."""
from ..ecosystem_service import get_status

def get_category_status() -> dict:
    return get_status()
