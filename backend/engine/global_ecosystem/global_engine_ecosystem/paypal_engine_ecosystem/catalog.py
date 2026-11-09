"""Independent ENGINE catalog for PAYPAL."""
from .models import EngineDescriptor
PROVIDER = "PAYPAL"
CHILD_ECOSYSTEMS = [
    "PAYPAL BILLING PLANS",
    "PAYPAL CHECKOUT",
    "PAYPAL DISPUTES",
    "PAYPAL IDENTITY OAUTH",
    "PAYPAL INVOICING",
    "PAYPAL MERCHANT ONBOARDING",
    "PAYPAL ORDERS",
    "PAYPAL PAYMENTS",
    "PAYPAL PAYOUTS",
    "PAYPAL SUBSCRIPTIONS",
    "PAYPAL TRANSACTION SEARCH",
    "PAYPAL VAULT PAYMENT METHODS",
    "PAYPAL WEBHOOKS"
]
CATALOG = (EngineDescriptor("ENGINE-PAYPAL", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
