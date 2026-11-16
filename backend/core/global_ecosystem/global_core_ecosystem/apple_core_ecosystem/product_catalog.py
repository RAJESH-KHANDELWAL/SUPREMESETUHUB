"""Canonical Apple product inventory from the Core registry."""
from __future__ import annotations
from typing import Any
from .catalog import list_apple_core_modules
_PRODUCTS=[{"id":"app_store_connect","name":"App Store Connect","category":"APP_STORE_MANAGEMENT"},{"id":"app_store_server","name":"App Store Server","category":"APP_STORE_COMMERCE"},{"id":"device_management","name":"Apple Device Management","category":"DEVICE_MANAGEMENT"},{"id":"icloud_cloudkit","name":"iCloud CloudKit","category":"CLOUD_DATA"},{"id":"apple_pay","name":"Apple Pay","category":"PAYMENTS"},{"id":"push_notification","name":"Apple Push Notification Service","category":"NOTIFICATIONS"},{"id":"sign_in_with_apple","name":"Sign in with Apple","category":"IDENTITY"},{"id":"storekit","name":"StoreKit","category":"IN_APP_COMMERCE"}]
def list_apple_offerings()->list[dict[str,Any]]:
 by_id={x["id"]:x for x in _PRODUCTS}
 return [{"id":x["ecosystem_id"].removeprefix("APPLE-").removesuffix("-CORE-ECOSYSTEM").lower().replace("-","_"),"name":by_id[x["ecosystem_id"].removeprefix("APPLE-").removesuffix("-CORE-ECOSYSTEM").lower().replace("-","_")]["name"],"category":by_id[x["ecosystem_id"].removeprefix("APPLE-").removesuffix("-CORE-ECOSYSTEM").lower().replace("-","_")]["category"],"core_ecosystem_id":x["ecosystem_id"],"api_catalog_ref":x["api_catalog_ref"],"api_available":None,"live_connection_verified":False,"status":x["status"]} for x in list_apple_core_modules()]
def apple_offerings_summary()->dict[str,Any]:
 offerings=list_apple_offerings()
 return {"success":True,"provider":"apple","offering_count":len(offerings),"live_connections_verified":0,"api_availability":"NOT_VERIFIED","note":"Core registration does not establish API availability, entitlement, authentication or live connectivity.","offerings":offerings}
