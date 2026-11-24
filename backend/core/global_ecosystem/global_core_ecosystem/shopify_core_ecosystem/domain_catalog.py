"""Product-to-domain grouping."""
from .product_catalog import PRODUCTS
def list_domains():
    grouped={}
    for p in PRODUCTS: grouped.setdefault(p["domain_id"],[]).append(p["product_id"])
    return [{"domain_id":k,"product_ids":sorted(v)} for k,v in sorted(grouped.items())]
