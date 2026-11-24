"""Structural validation for professional occupation taxonomy records."""
import re
from collections.abc import Mapping
_ID = re.compile(r"^[a-z][a-z0-9_]{1,79}$")
def validate_subcategory(record: Mapping) -> dict:
    required = ("id", "name", "description", "parent_field_id")
    missing = [key for key in required if not isinstance(record.get(key), str) or not record[key].strip()]
    valid_id = isinstance(record.get("id"), str) and bool(_ID.fullmatch(record["id"]))
    valid_parent = isinstance(record.get("parent_field_id"), str) and bool(_ID.fullmatch(record["parent_field_id"]))
    return {"valid": not missing and valid_id and valid_parent, "missing_fields": missing, "taxonomy_only": True, "vacancy_verified": False, "employer_verified": False, "credential_verified": False}
