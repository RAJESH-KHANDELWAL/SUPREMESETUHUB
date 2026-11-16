"""Cloudflare Core product catalog; runtime Cloudflare catalog is authoritative."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from backend.global_ecosystem.global_cloudflare_ecosystem.catalog import (
    get_cloudflare_catalog,
    validate_cloudflare_catalog,
)

_ROOT = Path(__file__).resolve().parent
_PROVIDER = "cloudflare"


def get_cloudflare_core_catalog() -> dict[str, Any]:
    """Return detached Core product metadata derived from the provider catalog."""
    source = get_cloudflare_catalog()
    products = []
    for product in source["products"]:
        item = deepcopy(product)
        item["core_path"] = (
            f"backend/core/global_ecosystem/global_core_ecosystem/"
            f"global_cloudflare_core_ecosystem/{item['id']}_cloudflare_core_ecosystem"
        )
        item["ecosystem_id"] = f"CLOUDFLARE-{item['id'].upper()}-CORE-ECOSYSTEM"
        item["status"] = "CORE_CATALOG_ONLY"
        item["live_connection"] = False
        products.append(item)
    return {
        "ecosystem_id": "GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM",
        "name": "GLOBAL CLOUDFLARE CORE ECOSYSTEM",
        "provider": _PROVIDER,
        "status": "REGISTERED",
        "integration_status": source["integration_status"],
        "live_connection_verified": False,
        "runtime_source_of_record": (
            "backend/global_ecosystem/global_cloudflare_ecosystem/catalog.py"
        ),
        "products": products,
    }


def validate_cloudflare_core_catalog() -> tuple[str, ...]:
    """Validate provider catalog and canonical Core product package coverage."""
    errors = list(validate_cloudflare_catalog())
    catalog = get_cloudflare_core_catalog()
    ids = [item["id"] for item in catalog["products"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate Cloudflare Core product IDs")
    for item in catalog["products"]:
        package = _ROOT / f"{item['id']}_cloudflare_core_ecosystem"
        if not package.is_dir():
            errors.append(f"{item['id']} Core package is missing")
            continue
        manifest_path = package / "ecosystem_manifest.json"
        if not manifest_path.is_file():
            errors.append(f"{item['id']} Core manifest is missing")
    if catalog["live_connection_verified"] is not False:
        errors.append("Cloudflare Core must not claim live connection verification")
    return tuple(errors)


__all__ = ["get_cloudflare_core_catalog", "validate_cloudflare_core_catalog"]
