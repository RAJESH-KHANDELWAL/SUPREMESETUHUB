"""Read-only discovery and dependency metadata."""
from .catalog import ECOSYSTEM_ID, get_catalog

def health() -> dict:
    catalog = get_catalog()
    return {"success": bool(catalog["work_models"]), "ecosystem_id": ECOSYSTEM_ID,
            "status": "FOUNDATION_READY" if catalog["work_models"] else "FOUNDATION_INCOMPLETE",
            "work_model_count": catalog["work_model_count"]}

def dependency_map() -> dict:
    return {"success": True, "source": ECOSYSTEM_ID,
            "canonical_work_model_owner": "GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-PART-TIME-FULL-TIME-WORK-FROM-HOME-GIG-CORE-ECOSYSTEM",
            "relationship": "BUSINESS_CAPABILITY_ADAPTER"}
