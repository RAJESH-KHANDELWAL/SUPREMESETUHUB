"""Google Ecosystem facade beside the backend/google/google_ecosystem/ folder."""
from __future__ import annotations

from typing import Any

from .google_ecosystem.service import GOOGLE_PRODUCTS, GoogleEcosystemService

_service = GoogleEcosystemService()


def list_products() -> list[dict[str, Any]]:
    return _service.catalog()


def get_product(product_id: str) -> dict[str, Any] | None:
    return _service.get_product(product_id)


def get_status() -> dict[str, Any]:
    return _service.status()


__all__ = ["GOOGLE_PRODUCTS", "GoogleEcosystemService", "list_products", "get_product", "get_status"]
