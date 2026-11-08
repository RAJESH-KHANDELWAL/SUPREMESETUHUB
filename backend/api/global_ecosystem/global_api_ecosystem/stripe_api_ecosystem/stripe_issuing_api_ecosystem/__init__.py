"""STRIPE ISSUING API ECOSYSTEM package metadata."""
STRIPE_SERVICE_ECOSYSTEM = {
    "provider_id": "stripe",
    "service_id": "issuing",
    "name": "STRIPE_ISSUING_API_ECOSYSTEM",
    "scope": "Issuing cards, cardholders and authorizations",
    "primary_endpoint": "/v1/issuing",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
}
__all__ = ["STRIPE_SERVICE_ECOSYSTEM"]
