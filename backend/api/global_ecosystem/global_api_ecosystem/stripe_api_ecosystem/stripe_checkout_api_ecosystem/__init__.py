"""STRIPE CHECKOUT API ECOSYSTEM package metadata."""
STRIPE_SERVICE_ECOSYSTEM = {
    "provider_id": "stripe",
    "service_id": "checkout",
    "name": "STRIPE_CHECKOUT_API_ECOSYSTEM",
    "scope": "Checkout Sessions and hosted payment flows",
    "primary_endpoint": "/v1/checkout/sessions",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
}
__all__ = ["STRIPE_SERVICE_ECOSYSTEM"]
