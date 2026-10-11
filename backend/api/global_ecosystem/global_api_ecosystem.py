
"""GLOBAL API ECOSYSTEM registry for SUPREMESETUHUB."""

from __future__ import annotations

from typing import Any

ECOSYSTEM_ID = "GLOBAL_API_ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL API ECOSYSTEM"
ECOSYSTEM_VERSION = "1.0.0"

CATEGORY_ECOSYSTEMS: tuple[dict[str, str], ...] = (
    {
        "id": "business",
        "name": "GLOBAL BUSINESS API ECOSYSTEM",
        "folder": "global_business_api_ecosystem",
    },
    {
        "id": "server",
        "name": "GLOBAL SERVER API ECOSYSTEM",
        "folder": "global_server_api_ecosystem",
    },
    {
        "id": "ai",
        "name": "GLOBAL AI API ECOSYSTEM",
        "folder": "global_ai_api_ecosystem",
    },
    {
        "id": "software-ai",
        "name": "GLOBAL SOFTWARE AI ECOSYSTEM",
        "folder": "global_software_ai_ecosystem",
    },
    {
        "id": "cloud",
        "name": "GLOBAL CLOUD API ECOSYSTEM",
        "folder": "global_cloud_api_ecosystem",
    },
    {
        "id": "security",
        "name": "GLOBAL SECURITY API ECOSYSTEM",
        "folder": "global_security_api_ecosystem",
    },
    {
        "id": "individual",
        "name": "GLOBAL INDIVIDUAL API ECOSYSTEM",
        "folder": "global_individual_api_ecosystem",
    },
    {
        "id": "developer",
        "name": "GLOBAL DEVELOPER API ECOSYSTEM",
        "folder": "global_developer_api_ecosystem",
    },
    {
        "id": "communication",
        "name": "GLOBAL COMMUNICATION API ECOSYSTEM",
        "folder": "global_communication_api_ecosystem",
    },
    {
        "id": "language",
        "name": "GLOBAL LANGUAGE API ECOSYSTEM",
        "folder": "global_language_api_ecosystem",
    },
    {
        "id": "video",
        "name": "GLOBAL VIDEO API ECOSYSTEM",
        "folder": "global_video_api_ecosystem",
    },
    {
        "id": "payment",
        "name": "GLOBAL PAYMENT API ECOSYSTEM",
        "folder": "global_payment_api_ecosystem",
    },
    {
        "id": "storage",
        "name": "GLOBAL STORAGE API ECOSYSTEM",
        "folder": "global_storage_api_ecosystem",
    },
    {
        "id": "system",
        "name": "GLOBAL SYSTEM API ECOSYSTEM",
        "folder": "global_system_api_ecosystem",
    },
    {
        "id": "hosting",
        "name": "GLOBAL HOSTING API ECOSYSTEM",
        "folder": "global_hosting_api_ecosystem",
    },
    {
        "id": "domain",
        "name": "GLOBAL DOMAIN API ECOSYSTEM",
        "folder": "global_domain_api_ecosystem",
    },
    {
        "id": "web",
        "name": "GLOBAL WEB API ECOSYSTEM",
        "folder": "global_web_api_ecosystem",
    },
    {
        "id": "social-media",
        "name": "GLOBAL SOCIAL MEDIA API ECOSYSTEM",
        "folder": "global_social_media_api_ecosystem",
    },
    {
        "id": "database",
        "name": "GLOBAL DATABASE API ECOSYSTEM",
        "folder": "global_database_api_ecosystem",
    },
)


def status() -> dict[str, Any]:
    return {
        "success": True,
        "ecosystem_id": ECOSYSTEM_ID,
        "ecosystem": ECOSYSTEM_NAME,
        "version": ECOSYSTEM_VERSION,
        "status": "registered",
        "category_count": len(CATEGORY_ECOSYSTEMS),
        "provider_integrations_connected": 0,
    }


def list_categories() -> dict[str, Any]:
    return {
        "success": True,
        "count": len(CATEGORY_ECOSYSTEMS),
        "items": [dict(item) for item in CATEGORY_ECOSYSTEMS],
    }


def get_category(category_id: str) -> dict[str, Any]:
    wanted = category_id.strip().lower()

    for item in CATEGORY_ECOSYSTEMS:
        if item["id"] == wanted:
            return {
                "success": True,
                "item": dict(item),
            }

    return {
        "success": False,
        "error": "CATEGORY_NOT_FOUND",
        "category_id": category_id,
    }


def tree() -> dict[str, Any]:
    return {
        "success": True,
        "name": ECOSYSTEM_NAME,
        "id": ECOSYSTEM_ID,
        "children": [dict(item) for item in CATEGORY_ECOSYSTEMS],
    }


__all__ = [
    "CATEGORY_ECOSYSTEMS",
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "ECOSYSTEM_VERSION",
    "status",
    "list_categories",
    "get_category",
    "tree",
]
