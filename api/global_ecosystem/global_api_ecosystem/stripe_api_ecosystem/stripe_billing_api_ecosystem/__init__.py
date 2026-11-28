"""STRIPE BILLING API ECOSYSTEM package metadata."""
STRIPE_SERVICE_ECOSYSTEM = {
    "provider_id": "stripe",
    "service_id": "billing",
    "name": "STRIPE_BILLING_API_ECOSYSTEM",
    "scope": "Billing, invoices, quotes and customer balance",
    "primary_endpoint": "/v1/invoices",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
}
__all__ = ["STRIPE_SERVICE_ECOSYSTEM"]
