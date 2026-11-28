"""Customers API service-family catalog; not a live API adapter."""
from __future__ import annotations

SHOPIFY_SERVICE_ECOSYSTEM = {
    "provider_id": "shopify",
    "name": "SHOPIFY CUSTOMERS API ECOSYSTEM",
    "service_id": "customers",
    "scope": "Customer records and customer data access subject to protected customer data approval.",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/shopify_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "documentation": "https://shopify.dev/docs/api",
}

__all__ = ["SHOPIFY_SERVICE_ECOSYSTEM"]
