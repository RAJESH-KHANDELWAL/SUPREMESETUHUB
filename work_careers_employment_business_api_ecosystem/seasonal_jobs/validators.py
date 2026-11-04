"""Structural validation for work-and-career taxonomy records."""
import re
from collections.abc import Mapping

_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]{1,79}$")

def validate_track_record(record: Mapping) -> dict:
    """Validate record shape; never infer vacancy or employer verification."""
    required = ("id", "name", "description")
    missing = [key for key in required if not isinstance(record.get(key), str) or not record[key].strip()]
    track_id = record.get("id", "")
    invalid_id = not isinstance(track_id, str) or not _ID_PATTERN.fullmatch(track_id)
    keywords = record.get("keywords", [])
    invalid_keywords = not isinstance(keywords, list) or any(not isinstance(item, str) or not item.strip() for item in keywords)
    related = record.get("related_track_ids", [])
    invalid_related = not isinstance(related, list) or any(not isinstance(item, str) or not _ID_PATTERN.fullmatch(item) for item in related)
    return {
        "valid": not missing and not invalid_id and not invalid_keywords and not invalid_related,
        "missing_fields": missing,
        "invalid_id": invalid_id,
        "invalid_keywords": invalid_keywords,
        "invalid_related_track_ids": invalid_related,
        "vacancy_verified": False,
        "employer_verified": False,
        "eligibility_verified": False,
    }
