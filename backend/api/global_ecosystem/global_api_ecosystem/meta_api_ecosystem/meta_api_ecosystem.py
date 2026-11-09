"""Canonical Meta provider-owned API ecosystem catalog.

Catalog metadata only. This module does not authenticate or make network requests.
A catalog entry is not evidence of product eligibility or live connectivity.
"""
from __future__ import annotations

META_API_ECOSYSTEM = {
    "provider_id": "meta",
    "name": "META API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "platforms": [
        "Meta for Developers", "Meta Graph API", "Facebook Platform",
        "Instagram Platform", "WhatsApp Business Platform",
        "Messenger Platform", "Threads API", "Meta Business Suite and Marketing APIs",
    ],
    "api_families": [
        "graph_core", "facebook_pages", "instagram", "whatsapp_business",
        "messenger", "threads", "marketing_ads", "login_identity",
        "business_management", "webhooks", "sdk_developer_tools", "meta_ai",
    ],
    "children": [
        {"id": "graph_core", "name": "META GRAPH API ECOSYSTEM", "folder": "meta_graph_api_ecosystem", "status": "catalog_only"},
        {"id": "facebook_pages", "name": "META FACEBOOK PAGES API ECOSYSTEM", "folder": "meta_facebook_pages_api_ecosystem", "status": "catalog_only"},
        {"id": "instagram", "name": "META INSTAGRAM API ECOSYSTEM", "folder": "meta_instagram_api_ecosystem", "status": "catalog_only"},
        {"id": "whatsapp_business", "name": "META WHATSAPP BUSINESS API ECOSYSTEM", "folder": "meta_whatsapp_business_api_ecosystem", "status": "catalog_only"},
        {"id": "messenger", "name": "META MESSENGER PLATFORM API ECOSYSTEM", "folder": "meta_messenger_api_ecosystem", "status": "catalog_only"},
        {"id": "threads", "name": "META THREADS API ECOSYSTEM", "folder": "meta_threads_api_ecosystem", "status": "catalog_only"},
        {"id": "marketing_ads", "name": "META MARKETING AND ADS API ECOSYSTEM", "folder": "meta_marketing_ads_api_ecosystem", "status": "catalog_only"},
        {"id": "login_identity", "name": "META LOGIN AND IDENTITY API ECOSYSTEM", "folder": "meta_login_identity_api_ecosystem", "status": "catalog_only"},
        {"id": "business_management", "name": "META BUSINESS MANAGEMENT API ECOSYSTEM", "folder": "meta_business_management_api_ecosystem", "status": "catalog_only"},
        {"id": "webhooks", "name": "META WEBHOOKS API ECOSYSTEM", "folder": "meta_webhooks_api_ecosystem", "status": "catalog_only"},
        {"id": "sdk_developer_tools", "name": "META SDK AND DEVELOPER TOOLS ECOSYSTEM", "folder": "meta_sdk_developer_tools_ecosystem", "status": "catalog_only"},
        {"id": "meta_ai", "name": "META AI ECOSYSTEM", "folder": "meta_ai_ecosystem", "status": "discovery_only"},
    ],
    "related_ecosystems": [
        "GLOBAL AI API ECOSYSTEM", "GLOBAL COMMUNICATION API ECOSYSTEM",
        "GLOBAL SOCIAL MEDIA API ECOSYSTEM", "GLOBAL SECURITY API ECOSYSTEM",
        "GLOBAL DEVELOPER API ECOSYSTEM", "GLOBAL BUSINESS API ECOSYSTEM",
    ],
    "adapter_path": "backend/integrations/providers/meta.py",
    "credential_source": "oauth_and_managed_secret_store",
    "security_requirements": [
        "server_side_oauth_code_exchange", "tenant_scoped_encrypted_token_storage",
        "minimum_required_permissions", "never_log_or_return_access_tokens",
        "webhook_signature_verification", "token_expiry_rotation_and_revocation",
        "rate_limits_and_request_timeouts", "product_app_review_and_business_verification",
    ],
}


def list_meta_api_ecosystems() -> dict[str, object]:
    """List Meta service-family catalogs without asserting live connectivity."""
    children = [dict(item) for item in META_API_ECOSYSTEM["children"]]
    return {
        "success": True,
        "provider_id": META_API_ECOSYSTEM["provider_id"],
        "provider": META_API_ECOSYSTEM["name"],
        "status": META_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }


def get_meta_api_ecosystem(family_id: str) -> dict[str, object]:
    """Resolve a service family by stable ID."""
    wanted = family_id.strip().lower()
    for item in META_API_ECOSYSTEM["children"]:
        if item["id"] == wanted:
            return {"success": True, "item": dict(item)}
    return {"success": False, "error": "META_API_FAMILY_NOT_FOUND", "family_id": family_id}


__all__ = ["META_API_ECOSYSTEM", "list_meta_api_ecosystems", "get_meta_api_ecosystem"]
