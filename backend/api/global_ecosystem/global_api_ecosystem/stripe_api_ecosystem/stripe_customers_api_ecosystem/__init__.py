"""STRIPE CUSTOMERS API ECOSYSTEM package metadata."""
STRIPE_SERVICE_ECOSYSTEM = {
    "provider_id": "stripe",
    "service_id": "customers",
    "name": "STRIPE_CUSTOMERS_API_ECOSYSTEM",
    "scope": "Customer profiles, payment methods and tax IDs",
    "primary_endpoint": "/v1/customers",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
}
__all__ = ["STRIPE_SERVICE_ECOSYSTEM"]
