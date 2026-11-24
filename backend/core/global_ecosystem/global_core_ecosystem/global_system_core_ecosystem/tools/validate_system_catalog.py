"""Validate System Core provider, product and domain inventory invariants."""
from __future__ import annotations
from pathlib import Path
from ..catalog import list_system_providers
from ..domain_catalog import DOMAIN_DEFINITIONS, system_domain_summary
from ..product_catalog import list_system_products

ROOT = Path(__file__).resolve().parents[1]


def validate() -> dict[str, int]:
    providers = list_system_providers()
    products = list_system_products()
    provider_ids = [item["provider_id"] for item in providers]
    product_ids = [item["product_id"] for item in products]
    domains = DOMAIN_DEFINITIONS
    if len(provider_ids) != len(set(provider_ids)):
        raise ValueError("DUPLICATE_PROVIDER_ID")
    if len(product_ids) != len(set(product_ids)):
        raise ValueError("DUPLICATE_PRODUCT_ID")
    if not set(item["provider_id"] for item in products).issubset(set(provider_ids)):
        raise ValueError("PRODUCT_PROVIDER_NOT_REGISTERED")
    unknown_domains = {domain for item in products for domain in item.get("domain_ids", [])} - set(domains)
    if unknown_domains:
        raise ValueError(f"UNKNOWN_DOMAIN_IDS: {sorted(unknown_domains)}")
    for provider in providers:
        manager = ROOT / f'{provider["provider_id"]}_system_core_ecosystem' / "manager.py"
        if not manager.is_file():
            raise FileNotFoundError(f"PROVIDER_MANAGER_MISSING: {manager}")
    for domain_id in domains:
        manager = ROOT / f'global_{domain_id.lower()}_core_ecosystem' / "manager.py"
        if not manager.is_file():
            raise FileNotFoundError(f"DOMAIN_MANAGER_MISSING: {manager}")
    summary = system_domain_summary()
    if summary["unassigned_product_count"]:
        raise ValueError("UNASSIGNED_PRODUCTS_PRESENT")
    return {"providers": len(providers), "products": len(products), "domains": len(domains)}


if __name__ == "__main__":
    counts = validate()
    print("System Core catalog valid: " + ", ".join(f"{key}={value}" for key, value in counts.items()))
