"""Hostinger service catalog for the SUPREMESETUHUB infrastructure control plane.

This module describes publicly documented Hostinger service categories. It does
not claim that an account is connected, that a plan is purchased, or that an
API can provision every service. Live actions must be added only against
documented, authorized Hostinger APIs and tested credentials.
"""
from __future__ import annotations

import os
from typing import Any

HOSTINGER_PROVIDER_ID = "hostinger"
HOSTINGER_PROVIDER_NAME = "Hostinger"

HOSTINGER_SERVICES: list[dict[str, Any]] = [
    {
        "service_id": "domain_registration",
        "name": "Domain Registration",
        "category": "domains",
        "description": "Search, register and manage eligible domain names and extensions.",
        "url": "https://www.hostinger.com/in/domains",
        "capabilities": ["domain_search", "registration", "renewal", "domain_management"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "domain_transfer",
        "name": "Domain Transfer",
        "category": "domains",
        "description": "Transfer an eligible existing domain to Hostinger, subject to transfer rules.",
        "url": "https://www.hostinger.com/in/domains",
        "capabilities": ["transfer_eligibility", "transfer_workflow"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "dns_management",
        "name": "DNS and Nameserver Management",
        "category": "domains_dns",
        "description": "Manage DNS records and nameservers in the Hostinger account control panel.",
        "url": "https://www.hostinger.com/",
        "capabilities": ["dns_records", "nameservers", "domain_connection"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "shared_web_hosting",
        "name": "Web Hosting",
        "category": "web_hosting",
        "description": "Managed shared hosting for websites and small business projects.",
        "url": "https://www.hostinger.com/in/web-hosting",
        "capabilities": ["website_files", "php_websites", "database_hosting", "ssl_options"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "wordpress_hosting",
        "name": "WordPress Hosting",
        "category": "web_hosting",
        "description": "Hosting and management tools for WordPress websites.",
        "url": "https://www.hostinger.com/in/wordpress-hosting",
        "capabilities": ["wordpress_installation", "website_management", "backup_options"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "woocommerce_hosting",
        "name": "WooCommerce / Online Store Hosting",
        "category": "ecommerce",
        "description": "Hosting options for eligible WordPress and WooCommerce storefronts.",
        "url": "https://www.hostinger.com/in/woocommerce-hosting",
        "capabilities": ["wordpress_storefront", "ecommerce_site_hosting"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "cloud_hosting",
        "name": "Cloud Hosting",
        "category": "cloud_hosting",
        "description": "Managed cloud hosting plans for growing websites and stores.",
        "url": "https://www.hostinger.com/in/cloud-hosting",
        "capabilities": ["managed_cloud_environment", "scalable_web_hosting"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "vps_hosting",
        "name": "VPS Hosting",
        "category": "compute",
        "description": "Virtual private servers for workloads that need more control over the runtime.",
        "url": "https://www.hostinger.com/in/vps-hosting",
        "capabilities": ["virtual_server", "server_administration", "docker_deployment"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "website_builder",
        "name": "Website Builder and AI Website Creation",
        "category": "website_tools",
        "description": "Visual and AI-assisted tools for creating and publishing websites.",
        "url": "https://www.hostinger.com/in/website-builder",
        "capabilities": ["visual_site_building", "templates", "publish_website"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "business_email",
        "name": "Business Email",
        "category": "email",
        "description": "Domain-based email plans and mailbox management.",
        "url": "https://www.hostinger.com/in/business-email",
        "capabilities": ["domain_mailboxes", "email_client_setup", "email_migration_options"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "ssl",
        "name": "SSL Certificates and HTTPS",
        "category": "security",
        "description": "SSL/TLS options associated with eligible hosting and domain plans.",
        "url": "https://www.hostinger.com/",
        "capabilities": ["https_enablement", "certificate_management_options"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "cdn_and_performance",
        "name": "CDN and Website Performance",
        "category": "performance",
        "description": "CDN and performance features where included or available for the selected plan.",
        "url": "https://www.hostinger.com/in/web-hosting",
        "capabilities": ["cdn_options", "performance_features"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "backups_and_restore",
        "name": "Backups and Restore",
        "category": "reliability",
        "description": "Backup and restore features according to the selected hosting plan.",
        "url": "https://www.hostinger.com/in/web-hosting",
        "capabilities": ["backup_options", "restore_options"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "website_migration",
        "name": "Website Migration",
        "category": "migration",
        "description": "Migration options for eligible websites and hosting plans.",
        "url": "https://www.hostinger.com/",
        "capabilities": ["website_migration_options"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "email_marketing",
        "name": "Email Marketing",
        "category": "marketing",
        "description": "Email marketing tools and plans where offered for the account and region.",
        "url": "https://www.hostinger.com/",
        "capabilities": ["campaign_management_options", "marketing_analytics_options"],
        "integration_status": "CATALOG_ONLY",
    },
    {
        "service_id": "hostinger_agent",
        "name": "Hostinger Agent and Hosting Tools",
        "category": "management_tools",
        "description": "Hostinger's account-level AI assistance and management tools, subject to availability.",
        "url": "https://www.hostinger.com/",
        "capabilities": ["guided_hosting_management", "website_workflows"],
        "integration_status": "CATALOG_ONLY",
    },
]


def hostinger_catalog() -> dict[str, Any]:
    """Return a non-sensitive, stable catalog without inventing live connectivity."""
    return {
        "success": True,
        "provider_id": HOSTINGER_PROVIDER_ID,
        "provider_name": HOSTINGER_PROVIDER_NAME,
        "provider_role": "DOMAIN_REGISTRAR_AND_HOSTING_PROVIDER",
        "catalog_status": "AVAILABLE",
        "account_connection_status": "NOT_VERIFIED",
        "live_provisioning_enabled": False,
        "service_count": len(HOSTINGER_SERVICES),
        "services": HOSTINGER_SERVICES,
        "notes": [
            "Service availability and included features vary by country, plan and account.",
            "Prices and promotional offers are intentionally not hard-coded because they change.",
            "Catalog entries are not proof that a domain or hosting plan is purchased or connected.",
            "Live provisioning must use supported official APIs or an explicitly configured, authorized deployment workflow.",
        ],
    }


def hostinger_readiness() -> dict[str, Any]:
    """Report only whether optional deployment settings exist; never expose values."""
    required = {
        "hostinger_api_key_present": "HOSTINGER_API_KEY",
        "hostinger_vps_id_present": "HOSTINGER_VPS_ID",
    }
    checks = {
        public_name: bool(os.getenv(env_name, "").strip())
        for public_name, env_name in required.items()
    }
    return {
        "success": True,
        "provider_id": HOSTINGER_PROVIDER_ID,
        "status": "CONFIGURATION_PRESENT_NOT_CONNECTION_VERIFIED"
        if all(checks.values())
        else "CATALOG_ONLY_NEEDS_ACCOUNT_CONFIGURATION",
        "settings_present": checks,
        "secrets_returned": False,
        "live_api_test_performed": False,
        "live_provisioning_enabled": False,
        "note": (
            "Environment-variable presence is not proof of valid credentials or a successful API connection. "
            "This catalog does not provision domains, hosting plans, DNS, email or servers."
        ),
    }
