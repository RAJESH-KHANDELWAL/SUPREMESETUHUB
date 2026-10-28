"""Apple provider-owned API ecosystem metadata.

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
        "Apple Business Manager", "iCloud developer capabilities"
    ],
    "api_families": [
        "app_store_connect", "sign_in_with_apple", "apns",
        "storekit", "app_distribution", "apple_pay_eligible_integrations",
        "device_management"
    ],
    "related_ecosystems": [
        "APP", "COMPANIES", "DEVELOPER", "INTEGRATIONS",
        "PAYMENT", "PLATFORMS", "SECURITY", "SYSTEM"
    ],
    "adapter_path": "backend/integrations/providers/apple.py",
    "credential_source": "environment_or_managed_secret_store",
}
