"""Canonical inventory of Shopify product families."""
from typing import Any
PRODUCTS: tuple[dict[str, Any], ...] = (
    {"product_id":"SHOPIFY_ADMIN","ecosystem_id":"SHOPIFY-ADMIN-CORE-ECOSYSTEM","name":"admi","package_name":"shopify_admin_core_ecosystem","domain_id":"ADMINISTRATION","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_BILLING","ecosystem_id":"SHOPIFY-BILLING-CORE-ECOSYSTEM","name":"billin","package_name":"shopify_billing_core_ecosystem","domain_id":"BILLING","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_CUSTOMERS","ecosystem_id":"SHOPIFY-CUSTOMERS-CORE-ECOSYSTEM","name":"customer","package_name":"shopify_customers_core_ecosystem","domain_id":"CUSTOMERS","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_DISCOUNTS","ecosystem_id":"SHOPIFY-DISCOUNTS-CORE-ECOSYSTEM","name":"discount","package_name":"shopify_discounts_core_ecosystem","domain_id":"COMMERCE","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_FULFILLMENT","ecosystem_id":"SHOPIFY-FULFILLMENT-CORE-ECOSYSTEM","name":"fulfillmen","package_name":"shopify_fulfillment_core_ecosystem","domain_id":"FULFILLMENT","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_INVENTORY","ecosystem_id":"SHOPIFY-INVENTORY-CORE-ECOSYSTEM","name":"inventor","package_name":"shopify_inventory_core_ecosystem","domain_id":"INVENTORY","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_LOCALIZATION","ecosystem_id":"SHOPIFY-LOCALIZATION-CORE-ECOSYSTEM","name":"localizatio","package_name":"shopify_localization_core_ecosystem","domain_id":"LOCALIZATION","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_METAOBJECTS","ecosystem_id":"SHOPIFY-METAOBJECTS-CORE-ECOSYSTEM","name":"metaobject","package_name":"shopify_metaobjects_core_ecosystem","domain_id":"CONTENT","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_ORDERS","ecosystem_id":"SHOPIFY-ORDERS-CORE-ECOSYSTEM","name":"order","package_name":"shopify_orders_core_ecosystem","domain_id":"ORDERS","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_PAYMENTS","ecosystem_id":"SHOPIFY-PAYMENTS-CORE-ECOSYSTEM","name":"payment","package_name":"shopify_payments_core_ecosystem","domain_id":"PAYMENTS","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_PRODUCTS","ecosystem_id":"SHOPIFY-PRODUCTS-CORE-ECOSYSTEM","name":"product","package_name":"shopify_products_core_ecosystem","domain_id":"CATALOG","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_SHIPPING","ecosystem_id":"SHOPIFY-SHIPPING-CORE-ECOSYSTEM","name":"shippin","package_name":"shopify_shipping_core_ecosystem","domain_id":"FULFILLMENT","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_STOREFRONT","ecosystem_id":"SHOPIFY-STOREFRONT-CORE-ECOSYSTEM","name":"storefron","package_name":"shopify_storefront_core_ecosystem","domain_id":"STOREFRONT","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_STOREFRONT_GRAPHQL","ecosystem_id":"SHOPIFY-STOREFRONT-GRAPHQL-CORE-ECOSYSTEM","name":"storefront graphq","package_name":"shopify_storefront_graphql_core_ecosystem","domain_id":"STOREFRONT","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
    {"product_id":"SHOPIFY_WEBHOOKS","ecosystem_id":"SHOPIFY-WEBHOOKS-CORE-ECOSYSTEM","name":"webhook","package_name":"shopify_webhooks_core_ecosystem","domain_id":"EVENTS","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False},
)
def list_products(*, enabled_only=False):
    items=[dict(p) for p in PRODUCTS]
    return [p for p in items if p["enabled"]] if enabled_only else items
def get_product(key):
    needle=key.strip().casefold()
    return next((dict(p) for p in PRODUCTS if needle in {p["product_id"].casefold(),p["ecosystem_id"].casefold(),p["package_name"].casefold(),p["name"].casefold()}),None) if needle else None
