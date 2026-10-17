"""Python entry point alongside the lowercase Google folder.

The canonical product catalog lives in google_ecosystem.service. This facade
makes it available from backend.google.google without duplicating catalog data.
It does not authenticate to Google or perform live Gmail/Drive operations.
"""
from __future__ import annotations

from typing import Any

from .google_ecosystem.service import GOOGLE_PRODUCTS, GoogleEcosystemService

_service = GoogleEcosystemService()


def list_products() -> list[dict[str, Any]]:
    """Return metadata for Gmail, Drive, and other registered Google products."""
    return _service.catalog()


def get_product(product_id: str) -> dict[str, Any] | None:
    """Return metadata for a product ID such as 'gmail' or 'drive'."""
    return _service.get_product(product_id)


def get_status() -> dict[str, Any]:
    """Return implementation/configuration status, not live connectivity."""
    return _service.status()


__all__ = [
    "GOOGLE_PRODUCTS",
    "GoogleEcosystemService",
    "get_product",
    "get_status",
    "list_products",
]
