"""Bharat and global regional scope profiles."""
from ..catalog import GEOGRAPHIC_SCOPES

def get_regional_scope(scope: str) -> dict | None:
    key = str(scope or "").strip().casefold()
    if key not in GEOGRAPHIC_SCOPES:
        return None
    return {
        "scope": key,
        "catalog_scope": "Bharat_to_global",
        "local_law_review_required": True,
        "status": "REGIONAL_METADATA_ONLY",
    }

__all__ = ["get_regional_scope"]
