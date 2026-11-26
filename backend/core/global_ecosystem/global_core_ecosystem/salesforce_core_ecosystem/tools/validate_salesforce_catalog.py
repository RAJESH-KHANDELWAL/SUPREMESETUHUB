"""Local consistency validator (no provider network calls)."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent))
from salesforce_core_ecosystem.catalog import list_products
from salesforce_core_ecosystem.domain_catalog import list_domains
def main():
 m=json.loads((ROOT/"ecosystem_manifest.json").read_text(encoding="utf-8")); p=list_products(); d=list_domains()
 assert len(p)==m["product_count"] and len(d)==m["domain_count"]
 assert len({x["product_id"] for x in p})==len(p)
 assert all(x["domain_id"] in {z["id"] for z in d} for x in p)
 print(f"Salesforce catalog valid: {len(p)} products / {len(d)} domains")
if __name__=="__main__": main()
