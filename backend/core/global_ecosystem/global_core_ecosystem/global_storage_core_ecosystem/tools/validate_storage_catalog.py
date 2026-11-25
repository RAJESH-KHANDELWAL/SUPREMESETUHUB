"""Offline consistency validator for the Global Storage Core catalog."""
from __future__ import annotations
from ..catalog import get_storage_core_catalog
from ..domain_catalog import DOMAIN_DEFINITIONS

def validate()->list[str]:
 c=get_storage_core_catalog(); errors=[]
 providers={p["provider_id"] for p in c["providers"]}
 domains=set(DOMAIN_DEFINITIONS)
 product_ids=set()
 for p in c["products"]:
  if p["provider_id"] not in providers: errors.append(f"UNKNOWN_PROVIDER:{p['product_id']}")
  if p["domain_id"] not in domains: errors.append(f"UNKNOWN_DOMAIN:{p['product_id']}")
  if p["product_id"] in product_ids: errors.append(f"DUPLICATE_PRODUCT:{p['product_id']}")
  product_ids.add(p["product_id"])
 if len(providers)!=len(c["providers"]): errors.append("DUPLICATE_PROVIDER")
 if len(domains)!=len(c["domains"]): errors.append("DOMAIN_COUNT_MISMATCH")
 return errors
if __name__=="__main__":
 problems=validate()
 if problems: raise SystemExit("\n".join(problems))
 catalog = get_storage_core_catalog()
 print(f"Storage catalog valid: {len(catalog["providers"])} providers, {len(product_ids)} products, {len(domains)} domains")
