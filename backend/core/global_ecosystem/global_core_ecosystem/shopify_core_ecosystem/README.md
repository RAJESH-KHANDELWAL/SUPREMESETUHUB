# SHOPIFY CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/shopify_core_ecosystem/`

## Mission

Provider-level control plane for Shopify product identity, product discovery, store/tenant metadata contracts, capability inventory, domain classification, policy boundaries and readiness.

## Shared architecture

- `manager.py`: canonical Python entry point.
- `manager.php` and `shopify_php_core_ecosystem/ShopifyCoreContract.php`: PHP interoperability facade and sanitized result contract.
- `catalog.py`, `product_catalog.py`, `domain_catalog.py`: provider, product and domain inventories.
- `contracts.py`: tenant context and result contracts.
- `policy.py`: metadata policy and secret-field sanitization.
- `module_service.py`: shared product Core service.
- `orchestrator.py`, `service.py`: discovery and status.
- `ecosystem_manifest.json`: machine-readable package inventory.

## Product packages

- `shopify_admin_core_ecosystem/`: SHOPIFY ADMIN capability metadata.
- `shopify_billing_core_ecosystem/`: SHOPIFY BILLING capability metadata.
- `shopify_customers_core_ecosystem/`: SHOPIFY CUSTOMERS capability metadata.
- `shopify_discounts_core_ecosystem/`: SHOPIFY DISCOUNTS capability metadata.
- `shopify_fulfillment_core_ecosystem/`: SHOPIFY FULFILLMENT capability metadata.
- `shopify_inventory_core_ecosystem/`: SHOPIFY INVENTORY capability metadata.
- `shopify_localization_core_ecosystem/`: SHOPIFY LOCALIZATION capability metadata.
- `shopify_metaobjects_core_ecosystem/`: SHOPIFY METAOBJECTS capability metadata.
- `shopify_orders_core_ecosystem/`: SHOPIFY ORDERS capability metadata.
- `shopify_payments_core_ecosystem/`: SHOPIFY PAYMENTS capability metadata.
- `shopify_products_core_ecosystem/`: SHOPIFY PRODUCTS capability metadata.
- `shopify_shipping_core_ecosystem/`: SHOPIFY SHIPPING capability metadata.
- `shopify_storefront_core_ecosystem/`: SHOPIFY STOREFRONT capability metadata.
- `shopify_storefront_graphql_core_ecosystem/`: SHOPIFY STOREFRONT GRAPHQL capability metadata.
- `shopify_webhooks_core_ecosystem/`: SHOPIFY WEBHOOKS capability metadata.

Each product package contains only `__init__.py` and its product-specific `manager.py`; common logic stays centralized.

## Boundaries

OAuth, token exchange, Shopify Admin/Storefront GraphQL transport, webhook delivery, persistence, billing execution and UI belong to API, security, storage, runtime and application layers. Use least-privilege scopes, authenticated tenant identity, encrypted external secret storage, webhook signature verification, idempotent event handling and explicit authorization for sensitive writes. Catalog registration is not proof of app authorization, store entitlement or live connectivity.
