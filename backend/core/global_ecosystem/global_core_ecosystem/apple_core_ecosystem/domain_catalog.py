"""Apple Core domain taxonomy and product-family routing."""
from __future__ import annotations
from typing import Any
from .product_catalog import list_apple_offerings
DOMAIN_DEFINITIONS={
 "APP_STORE_AND_DISTRIBUTION":{"name":"App Store and Distribution","purpose":"App Store Connect metadata and app lifecycle boundaries."},
 "APP_STORE_COMMERCE":{"name":"App Store Commerce","purpose":"App Store Server transaction and subscription state."},
 "DEVICE_MANAGEMENT":{"name":"Device Management","purpose":"Apple device enrollment and management policy metadata."},
 "CLOUD_DATA":{"name":"Cloud Data and Sync","purpose":"iCloud CloudKit container, schema and subscription metadata."},
 "PAYMENTS_AND_COMMERCE":{"name":"Payments and In-App Commerce","purpose":"Apple Pay merchant/payment handoff and StoreKit purchase lifecycle."},
 "IDENTITY_AND_NOTIFICATIONS":{"name":"Identity and Notifications","purpose":"Sign in with Apple identity and APNs notification metadata."}}
PRODUCT_DOMAIN={"app_store_connect":"APP_STORE_AND_DISTRIBUTION","app_store_server":"APP_STORE_COMMERCE","device_management":"DEVICE_MANAGEMENT","icloud_cloudkit":"CLOUD_DATA","apple_pay":"PAYMENTS_AND_COMMERCE","push_notification":"IDENTITY_AND_NOTIFICATIONS","sign_in_with_apple":"IDENTITY_AND_NOTIFICATIONS","storekit":"PAYMENTS_AND_COMMERCE"}
def list_apple_domain_inventory()->list[dict[str,Any]]:
 return [{"domain_id":d,"name":m["name"],"purpose":m["purpose"],"product_ids":[p for p,v in PRODUCT_DOMAIN.items() if v==d],"product_count":sum(v==d for v in PRODUCT_DOMAIN.values())} for d,m in DOMAIN_DEFINITIONS.items()]
def apple_domain_summary()->dict[str,Any]:
 domains=list_apple_domain_inventory()
 return {"success":True,"provider":"apple","domain_count":len(domains),"offering_count":sum(x["product_count"] for x in domains),"domains":domains,"live_connections_verified":0}
