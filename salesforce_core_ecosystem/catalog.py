"""Product catalog lookup helpers."""
from .product_catalog import PRODUCTS
def list_products(enabled_only=False):
    result=[dict(p) for p in PRODUCTS]
    return [p for p in result if p["enabled"]] if enabled_only else result
def get_product(product_id):
    target=str(product_id).strip().upper()
    for p in PRODUCTS:
        if target in (p["product_id"].upper(),p["slug"].upper()): return dict(p)
    return None
