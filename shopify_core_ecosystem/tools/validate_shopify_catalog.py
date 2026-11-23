import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/"ecosystem_manifest.json").read_text(encoding="utf-8"))
assert data["ecosystem_id"]=="SHOPIFY-CORE-ECOSYSTEM"
assert data["product_count"]==len(data["products"])==15
assert len({p["product_id"] for p in data["products"]})==15
for p in data["products"]:
 d=root/p["package_name"]
 assert (d/"__init__.py").is_file(), d
 assert (d/"manager.py").is_file(), d
print("Shopify Core catalog validation: PASS")
