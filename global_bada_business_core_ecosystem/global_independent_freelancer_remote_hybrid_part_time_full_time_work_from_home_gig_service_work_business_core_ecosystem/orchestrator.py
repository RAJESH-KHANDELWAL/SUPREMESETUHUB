"""Read-only discovery and dependency metadata for the Bada Business adapter."""
from .catalog import ECOSYSTEM_ID, get_catalog


def health() -> dict:
    catalog = get_catalog()
    ready = bool(catalog["business_capabilities"] and catalog["work_models"])
    return {
        "success": ready,
        "ecosystem_id": ECOSYSTEM_ID,
        "status": "FOUNDATION_READY" if ready else "FOUNDATION_INCOMPLETE",
        "work_model_count": catalog["work_model_count"],
        "business_capability_count": catalog["business_capability_count"],
    }


def dependency_map() -> dict:
    return {
        "success": True,
        "source": ECOSYSTEM_ID,
        "parent": "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM",
        "canonical_work_model_owner": "GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-PART-TIME-FULL-TIME-WORK-FROM-HOME-GIG-CORE-ECOSYSTEM",
        "relationship": "BUSINESS_CAPABILITY_ADAPTER",
    }
