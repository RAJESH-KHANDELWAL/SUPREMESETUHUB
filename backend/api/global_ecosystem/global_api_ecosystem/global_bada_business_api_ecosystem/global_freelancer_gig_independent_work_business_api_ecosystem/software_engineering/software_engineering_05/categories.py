"""Canonical binding for this work type; parent work_types.py remains source of truth."""
from importlib import import_module

WORK_TYPE_ID = __package__.rsplit(".", 1)[-1]
SPECIALIZATION_PACKAGE = __package__.rsplit(".", 1)[0]
SPECIALIZATION_ID = SPECIALIZATION_PACKAGE.rsplit(".", 1)[-1]


def get_work_type_definition() -> dict:
    module = import_module(f"{SPECIALIZATION_PACKAGE}.work_types")
    record = next((item for item in module.WORK_TYPES if item.get("id") == WORK_TYPE_ID), None)
    if record is None:
        raise LookupError(
            f"Work type '{WORK_TYPE_ID}' is not registered in '{SPECIALIZATION_ID}'."
        )
    return dict(record)


def validate_work_type_definition() -> dict:
    try:
        record = get_work_type_definition()
    except LookupError as exc:
        return {
            "specialization_id": SPECIALIZATION_ID,
            "work_type_id": WORK_TYPE_ID,
            "structurally_valid": False,
            "errors": [str(exc)],
            "taxonomy_status": "taxonomy_only",
        }
    required = ("id", "name", "description")
    missing = [field for field in required if not str(record.get(field, "")).strip()]
    return {
        "specialization_id": SPECIALIZATION_ID,
        "work_type_id": WORK_TYPE_ID,
        "missing_fields": missing,
        "structurally_valid": not missing and record["id"] == WORK_TYPE_ID,
        "taxonomy_status": "taxonomy_only",
    }
