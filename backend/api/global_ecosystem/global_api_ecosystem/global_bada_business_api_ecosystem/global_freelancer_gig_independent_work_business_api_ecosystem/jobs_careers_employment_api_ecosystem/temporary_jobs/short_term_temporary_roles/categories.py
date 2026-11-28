"""Track-specific taxonomy binding for short_term_temporary_roles."""
from ...categories import get_track as _get_category_track

TRACK_ID = "short_term_temporary_roles"
CATEGORY_ID = "temporary_jobs"
TAXONOMY_STATUS = "taxonomy_only"

def get_track_definition() -> dict:
    definition = _get_category_track(TRACK_ID)
    if definition is None:
        raise LookupError(f"Track '{TRACK_ID}' is not registered in category '{CATEGORY_ID}'.")
    return definition
