"""Stripe product inventory projected from the existing canonical provider catalog."""
from .catalog import get_stripe_core_catalog
from .policy import StripeCorePolicy
DOMAIN_BY_FAMILY={"accounts":"ACCOUNTS_AND_IDENTITY","customers":"ACCOUNTS_AND_IDENTITY","checkout":"PAYMENTS_AND_CHECKOUT","payment_intents":"PAYMENTS_AND_CHECKOUT","payment_methods":"PAYMENTS_AND_CHECKOUT","payment_links":"PAYMENTS_AND_CHECKOUT","billing":"BILLING_AND_SUBSCRIPTIONS","subscriptions":"BILLING_AND_SUBSCRIPTIONS","tax":"BILLING_AND_SUBSCRIPTIONS","payouts":"FINANCIAL_OPERATIONS","treasury":"FINANCIAL_OPERATIONS","reporting":"FINANCIAL_OPERATIONS","disputes":"RISK_AND_DISPUTES","fraud":"RISK_AND_DISPUTES","refunds":"RISK_AND_DISPUTES","events":"EVENTS_AND_WEBHOOKS","webhooks":"EVENTS_AND_WEBHOOKS","products_prices":"PRODUCT_CATALOG","terminal":"IN_PERSON_COMMERCE","issuing":"ISSUING_AND_CARDS","climate":"CLIMATE_AND_EMERGING_RAILS","crypto_onramp":"CLIMATE_AND_EMERGING_RAILS"}
DOMAIN_DEFINITIONS={
  "ACCOUNTS_AND_IDENTITY": {
    "name": "Accounts and Identity",
    "purpose": "Connected account references, merchant onboarding and customer identity lifecycle metadata."
  },
  "PAYMENTS_AND_CHECKOUT": {
    "name": "Payments and Checkout",
    "purpose": "Payment intent, checkout, payment method and payment link capability metadata."
  },
  "BILLING_AND_SUBSCRIPTIONS": {
    "name": "Billing and Subscriptions",
    "purpose": "Invoices, recurring billing, subscription lifecycle and tax configuration metadata."
  },
  "FINANCIAL_OPERATIONS": {
    "name": "Financial Operations",
    "purpose": "Payout, treasury, balance and financial reporting metadata."
  },
  "RISK_AND_DISPUTES": {
    "name": "Risk and Disputes",
    "purpose": "Fraud signals, disputes and refund lifecycle metadata."
  },
  "EVENTS_AND_WEBHOOKS": {
    "name": "Events and Webhooks",
    "purpose": "Event routing metadata; signature verification remains in the API security adapter."
  },
  "PRODUCT_CATALOG": {
    "name": "Product Catalog",
    "purpose": "Product and price reference metadata for commerce and billing."
  },
  "IN_PERSON_COMMERCE": {
    "name": "In-person Commerce",
    "purpose": "Terminal readers, locations and in-person payment capability metadata."
  },
  "ISSUING_AND_CARDS": {
    "name": "Issuing and Cards",
    "purpose": "Issuing eligibility, cardholder and card lifecycle metadata."
  },
  "CLIMATE_AND_EMERGING_RAILS": {
    "name": "Climate and Emerging Rails",
    "purpose": "Stripe Climate and crypto onramp eligibility and transaction-state metadata."
  }
}
def list_stripe_products(*,enabled_only=False):
 result=[]
 for child in get_stripe_core_catalog().get("children",[]):
  if enabled_only and not child.get("enabled",True): continue
  family=str(child.get("api_family",""))
  result.append({**child,"domain_id":DOMAIN_BY_FAMILY.get(family,"SPECIALTY_REVIEW_REQUIRED"),"readiness":child.get("status","CORE_CATALOG_ONLY"),"live_connection_verified":False})
 return result
def get_stripe_product(identifier):
 key=identifier.strip().casefold()
 if not key:return None
 for item in list_stripe_products():
  if key in {str(item.get("ecosystem_id","")).casefold(),str(item.get("module","")).casefold(),str(item.get("api_family","")).casefold()}:return dict(item)
 return None
def stripe_product_summary():
 products=list_stripe_products()
 return {"success":True,"provider":"stripe","product_count":len(products),"catalog_only_count":sum(p.get("readiness")=="CORE_CATALOG_ONLY" for p in products),"live_connections_verified":0,"products":[StripeCorePolicy.sanitize(p) for p in products]}
