from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class StorageProviderStatus:
    provider_id: str
    display_name: str
    implemented: bool
    configured: bool
    connected: bool
    status: str
    purpose: str


# Keep the provider inventory explicit. A listed provider is not considered
# connected until its adapter, credentials, and end-to-end checks exist.
PROVIDER_CATALOG = {
    "local": {
        "display_name": "Local / Hostinger filesystem",
        "implemented": True,
        "purpose": "Development or an explicitly mounted persistent volume",
        "credential_env": (),
    },
    "aws_s3": {
        "display_name": "Amazon Web Services S3",
        "implemented": True,
        "purpose": "Durable object storage for uploads and backups",
        "credential_env": ("AWS_S3_BUCKET",),
    },
    "google_drive": {
        "display_name": "Google Drive",
        "implemented": False,
        "purpose": "Owner-authorized Drive file storage and synchronization",
        "credential_env": ("GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET"),
    },
    "microsoft_onedrive": {
        "display_name": "Microsoft OneDrive / Graph",
        "implemented": False,
        "purpose": "Owner-authorized OneDrive and Microsoft Graph storage",
        "credential_env": ("MICROSOFT_CLIENT_ID", "MICROSOFT_CLIENT_SECRET", "MICROSOFT_TENANT_ID"),
    },
    "mega": {
        "display_name": "MEGA",
        "implemented": False,
        "purpose": "Optional owner-authorized cloud file synchronization",
        "credential_env": (),
    },
    "hostinger": {
        "display_name": "Hostinger",
        "implemented": False,
        "purpose": "Web hosting target; object storage depends on the specific product/plan",
        "credential_env": (),
    },
}


def get_storage_provider_status(provider_id: str | None = None) -> dict:
    selected = (
        provider_id
        or os.getenv("SUPREME_STORAGE_PROVIDER", "local")
    ).strip().lower()
    catalog = PROVIDER_CATALOG.get(selected)
    if catalog is None:
        return {
            "selected_provider": selected,
            "status": "UNSUPPORTED_PROVIDER",
            "implemented": False,
            "configured": False,
            "connected": False,
            "available_providers": sorted(PROVIDER_CATALOG),
        }

    missing = [
        name for name in catalog["credential_env"]
        if not os.getenv(name, "").strip()
    ]
    if not catalog["implemented"]:
        state = "ADAPTER_NOT_IMPLEMENTED"
    elif selected == "local":
        state = "LOCAL_BACKEND_REQUIRES_STORAGE_CONFIGURATION"
    elif missing:
        state = "CONFIGURATION_REQUIRED"
    else:
        state = "CONFIGURED_NOT_CONNECTED"

    configured = not missing
    if selected == "local":
        configured = bool(os.getenv("SUPREME_FILE_STORAGE_DIR", "").strip() or os.getenv("GALLERY_WOULT_STORAGE_ROOT", "").strip())

    return {
        "selected_provider": selected,
        "display_name": catalog["display_name"],
        "status": state,
        "implemented": catalog["implemented"],
        "configured": configured,
        "connected": False,
        "missing_environment": missing,
        "purpose": catalog["purpose"],
        "available_providers": sorted(PROVIDER_CATALOG),
        "note": "Provider inventory does not prove authentication, connectivity, permissions, or durable storage.",
    }
