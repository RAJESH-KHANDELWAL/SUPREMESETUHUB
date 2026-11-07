"""Canonical Google Core Ecosystem catalog.

This is a core-layer inventory and orchestration contract, not the Google API
implementation itself. API adapters remain under backend/api/.../google_api_ecosystem.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

GOOGLE_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "GOOGLE-CORE-ECOSYSTEM",
    "name": "GOOGLE CORE ECOSYSTEM",
    "provider": "google",
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": True,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem",
    "existing_google_core_ref": "backend/google/google_ecosystem/core",
    "capabilities": [
        "GOOGLE_PROVIDER_CORE_REGISTRY",
        "GOOGLE_WORKSPACE_CORE",
        "GOOGLE_CLOUD_CORE",
        "GOOGLE_IDENTITY_OAUTH_CORE",
        "GOOGLE_PRODUCT_SERVICE_DISCOVERY",
        "TENANT_SCOPED_CONNECTION_METADATA",
        "CREDENTIAL_BOUNDARY_AND_SECRET_REFERENCE",
        "QUOTA_AND_HEALTH_METADATA",
    ],
    "children": [
        {
            "ecosystem_id": "GOOGLE-GMAIL-CORE-ECOSYSTEM",
            "name": "GOOGLE GMAIL CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "GOOGLE-CORE-ECOSYSTEM",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_gmail_api_ecosystem",
            "service_ref": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_gmail_api_ecosystem/service.py",
            "capabilities": [
                "MAILBOX_OAUTH_AUTHORIZATION",
                "MAILBOX_CONNECTION_STATUS",
                "MAIL_SEND",
                "MAIL_MESSAGE_ID_REFERENCE",
                "TOKEN_REFRESH_BOUNDARY",
                "MAILBOX_DISCONNECT_AND_REVOCATION_BOUNDARY",
            ],
            "scope_policy": {
                "default_scopes": ["https://www.googleapis.com/auth/gmail.send"],
                "least_privilege": True,
                "read_access_enabled_by_default": False,
            },
            "status": "ADAPTER_SCAFFOLD_NOT_LIVE_VERIFIED",
            "connected": False,
        },
        {
            "ecosystem_id": "GOOGLE-DRIVE-CORE-ECOSYSTEM",
            "name": "GOOGLE DRIVE CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "GOOGLE-CORE-ECOSYSTEM",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_drive_api_ecosystem",
            "capabilities": ["FILE_METADATA", "FILE_UPLOAD_DOWNLOAD_BOUNDARY", "PERMISSION_METADATA"],
            "status": "CORE_CATALOG_ONLY",
            "connected": False,
        },
        {
            "ecosystem_id": "GOOGLE-CALENDAR-CORE-ECOSYSTEM",
            "name": "GOOGLE CALENDAR CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "GOOGLE-CORE-ECOSYSTEM",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_calendar_api_ecosystem",
            "capabilities": ["CALENDAR_METADATA", "EVENT_LIFECYCLE", "AVAILABILITY_BOUNDARY"],
            "status": "CORE_CATALOG_ONLY",
            "connected": False,
        },
        {
            "ecosystem_id": "GOOGLE-PEOPLE-CORE-ECOSYSTEM",
            "name": "GOOGLE PEOPLE CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "GOOGLE-CORE-ECOSYSTEM",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_people_api_ecosystem",
            "capabilities": ["PEOPLE_PROFILE_METADATA", "CONTACTS_BOUNDARY"],
            "status": "CORE_CATALOG_ONLY",
            "connected": False,
        },
        {
            "ecosystem_id": "GOOGLE-GEMINI-CORE-ECOSYSTEM",
            "name": "GOOGLE GEMINI CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "GOOGLE-CORE-ECOSYSTEM",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_gemini_api_ecosystem",
            "capabilities": ["GEMINI_MODEL_DISCOVERY", "GENERATIVE_AI_REQUEST_BOUNDARY"],
            "status": "ADAPTER_SCAFFOLD_NOT_LIVE_VERIFIED",
            "connected": False,
        },
        {
            "ecosystem_id": "GOOGLE-VERTEX-AI-CORE-ECOSYSTEM",
            "name": "GOOGLE VERTEX AI CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "GOOGLE-CORE-ECOSYSTEM",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_vertex_ai_api_ecosystem",
            "capabilities": ["CLOUD_AI_MODEL_DISCOVERY", "PROJECT_REGION_BOUNDARY"],
            "status": "CORE_CATALOG_ONLY",
            "connected": False,
        },
    ],
}


def get_google_core_catalog() -> dict[str, Any]:
    """Return a defensive copy of the Google core ecosystem catalog."""
    return deepcopy(GOOGLE_CORE_ECOSYSTEM)


def list_google_core_modules(include_disabled: bool = False) -> list[dict[str, Any]]:
    """Return child core modules without exposing credentials or token data."""
    modules = deepcopy(GOOGLE_CORE_ECOSYSTEM["children"])
    if include_disabled:
        return modules
    return [item for item in modules if item.get("status") != "DISABLED"]
