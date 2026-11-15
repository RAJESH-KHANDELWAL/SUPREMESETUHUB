"""Canonical Apple provider-owned API ecosystem metadata.

Catalog metadata only. This module does not authenticate or make network requests.
"""
from __future__ import annotations

APPLE_API_ECOSYSTEM = {
    "provider_id": "apple",
    "name": "APPLE API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "platforms": [
        "Apple Developer", "App Store Connect", "App Store",
        "Apple Business Manager", "Apple Push Notification service",
        "Sign in with Apple", "StoreKit",
    ],
    "api_families": [
        "app_store_connect", "sign_in_with_apple", "apns", "storekit",
        "app_store_server_api", "apple_pay", "device_management",
        "icloud_and_cloudkit",
    ],
    "children": [
        {"id": "app_store_connect", "name": "APPLE APP STORE CONNECT API ECOSYSTEM", "folder": "apple_app_store_connect_api_ecosystem", "status": "catalog_only"},
        {"id": "sign_in_with_apple", "name": "APPLE SIGN IN WITH APPLE API ECOSYSTEM", "folder": "apple_sign_in_with_apple_api_ecosystem", "status": "catalog_only"},
        {"id": "apns", "name": "APPLE PUSH NOTIFICATION API ECOSYSTEM", "folder": "apple_push_notification_api_ecosystem", "status": "catalog_only"},
        {"id": "storekit", "name": "APPLE STOREKIT API ECOSYSTEM", "folder": "apple_storekit_api_ecosystem", "status": "catalog_only"},
        {"id": "app_store_server", "name": "APPLE APP STORE SERVER API ECOSYSTEM", "folder": "apple_app_store_server_api_ecosystem", "status": "catalog_only"},
        {"id": "apple_pay", "name": "APPLE PAY API ECOSYSTEM", "folder": "apple_pay_api_ecosystem", "status": "catalog_only"},
        {"id": "device_management", "name": "APPLE DEVICE MANAGEMENT API ECOSYSTEM", "folder": "apple_device_management_api_ecosystem", "status": "catalog_only"},
        {"id": "icloud_cloudkit", "name": "APPLE ICLOUD AND CLOUDKIT API ECOSYSTEM", "folder": "apple_icloud_cloudkit_api_ecosystem", "status": "catalog_only"},
    ],
    "related_ecosystems": [
        "APP", "COMPANIES", "DEVELOPER", "INTEGRATIONS",
        "PAYMENT", "PLATFORMS", "SECURITY", "SOFTWARE", "SYSTEM",
    ],
    "adapter_path": "backend/integrations/providers/apple.py",
    "credential_source": "environment_or_managed_secret_store",
}


def list_apple_api_ecosystems() -> dict[str, object]:
    """List Apple API family catalogs; this does not assert live connectivity."""
    children = [dict(item) for item in APPLE_API_ECOSYSTEM["children"]]
    return {
        "success": True,
        "provider": APPLE_API_ECOSYSTEM["name"],
        "status": APPLE_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }


__all__ = ["APPLE_API_ECOSYSTEM", "list_apple_api_ecosystems"]
