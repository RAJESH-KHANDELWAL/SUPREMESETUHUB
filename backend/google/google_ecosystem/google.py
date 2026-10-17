"""Python entry point for the lowercase Google ecosystem package.

This module exposes the existing catalog as a stable import path. It does not
authenticate to Google or perform Gmail/Drive operations; live API access must
be added through consent-based, least-privilege provider adapters.
"""
from __future__ import annotations

from typing import Any

from .service import GOOGLE_PRODUCTS, GoogleEcosystemService

_service = GoogleEcosystemService()


def list_products() -> list[dict[str, Any]]:
    """Return catalog metadata for Gmail, Drive, and other Google services."""
    return _service.catalog()


def get_product(product_id: str) -> dict[str, Any] | None:
    """Return metadata for one product ID, e.g. 'gmail' or 'drive'."""
    return _service.get_product(product_id)


def get_status() -> dict[str, Any]:
    """Return configuration/implementation status without claiming connectivity."""
    return _service.status()


__all__ = [
    "GOOGLE_PRODUCTS",
    "GoogleEcosystemService",
    "get_product",
    "get_status",
    "list_products",
]
