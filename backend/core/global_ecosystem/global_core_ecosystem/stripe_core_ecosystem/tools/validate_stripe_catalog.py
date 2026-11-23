"""Validate Stripe Core packages and security boundaries."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/"ecosystem_manifest.json").read_text())
assert manifest["product_family_count"]==22 and manifest["domain_count"]==10
for item in manifest["products"]:
 package=ROOT/item["package_name"]
 for filename in ("__init__.py","catalog.py","manager.py","README.md"):assert (package/filename).is_file(),f"{item['package_name']}/{filename}"
assert (ROOT/"manager.py").is_file() and (ROOT/"manager.php").is_file()
assert (ROOT/"stripe_php_core_ecosystem"/"StripeCoreContract.php").is_file()
assert manifest["security"]["live_connection_verified"] is False and manifest["security"]["api_transport_in_core"] is False
print("Stripe Core validation passed: 22 product managers, 10 domains, PHP contract and security boundaries.")
