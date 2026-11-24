"""Google product catalog facade in the canonical global Google ecosystem.

The canonical implementation lives in backend/global_ecosystem/google_ecosystem/runtime/service.py.
This file is a script/facade; Python package imports should use
backend.global_ecosystem.google_ecosystem.runtime.
"""
from __future__ import annotations

from typing import Any

from backend.global_ecosystem.google_ecosystem.runtime.service import GOOGLE_PRODUCTS, GoogleEcosystemService

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
