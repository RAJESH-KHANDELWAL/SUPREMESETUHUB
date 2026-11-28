"""Product lookup and domain routing for the PayPal Core inventory."""
from __future__ import annotations
from typing import Any
from .catalog import get_paypal_core_catalog

def list_paypal_products() -> list[dict[str, Any]]:
    return get_paypal_core_catalog()["children"]

def get_paypal_product(ecosystem_id: str) -> dict[str, Any] | None:
    needle = ecosystem_id.strip().casefold()
    if not needle: return None
    for product in list_paypal_products():
        if needle in {product["ecosystem_id"].casefold(), product["package"].casefold(), product["name"].casefold()}:
            return product
    return None

def product_summary() -> dict[str, Any]:
    products = list_paypal_products()
    return {"count": len(products), "products": products}
