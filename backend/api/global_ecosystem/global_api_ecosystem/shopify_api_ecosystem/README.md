# Shopify API Ecosystem

Provider catalog for Shopify commerce APIs, including Admin, Storefront, products,
orders, customers, inventory, fulfillment, webhooks, payments, billing and related
service families.

## Status

This folder is a structured metadata catalog. It is **not** a live Shopify connector.
Live connectivity requires a registered app, authorized shop, approved OAuth flow,
the minimum required scopes, secrets stored outside source control, and verified
development-store integration tests.

## Structure

- `shopify_api_ecosystem.py` — provider metadata and service-family registry.
- `shopify_*_api_ecosystem/` — service-family catalog modules.
- `__init__.py` — package exports.

Official documentation: https://shopify.dev/docs/api
