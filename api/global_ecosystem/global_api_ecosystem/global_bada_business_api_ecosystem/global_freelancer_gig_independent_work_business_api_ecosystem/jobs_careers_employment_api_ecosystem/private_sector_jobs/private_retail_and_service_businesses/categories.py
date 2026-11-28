"""Track-specific taxonomy binding for private_retail_and_service_businesses."""
from ...categories import get_track as _get_category_track

TRACK_ID = "private_retail_and_service_businesses"
CATEGORY_ID = "private_sector_jobs"
TAXONOMY_STATUS = "taxonomy_only"

def get_track_definition() -> dict:
    definition = _get_category_track(TRACK_ID)
    if definition is None:
        raise LookupError(f"Track '{TRACK_ID}' is not registered in category '{CATEGORY_ID}'.")
    return definition
