"""GOOGLE FORMS CORE ECOSYSTEM package exports."""
ECOSYSTEM_ID = "GOOGLE-FORMS-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GOOGLE FORMS CORE ECOSYSTEM"
API_CATALOG_REF = "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_forms_api_ecosystem"
IMPLEMENTATION_STATUS = "CORE_CATALOG_ONLY"
LIVE_CONNECTION_VERIFIED = False

from .service import GoogleFormsCoreService

__all__ = [
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "API_CATALOG_REF",
    "IMPLEMENTATION_STATUS",
    "LIVE_CONNECTION_VERIFIED",
    "GoogleFormsCoreService",
]
