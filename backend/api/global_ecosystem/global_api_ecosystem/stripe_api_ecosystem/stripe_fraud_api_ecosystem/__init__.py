"""STRIPE FRAUD API ECOSYSTEM package metadata."""
STRIPE_SERVICE_ECOSYSTEM = {
    "provider_id": "stripe",
    "service_id": "fraud",
    "name": "STRIPE_FRAUD_API_ECOSYSTEM",
    "scope": "Radar risk evaluation and fraud signals",
    "primary_endpoint": "/v1/radar",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
}
__all__ = ["STRIPE_SERVICE_ECOSYSTEM"]
