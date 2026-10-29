"""Cloudflare provider-owned API ecosystem metadata.

This index covers Cloudflare-specific product APIs and documented cross-provider
integration catalogs. Shared AI, APP, CLOUD, and other family mappings live in
their respective GLOBAL API ECOSYSTEM directories. Catalog metadata only.
"""
from __future__ import annotations

CLOUDFLARE_API_ECOSYSTEM = {
    "provider_id": "cloudflare",
    "name": "GLOBAL CLOUDFLARE API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "purpose": "Cloudflare-specific product APIs, edge/networking, DNS, security, developer platform, and documented provider integrations",
    "product_api_catalog": "cloudflare_product_api_catalog.py",
    "product_api_modules": {
        "accounts": "accounts_cloudflare_api_ecosystem/accounts_cloudflare_api_ecosystem.py",
        "zones": "zones_cloudflare_api_ecosystem/zones_cloudflare_api_ecosystem.py",
        "dns": "dns_cloudflare_api_ecosystem/dns_cloudflare_api_ecosystem.py",
        "workers": "workers_cloudflare_api_ecosystem/workers_cloudflare_api_ecosystem.py",
        "pages": "pages_cloudflare_api_ecosystem/pages_cloudflare_api_ecosystem.py",
        "r2": "r2_cloudflare_api_ecosystem/r2_cloudflare_api_ecosystem.py",
        "ai_gateway": "ai_gateway_cloudflare_api_ecosystem/ai_gateway_cloudflare_api_ecosystem.py",
        "security": "security_cloudflare_api_ecosystem/security_cloudflare_api_ecosystem.py",
        "ssl_tls": "ssl_tls_cloudflare_api_ecosystem/ssl_tls_cloudflare_api_ecosystem.py",
        "analytics_logpush": "analytics_logpush_cloudflare_api_ecosystem/analytics_logpush_cloudflare_api_ecosystem.py",
    },
    "official_api_reference": "https://developers.cloudflare.com/api/",
    "authentication_reference": "https://developers.cloudflare.com/fundamentals/api/get-started/",
    "platforms_and_api_areas": [
        "Accounts and account settings",
        "Zones and zone settings",
        "DNS records",
        "Workers and developer platform",
        "Pages deployments",
        "R2 object storage",
        "Workers AI and AI Gateway",
        "SSL/TLS",
        "Security, WAF, and rulesets",
        "Analytics and Logpush",
    ],
    "related_ecosystem_families": [
        "AI",
        "APP",
        "CLOUD",
        "DOMAIN",
        "DNS",
        "SECURITY",
        "SERVER",
        "WEB",
        "VPS",
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
    "provider_integration_index": "backend/api/global_ecosystem/global_api_ecosystem/global_cloudflare_api_ecosystem/cloudflare_provider_integrations.py",
    "provider_integration_modules": {
        "AWS": "aws_cloudflare_api_ecosystem.py",
        "GOOGLE_CLOUD": "google_cloud_cloudflare_api_ecosystem.py",
        "MICROSOFT_AZURE": "microsoft_azure_cloudflare_api_ecosystem.py",
        "ORACLE_CLOUD": "oracle_cloud_cloudflare_api_ecosystem.py",
        "ALIBABA_CLOUD": "alibaba_cloud_cloudflare_api_ecosystem.py",
    },
    "dns_implementation_path": "backend/dns/global_ecosystem/global_dns_ecosystem/cloudflare_dns",
    "credential_source": "environment_or_managed_secret_store",
}
