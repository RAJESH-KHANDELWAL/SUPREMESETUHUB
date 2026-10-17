"""Top-level Google entry point beside the backend/google/ package directory.

The canonical implementation remains in backend/google/google_ecosystem/service.py.
This file is a script/facade; Python package imports should use
backend.google.google_ecosystem directly because the sibling package directory
and this same-named module share the name 'google'.
"""
from __future__ import annotations

from typing import Any

from backend.google.google_ecosystem.service import GOOGLE_PRODUCTS, GoogleEcosystemService

_service = GoogleEcosystemService()


def list_products() -> list[dict[str, Any]]:
    return _service.catalog()


def get_product(product_id: str) -> dict[str, Any] | None:
    return _service.get_product(product_id)


def get_status() -> dict[str, Any]:
    return _service.status()


if __name__ == "__main__":
    import json
    print(json.dumps(get_status(), indent=2))


__all__ = ["GOOGLE_PRODUCTS", "GoogleEcosystemService", "list_products", "get_product", "get_status"]
