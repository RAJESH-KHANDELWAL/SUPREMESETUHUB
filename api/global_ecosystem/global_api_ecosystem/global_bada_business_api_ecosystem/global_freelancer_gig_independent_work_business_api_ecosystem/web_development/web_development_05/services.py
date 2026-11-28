"""Service facade for one independently addressable work type."""
from .catalog import get_work_type, serialize_work_type
from .categories import SPECIALIZATION_ID, WORK_TYPE_ID, validate_work_type_definition


def get_work_type_resource() -> dict:
    return {
        "success": True,
        "specialization_id": SPECIALIZATION_ID,
        "work_type": serialize_work_type(),
        "taxonomy_status": "taxonomy_only",
        "live_gig_available": False,
    }


def get_work_type_status() -> dict:
    integrity = validate_work_type_definition()
    return {
        "success": integrity["structurally_valid"],
        "specialization_id": SPECIALIZATION_ID,
        "work_type_id": WORK_TYPE_ID,
        "taxonomy_status": "taxonomy_only",
        "live_gig_available": False,
        **integrity,
    }
