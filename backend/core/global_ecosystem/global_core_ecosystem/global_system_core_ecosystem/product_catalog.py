"""Canonical operating-system and system-platform inventory."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_INDEX_PATH = Path(__file__).with_name("product_ecosystem_index.json")


def list_system_products(*, provider_id: str | None = None, enabled_only: bool = False) -> list[dict[str, Any]]:
    payload = json.loads(_INDEX_PATH.read_text(encoding="utf-8"))
    products = payload["products"]
    if provider_id:
        needle = provider_id.strip().casefold()
        products = [item for item in products if item["provider_id"].casefold() == needle]
    if enabled_only:
        products = [item for item in products if item.get("enabled", True)]
    return products


def get_system_product(product_id: str) -> dict[str, Any] | None:
    needle = product_id.strip().casefold()
    if not needle:
        return None
    return next((item for item in list_system_products() if item["product_id"].casefold() == needle), None)


def system_products_summary() -> dict[str, Any]:
    products = list_system_products()
    providers = sorted({item["provider_id"] for item in products})
    return {
        "success": True,
        "product_count": len(products),
        "provider_count": len(providers),
        "live_connections_verified": 0,
        "products": products,
        "scope_note": "Curated system-platform inventory; not an exhaustive list of every distribution, release or hardware image.",
    }
