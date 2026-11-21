"""Validate curated inventory consistency and provider facade coverage."""
import json
from pathlib import Path
from ..catalog import list_providers
from ..product_catalog import list_products
from ..domain_catalog import list_domains, DOMAIN_DEFINITIONS

def validate():
    root = Path(__file__).resolve().parents[1]
    idx = json.loads((root / "product_ecosystem_index.json").read_text())
    manifest = json.loads((root / "ecosystem_manifest.json").read_text())
    providers = list_providers()
    products = list_products()
    domains = list_domains()
    errors = []
    provider_ids = [item["provider_id"] for item in providers]
    product_ids = [item["product_id"] for item in products]
    if len(set(provider_ids)) != len(provider_ids):
        errors.append("DUPLICATE_PROVIDER_ID")
    if len(set(product_ids)) != len(product_ids):
        errors.append("DUPLICATE_PRODUCT_ID")
    if {item["provider_id"] for item in products} - set(provider_ids):
        errors.append("UNKNOWN_PRODUCT_PROVIDER")
    if idx.get("provider_count") != len(providers):
        errors.append("PRODUCT_INDEX_PROVIDER_COUNT_MISMATCH")
    if idx.get("product_family_count") != len(products):
        errors.append("PRODUCT_COUNT_MISMATCH")
    if manifest.get("provider_count") != len(providers):
        errors.append("MANIFEST_PROVIDER_COUNT_MISMATCH")
    if manifest.get("product_family_count") != len(products):
        errors.append("MANIFEST_PRODUCT_COUNT_MISMATCH")
    if {item["provider_id"] for item in manifest.get("providers", [])} != set(provider_ids):
        errors.append("MANIFEST_PROVIDER_SET_MISMATCH")
    if len(domains) != len(DOMAIN_DEFINITIONS) or manifest.get("domain_count") != len(domains):
        errors.append("DOMAIN_COUNT_MISMATCH")
    for provider in providers:
        manager_path = root / f"{provider['provider_id']}_tools_core_ecosystem" / "manager.py"
        if not manager_path.is_file():
            errors.append(f"MISSING_PROVIDER_MANAGER:{provider['provider_id']}")
    return {
        "success": not errors,
        "provider_count": len(providers),
        "product_family_count": len(products),
        "domain_count": len(domains),
        "errors": errors,
    }

if __name__ == "__main__":
    import sys
    result = validate()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["success"] else 1)
