"""Central social platform registry for SUPREME OWNER ADMIN.

This is a capability/readiness registry, not a claim that providers are connected.
Actual publishing and inbox actions require official APIs, permissions, and tests.
"""

from __future__ import annotations

import os
from typing import Any


SOCIAL_PLATFORMS: tuple[dict[str, Any], ...] = (
    {
        "platform_id": "FACEBOOK",
        "provider": "META_GRAPH_API",
        "capabilities": ["TEXT_POST", "IMAGE_POST", "VIDEO_POST", "COMMENTS", "REPLIES", "INSIGHTS"],
        "auth_env": ["META_APP_ID", "META_APP_SECRET", "META_ACCESS_TOKEN"],
        "notes": "Page publishing and moderation depend on Meta app review, Page permissions, and supported endpoints.",
    },
    {
        "platform_id": "INSTAGRAM",
        "provider": "META_GRAPH_API",
        "capabilities": ["IMAGE_POST", "VIDEO_REEL", "CAPTION", "COMMENTS", "REPLIES", "INSIGHTS"],
        "auth_env": ["META_APP_ID", "META_APP_SECRET", "META_ACCESS_TOKEN", "INSTAGRAM_BUSINESS_ACCOUNT_ID"],
        "notes": "Publishing capabilities depend on account type, linked Page, permissions, and current API support.",
    },
    {
        "platform_id": "LINKEDIN",
        "provider": "LINKEDIN_API",
        "capabilities": ["TEXT_POST", "IMAGE_POST", "VIDEO_POST", "COMMENTS", "REPLIES"],
        "auth_env": ["LINKEDIN_CLIENT_ID", "LINKEDIN_CLIENT_SECRET", "LINKEDIN_ACCESS_TOKEN"],
        "notes": "Posting and organization access require the applicable LinkedIn API products and permissions.",
    },
    {
        "platform_id": "X",
        "provider": "X_API",
        "capabilities": ["TEXT_POST", "IMAGE_POST", "VIDEO_POST", "REPLIES"],
        "auth_env": ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"],
        "notes": "Available actions depend on the X API access tier and current API entitlements.",
    },
    {
        "platform_id": "WHATSAPP",
        "provider": "WHATSAPP_BUSINESS_PLATFORM",
        "capabilities": ["INBOUND_MESSAGES", "REPLIES", "APPROVED_TEMPLATE_MESSAGES", "MEDIA_MESSAGING"],
        "auth_env": ["WHATSAPP_ACCESS_TOKEN", "WHATSAPP_PHONE_NUMBER_ID", "WHATSAPP_APP_SECRET", "WHATSAPP_VERIFY_TOKEN"],
        "notes": "Business messaging requires WhatsApp Business Platform setup, webhook verification, and policy-compliant consent.",
    },
    {
        "platform_id": "YOUTUBE",
        "provider": "YOUTUBE_DATA_API",
        "capabilities": ["VIDEO_UPLOAD", "VIDEO_METADATA", "COMMENTS", "REPLIES"],
        "auth_env": ["YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN"],
        "notes": "Video upload and comment actions require OAuth scopes and API quota.",
    },
    {
        "platform_id": "TELEGRAM",
        "provider": "TELEGRAM_BOT_API",
        "capabilities": ["TEXT_POST", "MEDIA_POST", "BOT_REPLIES"],
        "auth_env": ["TELEGRAM_BOT_TOKEN"],
        "notes": "Bot actions apply only where the bot has been added and granted permission.",
    },
)


def social_platform_status() -> dict[str, Any]:
    """Return safe readiness indicators without exposing secret values."""
    platforms = []
    for item in SOCIAL_PLATFORMS:
        configured = all(os.getenv(key, "").strip() for key in item["auth_env"])
        platforms.append({
            "platform_id": item["platform_id"],
            "provider": item["provider"],
            "capabilities": list(item["capabilities"]),
            "required_settings": list(item["auth_env"]),
            "configuration_present": configured,
            "connected": False,
            "connection_verified": False,
            "publishing_enabled": False,
            "inbox_sync_enabled": False,
            "notes": item["notes"],
        })
    return {
        "success": True,
        "control_plane": "SUPREME OWNER ADMIN",
        "privacy": "OWNER_ONLY",
        "status": "REGISTRY_READY_PROVIDER_CONNECTIONS_NOT_VERIFIED",
        "platforms": platforms,
        "shared_capabilities": [
            "CONTENT_COMPOSER",
            "MEDIA_LIBRARY",
            "DRAFTS",
            "SCHEDULED_PUBLISHING",
            "PUBLISHING_STATUS",
            "COMMENTS_AND_REPLIES",
            "INBOX",
            "ANALYTICS",
            "AUDIT_LOG",
        ],
        "shared_capabilities_status": "PLANNED_UNTIL_PROVIDER_ADAPTERS_AND_STORAGE_ARE_IMPLEMENTED",
        "security": [
            "Use official provider APIs and OAuth with least-privilege scopes",
            "Store credentials and tokens only in secret storage and encrypted token storage",
            "Never publish or send messages without explicit owner action or an approved schedule",
            "Respect platform rate limits, consent, messaging policies, and user privacy",
        ],
    }
