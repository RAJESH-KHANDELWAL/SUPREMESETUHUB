"""Deterministic registry for DeepSeek catalog capabilities."""
from __future__ import annotations
from .catalog import CAPABILITIES, get_catalog

def list_products() -> list[dict]:
    return get_catalog()["products"]

def list_capabilities() -> list[str]:
    return list(CAPABILITIES)

def get_product(product_id: str) -> dict | None:
    return next((item for item in list_products() if item["id"] == product_id), None)

__all__ = ["list_products", "list_capabilities", "get_product"]
