"""IBM provider-owned API ecosystem metadata.

This module declares catalog scope only. It performs no authentication,
network requests, entitlement checks, or live-connectivity verification.
"""
from __future__ import annotations

IBM_API_ECOSYSTEM = {
    "provider_id": "ibm",
    "name": "IBM API ECOSYSTEM",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "purpose": "IBM enterprise AI, cloud, data, language, business, security and infrastructure API catalog",
    "platforms_and_api_areas": [
        "IBM Cloud",
        "watsonx and other documented IBM AI services",
        "IBM Db2 and supported data-platform APIs",
        "IBM language, speech and translation APIs where currently offered",
        "IBM enterprise and business-platform APIs",
        "IBM security, identity and access-related APIs",
        "IBM Cloud infrastructure and operations APIs",
    ],
    "families": ["AI", "CLOUD", "DATABASE", "LANGUAGE", "BUSINESS", "SECURITY", "VPS"],
    "related_ecosystems": ["AI", "CLOUD", "DATABASE", "LANGUAGE", "BUSINESS", "SECURITY", "VPS"],
    "credential_source": "environment_or_managed_secret_store",
    "official_references": [
        "https://www.ibm.com/",
        "https://www.ibm.com/cloud",
        "https://www.ibm.com/docs/",
        "https://cloud.ibm.com/apidocs",
    ],
}
