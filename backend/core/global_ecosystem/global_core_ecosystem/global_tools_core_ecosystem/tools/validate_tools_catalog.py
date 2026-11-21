"""Validate curated inventory consistency."""
import json
from pathlib import Path
from ..catalog import list_providers
from ..product_catalog import list_products
from ..domain_catalog import list_domains,DOMAIN_DEFINITIONS
def validate():
 root=Path(__file__).resolve().parents[1]; idx=json.loads((root/"product_ecosystem_index.json").read_text())
 p=list_providers(); r=list_products(); d=list_domains(); e=[]
 if len({x["provider_id"] for x in p})!=len(p): e.append("DUPLICATE_PROVIDER_ID")
 if len({x["product_id"] for x in r})!=len(r): e.append("DUPLICATE_PRODUCT_ID")
 if {x["provider_id"] for x in r}-{x["provider_id"] for x in p}: e.append("UNKNOWN_PRODUCT_PROVIDER")
 if idx["product_family_count"]!=len(r): e.append("PRODUCT_COUNT_MISMATCH")
 if len(d)!=len(DOMAIN_DEFINITIONS): e.append("DOMAIN_COUNT_MISMATCH")
 return {"success":not e,"provider_count":len(p),"product_family_count":len(r),"domain_count":len(d),"errors":e}
if __name__=="__main__":
 import sys
 x=validate(); print(json.dumps(x,indent=2)); sys.exit(0 if x["success"] else 1)
