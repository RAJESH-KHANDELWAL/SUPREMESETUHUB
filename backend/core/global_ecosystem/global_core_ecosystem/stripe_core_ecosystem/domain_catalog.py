"""Ten Stripe Core responsibility domains."""
from collections import Counter
from .product_catalog import DOMAIN_DEFINITIONS,list_stripe_products
def list_stripe_domains():
 products=list_stripe_products();counts=Counter(p["domain_id"] for p in products)
 return [{"domain_id":k,**v,"product_count":counts.get(k,0),"products":[p["api_family"] for p in products if p["domain_id"]==k]} for k,v in DOMAIN_DEFINITIONS.items()]
def stripe_domain_summary():
 domains=list_stripe_domains()
 return {"success":True,"domain_count":len(domains),"product_count":sum(d["product_count"] for d in domains),"domains":domains,"live_connections_verified":0,"note":"Classification is metadata only; merchant eligibility, authorization and live connectivity must be verified separately."}
