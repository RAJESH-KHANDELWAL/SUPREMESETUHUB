"""Provider and sub-ecosystem registry for GLOBAL API ECOSYSTEM.

Catalog metadata is intentionally distinct from a live integration. Each provider
record points to the existing code area where one is known and reports whether
the project currently has a provider-specific readiness scaffold or only catalog
coverage. No credentials or account data are stored here.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any


GLOBAL_API_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {"ecosystem_id": "AI", "name": "GLOBAL AI API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem", "purpose": "AI models, inference, generation and AI service APIs"},
    {"ecosystem_id": "APP", "name": "GLOBAL APP API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_app_api_ecosystem", "purpose": "Application platforms and app lifecycle APIs"},
    {"ecosystem_id": "BUSINESS", "name": "GLOBAL BUSINESS API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_business_api_ecosystem", "purpose": "Business, commerce and enterprise APIs"},
    {"ecosystem_id": "CLOUD", "name": "GLOBAL CLOUD API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_cloud_api_ecosystem", "purpose": "Cloud infrastructure, compute, networking and operations"},
    {"ecosystem_id": "COMMUNICATION", "name": "GLOBAL COMMUNICATION API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_communication_api_ecosystem", "purpose": "Messaging, email, meetings, voice and communication APIs"},
    {"ecosystem_id": "COMPANIES", "name": "GLOBAL COMPANIES API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_companies_api_ecosystem", "purpose": "Company and vendor-specific ecosystems including Google, Microsoft, AWS and Apple"},
    {"ecosystem_id": "DATABASE", "name": "GLOBAL DATABASE API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_database_api_ecosystem", "purpose": "Database, query, replication and data-platform APIs"},
    {"ecosystem_id": "DEVELOPER", "name": "GLOBAL DEVELOPER API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_developer_api_ecosystem", "purpose": "Source control, CI/CD, developer tools and software delivery APIs"},
    {"ecosystem_id": "DOMAIN", "name": "GLOBAL DOMAIN API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_domain_api_ecosystem", "purpose": "Domains, DNS, certificates and registrar APIs"},
    {"ecosystem_id": "FREELANCER", "name": "GLOBAL FREELANCER API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_freelancer_api_ecosystem", "purpose": "Freelance work, marketplaces and professional workflow APIs"},
    {"ecosystem_id": "HOSTING", "name": "GLOBAL HOSTING API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_hosting_api_ecosystem", "purpose": "Hosting providers, deployments and web infrastructure APIs"},
    {"ecosystem_id": "INDIVIDUAL", "name": "GLOBAL INDIVIDUAL API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_individual_api_ecosystem", "purpose": "Individual identity, profiles and personal productivity APIs"},
    {"ecosystem_id": "INTEGRATIONS", "name": "GLOBAL INTEGRATIONS API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_integrations_api_ecosystem", "purpose": "Cross-provider connectors, integration lifecycle and common adapters"},
    {"ecosystem_id": "INTIMACY", "name": "GLOBAL INTIMACY API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_intimacy_api_ecosystem", "purpose": "Its separately scoped product and service APIs"},
    {"ecosystem_id": "LANGUAGE", "name": "GLOBAL LANGUAGE API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_language_api_ecosystem", "purpose": "Translation, speech, language and localization APIs"},
    {"ecosystem_id": "PAYMENT", "name": "GLOBAL PAYMENT API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_payment_api_ecosystem", "purpose": "Payment processors, payouts, billing and financial APIs"},
    {"ecosystem_id": "PLATFORMS", "name": "GLOBAL PLATFORMS API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_platforms_api_ecosystem", "purpose": "Consumer and business platforms, including Google Workspace, Google Play, Microsoft 365, Apple App Store and AWS Console"},
    {"ecosystem_id": "SECURITY", "name": "GLOBAL SECURITY API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_security_api_ecosystem", "purpose": "Identity, access, security posture and audit APIs"},
    {"ecosystem_id": "SERVER", "name": "GLOBAL SERVER API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_server_api_ecosystem", "purpose": "Server control, monitoring and administration APIs"},
    {"ecosystem_id": "SERVICES", "name": "GLOBAL SERVICES API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_services_api_ecosystem", "purpose": "External and internal service APIs"},
    {"ecosystem_id": "SOCIAL_MEDIA", "name": "GLOBAL SOCIAL MEDIA API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_social_media_api_ecosystem", "purpose": "Social publishing, analytics and audience APIs"},
    {"ecosystem_id": "SOFTWARE", "name": "GLOBAL SOFTWARE API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_software_api_ecosystem", "purpose": "Software products, licensing and product APIs"},
    {"ecosystem_id": "STORAGE", "name": "GLOBAL STORAGE API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_storage_api_ecosystem", "purpose": "Object, file, drive and backup storage APIs"},
    {"ecosystem_id": "SYSTEM", "name": "GLOBAL SYSTEM API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_system_api_ecosystem", "purpose": "Operating systems, devices and system management APIs"},
    {"ecosystem_id": "TOOLS", "name": "GLOBAL TOOLS API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_tools_api_ecosystem", "purpose": "Utility, workflow and productivity tool APIs"},
    {"ecosystem_id": "VIDEO", "name": "GLOBAL VIDEO API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_video_api_ecosystem", "purpose": "Video creation, hosting, streaming and processing APIs"},
    {"ecosystem_id": "WEB", "name": "GLOBAL WEB API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_web_api_ecosystem", "purpose": "Web search, browsing, web analytics and web-platform APIs"},
    {"ecosystem_id": "WEBSITE", "name": "GLOBAL WEBSITE API ECOSYSTEM", "path": "backend/api/global_ecosystem/global_api_ecosystem/global_website_api_ecosystem", "purpose": "Website management, CMS, publishing and website operations APIs"},
    {"ecosystem_id": "CORE", "name": "GLOBAL CORE API ECOSYSTEM", "path": "backend/engines/core", "purpose": "Shared application foundation and core readiness APIs"},
    {"ecosystem_id": "ENGINE", "name": "GLOBAL ENGINE API ECOSYSTEM", "path": "backend/engines", "purpose": "Runtime engines, registries, lifecycle and orchestration APIs"},
    {"ecosystem_id": "VPS", "name": "GLOBAL VPS API ECOSYSTEM", "path": "backend/engines/cloud", "purpose": "Virtual server inventory, provisioning adapters and server operations APIs"},
    {"ecosystem_id": "VPN", "name": "GLOBAL VPN API ECOSYSTEM", "path": "backend/engines/connectivity", "purpose": "VPN configuration and connectivity lifecycle API boundaries"},
    {"ecosystem_id": "DNS", "name": "GLOBAL DNS API ECOSYSTEM", "path": "backend/api/dns.py", "purpose": "DNS zones, records, domain routing and registrar APIs"},
)

# Provider records are catalog/architecture links, not live-connectivity claims.
# "CONFIGURATION_READINESS_SCAFFOLD" describes the current provider registry code.
# Other providers remain "CATALOG_ONLY" until their adapters are implemented and tested.
PROVIDER_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {"provider_id": "google", "name": "GOOGLE API ECOSYSTEM", "vendor": "Google", "families": ["AI", "CLOUD", "COMMUNICATION", "COMPANIES", "DATABASE", "DEVELOPER", "PLATFORMS", "STORAGE", "WEB"], "code_path": "backend/integrations/providers/google.py", "ecosystem_path": "backend/api/global_ecosystem/global_api_ecosystem/global_companies_api_ecosystem/global_companies_ecosystem/google", "platform_paths": ["backend/api/global_ecosystem/global_api_ecosystem/global_platforms_api_ecosystem/global_platforms_ecosystem/google_workspace", "backend/api/global_ecosystem/global_api_ecosystem/global_platforms_api_ecosystem/global_platforms_ecosystem/google_cloud", "backend/api/global_ecosystem/global_api_ecosystem/global_platforms_api_ecosystem/global_platforms_ecosystem/google_play"], "runtime_ai_provider_ids": ["google_veo"], "implementation_status": "CONFIGURATION_READINESS_SCAFFOLD", "live_connection_verified": False},
    {"provider_id": "microsoft", "name": "MICROSOFT API ECOSYSTEM", "vendor": "Microsoft", "families": ["AI", "CLOUD", "COMMUNICATION", "COMPANIES", "DATABASE", "DEVELOPER", "PLATFORMS", "STORAGE", "SECURITY"], "code_path": "backend/integrations/providers/microsoft.py", "ecosystem_path": "backend/api/global_ecosystem/global_api_ecosystem/global_companies_api_ecosystem/global_companies_ecosystem/microsoft", "platform_paths": ["backend/api/global_ecosystem/global_api_ecosystem/global_platforms_api_ecosystem/global_platforms_ecosystem/microsoft_365"], "implementation_status": "CONFIGURATION_READINESS_SCAFFOLD", "live_connection_verified": False},
    {"provider_id": "aws", "name": "AWS API ECOSYSTEM", "vendor": "Amazon Web Services", "families": ["AI", "CLOUD", "DATABASE", "DEVELOPER", "HOSTING", "PLATFORMS", "SECURITY", "SERVER", "STORAGE"], "code_path": "backend/integrations/providers/aws.py", "ecosystem_path": "backend/api/global_ecosystem/global_api_ecosystem/global_companies_api_ecosystem/global_companies_ecosystem/aws", "platform_paths": ["backend/api/global_ecosystem/global_api_ecosystem/global_platforms_api_ecosystem/global_platforms_ecosystem/aws_console"], "implementation_status": "CONFIGURATION_READINESS_SCAFFOLD", "live_connection_verified": False},
    {"provider_id": "apple", "name": "APPLE API ECOSYSTEM", "vendor": "Apple", "families": ["APP", "COMPANIES", "INDIVIDUAL", "PLATFORMS", "SECURITY", "SYSTEM"], "code_path": "backend/integrations/providers/apple.py", "ecosystem_path": "backend/api/global_ecosystem/global_api_ecosystem/global_companies_api_ecosystem/global_companies_ecosystem/apple", "platform_paths": ["backend/api/global_ecosystem/global_api_ecosystem/global_platforms_api_ecosystem/global_platforms_ecosystem/apple_app_store"], "implementation_status": "CONFIGURATION_READINESS_SCAFFOLD", "live_connection_verified": False},
    {"provider_id": "openai", "name": "OPENAI API ECOSYSTEM", "vendor": "OpenAI", "families": ["AI", "DEVELOPER", "TOOLS"], "code_path": "backend/engines/ai/manager.py", "implementation_status": "CENTRAL_AI_ENGINE_REGISTRY", "live_connection_verified": False},
    {"provider_id": "nsfwinfra", "name": "NSWFINFRA API ECOSYSTEM", "vendor": "NSFWInfra", "families": ["AI", "IMAGE"], "code_path": "backend/engines/ai/manager.py", "runtime_ai_provider_ids": ["nsfwinfra"], "implementation_status": "CENTRAL_AI_ENGINE_REGISTRY", "live_connection_verified": False},
    {"provider_id": "anthropic", "name": "ANTHROPIC API ECOSYSTEM", "vendor": "Anthropic", "families": ["AI", "DEVELOPER"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "meta", "name": "META API ECOSYSTEM", "vendor": "Meta", "families": ["AI", "COMMUNICATION", "SOCIAL_MEDIA"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "x", "name": "X API ECOSYSTEM", "vendor": "X", "families": ["AI", "SOCIAL_MEDIA"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "github", "name": "GITHUB API ECOSYSTEM", "vendor": "GitHub", "families": ["DEVELOPER", "SOFTWARE", "TOOLS"], "code_path": "backend/api/connectors.py", "implementation_status": "PUBLIC_REPOSITORY_STATUS_CHECK_EXISTS", "live_connection_verified": False},
    {"provider_id": "cloudflare", "name": "CLOUDFLARE API ECOSYSTEM", "vendor": "Cloudflare", "families": ["CLOUD", "DOMAIN", "SECURITY", "SERVER", "WEB"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "digitalocean", "name": "DIGITALOCEAN API ECOSYSTEM", "vendor": "DigitalOcean", "families": ["CLOUD", "HOSTING", "SERVER", "STORAGE"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "oracle", "name": "ORACLE API ECOSYSTEM", "vendor": "Oracle", "families": ["AI", "CLOUD", "DATABASE", "BUSINESS"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "ibm", "name": "IBM API ECOSYSTEM", "vendor": "IBM", "families": ["AI", "CLOUD", "DATABASE", "BUSINESS", "SECURITY"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "nvidia", "name": "NVIDIA API ECOSYSTEM", "vendor": "NVIDIA", "families": ["AI", "CLOUD", "DEVELOPER", "VIDEO"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "huggingface", "name": "HUGGING FACE API ECOSYSTEM", "vendor": "Hugging Face", "families": ["AI", "DEVELOPER"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "deepseek", "name": "DEEPSEEK API ECOSYSTEM", "vendor": "DeepSeek", "families": ["AI", "DEVELOPER"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "mistral", "name": "MISTRAL API ECOSYSTEM", "vendor": "Mistral AI", "families": ["AI", "DEVELOPER"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "cohere", "name": "COHERE API ECOSYSTEM", "vendor": "Cohere", "families": ["AI", "DEVELOPER"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "stripe", "name": "STRIPE API ECOSYSTEM", "vendor": "Stripe", "families": ["BUSINESS", "PAYMENT"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "paypal", "name": "PAYPAL API ECOSYSTEM", "vendor": "PayPal", "families": ["BUSINESS", "PAYMENT"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "twilio", "name": "TWILIO API ECOSYSTEM", "vendor": "Twilio", "families": ["COMMUNICATION", "TOOLS"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "slack", "name": "SLACK API ECOSYSTEM", "vendor": "Slack", "families": ["COMMUNICATION", "BUSINESS"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "zoom", "name": "ZOOM API ECOSYSTEM", "vendor": "Zoom", "families": ["COMMUNICATION", "VIDEO"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "salesforce", "name": "SALESFORCE API ECOSYSTEM", "vendor": "Salesforce", "families": ["BUSINESS", "DATABASE", "TOOLS"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "adobe", "name": "ADOBE API ECOSYSTEM", "vendor": "Adobe", "families": ["AI", "APP", "SOFTWARE", "VIDEO"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "shopify", "name": "SHOPIFY API ECOSYSTEM", "vendor": "Shopify", "families": ["APP", "BUSINESS", "PAYMENT"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "atlassian", "name": "ATLASSIAN API ECOSYSTEM", "vendor": "Atlassian", "families": ["BUSINESS", "DEVELOPER", "TOOLS"], "code_path": None, "implementation_status": "CATALOG_ONLY", "live_connection_verified": False},
)


AI_API_PROVIDER_IDS = {
    "openai", "google", "microsoft", "aws", "nsfwinfra", "anthropic", "meta",
    "nvidia", "huggingface", "deepseek", "mistral", "cohere", "oracle", "ibm",
}


def list_ecosystems() -> list[dict[str, Any]]:
    return deepcopy(list(GLOBAL_API_ECOSYSTEMS))


def list_provider_ecosystems(family: str | None = None) -> list[dict[str, Any]]:
    records = list(PROVIDER_ECOSYSTEMS)
    if family:
        key = family.strip().upper()
        records = [record for record in records if key in record["families"]]
    return deepcopy(records)


def get_provider_ecosystem(provider_id: str) -> dict[str, Any] | None:
    key = provider_id.strip().casefold()
    for record in PROVIDER_ECOSYSTEMS:
        if record["provider_id"] == key:
            return deepcopy(record)
    return None


def list_ai_api_provider_ecosystems() -> list[dict[str, Any]]:
    return [
        record for record in list_provider_ecosystems("AI")
        if record["provider_id"] in AI_API_PROVIDER_IDS
    ]
