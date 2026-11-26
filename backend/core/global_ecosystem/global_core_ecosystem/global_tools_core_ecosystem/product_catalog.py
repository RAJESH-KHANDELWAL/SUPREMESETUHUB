"""Read-only product family discovery."""
import json
from pathlib import Path
def list_products(provider_id=None,category=None):
 r=json.loads(Path(__file__).with_name("product_ecosystem_index.json").read_text())["product_ecosystems"]
 if provider_id: r=[x for x in r if x["provider_id"]==provider_id.strip().casefold()]
 if category: r=[x for x in r if x["category"]==category.strip().upper()]
 return r
def get_product(product_id):
 k=product_id.strip().casefold(); return next((x for x in list_products() if x["product_id"]==k),None)
