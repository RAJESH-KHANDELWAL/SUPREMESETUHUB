"""Independent ENGINE catalog for SHOPIFY."""
from .models import EngineDescriptor
PROVIDER = "SHOPIFY"
CHILD_ECOSYSTEMS = [
    "SHOPIFY ADMIN",
    "SHOPIFY BILLING",
    "SHOPIFY CUSTOMERS",
    "SHOPIFY DISCOUNTS",
    "SHOPIFY FULFILLMENT",
    "SHOPIFY INVENTORY",
    "SHOPIFY LOCALIZATION",
    "SHOPIFY METAOBJECTS",
    "SHOPIFY ORDERS",
    "SHOPIFY PAYMENTS",
    "SHOPIFY PRODUCTS",
    "SHOPIFY SHIPPING",
    "SHOPIFY STOREFRONT",
    "SHOPIFY STOREFRONT GRAPHQL",
    "SHOPIFY WEBHOOKS"
]
CATALOG = (EngineDescriptor("ENGINE-SHOPIFY", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
