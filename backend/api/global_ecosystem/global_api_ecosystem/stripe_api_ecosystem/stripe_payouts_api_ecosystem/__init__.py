"""STRIPE PAYOUTS API ECOSYSTEM package metadata."""
STRIPE_SERVICE_ECOSYSTEM = {
    "provider_id": "stripe",
    "service_id": "payouts",
    "name": "STRIPE_PAYOUTS_API_ECOSYSTEM",
    "scope": "Payouts and balance transactions",
    "primary_endpoint": "/v1/payouts",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
}
__all__ = ["STRIPE_SERVICE_ECOSYSTEM"]
