"""Central registry for Google products and their integration boundaries.

A registry entry is descriptive metadata, not proof of an active Google connection.
OAuth token storage and provider API calls must be implemented and verified separately.
"""
from __future__ import annotations

import os
from typing import Any


GOOGLE_PRODUCTS: dict[str, dict[str, Any]] = {
    "gmail": {
        "name": "Google Gmail",
        "category": "COMMUNICATION",
        "api": "Gmail API",
        "auth": "Google OAuth 2.0",
        "scopes": ["https://www.googleapis.com/auth/gmail.readonly"],
        "integration_mode": "USER_OAUTH",
        "availability": "API_AVAILABLE",
    },
    "drive": {
        "name": "Google Drive",
        "category": "STORAGE",
        "api": "Google Drive API",
        "auth": "Google OAuth 2.0",
        "scopes": ["https://www.googleapis.com/auth/drive.file"],
        "integration_mode": "USER_OAUTH",
        "availability": "API_AVAILABLE",
    },
    "google_one": {
        "name": "Google One",
        "category": "SUBSCRIPTION_AND_STORAGE_PLAN",
        "api": None,
        "auth": "Google account / plan management",
        "scopes": [],
        "integration_mode": "PRODUCT_INFORMATION_ONLY",
        "availability": "NO_GENERAL_PUBLIC_GOOGLE_ONE_API",
        "notes": "Google One membership and consumer plan controls are not exposed as a general public API for this backend.",
    },
    "cloud": {
        "name": "Google Cloud",
        "category": "CLOUD_INFRASTRUCTURE",
        "api": "Google Cloud APIs",
        "auth": "Workload Identity Federation or service account; OAuth where appropriate",
        "scopes": [],
        "integration_mode": "CLOUD_PROJECT_CREDENTIALS",
        "availability": "API_AVAILABLE",
        "notes": "Use least-privilege IAM and workload identity where possible; do not reuse consumer Gmail OAuth as Cloud administrator credentials.",
    },
    "meet": {
        "name": "Google Meet",
        "category": "VIDEO_MEETINGS",
        "api": "Google Meet REST API",
        "auth": "Google OAuth 2.0",
        "scopes": ["https://www.googleapis.com/auth/meetings.space.readonly"],
        "integration_mode": "USER_OAUTH",
        "availability": "API_AVAILABLE_WITH_ELIGIBILITY_AND_SCOPES",
    },
    "calendar": {
        "name": "Google Calendar",
        "category": "SCHEDULING",
        "api": "Google Calendar API",
        "auth": "Google OAuth 2.0",
        "scopes": ["https://www.googleapis.com/auth/calendar.events"],
        "integration_mode": "USER_OAUTH",
        "availability": "API_AVAILABLE",
    },
    "docs": {
        "name": "Google Docs",
        "category": "PRODUCTIVITY",
        "api": "Google Docs API",
        "auth": "Google OAuth 2.0",
        "scopes": ["https://www.googleapis.com/auth/documents"],
        "integration_mode": "USER_OAUTH",
        "availability": "API_AVAILABLE",
    },
    "sheets": {
        "name": "Google Sheets",
        "category": "PRODUCTIVITY",
        "api": "Google Sheets API",
        "auth": "Google OAuth 2.0",
        "scopes": ["https://www.googleapis.com/auth/spreadsheets"],
        "integration_mode": "USER_OAUTH",
        "availability": "API_AVAILABLE",
    },
    "contacts": {
        "name": "Google Contacts",
        "category": "CONTACTS",
        "api": "People API",
        "auth": "Google OAuth 2.0",
        "scopes": ["https://www.googleapis.com/auth/contacts.readonly"],
        "integration_mode": "USER_OAUTH",
        "availability": "API_AVAILABLE",
    },
    "tasks": {
        "name": "Google Tasks",
        "category": "TASK_MANAGEMENT",
        "api": "Google Tasks API",
        "auth": "Google OAuth 2.0",
        "scopes": ["https://www.googleapis.com/auth/tasks.readonly"],
        "integration_mode": "USER_OAUTH",
        "availability": "API_AVAILABLE",
    },
    "photos": {
        "name": "Google Photos",
        "category": "MEDIA",
        "api": "Google Photos APIs",
        "auth": "Google OAuth 2.0",
        "scopes": [],
        "integration_mode": "USER_OAUTH",
        "availability": "LIMITED_API_AND_SCOPE_AVAILABILITY",
        "notes": "Google Photos API access is restricted by current API policies; validate the exact supported use case before enabling.",
    },
    "youtube": {
        "name": "YouTube",
        "category": "VIDEO_AND_CHANNEL",
        "api": "YouTube Data API",
        "auth": "OAuth 2.0 or API key, depending on operation",
        "scopes": ["https://www.googleapis.com/auth/youtube.readonly"],
        "integration_mode": "USER_OAUTH",
        "availability": "API_AVAILABLE",
    },
    "analytics": {
        "name": "Google Analytics",
        "category": "ANALYTICS",
        "api": "Google Analytics Data API",
        "auth": "OAuth 2.0 or service account where supported",
        "scopes": ["https://www.googleapis.com/auth/analytics.readonly"],
        "integration_mode": "USER_OAUTH_OR_CLOUD_IDENTITY",
        "availability": "API_AVAILABLE",
    },
    "maps": {
        "name": "Google Maps Platform",
        "category": "MAPS_AND_LOCATION",
        "api": "Google Maps Platform APIs",
        "auth": "Restricted API key or supported OAuth flow",
        "scopes": [],
        "integration_mode": "API_KEY_OR_OAUTH",
        "availability": "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS",
    },
}


class GoogleEcosystemService:
    """Expose safe integration metadata without claiming live connectivity."""

    def catalog(self) -> list[dict[str, Any]]:
        return [
            {"id": key, **value}
            for key, value in GOOGLE_PRODUCTS.items()
        ]

    def status(self) -> dict[str, Any]:
        oauth_configured = all(
            os.getenv(name, "").strip()
            for name in (
                "GOOGLE_CLIENT_ID",
                "GOOGLE_CLIENT_SECRET",
                "GOOGLE_REDIRECT_URI",
            )
        )
        cloud_configured = bool(
            os.getenv("GOOGLE_CLOUD_PROJECT", "").strip()
            and (
                os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "").strip()
                or os.getenv("GOOGLE_CLOUD_CREDENTIALS_JSON", "").strip()
                or os.getenv("GOOGLE_CLOUD_WORKLOAD_IDENTITY_PROVIDER", "").strip()
            )
        )
        return {
            "success": True,
            "ecosystem": "GOOGLE_ECOSYSTEM",
            "status": "REGISTRY_READY",
            "product_count": len(GOOGLE_PRODUCTS),
            "google_oauth_app_configured": oauth_configured,
            "google_cloud_identity_configured": cloud_configured,
            "live_connection_verified": False,
            "oauth_flow_status": "PENDING_IMPLEMENTATION",
            "token_storage_status": "NOT_IMPLEMENTED",
            "products": [
                {
                    "id": product_id,
                    "name": product["name"],
                    "availability": product["availability"],
                    "integration_mode": product["integration_mode"],
                    "connected": False,
                }
                for product_id, product in GOOGLE_PRODUCTS.items()
            ],
            "security_note": (
                "Configuration is not a connection. No Google token is stored or "
                "returned by this registry. Connect only after consent, secure token "
                "storage, least-privilege scopes, and end-to-end verification."
            ),
        }

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        product = GOOGLE_PRODUCTS.get(product_id.strip().lower())
        if product is None:
            return None
        return {"id": product_id.strip().lower(), **product}
