"""Track-specific taxonomy binding for technical_and_specialist_recruitment."""
from ...categories import get_track as _get_category_track

TRACK_ID = "technical_and_specialist_recruitment"
CATEGORY_ID = "recruitment"
TAXONOMY_STATUS = "taxonomy_only"

def get_track_definition() -> dict:
    definition = _get_category_track(TRACK_ID)
    if definition is None:
        raise LookupError(f"Track '{TRACK_ID}' is not registered in category '{CATEGORY_ID}'.")
    return definition
