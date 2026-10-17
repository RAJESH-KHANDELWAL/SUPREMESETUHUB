"""Provider inventory and readiness checks for GLOBAL FREELANCER ECOSYSTEM.

This module reports configuration only. It never exposes credential values and
never claims a provider is connected until a real authorization/health check exists.
"""
from __future__ import annotations

import os
from typing import Any


PROVIDER_DEFINITIONS: tuple[dict[str, Any], ...] = (
    {
        "provider_id": "google_drive",
        "display_name": "Google Drive",
        "category": "CLOUD_FILE_STORAGE",
        "purpose": "Owner-authorized file storage and synchronization",
        "auth_model": "Google OAuth 2.0",
        "environment": ("GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET"),
        "implementation_status": "SCAFFOLD_ONLY",
        "required_scopes": ["drive.file"],
    },
    {
        "provider_id": "google_cloud_storage",
        "display_name": "Google Cloud Storage",
        "category": "OBJECT_STORAGE",
        "purpose": "Application-managed object storage",
        "auth_model": "Google Cloud service account or workload identity",
        "environment": ("GOOGLE_CLOUD_PROJECT", "GOOGLE_CLOUD_STORAGE_BUCKET"),
        "implementation_status": "SCAFFOLD_ONLY",
        "required_scopes": [],
    },
    {
        "provider_id": "microsoft_onedrive",
        "display_name": "Microsoft OneDrive / Microsoft Graph",
        "category": "CLOUD_FILE_STORAGE",
        "purpose": "Owner-authorized OneDrive file access and synchronization",
        "auth_model": "Microsoft Entra ID OAuth 2.0",
        "environment": ("MICROSOFT_CLIENT_ID", "MICROSOFT_TENANT_ID"),
        "implementation_status": "SCAFFOLD_ONLY",
        "required_scopes": ["Files.ReadWrite", "offline_access"],
    },
    {
        "provider_id": "aws_s3",
        "display_name": "Amazon Web Services S3",
        "category": "OBJECT_STORAGE",
        "purpose": "Application-managed durable object storage",
        "auth_model": "AWS SDK credential chain / IAM role",
        "environment": ("AWS_S3_BUCKET",),
        "implementation_status": "ADAPTER_EXISTS_LIVE_CONNECTION_UNVERIFIED",
        "required_scopes": [],
    },
    {
        "provider_id": "apple_sign_in",
        "display_name": "Apple Sign in",
        "category": "IDENTITY",
        "purpose": "Optional Apple identity sign-in for freelancer accounts",
        "auth_model": "Sign in with Apple / OAuth 2.0 and OpenID Connect",
        "environment": ("APPLE_CLIENT_ID", "APPLE_TEAM_ID", "APPLE_KEY_ID", "APPLE_PRIVATE_KEY"),
        "implementation_status": "SCAFFOLD_ONLY",
        "required_scopes": ["openid", "email", "name"],
        "limitation": "Identity only; this is not an iCloud Drive file-storage adapter.",
    },
)


def get_freelancer_provider_status() -> dict[str, Any]:
    """Return safe provider readiness metadata without returning secret values."""
    providers = []
    for definition in PROVIDER_DEFINITIONS:
        missing = [
            name for name in definition["environment"]
            if not os.getenv(name, "").strip()
        ]
        # AWS can also use workload/instance roles; only the bucket is required
        # here. A populated environment is not proof of successful connectivity.
        configured = not missing
        implementation_status = definition["implementation_status"]
        if not configured:
            state = "CONFIGURATION_REQUIRED"
        elif implementation_status == "ADAPTER_EXISTS_LIVE_CONNECTION_UNVERIFIED":
            state = "CONFIGURED_NOT_CONNECTED"
        else:
            state = "SCAFFOLD_ONLY"
        providers.append({
            "provider_id": definition["provider_id"],
            "display_name": definition["display_name"],
            "category": definition["category"],
            "purpose": definition["purpose"],
            "auth_model": definition["auth_model"],
            "implementation_status": implementation_status,
            "configured": configured,
            "connected": False,
            "status": state,
            "missing_environment": missing,
            "required_scopes": list(definition["required_scopes"]),
            **({"limitation": definition["limitation"]} if definition.get("limitation") else {}),
        })
    return {
        "success": True,
        "connected_provider_count": 0,
        "providers": providers,
        "security_note": "Only readiness metadata is returned; secret values are never exposed. Configuration does not prove live authentication or access.",
    }
