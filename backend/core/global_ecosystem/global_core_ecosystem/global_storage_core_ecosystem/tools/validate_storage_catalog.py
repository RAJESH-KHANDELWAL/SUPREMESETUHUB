"""Offline consistency validator for the Global Storage Core catalog."""
from __future__ import annotations
from ..catalog import get_storage_core_catalog
from ..domain_catalog import DOMAIN_DEFINITIONS

def validate() -> list[str]:
    catalog = get_storage_core_catalog()
    errors = []
    providers = {provider["provider_id"] for provider in catalog["providers"]}
    domains = set(DOMAIN_DEFINITIONS)
    product_ids = set()

    for product in catalog["products"]:
        if product["provider_id"] not in providers:
            errors.append(f"UNKNOWN_PROVIDER:{product['product_id']}")
        if product["domain_id"] not in domains:
            errors.append(f"UNKNOWN_DOMAIN:{product['product_id']}")
        if product["product_id"] in product_ids:
            errors.append(f"DUPLICATE_PRODUCT:{product['product_id']}")
        product_ids.add(product["product_id"])

    if len(providers) != len(catalog["providers"]):
        errors.append("DUPLICATE_PROVIDER")
    if len(domains) != len(catalog["domains"]):
        errors.append("DOMAIN_COUNT_MISMATCH")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        raise SystemExit("\n".join(problems))
    catalog = get_storage_core_catalog()
    print(
        f"Storage catalog valid: {len(catalog['providers'])} providers, "
        f"{len(catalog['products'])} products, {len(catalog['domains'])} domains"
    )
