"""Shopify provider API ecosystem catalog and service-family registry.

Metadata only. Catalog entries do not imply app approval, shop authorization,
credentials, granted scopes, or live API connectivity.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

PROVIDER_ID = "shopify"
PROVIDER_NAME = "SHOPIFY API ECOSYSTEM"
PROVIDER_VENDOR = "Shopify"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/shopify_api_ecosystem"

SHOPIFY_SERVICE_ECOSYSTEMS = [
    {"id": "admin", "name": "SHOPIFY ADMIN API ECOSYSTEM", "folder": "shopify_admin_api_ecosystem", "status": "catalog_only"},
    {"id": "storefront", "name": "SHOPIFY STOREFRONT API ECOSYSTEM", "folder": "shopify_storefront_api_ecosystem", "status": "catalog_only"},
    {"id": "storefront_graphql", "name": "SHOPIFY STOREFRONT GRAPHQL API ECOSYSTEM", "folder": "shopify_storefront_graphql_api_ecosystem", "status": "catalog_only"},
    {"id": "products", "name": "SHOPIFY PRODUCTS API ECOSYSTEM", "folder": "shopify_products_api_ecosystem", "status": "catalog_only"},
    {"id": "orders", "name": "SHOPIFY ORDERS API ECOSYSTEM", "folder": "shopify_orders_api_ecosystem", "status": "catalog_only"},
    {"id": "customers", "name": "SHOPIFY CUSTOMERS API ECOSYSTEM", "folder": "shopify_customers_api_ecosystem", "status": "catalog_only"},
    {"id": "inventory", "name": "SHOPIFY INVENTORY API ECOSYSTEM", "folder": "shopify_inventory_api_ecosystem", "status": "catalog_only"},
    {"id": "fulfillment", "name": "SHOPIFY FULFILLMENT API ECOSYSTEM", "folder": "shopify_fulfillment_api_ecosystem", "status": "catalog_only"},
    {"id": "webhooks", "name": "SHOPIFY WEBHOOKS API ECOSYSTEM", "folder": "shopify_webhooks_api_ecosystem", "status": "catalog_only"},
    {"id": "payments", "name": "SHOPIFY PAYMENTS API ECOSYSTEM", "folder": "shopify_payments_api_ecosystem", "status": "catalog_only"},
    {"id": "billing", "name": "SHOPIFY BILLING API ECOSYSTEM", "folder": "shopify_billing_api_ecosystem", "status": "catalog_only"},
    {"id": "discounts", "name": "SHOPIFY DISCOUNTS API ECOSYSTEM", "folder": "shopify_discounts_api_ecosystem", "status": "catalog_only"},
    {"id": "shipping", "name": "SHOPIFY SHIPPING API ECOSYSTEM", "folder": "shopify_shipping_api_ecosystem", "status": "catalog_only"},
    {"id": "localization", "name": "SHOPIFY LOCALIZATION API ECOSYSTEM", "folder": "shopify_localization_api_ecosystem", "status": "catalog_only"},
    {"id": "metaobjects", "name": "SHOPIFY METAOBJECTS API ECOSYSTEM", "folder": "shopify_metaobjects_api_ecosystem", "status": "catalog_only"},
]

PROVIDER_API_ECOSYSTEM: dict[str, Any] = {
    "provider_id": PROVIDER_ID,
    "name": PROVIDER_NAME,
    "vendor": PROVIDER_VENDOR,
    "families": ["APP", "BUSINESS", "PAYMENT"],
    "scope": "Storefront, Admin, products, orders, customers, inventory, fulfillment and commerce APIs subject to app scopes, shop authorization and regional availability.",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_EXPANDED_LIVE_API_UNVERIFIED",
    "live_connection_verified": False,
    "provider_catalog_path": PROVIDER_CATALOG_PATH,
    "authentication": {
        "methods": ["SHOPIFY_OAUTH_2_AUTHORIZATION_CODE", "SHOPIFY_CLIENT_CREDENTIALS_WHERE_SUPPORTED"],
        "credential_source": "environment_or_managed_secret_store",
        "required_environment": ["SHOPIFY_API_KEY", "SHOPIFY_API_SECRET"],
        "shop_domain_required": True,
        "secrets_in_repository": False,
    },
    "endpoint_strategy": {
        "admin_api": "https://{shop}.myshopify.com/admin/api/{api_version}/",
        "storefront_api": "https://{shop}.myshopify.com/api/{api_version}/graphql.json",
        "api_version": "explicitly_configured_supported_version",
        "never_assume_shop_or_scopes": True,
    },
    "service_ecosystems": SHOPIFY_SERVICE_ECOSYSTEMS,
    "integration_requirements": [
        "official_api_reference_review",
        "shop_domain_validation",
        "oauth_state_and_callback_validation",
        "least_privilege_scope_review",
        "webhook_hmac_verification",
        "api_version_and_deprecation_policy",
        "graphql_cost_and_rate_limit_handling",
        "timeouts_retries_and_idempotency_where_supported",
        "unit_tests_with_mocked_responses",
        "opt_in_development_store_integration_tests",
    ],
    "security": {
        "never_log_client_secrets_or_access_tokens": True,
        "verify_webhook_hmac": True,
        "use_least_privilege_scopes": True,
        "live_connection_requires_successful_authenticated_shop_api_test": True,
    },
    "documentation": [
        "https://shopify.dev/docs/api",
        "https://shopify.dev/docs/api/admin-graphql",
        "https://shopify.dev/docs/api/storefront",
        "https://shopify.dev/docs/apps/auth",
        "https://shopify.dev/docs/apps/build/webhooks",
    ],
}

SHOPIFY_API_ECOSYSTEM = PROVIDER_API_ECOSYSTEM

def get_shopify_api_ecosystem() -> dict[str, Any]:
    """Return an isolated copy of Shopify provider metadata."""
    return deepcopy(PROVIDER_API_ECOSYSTEM)

def list_shopify_api_ecosystems() -> dict[str, object]:
    """List Shopify API service-family catalogs without claiming live connectivity."""
    children = [dict(item) for item in SHOPIFY_SERVICE_ECOSYSTEMS]
    return {
        "success": True,
        "provider": PROVIDER_NAME,
        "status": PROVIDER_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }

__all__ = [
    "PROVIDER_ID", "PROVIDER_NAME", "PROVIDER_VENDOR", "PROVIDER_CATALOG_PATH",
    "PROVIDER_API_ECOSYSTEM", "SHOPIFY_API_ECOSYSTEM", "SHOPIFY_SERVICE_ECOSYSTEMS",
    "get_shopify_api_ecosystem", "list_shopify_api_ecosystems",
]
