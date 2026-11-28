"""Track-specific taxonomy binding for second_career_opportunities."""
from ...categories import get_track as _get_category_track

TRACK_ID = "second_career_opportunities"
CATEGORY_ID = "career_changes"
TAXONOMY_STATUS = "taxonomy_only"

def get_track_definition() -> dict:
    definition = _get_category_track(TRACK_ID)
    if definition is None:
        raise LookupError(f"Track '{TRACK_ID}' is not registered in category '{CATEGORY_ID}'.")
    return definition
