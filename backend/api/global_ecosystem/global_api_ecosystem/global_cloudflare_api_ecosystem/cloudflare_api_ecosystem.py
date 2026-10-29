"""Cloudflare provider-owned API ecosystem metadata.

This is the provider-specific catalog index. Shared AI, APP, CLOUD and other
category mappings remain in their respective GLOBAL API ECOSYSTEM families.
Catalog metadata only; no authentication or network requests are performed.
"""
from __future__ import annotations

CLOUDFLARE_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "name": "GLOBAL CLOUDFLARE API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "purpose": "Cloudflare-specific platform, edge, networking, DNS, security, and developer APIs",
    "platforms_and_api_areas": [
        "Cloudflare account and account-level APIs",
        "Zones and zone settings",
        "DNS records",
        "Workers",
        "Workers AI and AI Gateway",
        "Pages",
        "R2 object storage",
        "SSL/TLS",
        "Security and WAF",
    ],
    "related_ecosystem_families": [
        "AI",
        "APP",
        "CLOUD",
        "DOMAIN",
        "DNS",
        "SECURITY",
        "SERVER",
        "VPS",
        "WEB",
    ],
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
    "dns_implementation_path": "backend/dns/global_ecosystem/global_dns_ecosystem/cloudflare_dns",
    "credential_source": "environment_or_managed_secret_store",
}
