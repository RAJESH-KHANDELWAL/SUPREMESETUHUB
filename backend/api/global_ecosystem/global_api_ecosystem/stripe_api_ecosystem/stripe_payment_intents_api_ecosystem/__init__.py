"""STRIPE PAYMENT INTENTS API ECOSYSTEM package metadata."""
STRIPE_SERVICE_ECOSYSTEM = {
    "provider_id": "stripe",
    "service_id": "payment_intents",
    "name": "STRIPE_PAYMENT_INTENTS_API_ECOSYSTEM",
    "scope": "Payment Intents and payment lifecycle",
    "primary_endpoint": "/v1/payment_intents",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
}
__all__ = ["STRIPE_SERVICE_ECOSYSTEM"]
