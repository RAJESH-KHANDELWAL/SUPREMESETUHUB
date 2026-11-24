"""Independent ENGINE catalog for STRIPE."""
from .models import EngineDescriptor
PROVIDER = "STRIPE"
CHILD_ECOSYSTEMS = [
    "STRIPE ACCOUNTS",
    "STRIPE BILLING",
    "STRIPE CHECKOUT",
    "STRIPE CLIMATE",
    "STRIPE CRYPTO ONRAMP",
    "STRIPE CUSTOMERS",
    "STRIPE DISPUTES",
    "STRIPE EVENTS",
    "STRIPE FRAUD",
    "STRIPE ISSUING",
    "STRIPE PAYMENT INTENTS",
    "STRIPE PAYMENT LINKS",
    "STRIPE PAYMENT METHODS",
    "STRIPE PAYOUTS",
    "STRIPE PRODUCTS PRICES",
    "STRIPE REFUNDS",
    "STRIPE REPORTING",
    "STRIPE SUBSCRIPTIONS",
    "STRIPE TAX",
    "STRIPE TERMINAL",
    "STRIPE TREASURY",
    "STRIPE WEBHOOKS",
    "TESTS"
]
CATALOG = (EngineDescriptor("ENGINE-STRIPE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
