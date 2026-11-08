"""Top-level entry point for the Bada Business API ecosystem."""
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem import router
API_ECOSYSTEM_ID = "GLOBAL_BADA_BUSINESS_API_ECOSYSTEM"
API_ECOSYSTEM_NAME = "GLOBAL BADA BUSINESS API ECOSYSTEM"
__all__ = ["router","API_ECOSYSTEM_ID","API_ECOSYSTEM_NAME"]
