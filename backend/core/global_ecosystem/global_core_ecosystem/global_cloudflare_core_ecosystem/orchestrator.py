"""Read-only Cloudflare product discovery and health orchestration."""
from __future__ import annotations

from typing import Any

from .catalog import get_cloudflare_core_catalog, validate_cloudflare_core_catalog
from .policy import CloudflareCorePolicy


class CloudflareCoreOrchestrator:
    def list_products(self, *, category: str | None = None) -> dict[str, Any]:
        products = get_cloudflare_core_catalog()["products"]
        if category is not None:
            products = [item for item in products if item["category"] == category]
        return {
            "success": True,
            "count": len(products),
            "products": [CloudflareCorePolicy.safe_product_summary(item) for item in products],
        }

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        key = str(product_id or "").strip().lower()
        for item in get_cloudflare_core_catalog()["products"]:
            if item["id"] == key:
                return CloudflareCorePolicy.safe_product_summary(item)
        return None

    def health(self) -> dict[str, Any]:
        catalog = get_cloudflare_core_catalog()
        errors = validate_cloudflare_core_catalog()
        return {
            "healthy": not errors,
            "provider": "cloudflare",
            "product_count": len(catalog["products"]),
            "catalog_errors": list(errors),
            "integration_status": catalog["integration_status"],
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "execution_performed": False,
            "persistence_performed": False,
        }

    def dependency_map(self) -> dict[str, str]:
        return {
            "core": "backend/core/global_ecosystem/global_core_ecosystem/global_cloudflare_core_ecosystem",
            "runtime_catalog": "backend/global_ecosystem/global_cloudflare_ecosystem/catalog.py",
            "api_adapter": "backend/global_ecosystem/global_cloudflare_ecosystem/client.py",
            "engine": "backend/engine (provider-neutral execution ownership)",
            "database": "backend/database (durable persistence ownership)",
            "storage": "backend/storage (asset persistence ownership)",
            "security_identity": "canonical SECURITY and IDENTITY layers",
        }


__all__ = ["CloudflareCoreOrchestrator"]
