"""Cloudflare provider-owned API ecosystem metadata.

The AI, APP and CLOUD subpackages are catalog-only scaffolds. This module makes
no authentication or network requests.
"""
from __future__ import annotations

CLOUDFLARE_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "name": "GLOBAL CLOUDFLARE API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "purpose": "DNS, edge networking, security and developer platform APIs",
    "platforms_and_api_areas": [
        "Cloudflare dashboard",
        "DNS and zones",
        "Workers",
        "Workers AI and AI Gateway",
        "Pages and application APIs",
        "R2",
        "SSL/TLS and security APIs",
    ],
    "provider_owned_modules": {
        "AI": "backend/api/global_ecosystem/global_api_ecosystem/global_cloudflare_api_ecosystem/ai",
        "APP": "backend/api/global_ecosystem/global_api_ecosystem/global_cloudflare_api_ecosystem/app",
        "CLOUD": "backend/api/global_ecosystem/global_api_ecosystem/global_cloudflare_api_ecosystem/cloud",
    },
    "shared_category_paths": {
        "AI": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/cloudflare_ai_api_ecosystem",
        "APP": "backend/api/global_ecosystem/global_api_ecosystem/global_app_api_ecosystem/cloudflare_app_api_ecosystem",
        "CLOUD": "backend/api/global_ecosystem/global_api_ecosystem/global_cloud_api_ecosystem/cloudflare_cloud_api_ecosystem",
        "DOMAIN": "backend/api/global_ecosystem/global_api_ecosystem/global_domain_api_ecosystem/cloudflare_domain_api_ecosystem",
        "SECURITY": "backend/api/global_ecosystem/global_api_ecosystem/global_security_api_ecosystem/cloudflare_security_api_ecosystem",
        "SERVER": "backend/api/global_ecosystem/global_api_ecosystem/global_server_api_ecosystem/cloudflare_server_api_ecosystem",
        "VPS": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem/cloudflare_vps_api_ecosystem",
        "WEB": "backend/api/global_ecosystem/global_api_ecosystem/global_web_api_ecosystem/cloudflare_web_api_ecosystem",
    },
    "credential_source": "environment_or_managed_secret_store",
}
