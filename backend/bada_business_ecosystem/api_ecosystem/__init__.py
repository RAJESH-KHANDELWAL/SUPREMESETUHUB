"""Public API entry point for the Bada Business product ecosystem.

The API source modules are intentionally still implemented in the API layer.
This adapter exposes the existing router without forking or copying routes.
"""
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem import router

API_ECOSYSTEM_ID = "GLOBAL_BADA_BUSINESS_API_ECOSYSTEM"
API_ECOSYSTEM_NAME = "GLOBAL BADA BUSINESS API ECOSYSTEM"
API_IMPLEMENTATION_PATH = (
    "backend/api/global_ecosystem/global_api_ecosystem/"
    "global_bada_business_api_ecosystem"
)

__all__ = [
    "router",
    "API_ECOSYSTEM_ID",
    "API_ECOSYSTEM_NAME",
    "API_IMPLEMENTATION_PATH",
]
